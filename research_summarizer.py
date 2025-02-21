from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from tempfile import NamedTemporaryFile
import time
import re
import os
import traceback
import requests
import uuid

# Load embedding model
try:
    embedding_model_name = "sentence-transformers/all-mpnet-base-v2"
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model_name)
except Exception as e:
    print("failed at embedding model loading")
    print(str(e))

try:
    # Initialize the LLaMA model
    llm = Ollama(model="llama3.2")
except Exception as e:
    print("failed at llm model loading")
    print(str(e))

# Define LLM-Powered RAG Prompt
template="""
You are an advanced AI research assistant designed to help researchers understand academic papers efficiently. 
Given the extracted content from a research paper, perform the following tasks:

**Summary:** 
Provide a concise summary covering:
- Research problem & motivation  
- Key methods used  
- Main findings & conclusions  

**Key Insights:** 
- Important takeaways from the study  
- Implications of the findings  
- Potential applications of the research  

**Related Studies:** 
Suggest similar papers based on the study’s topic and methodology.

Note: 
Be detailed and precise. 
Provide your structured response in a clear bullet-point format. 
Also extract any impoetant links or urls mentioned.

Context: 
{context}

Provide your structured response below:
"""


def research_paper_summarizer(file):
    try:
        with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.file.read())
            temp_file_path = temp_file.name
        
        # Load the documents
        loader = PyPDFLoader(temp_file_path)
        documents = loader.load()

        # Split the document into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents=documents)

        vectorstore = FAISS.from_documents(docs, embeddings)

        # Create a retriever
        retriever = vectorstore.as_retriever()

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
        )

        output = qa_chain.invoke({"query": template})

        response=output["result"]

        # Cleanup temp file
        os.remove(temp_file_path)

        return {"summary": response}
    
    except Exception as e:
        print("failed at research_paper_summarizer")
        print(str(e))
