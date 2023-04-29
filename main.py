import openai
from fastapi import FastAPI, Form, Depends, Request
from decouple import config
from utils import send_message, logger

app = FastAPI()
openai.api_key = config("OPENAI_API_KEY")
whatsapp_number = config("TO_NUMBER")

conversations = {}

@app.post("/message")
async def reply(From: str = Form(), Body: str = Form()):
    logger.info(From[9:])
    phone_number = From[9:]

    if phone_number not in conversations:
        conversations[phone_number] = [
            {
                "role": "system",
                "content": "Hello! I'm your personal AI health and fitness assistant, here to help you live a healthy and happy life. As a certified health and fitness expert, I have the knowledge and experience to help you achieve your goals."
            }
        ]

    conversations[phone_number].append({"role": "user", "content": Body})

    # Call the OpenAI API to generate text with GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversations[phone_number],
        temperature=0.7,
        max_tokens=2966,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    logger.info(response)

    # The generated text
    chat_response = response.choices[0]['message']['content'].strip()

    # Store the assistant's response in the conversation history
    conversations[phone_number].append({"role": "assistant", "content": chat_response})

    # Send the message
    send_message(phone_number, chat_response)
    return ""
