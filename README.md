# 🏥 Multilingual Health Chatbot with TF-IDF, FAISS, and Bloom LLM

This project is a **multilingual chatbot** that helps users find **health-related information** using **Rasa for intent detection**, **FAISS for document retrieval**, and the **Bloom-560m model** for generating responses. The bot supports multiple languages by translating user queries and responses when necessary. Users interact with the bot through **Telegram** using the **Telegram Bot API**.

---

## 🚀 Project Workflow

1. **User Interaction:**  
   Users interact with the bot on **Telegram** by asking health-related questions in **any supported language**.

2. **Language Detection and Translation:**  
   - The **`translator.py`** script detects the language of the user query.
   - If the query is not in English, it is translated into English using **Deep Translator**.

3. **Intent Detection (Rasa NLU):**  
   - The translated query is passed to the **Rasa NLU server**, which detects the **user’s intent** (e.g., asking about symptoms, treatments, or policies).

4. **Document Retrieval (FAISS):**  
   - Based on the detected intent, the bot retrieves the **most relevant documents** using a **FAISS-based search engine**.

5. **Context Generation and Response:**  
   - The top documents are **cleaned and combined** into a concise context.
   - The **Bloom-560m model** generates a response using the context and the user query.

6. **Translation Back to the User’s Language:**  
   - If the original query was not in English, the response is translated back to the user’s language.

7. **Response Sent to Telegram:**  
   The chatbot sends the final response back to the user via the **Telegram Bot API**.

---

## 📂 Project Structure

/Quark_final
│
├── bot.py                      # Main file to run the Telegram bot
├── bloom_response.py           # Handles response generation using Bloom-560m
├── translator.py               # Handles language detection and translation
├── vector_store.py             # Manages FAISS-based document retrieval
├── index_documents.py          # Indexes health-related documents using TF-IDF and FAISS
├── search.py                   # Test script to manually search FAISS
│
├── domain.yml                  # Defines intents, entities, and responses for Rasa
├── config.yml                  # Rasa configuration for pipelines
├── nlu.yml                     # Training data for Rasa NLU
│
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

---

## 📋 Requirements
- **Python**: 3.8+
- **Pip**: Latest version
- **Rasa**: Installed in a virtual environment
- The required Python dependencies are listed in **`requirements.txt`**.

---

## 🛠️ Setup Instructions
1. Clone the Repository
- git clone https://github.com/your-username/health-chatbot.git
- cd health-chatbot

2. Set Up Virtual Environments
- For Bloom LLM and FAISS:

- Create separate virtual environments for Bloom , FAISS , RASA.

3. Train the Rasa NLU Model
- Activate the Rasa virtual environment and train the model using the provided NLU data.

4. Index the Health Documents Using TF-IDF and FAISS
- Activate the FAISS environment and run index_documents.py to index the documents:

5. Start the Rasa NLU Server and Run the Telegram Bot
   1. Activate the Rasa virtual environment
   2. Start the Rasa server with the API enabled

6. Run the Telegram Bot
   1. Open a new terminal and navigate to the project directory
   2. Activate the Bloom virtual environment
   3. Run the bot

---

## 🛠️ How to Interact with the Bot
- Open Telegram and search for your bot using the Bot Token provided by BotFather.
- Start interacting with the bot by sending health-related queries.
  
---

## 🌟 Future Enhancements
- **Fine-tune Bloom or use a larger model:**  
  Experiment with Bloom-1B or fine-tune the existing model for more specific health-related answers.

- **Expand document base:**  
  Add documents covering a wider range of health topics, treatments, and policies.

- **Integrate a knowledge graph:**  
  Use a knowledge graph to provide structured and context-aware responses.

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

---

## 📬 Contact
If you have any questions or suggestions, feel free to contact me:
- **Email:** anshagrawal148@gmail.com.com

---
