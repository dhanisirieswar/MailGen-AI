# 🤖 MailGen AI

An AI-powered email assistant built using Python, Streamlit, and Google's Gemini API. It helps users generate professional emails and relevant email replies based on their requirements.

## 🚀 Live Demo

[Try MailGen AI](https://mailgen-aigit-peo5am9t7cbjxcpjxr2kyq.streamlit.app/)

## ✨ Features

- **Email Generation:** Generate professional emails based on recipient, subject, purpose, and tone.
- **Email Reply Generation:** Create relevant replies using received email content.
- **Multiple Writing Tones:** Professional, Friendly, Casual, Concise, and Formal.
- **AI-Powered Responses:** Uses Google Gemini API to generate content.
- **Interactive UI:** User-friendly interface built with Streamlit.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- python-dotenv

## 📁 Project Structure

```text
MailGen-AI/
│
├── app.py
├── requirements.txt
├── .gitignore
└── .env
```

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/dhanisirieswar/MailGen-AI.git
```

2. Navigate to the project directory:

```bash
cd MailGen-AI
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_actual_api_key
```

7. Run the application:

```bash
streamlit run app.py
```

## 🔐 API Configuration

Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

For local execution, configure it in `.env`. For Streamlit Cloud, configure it under App Settings → Secrets.

**Never upload your actual API key to GitHub.**

## 👨‍💻 Author

**Dhanisiri Eswar**

[GitHub Profile](https://github.com/dhanisirieswar)
