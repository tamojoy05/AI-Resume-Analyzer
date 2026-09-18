# 🤖 AI Resume Analyzer

An AI-powered web application that analyzes resumes against a given job description and provides insights into skills, semantic similarity, ATS keywords, resume information, and improvement recommendations.

## 🚀 Live Demo

**Streamlit App:**  https://ai-resume-analyzer-yni96hsrkjzngtxoyifhvn.streamlit.app/#ai-resume-analyzer

## 📌 Project Overview

The AI Resume Analyzer helps candidates understand how well their resume matches a specific job description.

The application extracts important information from an uploaded resume, identifies relevant skills, compares the resume with the job description, and generates different matching scores.

## ✨ Features

* 📄 PDF and DOCX resume upload
* 👤 Resume information extraction

  * Name
  * Email
  * Phone number
  * Education
  * Projects
  * Professional experience
  * Certifications
* 🛠️ Automatic skill extraction
* 🔍 Matching and missing skill detection
* 🤖 AI-based semantic similarity analysis
* 🔑 ATS keyword analysis
* 🎯 Overall resume-job match score
* 📊 Resume quality checks
* 💡 Personalized resume recommendations
* 🌐 Streamlit web interface

## 🧠 How It Works

```text
Resume Upload
      ↓
Resume Text Extraction
      ↓
Resume Information Extraction
      ↓
Skill Extraction
      ↓
Job Description Analysis
      ↓
Semantic Similarity Analysis
      ↓
Skill & ATS Keyword Matching
      ↓
Overall Match Score
      ↓
Recommendations
```

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Sentence Transformers
* PyPDF2
* python-docx
* spaCy
* NLTK

## 🤖 AI Model

The project uses the **Sentence Transformers** model:

```text
all-MiniLM-L6-v2
```

The model converts the resume and job description into numerical embeddings and uses cosine similarity to calculate semantic similarity.

## 📊 Matching Scores

The application provides:

### AI Semantic Match

Measures the semantic similarity between the resume and the job description.

### Skill Match

Compares detected resume skills with skills identified from the job description.

### ATS Keyword Match

Identifies relevant keywords and phrases shared between the resume and job description.

### Overall Match

The current application calculates the overall score using:

```text
Overall Match =
(Semantic Match × 60%)
+
(Skill Match × 40%)
```

## 📁 Project Structure

```text
AI Resume Analyzer/
│
├── app.py
├── resume_parser.py
├── resume_info_extractor.py
├── skill_extractor.py
├── job_matcher.py
├── recommendations.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/tamojoy05/AI-Resume-Analyzer.git
```

### 2. Open the project

```bash
cd AI-Resume-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

The application will open locally in your browser.

## 🎯 Use Case

This project can help students and job seekers:

* Understand how closely their resume matches a job description
* Identify missing technical skills
* Find important ATS keywords
* Review the structure and completeness of their resume
* Improve resume-job alignment

## 🔮 Future Improvements

* Advanced NLP-based skill extraction
* Better multi-word keyword detection
* Resume section quality scoring
* Experience relevance analysis
* Job recommendation system
* Multiple resume comparison
* Resume improvement suggestions using generative AI
* Support for additional resume formats

## 👨‍💻 Author

**Tamojoy Sanyal**

B.Tech — Artificial Intelligence & Machine Learning

GitHub: https://github.com/tamojoy05
