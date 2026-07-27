# Multi-PDF Chat AI

Chat with multiple PDF documents using natural language. Ask questions and get answers based on the content of your uploaded PDFs — powered by Groq LLM and local embeddings.

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red) ![LangChain](https://img.shields.io/badge/LangChain-0.2-green)

---

## How It Works

1. Upload one or more PDF files
2. Click **Process** — the app extracts text, splits it into chunks, and builds a local vector store
3. Ask any question in the chat — the app finds relevant chunks and sends them to Groq LLM for an answer
4. The conversation keeps memory so follow-up questions work naturally

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| PDF Parsing | PyPDF2 |
| Text Splitting | LangChain CharacterTextSplitter |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) — runs locally |
| Vector Store | FAISS (local) |
| LLM | Groq API (`llama-3.1-8b-instant`) — free tier |
| Memory | LangChain ConversationBufferMemory |

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/sheikh-saifi/multi-pdf-chat-ai.git
cd multi-pdf-chat-ai
```

### 2. Create a virtual environment
```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install streamlit==1.32.0 PyPDF2==3.0.1 python-dotenv==1.0.0 faiss-cpu==1.7.4 \
  sentence-transformers==2.7.0 transformers==4.41.2 "numpy<2" torch==2.2.2 \
  pycryptodome==3.20.0 "langchain==0.2.17" "langchain-core==0.2.43" \
  "langchain-community==0.2.19" "langchain-groq==0.1.9" "langchain-text-splitters==0.2.4"
```

### 4. Add your Groq API key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free API key at [console.groq.com](https://console.groq.com)

### 5. Run the app
```bash
streamlit run app.py
```

---

## Project Structure

```
multi-pdf-chat-ai/
├── app.py              # Main application
├── htmlTemplates.py    # Chat UI templates
├── .env                # API keys (not committed)
├── .gitignore
└── requirements.txt
```

---

## Notes

- Embeddings run fully locally — no data is sent to any embedding API
- Only the question + relevant PDF chunks are sent to Groq for answering
- Groq free tier is sufficient for this project
