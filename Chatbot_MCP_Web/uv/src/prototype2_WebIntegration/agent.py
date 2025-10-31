# 3rd-party imports
import uvicorn
import logfire
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_ai import Agent
from typing import List, Dict
# local imports
from server import get_servers

load_dotenv()
logfire.configure()

app = FastAPI()

class ChatAgent:
    def __init__(self):
        self.agent = Agent(
            model='gemini-2.0-flash',
            instrument=True,
            system_prompt="An agent designed for customer service of a hotel.",
            instructions="""Do follow the below procedures when a customer **first** approaches and have any inquiries.
                            1. Make sure you know the directories that you have access to via list_allowed_directories().
                            2. Make sure you know the files in the directory first via list_directory().
                            Do follow the behavior below.
                            1. If a tool(s) OR action(read file) is required in this process, **DON'T** ask the user, **DO** keep going.
                            2. Make sure every files has been read, before answering the customer the question asked is not documented and ask him/her to contact the phone number given. 
                            3. Use the retireved info to formulate answers
                            """,
            toolsets=get_servers()
        )
        self.conversation_history = []

    async def process_message(self, message: str) -> str:
        resp = await self.agent.run(message, message_history=self.conversation_history)
        self.conversation_history = list(resp.all_messages())
        return resp.output

chat_agent = ChatAgent()

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    response = await chat_agent.process_message(request.message)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)