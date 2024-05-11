import google.generativeai as genai
import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)

def displayMessage():
    print( " \n 📌 Little Tip \n Type \033[31m exit \033[0m to stop the program \n")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

conversation_history = []
convo = model.start_chat(history=conversation_history)

displayMessage()

user_input = input(" \033[35m (👉ﾟヮﾟ)👉 Type something : \033[0m").lower()
while True:
    if user_input == 'exit':
        break

    conversation_history.append(f"user: {user_input}")
    convo.send_message(user_input)
    print(convo.last.text)

    conversation_history.append(f"model: {convo.last.text}")
    user_input = input(" \033[35m (👉ﾟヮﾟ)👉 Type something : \033[0m ").lower()

sys.exit() 