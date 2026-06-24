# 🔍 Hybrid AI Search Engine

A dual-engine web application built in Python that allows users to seamlessly toggle between exact keyword matching and semantic conceptual search.

## ✨ Features
* **Dual-Engine Architecture:** Switch between traditional exact-match routing and AI-driven conceptual search.
* **Web Interface:** Fully functional local web server built with Flask, featuring a clean HTML toggle UI.
* **Exact Match (TF-IDF):** Custom-built Term Frequency-Inverse Document Frequency algorithm for high-precision string matching.
* **Semantic Search (LSA):** Utilizes `scikit-learn` (Singular Value Decomposition) to find conceptually related documents, even if exact keywords are missing.

## 💻 Technologies Used
* **Backend:** Python, Flask
* **Machine Learning:** `scikit-learn` (`TfidfVectorizer`, `TruncatedSVD`)
* **Frontend:** HTML5

## 📁 Project Structure

├── app.py
├── main.py
├── templates/
│   └── index.html
└── documents/
    ├── chemistry.txt
    ├── football.txt
    └── physics.txt

## 🚀 How to Run
1. Ensure your Python virtual environment is active.
2. Install the required dependencies: 
   `pip install flask scikit-learn`
3. Start the local server: 
   `python app.py`
4. Open your web browser and navigate to: 
   `http://127.0.0.1:5000`

## 📈 Project Evolution

### Version 1.0 (Legacy)
* Basic TF-IDF exact-match algorithm running exclusively in the command line interface.

### Version 2.0 (Current)
* Migrated to a Flask web architecture. Implemented Latent Semantic Analysis (LSA) using `scikit-learn` to allow for baseline conceptual matching alongside the custom TF-IDF engine. 
* *Scale Update:* Integrated a sliding-window text chunker (500 chars/50 overlap) with result deduplication. This prevents the transformer model from truncating large files and dramatically increases the precision of semantic retrieval without crashing local memory.

### Version 3.0 (Upcoming)
* **Pre-Trained AI Upgrade:** Replacing `scikit-learn` with Hugging Face `sentence-transformers` for true global vocabulary awareness and synonym detection.
* **UI Polish:** Full CSS styling for a modern, responsive layout.

