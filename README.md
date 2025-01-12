### LLM Chat Application
This project is a web application built with Streamlit, integrated with ChromaDB to store chat history, and uses the Ollama language model (LLM) to process user queries.
### Description
The application allows users to input text-based queries, which are then answered by the Ollama LLM. Both the queries and their corresponding responses are stored in ChromaDB for future use and analysis. This makes it easy to keep track of chat history and enhance the system's ability to process similar queries over time.
### Key Components
Streamlit — used to build the web interface.
ChromaDB — handles storing and querying data, including the chat history.
Ollama — generates answers to text queries using the LLM model.
### Features
Interactive Chat: Users can submit questions through a simple text input field.
LLM Integration: The app processes user queries using the Ollama LLM model.
Database Storage: Queries and their responses are stored in ChromaDB for future reference and easy retrieval.
Terminal Feedback: The terminal logs indicate successful document saving in the database.
### Requirements
To run this application on your local machine, you will need to install the following Python packages:
streamlit
chromadb
langchain-ollama
os (this is part of the Python standard library)
You can install all dependencies with the following command:
```bash
pip install -r requirements.txt
```
Alternatively, you can manually install each package:
```bash
pip install streamlit chromadb langchain-ollama
```
### Setup
### Clone the Repository:
You can clone the repository from GitHub:
```bash
git clone https://github.com/shyr1es/Advanced-Programming-Nurda-Dima-Ernur-.git
cd Advanced-Programming-Nurda-Dima-Ernur-
```
### Install Dependencies:
After cloning the repository, navigate to the project directory and install the dependencies:
```bash
pip install -r requirements.txt
```
### Run the Streamlit App:
To start the application, run the following command:
```bash
streamlit run app.py
```
### Using the App:
Open the app in your browser (usually at http://localhost:8501).
Enter a query in the text input field.
Press "Submit" to send the query to the LLM and receive a response.
Both the query and the response will be saved in ChromaDB for future reference.
### Terminal Feedback:
The terminal will show messages indicating that the query and response have been successfully saved in the database.
### Example of How It Works
User Query: "What is the weather like today?"
Model Response: "I don't have access to live data, but you can check the weather online."
Saved in ChromaDB: Both the user query and the response are stored in the database.
