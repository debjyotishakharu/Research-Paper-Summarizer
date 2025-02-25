# AI-Powered Research Assistant

## Overview
The **AI-Powered Research Assistant** is a tool designed to help researchers efficiently summarize academic papers, extract key insights, and suggest related studies using **Retrieval-Augmented Generation (RAG)** pipelines. It utilizes **LangChain**, **FastAPI**, **HuggingFace Embeddings**, and **Ollama LLM** to process and analyze research content.

## Features
- **PDF Research Paper Summarization**: Upload a PDF to generate a structured summary.
- **Web-Based Research Summarization**: Provide a URL to extract and summarize research articles.
- **Key Insights Extraction**: Identify important takeaways and implications from papers.
- **Related Studies Suggestion**: Suggest similar papers based on content.

## Technologies Used
- **LangChain**: For document processing, retrieval, and chaining LLMs.
- **FastAPI**: To provide an API interface for research paper summarization.
- **HuggingFace Embeddings**: For embedding and semantic search.
- **Ollama LLM**: To generate structured summaries and insights.
- **FAISS**: For efficient document retrieval.

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Pip
- Ollama (for running the LLaMA model)

### Steps
1. Clone the repository.
   
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```sh
   python main.py
   ```

## Usage
### API Endpoints
- **Upload a PDF for Summarization**
  - Input: PDF file
  - Output: Structured summary with key insights and related studies

- **Summarize a Research Paper from the Web**
  - Input: URL of the research article
  - Output: Summary, key insights, and related papers

## Future Improvements
- Support for more document formats (DOCX, TXT, etc.)
- Enhanced retrieval accuracy using advanced embeddings
- Integration with research databases for real-time paper recommendations

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the open-source community and contributors of LangChain, HuggingFace, FAISS, and Ollama.

