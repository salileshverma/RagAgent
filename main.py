from phi.agent import Agent
from phi.model.groq import Groq
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.lancedb import LanceDb, SearchType
from phi.embedder.base import Embedder

from sentence_transformers import SentenceTransformer
from pydantic import PrivateAttr

import os
from dotenv import load_dotenv


class LocalHFEmbedder(Embedder):

    _model: SentenceTransformer = PrivateAttr()

    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2", device=None):
        super().__init__(id=model_name)
        self._model = SentenceTransformer(model_name, device=device)

    def get_embedding(self, text: str):
        """Return only the embedding (list of floats)."""
        return self._model.encode([text], normalize_embeddings=True)[0].tolist()

    def get_embedding_and_usage(self, text: str):
        """Return embedding + dummy usage dict (to satisfy Phi API)."""
        embedding = self.get_embedding(text)
        usage = {"tokens": len(text.split())}
        return embedding, usage


def main():

    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

    print("Groq API Key Loaded:", bool(groq_api_key))
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")


    print("Setting up Groq model...")
    groq_model = Groq(
        id="llama-3.1-8b-instant",
        api_key=groq_api_key,
    )
    print("Groq model ready!")


    print("Setting up LanceDB...")
    db_path = "./lancedb_data"
    embedder = LocalHFEmbedder(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_db = LanceDb(
        table_name="recipes",
        uri=db_path,
        search_type=SearchType.vector,
        embedder=embedder,
    )
    print("LanceDB setup complete!")

    #Load PDF into knowledge base
    print("Creating knowledge base...")
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=vector_db,
    )
    print("Knowledge base created!")

    # Only run once to create vectors in LanceDB
    print("\n" + "-" * 50)
    print("Loading PDF and creating embeddings (first run may take a few minutes)…")
    print("-" * 50)

    try:
        knowledge_base.load()
        print("✅ Knowledge base loaded successfully!")
    except Exception as e:
        print(f"❌ Error loading knowledge base: {e}")
        raise

 #Create Agent
    print("\nCreating RAG agent...")
    agent = Agent(
        model=groq_model,
        knowledge=knowledge_base,
        show_tool_calls=True,
        markdown=True,
    )
    print("✅ Agent created successfully!")

    #Ask a question
    print("\n" + "=" * 60)
    print("🍲 ASKING QUESTION TO THE RAG AGENT")
    print("=" * 60 + "\n")

    question = "How do I make chicken and galangal in coconut milk soup?"
    print(f"Question: {question}\n")

    agent.print_response(
        question,
        stream=True,
    )

    print("\n" + "=" * 60)
    print("✅ RAG Agent Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
