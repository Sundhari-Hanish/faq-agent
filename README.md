**Support Assistant (FAQ Bot)**



**Overview**
A lightweight FAQ-based support assistant built with Streamlit. The app finds the best matching FAQ for a user question and returns the answer.



**Live demo**
Demo URL: https://faq-agent-gykdsmecmhkfu4vkfouamw.streamlit.app/



**Features**
Keyword overlap retrieval baseline (simple matching)

(Optional) AI-based semantic retrieval
Clean and simple UI where users can ask questions



**Tech stack**

&nbsp;-Python 3.10+
 -Streamlit
 -numpy
 -(Optional) OpenAI for embeddings or generation



**Files included**

-app.py — Main Streamlit app
-faqs.json — List of FAQ questions and answers
-requirements.txt — Python dependency list
-assets/architecture.png — Architecture diagram



**How to run locally**

1. Clone the repo
   git clone https://github.com/Sundhari-Hanish/faq-agent.git
   cd faq-agent
2. Create and activate virtual environment (Windows)
   python -m venv venv
   venv\\Scripts\\activate
3. Install dependencies
   pip install -r requirements.txt
4. Run the app
   streamlit run app.py
5. 

**Then open:**
http://localhost:8501



**Limitations**

-Small FAQ dataset
-Simple keyword matching (no deep understanding of meaning)
-Option B requires API keys and costs



**Future Improvements**

-Add admin panel to edit FAQs
-Use a vector database for better search
-Add user accounts and history
-Improve UI

