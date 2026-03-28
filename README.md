# 🤖 AI Resume Writer (Local AI)

## 📌 Overview

This project is an AI-powered Resume Generator that creates professional, ATS-friendly resumes based on user input.
It uses a local Large Language Model (LLM) via LM Studio, so no paid API is required.


## 🚀 Features

* Generate professional resumes using AI
* Input personal details, skills, projects, and education
* Phone number validation (10-digit format)
* Option to edit resume before downloading
* Download resume as PDF
* Runs completely on local AI (no internet dependency for AI)

---

## 🧠 Tech Stack

* Python
* Streamlit (UI)
* LM Studio (Local LLM)
* Requests (API calls)
* FPDF (PDF generation)

---

## ⚙️ How It Works

1. User enters details in the form
2. Data is sent to a local AI model via API
3. AI generates a structured resume
4. Resume can be downloaded as PDF

---

## 🖥️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/ai-resume-writer.git
cd ai-resume-writer


### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt


### 4. Start LM Studio

* Open LM Studio
* Load model (e.g., google/gemma-3-1b)
* Start local server at:


http://127.0.0.1:1234


### 5. Run the app

streamlit run app.py

This project is open-source and free to use.
