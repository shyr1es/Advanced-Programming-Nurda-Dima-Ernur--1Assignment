import os
import chromadb
import streamlit as st
from langchain_ollama import OllamaLLM

# Подключение к ChromaDB
chroma_client = chromadb.PersistentClient(path=os.path.join(os.getcwd(), "chroma_db"))
collection = chroma_client.get_or_create_collection(
    name="chat_data",
    metadata={"description": "Chat history"}
)

# Функции для работы с ChromaDB
def add_documents_to_collection(documents, ids):
    """Добавление документов в коллекцию и вывод в терминал."""
    collection.add(documents=documents, ids=ids)
    # Выводим информацию о сохранении в терминал
    print(f"Saved documents: {documents}")

def query_chromadb(query_text, n_results=1):
    """Запрос в ChromaDB."""
    results = collection.query(query_texts=[query_text], n_results=n_results)
    return results

# Настройка модели LLM Ollama
llm_model = "llama3.2"

def query_ollama(prompt):
    """Запрос к LLM Ollama."""
    llm = OllamaLLM(model=llm_model)
    response = llm.invoke(prompt)
    return response  # Возвращаем строковый ответ от модели

# Streamlit интерфейс
st.title("LLM Chat Application")

# Ввод пользователя
query = st.text_input("Enter your question:")

if st.button("Submit"):
    if query:
        # Получение ответа от LLM
        response = query_ollama(query)
        st.write("Response:", response)

        # Сохраняем запрос и ответ в коллекцию ChromaDB
        add_documents_to_collection([query, response], [f"query_{query}", f"response_{query}"])
    else:
        st.write("Please enter a question.")
