# ⚖️ Legal Document Simplifier

An AI-powered Legal Document Analysis System designed specifically for Indian legal documents. The platform enables users to upload contracts, agreements, notices, terms & conditions, legal documents, PDFs, DOCX files, and images, then automatically generates plain-language summaries, identifies risky clauses, performs legal analysis using Indian laws, and provides downloadable professional reports.

---

## 🚀 Features

### 📄 Multi-Format Document Processing

* PDF support
* DOCX support
* Image support (PNG, JPG, JPEG)
* OCR-based text extraction

### 🤖 AI-Powered Analysis

* Executive Summary Generation
* Legal Clause Identification
* Risk Assessment
* Red Flag Detection
* Legal Recommendations

### ⚖️ Indian Law RAG System

* Bharatiya Nyaya Sanhita (BNS)
* Indian Contract Act
* Information Technology Act
* Consumer Protection Act
* Labour Laws
* Constitutional References

### 🔍 Semantic Search

* Sentence Transformers Embeddings
* FAISS Vector Search
* Context-Aware Retrieval

### 📊 Professional Reporting

* Risk Score Calculation
* Clause Severity Categorization
* PDF Report Generation
* Downloadable Analysis Reports

### 🌐 Modern Web Application

* Streamlit Frontend
* Interactive Dashboard
* Risk Visualization
* Document Preview
* Professional UI

---

## 🛠 Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### OCR

* EasyOCR

### LLM

* Qwen2.5-7B-Instruct GGUF

### Embeddings

* sentence-transformers/all-MiniLM-L6-v2

### Vector Database

* FAISS

### Framework

* LangChain

### PDF Generation

* ReportLab

### Legal Knowledge Base

* Indian Laws Dataset

---

## 📂 Project Structure

legal-document-simplifier/

├── app.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── assets/

│ └── style.css

│

├── data/

│ ├── laws/

│ ├── uploads/

│ └── processed/

│

├── models/

│ └── qwen2.5-7b.gguf

│

├── modules/

│ ├── pdf_parser.py

│ ├── docx_parser.py

│ ├── ocr_parser.py

│ ├── document_loader.py

│ ├── law_loader.py

│ ├── chunker.py

│ ├── embeddings.py

│ ├── vector_store.py

│ ├── chunk_storage.py

│ ├── llm.py

│ ├── rag_pipeline.py

│ ├── legal_rag.py

│ ├── legal_analyzer.py

│ ├── red_flag_engine.py

│ ├── clause_explainer.py

│ ├── summarizer.py

│ ├── legal_report.py

│ └── report_generator.py

│

├── vector_db/

│ ├── document.index

│ ├── law.index

│ ├── chunks.pkl

│ └── law_chunks.pkl

│

├── reports/

├── uploads/

└── tests/

---

## ⚙️ Installation

### Clone Repository

git clone https://github.com/yourusername/legal-document-simplifier.git

cd legal-document-simplifier

### Create Virtual Environment

python -m venv nameenv

### Activate Environment

Windows

nameenv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## 📥 Download Qwen Model

Download:

Qwen2.5-7B-Instruct-Q4_K_M.gguf

Store:

models/qwen2.5-7b.gguf

---

## ▶️ Run Application

streamlit run app.py

---

## 📈 Workflow

Upload Document

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

FAISS Retrieval

↓

Indian Law Retrieval

↓

Qwen Analysis

↓

Risk Detection

↓

Legal Report Generation

↓

PDF Export

---

## 🎯 Future Improvements

* Legal Chat Assistant
* Clause Highlighting in Original PDF
* Case Law Retrieval
* Multi-Language Support
* Legal Compliance Scoring
* Named Entity Recognition
* Multi-Document Comparison
* User Authentication
* Cloud Deployment
* Citation-Based Legal Analysis

---

## 👨‍💻 Author

Shivam Salve

Built using Qwen2.5, FAISS, Streamlit, LangChain, and Indian Law RAG.

