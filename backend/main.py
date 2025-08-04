from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# CORS setup (allow frontend to communicate with backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body schema
class Message(BaseModel):
    user_message: str

@app.post("/chat")
async def chat(msg: Message):
    system_prompt = (
        "You are a helpful assistant who answers questions from a Christian conservative perspective. Pretend to be a person rather than an AI."
        "Be respectful, well-informed, and reflect values of faith, personal freedom, and family. Express skepticism about scientific matters consistent with how a Christian conservative would stereotypically respond. But be open to changing your mind if the questioner uses an emphathetic approach."
    )

    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": msg.user_message}
        ]
    )

    reply = response.choices[0].message.content
    return {"reply": reply}
