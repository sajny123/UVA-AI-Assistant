import os
import asyncio
from dotenv import load_dotenv
from anthropic import Anthropic
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from typing import Optional

load_dotenv()

class MCP:
    def __init__(self):
        self.client = Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
        self.model = "claude-sonnet-4-5"
        self.mcp_session: Optional[ClientSession] = None
        self.mcp_context = None

    async def connect_to_server(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.dirname(current_dir)
        courses_script_path = os.path.join(
            project_root, "mcp", "courses.py"
        )
        server_params = StdioServerParameters(
            command="python",
            args=[courses_script_path]
        )

        self.mcp_context = stdio_client(server_params)
        read, write = await self.mcp_context.__aenter__()

        self.mcp_session = ClientSession(read, write)
        await self.mcp_session.__aenter__()
        await self.mcp_session.initialize()

    async def get_tools(self):
        if not self.mcp_session:
            raise RuntimeError("Server not connected")
        
        tools_result = await self.mcp_session.list_tools()

        tools = []
        for tool in tools_result.tools:
            tools.append({
                "name": tool.name,
                "description": tool.description,
                "input_schema": tool.inputSchema
            })
        
        return tools
    
    async def call_tool(self, tool_name: str, tool_input: dict) -> str:
        if not self.mcp_session:
            raise RuntimeError("Server not connected")
        
        result = await self.mcp_session.call_tool(tool_name, tool_input or {})

        if result.content and len(result.content) > 0:
            return result.content[0].text
        
        return "{}"
    
    async def ask(self, prompt: str) -> str:
        if not self.mcp_session:
            raise RuntimeError("Server not connected")
        
        prompt += " Use linebreaks to make your response more readable."
        tools = await self.get_tools()
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        response = self.client.messages.create(
            model = self.model, 
            max_tokens=1000,
            tools=tools,
            messages=messages
        )

        while response.stop_reason == "tool_use":
            messages.append({
                "role": "assistant",
                "content": response.content
            })

            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result = await self.call_tool(block.name, block.input)

                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })
            messages.append({
                "role": "user",
                "content": tool_results
            })

            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                tools=tools,
                messages=messages
            )
        
        final_response = ""
        for block in response.content:
            if hasattr(block, "text"):
                final_response += block.text
        
        return final_response
    
    async def close(self):
        if self.mcp_session:
            await self.mcp_session.__aexit__(None, None, None)
        if self.mcp_context:
            await self.mcp_context.__aexit__(None, None, None)

    @staticmethod
    async def get_claude_response(prompt: str) -> str:
        agent = MCP()

        try:
            await agent.connect_to_server()
            response = await agent.ask(prompt)
            return response
        except Exception as e:
            return f"Error: {str(e)}"
        finally: 
            await agent.close()

    @staticmethod
    def ask_claude(prompt: str):
        return asyncio.run(MCP.get_claude_response(prompt))
    

