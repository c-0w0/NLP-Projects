# refering to https://github.com/riza-io/examples/blob/main/demos/mcp_and_pydanticai/agent_with_mcp_fetch.py

# 3rd-party imports
import logfire
from dotenv import load_dotenv
from pydantic_ai import Agent
# local imports
from server import get_servers

load_dotenv()
logfire.configure()

agent = Agent(model='gemini-2.0-flash',
              instrument=True, # logging of the agent's activities
              system_prompt="An agent designed for customer service of a hotel.",
              instructions="""Do follow the below procedures when a customer **first** approaches and have any inquiries.
                            1. Make sure you know the directories that you have access to via list_allowed_directories().
                            2. Make sure you know the files in the directory first via list_directory().
                            Do follow the behavior below.
                            1. If a tool(s) OR action(read file) is required in this process, **DON'T** ask the user, **DO** keep going.
                            2. Make sure every files has been read, before answering the customer the question asked is not documented and ask him/her to contact the phone number given. 
                            3. Use the retireved info to formulate answers
                            """,

              toolsets=get_servers())

async def main():
    async with agent.run_mcp_servers():
        history = []
        while True:
            user_input = input("\nInput: ")
            resp = await agent.run(user_input, message_history=history)
            history = list(resp.all_messages())
            print(resp.output)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

