# AI-Powered Visual Data Analytics & Business Intelligence

## Milestone 3 — Practice Package

---

## 📁 Project Structure

```
AI-POWERED-VISUAL-DATA-ANALYTICS-AND-BUSINESS-INTELLIGENCE/
│
├── data/
│   └── safety_manual.pdf          ← Workplace safety manual used for document processing
│
├── src/
│   ├── documents/
│   │   ├── __init__.py
│   │   ├── chunker.py             ← Splits text into chunks for RAG
│   │   ├── document_loader.py     ← Loads PDF / DOCX / TXT files
│   │   ├── metadata.py            ← Extracts file & chunk metadata
│   │   └── text_cleaner.py        ← Cleans & normalises raw text
│   │
│   └── knowledge_base/
│       ├── __init__.py
│       └── database.py            ← ChromaDB vector knowledge base
│
├── best.pt                        ← Fine-tuned PPE YOLO model
|
├── ppe_model.py                   ← PPE detection wrapper
├── vision.py                      ← Real-time vision pipeline
├── yolo_model.py                  ← General YOLO detection wrapper
│
├── milestone3_practice.py         ← Main script for the PDF processing workflow
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add required files
| File | Description |
|---|---|
| `data/safety_manual.pdf` |Workplace safety manual used for PDF document processing |
| `best.pt` | PPE detection model weights used for inference |
| `yolov8n.pt` | Auto-downloaded on first run |

---

## 🚀 Running the Code

### Full pipeline (Milestone 3 practice)
```bash
python milestone3_practice.py
```

### Live webcam (PPE monitoring)
```bash
python vision.py
```

### Single image
```bash
python vision.py --image path/to/photo.jpg
```

### Video file
```bash
python vision.py --video path/to/clip.mp4
```

### Individual module tests
```bash
python src/documents/document_loader.py
python src/documents/text_cleaner.py
python src/documents/chunker.py
python src/knowledge_base/database.py
python yolo_model.py path/to/image.jpg
```

---

## 🧠 Pipeline Overview

```
safety_manual.pdf
      │
      ▼
DocumentLoader  →  raw text
      │
      ▼
TextCleaner     →  cleaned text
      │
      ▼
Chunker         →  list[TextChunk]
      │
      ▼
KnowledgeBase   →  embeddings stored in ChromaDB
      │
      ▼
kb.search(query) →  relevant chunks  →  LLM answer
```
---
## 📦 Module Reference

| Module | Purpose |
|---|---|
| `document_loader.py` | Loads the safety manual PDF and extracts text |
| `text_cleaner.py` | Cleans and normalizes extracted text |
| `chunker.py` | Splits document text into chunks |
| `metadata.py` | Extracts file metadata and text statistics |
| `database.py` | Stores document chunks in the ChromaDB knowledge base and supports search |
| `milestone3_practice.py` | Runs the complete PDF processing and knowledge-base workflow |
| `yolo_model.py` | Performs YOLO object detection |
| `ppe_model.py` | Performs PPE detection |
| `vision.py` | Handles image/video/webcam vision processing |

## ❓ Troubleshooting

| Error | Fix |
|---|---|
| `ModuleNotFoundError: ultralytics` | `pip install ultralytics` |
| `ModuleNotFoundError: chromadb` | `pip install chromadb` |
| `ModuleNotFoundError: sentence_transformers` | `pip install sentence-transformers` |
| `FileNotFoundError: best.pt` | Place your trained model in the project root |
| Camera not opening | Check `camera_id=0` in `vision.py`; try `camera_id=1` |
