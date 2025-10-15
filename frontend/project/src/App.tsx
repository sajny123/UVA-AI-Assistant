import { useState } from "react";
import uvaLogo from "./assets/uvaLogo.png";

function App() {
    const [userInput, setUserInput] = useState("");
    const [claudeResponse, setClaudeResponse] = useState("");

    const handleSubmit = async () => {
        const apiURL = "/api/ask";

        try {
            const response = await fetch(apiURL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ question: userInput }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            setClaudeResponse(data.answer);
        } catch (error) {
            console.error("Error fetching data: ", error);
            setClaudeResponse("Somethign went wrong. ");
        }
    };

    return (
        <>
            <div className="bg-gray-100 min-h-screen w-full font-montserrat">
                {/* top bar */}
                <div className="w-full fixed bg-white top-0 sm:h-21 h-17 shadow-md shadow-black/10"></div>
                <div className="bg-white fixed top-3 w-full flex justify-center">
                    <div className="flex gap-3 items-center">
                        <img
                            src={uvaLogo}
                            className="sm:h-14 h-10"
                            alt="UVA Logo"
                        ></img>
                        <div className="h-8 w-[1px] bg-gray-400 mt-1"></div>
                        <h1 className="font-medium text-[#202D4B] sm:text-3xl text-2xl mt-1">
                            AI Assistant
                        </h1>
                    </div>
                </div>
                <div className="sm:pt-28 pt-23 px-6">
                    <div className="grid grid-cols-1 xl:grid-cols-2 gap-6 max-w-7xl mx-auto">
                        {/* input */}
                        <div className="bg-white w-full h-[500px] rounded-2xl overflow-hidden shadow-lg">
                            <div className="bg-[#202D4B] h-21 text-white px-5 py-4">
                                <h1 className="text-xl font-semibold">
                                    Your Question
                                </h1>
                                <p className="opacity-70 text-xs sm:text-base">
                                    Ask about requirements, classes, or anything
                                    else
                                </p>
                            </div>
                            <div className="p-4 h-[calc(500px-143px)]">
                                <textarea
                                    value={userInput}
                                    onChange={(e) =>
                                        setUserInput(e.target.value)
                                    }
                                    placeholder="Enter prompt here"
                                    className="w-full h-full border-gray-200 border-2 rounded-lg resize-none focus:outline-none p-3"
                                ></textarea>
                            </div>
                            <div className="px-4 flex gap-4">
                                <button
                                    onClick={handleSubmit}
                                    className="bg-[#F37D1F] text-white font-semibold px-3 py-2 w-full rounded-lg cursor-pointer border-2 hover:bg-gray-100 hover:border-[#F37D1F] hover:text-[#F37D1F] transition-all duration-250"
                                >
                                    Ask AI
                                </button>
                                <button className="bg-[#202D4B] text-white font-semibold px-3 py-2 w-40 rounded-lg cursor-pointer border-2 hover:bg-gray-100 hover:border-[#202D4B] hover:text-[#202D4B] transition-all duration-250">
                                    Clear
                                </button>
                            </div>
                        </div>
                        {/* output */}
                        <div className="bg-white w-full h-[500px] rounded-2xl overflow-hidden shadow-lg">
                            <div className="bg-[#202D4B] h-21 text-white px-5 py-4">
                                <h1 className="text-xl font-semibold">
                                    AI Response
                                </h1>
                                <p className="opacity-70 text-xs sm:text-base">
                                    Get instant answers from Claude Sonnet 4.5
                                </p>
                            </div>
                            <div className="p-4 h-[calc(500px-84px)]">
                                <div className="w-full h-full p-3 relative border-2 rounded-lg border-gray-200">
                                    <div className="absolute text-gray-500 flex flex-col inset-0 justify-center items-center pb-8">
                                        <h1>Your response will appear here</h1>
                                        <p>Ask a question to get started</p>
                                    </div>
                                    {/* actual text response field */}
                                    <div className="">
                                        <p>{claudeResponse}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

export default App;
