import { useState } from "react";
import uvaLogo from "./assets/uvaLogo.png";

function App() {
    return (
        <>
            <div className="bg-gray-100 min-h-screen w-full font-montserrat">
                {/* top bar */}
                <div className="w-full fixed bg-white top-0 h-21 shadow-md shadow-black/10"></div>
                <div className="bg-white fixed top-3 w-full flex justify-center md:justify-start md:left-[25%]">
                    <div className="flex gap-3 items-center">
                        <img
                            src={uvaLogo}
                            className="h-14"
                            alt="UVA Logo"
                        ></img>
                        <div className="h-8 w-[1px] bg-gray-400 mt-1"></div>
                        <h1 className="font-medium text-[#202D4B] text-3xl mt-1">
                            AI Assistant
                        </h1>
                    </div>
                </div>
                <div className="pt-26 px-6">
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 max-w-7xl mx-auto">
                        <div className="bg-white w-full h-[500px] rounded-2xl overflow-hidden">
                            <div className="bg-[#202D4B] h-21 text-white px-5 py-4">
                                <h1 className="text-xl font-semibold">
                                    Your Question
                                </h1>
                                <p className="opacity-70 text-xs sm:text-base">
                                    Ask about requirements, classes, or anything
                                    else
                                </p>
                            </div>
                            <input
                                type="text"
                                placeholder="Enter prompt here"
                                className="w-full h-full border-gray-200 p-6"
                            ></input>
                        </div>
                        <div className="bg-white w-full h-[500px]">
                            <input
                                type="text"
                                placeholder="Enter prompt here"
                                className="w-full h-full "
                            ></input>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}

export default App;
