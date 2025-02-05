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

