# 🎓 Sathyabama Chatbot

An AI-powered chatbot for **Sathyabama University** that answers university-related queries.  
Built with **Flask, NLTK, and Google Generative AI**.  

---

## 🚀 Features  
- Interactive chatbot interface (web-based).  
- Answers both static FAQs (faculty, departments, labs, etc.) and dynamic queries (time, AI responses).  
- Uses **Google Generative AI (Gemini)** for intelligent responses.  
- Simple Flask backend with HTML/JS frontend.  

---

## 📦 Installation  

```bash
# Clone the repository
git clone https://github.com/yourusername/sathyabama_chatbot.git
cd sathyabama_chatbot

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Download nltk data
python -m nltk.downloader punkt wordnet omw-1.4
