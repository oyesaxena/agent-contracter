# Document Automation Agent

## Overview

Document Automation Agent is an AI-powered workflow system that automates the processing of business documents such as contracts, agreements, and vendor documents.

The system uses a LangGraph-based orchestration workflow to:

* Extract document text and metadata
* Classify document type
* Extract structured business entities
* Validate extracted information
* Calculate confidence scores
* Determine whether a document can be automatically processed or requires manual review

---

## Business Problem

Organizations receive large volumes of documents that require manual review and data entry.

Typical challenges include:

* Manual document classification
* Data extraction from contracts
* Human review bottlenecks
* Inconsistent processing
* Lack of auditability

This solution automates the workflow while maintaining explainability and confidence-based review decisions.

---

## Solution Architecture

```text
                        ┌───────────────────┐
                        │   Streamlit UI    │
                        └─────────┬─────────┘
                                  │
                                  ▼
                        ┌───────────────────┐
                        │     FastAPI       │
                        └─────────┬─────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │  PDF Processing Layer  │
                     │ LangChain PDF Loader   │
                     └─────────┬──────────────┘
                               │
                               ▼
                    ┌─────────────────────────┐
                    │     LangGraph Flow      │
                    └─────────┬───────────────┘
                              │
      ┌───────────────────────┼───────────────────────┐
      ▼                       ▼                       ▼

┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│Classification│ -> │ Extraction   │ -> │ Validation   │
│   Agent      │    │   Agent      │    │   Agent      │
└──────────────┘    └──────────────┘    └──────────────┘
                                               │
                                               ▼

                                    ┌─────────────────┐
                                    │ Confidence Agent│
                                    └────────┬────────┘
                                             │
                                             ▼

                                     ┌─────────────┐
                                     │   Router    │
                                     └──────┬──────┘
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼

              Auto Approve                               Needs Review
```

---

## Workflow

### 1. Document Upload

Users upload PDF documents through the Streamlit interface.

### 2. PDF Processing

LangChain PDF Loader extracts:

* Text content
* Page count
* File size
* Author information (when available)
* Document metadata

### 3. Classification Agent

Determines:

* Document type
* Classification confidence
* Reasoning

### 4. Extraction Agent

Extracts structured information:

* Parties
* Effective Date
* Expiration Date
* Contract Value
* Obligations

### 5. Validation Agent

Validates:

* Required fields
* Missing information
* Schema compliance

### 6. Confidence Agent

Calculates:

* Overall confidence score
* Review recommendation

### 7. Router

Routes workflow outcome:

* Complete
* Needs Review

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI

### Workflow Orchestration

* LangGraph

### LLM Framework

* LangChain

### LLM Provider

* Google Gemini

### Document Processing

* LangChain PDF Loader
* PyPDF

---

## Project Structure

```text
backend/

├── app/
│
├── agents/
│   ├── classification_agent.py
│   ├── extraction_agent.py
│   ├── validation_agent.py
│   └── confidence_agent.py
│
├── api/
│   └── routes/
│
├── core/
│
├── prompts/
│
├── schemas/
│
├── services/
│   ├── llm/
│   └── pdf_service.py
│
├── workflows/
│   ├── graph.py
│   ├── router.py
│   └── state.py
│
└── main.py

frontend/
└── app.py
```

---

## Environment Variables

```env
GOOGLE_API_KEY=your_api_key

MODEL_NAME=gemini-2.5-flash

CONFIDENCE_THRESHOLD=0.8
```

---

## Local Development

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

### Frontend

```bash
cd frontend

streamlit run app.py
```

---

## Deployment

### Backend

Deploy FastAPI on Render.

### Frontend

Deploy Streamlit application on Streamlit Cloud.

---

## Future Enhancements

* Human Review Queue
* PostgreSQL Persistence
* Azure AI Search Integration
* Workflow Analytics
* Multi-Tenant Support
* Audit Trail & Observability
* Role-Based Access Control

---

## Author

Abhishek Saxena

AI Solutions Engineering Assessment Submission
