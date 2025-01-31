import os
import groq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = groq.Client(api_key=GROQ_API_KEY)

# FastAPI app
app = FastAPI()

# Request model
class TranslationRequest(BaseModel):
    text: str

@app.post("/translate/")
async def translate_text(request: TranslationRequest):
    try:
        prompt = f"Translate the following English text into Finnish:\n\n{request.text}"

        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Groq-supported model
            messages=[{"role": "user", "content": prompt}],
        )

        translated_text = response.choices[0].message.content.strip()

        return {"original_text": request.text, "translated_text": translated_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

