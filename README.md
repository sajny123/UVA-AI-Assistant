# UVA AI Assistant

An intelligent AI assistant powered by Anthropic's Claude, designed to answer questions about the University of Virginia's courses, degree requirements, and frequently asked questions. This project features a modern web interface built with React, a robust Flask backend, and a real-time data integration system using FastMCP servers.

## Live Demo

You can try out the application here:
https://uva-ai-assistant.onrender.com/

## Features

-   **Conversational AI:** Get instant, context-aware answers from Claude about UVA's academic landscape.
-   **Real-Time Data:** Asks questions about specific course requirements (e.g., "What are the upper-level CS requirements?") which are fulfilled by specialized `FastMCP` tool servers.
-   **FAQ Knowledge Base:** Capable of answering frequently asked questions about university policies and student life.
-   **Automated Logging:** Seamlessly integrates with an n8n workflow to log all questions and responses to a Google Sheet for analysis and improvement.
-   **Responsive Design:** A clean and modern user interface that works on both desktop and mobile devices.

## Tech Stack & Architecture

This project uses a modern, full-stack architecture to separate concerns and ensure scalability.

-   **Frontend:** React (with Vite) & Tailwind CSS
-   **Backend:** Python & Flask
-   **AI Model:** Anthropic Claude (Sonnet 4.5)
-   **Tooling / Data Layer:** `FastMCP`
-   **Automation & Logging:** n8n Workflow
-   **Database (for logs):** Google Sheets
-   **Deployment:** Onrender

### Application Flow

1.  The **React Frontend** captures the user's question and sends it to the Flask API.
2.  The **Flask Backend** receives the request and uses its Claude client to process the query.
3.  The Claude client determines if a specialized tool is needed and invokes the appropriate `FastMCP` server (e.g., to get course data).
4.  The tool returns structured data, which is used to generate a final, accurate response from Claude.
5.  (Asynchronously) The Flask backend sends the question and the final response to an **n8n Webhook**.
6.  The **n8n Workflow** takes this data and appends it as a new row in a **Google Sheet**.
