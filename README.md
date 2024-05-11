# 🤖 Gemini 1.5 Pro Chatbot 💬

This project implements a simple chatbot using Google's Gemini 1.5 Pro model via the `google-generativeai` library. 

## ✨ Features

- **Interactive Chat:** Engage in a conversation with the Gemini 1.5 Pro model. 💬
- **Safety Settings:**  Built-in safety mechanisms to filter content related to harassment, hate speech, sexually explicit material, and dangerous content. 🛡️
- **Conversation History:** Maintains the context of the conversation for more coherent interactions. 🧠

## 🧰 Requirements

- **Python 3.7 or higher** 🐍
- **google-generativeai** library: Install using `pip install google-generativeai` 
- **dotenv** library: Install using `pip install python-dotenv` 
- **Google  Account:** You'll need a Google account to be able access the Google AI Studio. ☁️
- **Gemini API :** Ensure that the Gemini API is active. ✅

![App Screenshot](https://i.ibb.co/kgn5fqY/a.png)

## 🚀 Setup

1. **Obtain your API Key:** 🗝️
   - Go to the [Google AI Studio](https://aistudio.google.com/).
   - Get API Key.
   - Create API Key".
   - Copy. 
   - **Important:**  Store this API key securely. 🔐

2. **Create a `.env` file:** 📝
   - In the project directory, create a file named `.env`.
   - Add the following line to the file, replacing `YOUR_API_KEY` with your actual API key:

     ```
     API_KEY=YOUR_API_KEY
     ```

3. **Run the Chatbot:** ▶️
   - Execute the Python script (e.g., `python chatbot.py`).
   - Start typing to chat with the chatbot! 💬
   - To exit the program, type `exit`. 🚪

![App Screenshot](https://i.ibb.co/YQkYjpN/c.png)

## 💻 Code Explanation

- **`google.generativeai`:**  Imports the necessary library for interacting with the Gemini API. 
- **`dotenv`:** Loads the API key from the `.env` file. 
- **`genai.configure(api_key=api_key)`:** Sets up your authentication for the API. 🔑
- **`model = genai.GenerativeModel(...)`:**  Initializes the Gemini 1.5 Pro model with specified parameters:
    - **`model_name`:**  Specifies the Gemini model to use. 
    - **`generation_config`:**  Controls model behavior:
        - **`temperature`:**  Higher values (e.g., 1) make the output more creative/random; lower values (e.g., 0.2) make it more deterministic. 🌡️
        - **`top_p`:**  Nucleus sampling parameter - influences the diversity of generated text.
        - **`top_k`:**  Top-k sampling parameter - limits the selection of words to the top k most probable words.
        - **`max_output_tokens`:**  Sets the maximum length of the model's responses. 
    - **`safety_settings`:**  Defines safety thresholds for various content categories. 🛡️
- **`convo = model.start_chat(...)`:**  Initiates a chat session with the model, optionally providing conversation history. 💬
- **`convo.send_message(user_input)`:** Sends the user's input to the model. ➡️
- **`print(convo.last.text)`:** Displays the model's response. ⬅️
- **`conversation_history`:** Keeps track of the conversation turns. 🔁
  
![App Screenshot](https://i.ibb.co/HKzYTrQ/b.png)

## 👍 Tips

- Experiment with the `temperature` parameter in `generation_config` to adjust the chatbot's creativity. 🌡️
- Explore different safety settings to customize the content filtering. 🛡️
- Consider expanding the chatbot's functionality by adding features like:
    -  User authentication 👤
    -  Topic-specific responses 🎯
    -  Integration with other services 🔗

**Remember to replace `YOUR_API_KEY` in the `.env` file with your actual API key!** 🔑
