#Rag-Agent
<img width="2608" height="942" alt="Screenshot 2025-08-25 at 9 32 58 PM" src="https://github.com/user-attachments/assets/2d378ebc-aa8e-4cde-be2b-e2d7768dfd26" />
<img width="2614" height="1032" alt="Screenshot 2025-08-25 at 9 33 14 PM" src="https://github.com/user-attachments/assets/3ce1c55f-a5b7-4d5d-812e-27a174829d60" />


🍲 RAG Agent with Groq LLM + LanceDB

A Retrieval-Augmented Generation (RAG) agent that can read documents (e.g., PDFs of recipes), store them in a vector database (LanceDB), and answer natural language queries using the Groq LLM for fast, context-aware responses.

📌 Features

📄 Document ingestion (PDF parsing)

🔎 Semantic search using embeddings stored in LanceDB

🧠 Retrieval-Augmented Generation with Groq LLM

⚡ Fast & accurate answers with contextual knowledge

🍴 Demo use case: Recipe Assistant that extracts ingredients, instructions, and suggestions from a cooking PDF

#installation 
# Clone repo
git clone https://github.com/yourusername/rag-agent-groq.git
cd rag-agent-groq

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

📂 Project Structure
├── main.py              # Entry point
├── requirements.txt     # Dependencies
├── README.md            # Documentation
├── .env.example         # Example env vars
├── lancedb_data/        # Vector database files

Pipeline Architecture

<img width="1536" height="1024" alt="ChatGPT Image Aug 25, 2025, 11_54_39 PM" src="https://github.com/user-attachments/assets/879d4d5e-6d8a-4d5c-8878-dd3ccf17a493" />

🔮 Future Improvements

Support for multiple document formats (Word, HTML, Markdown)

Web-based interface (Streamlit/Gradio)

Multi-turn conversations with memory

Fine-grained filtering (by topic, section, metadata)
