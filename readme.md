# XOXO Game Project

This project will guide you through creating an API to manage scores for the XOXO game using FastAPI. The project consists of two phases:

1. [Connecting database(SQLITE) and API](https://fastapi.tiangolo.com/tutorial/sql-databases/)
2. Creating a React UI

## Game Description

In the XOXO game, we need an API connection to keep track of scores in a table. There are two players in each match. The score submission follows this format:

```json
{
   "name": "JOHN",
   "status": "WIN"
}
{
    "name": "REZA",
    "status": "LOSE"
}
```

- If the status is "WIN", find the player's score in the table and increase it by one.
- If the status is "LOSE", find the player's score in the table and decrease it by one.

For each match, two records will be posted. For example:

- JOHN | 2pt
- REZA | 0pt

Phase 1: Connecting Database and API
In this phase, you will create routes to:

1. Get the top 10 players by rank.
2. Post score and player name.

Phase 2: React and UI
To be covered later.

## 2. Creating a Virtual Environment (.venv)

To create a virtual environment for your project, follow these steps:

1. Open your terminal (command prompt, PowerShell, or any terminal you prefer).
2. Create a virtual environment named .venv:

   ```bash
   python3 -m venv .venv
   ```

3. Activating the Virtual Environment
   Activate the virtual environment to ensure that any packages you install are local to this project.
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
4. You should now see your terminal prompt prefixed with (.venv), indicating that the virtual environment is active.
5. Installing FastAPI and Uvicorn
   With the virtual environment activated, install FastAPI and Uvicorn using pip:
   ```bash
   pip install fastapi uvicorn
   ```
6. Running the FastAPI Application
   Create a file named main.py in your project directory and add the following code:
   JUST FOR TEST :
   from fastapi import FastAPI

   ```
   app = FastAPI()


   @app.get("/")
   def read_root():
       return {"Hello": "World"}
   ```

7. To run the FastAPI application, use the following command:

   ```bash
   uvicorn main:app --reload
   ```

8. visit http://127.0.0.1:8000/docs for Swagger UI
