## Introduction
Development of Chatbot using MCP servers (and pending: locally defined tools), in Laravel (MVC) framework.

## Characters
| Body    | Actor |
| :--------: | :-------: |
| LLM | Gemini-2.5-pro    |
| AI Agent | Pydantic-AI     |
| MCP Server    | [Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch), [FileSystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)    |

## Protoypes
The prototypes below are the progression of the chatbot development, they can be found at `uv\src`
- `prototype1_CLI`
- `prototype2_WebIntegration`

## How to use 
- For `prototype1_CLI`, follow step1-4
- For `prototype2_WebIntegration`, follow all the steps below

1. In `uv` folder, create `.env` file 
```
LOGFIRE_TOKEN = 
GEMINI_API_KEY = 
```

2. In `uv` folder, create virtual environment and install python package dependencies
```
uv run sync
```

3. At the root (the directory contains `uv` and `web`), open the project in VSC
`Ctrl + Shift + P` -> `Python: Select Interpreter` -> `Enter Interpreter Path` -> Find...(Browse) -> `uv\.venv\Scripts\python.exe`

4. Run agent.py (the one in `uv\src\prototype1_CLI`/`uv\src\prototype2_WebIntegration`) via VSC UI

5. In `web`, run:
```
php artisan serve
```

6. Visit the webpage
http://127.0.0.1:8000/

## Screenshot
<img width="1855" height="1019" alt="image" src="https://github.com/user-attachments/assets/922528d6-f4a7-42f8-bbaa-2cbfe45bfae4" />

## Pending Tasks
1. Implement Vector Database to arm the chatbot with knowledge(dataset) given
2. Optimize server parameter syntax 
