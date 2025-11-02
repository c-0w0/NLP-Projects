## Introduction
This is my first contact on Retrieval-Augmented Generation (RAG) technique.

## Characters

| Role | Actor |
|:-:|:-:|
| Embedding model | sentence-transformers/all-MiniLM-L6-v2 |
| Gen AI | gemini-2.0-flash-exp |

## Procedures

### create_db.ipynb
`def load_doc() -> list[Document]:`

1. Load documents (i.e. `*.txt`)

`def split_txt(doc: list[Document]) -> list[Document]:`

2. Split texts into chunks (adjusting `chunk_size` yields different chunks amount)

`def save_to_chroma(chunks: list[Document]) -> None:`

3. Convert the chunked texts into numerical/vector emebeddings
4. Save the embeddings into **Chroma** database

`def check_database_content():`

6. [Optional] Authenticate the entries in the database

### query_db.ipynb
`def query_database(query_text: str) -> None:`

5. Prepare Chroma database and use the same Embedding model to convert query into vectors later
6. Receive user query, parse it to vector, and search the conduct simmilarity search with relevance score
7. Set a threshold score to filter the search result. If not met, it won't proceed to the steps below
8. Pass the search result to GenAI model, and get response from it
9. Format and display the result alongside the sources of the data

`def interactive_query() -> None:`
Let user input

## Note
Create `.env` file at the parent folder where `data` and `src` are located.
```
GEMINI_API_KEY=
```