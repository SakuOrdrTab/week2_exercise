# Week 2 exercise for TUNI finetuning course

This is a FastAPI translator.

## Install

1. clone

then in project root:
>python -m venv .venv
>.venv\scripts\activate
>pip install -r requirements.txt

2. run:
>uvicorn app:app

Then you have the server at your disposal. Sen translation tasks english to finnish to localhost:8000/translate, for example:
>POST http://127.0.0.1:8000/translate/
>Content-Type: application/json
>
>{
>  "text": "Can you translate numbers too? 123,456 and symbols like $ and %?"
>}

The repo includes some REST vscode extension API calls to try out in /tests/

## IMPORTANT NOTE:
You must set your Groq api key as an environment variable.
