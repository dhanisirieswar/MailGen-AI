
import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# =====================================
# 1. Load Environment Variables
# =====================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# =====================================
# 2. Page Configuration
# =====================================

st.set_page_config(
    page_title="MailGen AI",
    page_icon="🤖",
    layout="wide"
)

# =====================================
# 3. Check API Key
# =====================================

if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()

# =====================================
# 4. Initialize Gemini Client
# =====================================

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-3.8-flash"

# =====================================
# 5. Sidebar Navigation
# =====================================

with st.sidebar:

    st.title("🤖 MailGen AI")

    st.caption("Your AI-powered email assistant")

    st.divider()

    menu = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Generate Email",
            "Generate Reply",
            "About"
        ]
    )

    st.divider()

    st.caption("Powered by Gemini AI")


# =====================================
# 6. Dashboard
# =====================================

if menu == "Dashboard":

    st.title("Welcome to MailGen AI")

    st.write(
        "Generate professional emails and replies "
        "using Artificial Intelligence."
    )

    st.divider()

    st.subheader("What can you do?")

    col1, col2 = st.columns(2)

    with col1:
        st.info(
            "✉️ Generate professional emails "
            "based on your requirements."
        )

    with col2:
        st.info(
            "↩️ Generate suitable replies "
            "to emails you receive."
        )


# =====================================
# 7. Generate Email
# =====================================

elif menu == "Generate Email":

    st.title("✉️ Generate New Email")

    st.write(
        "Create professional emails in seconds using AI."
    )

    st.divider()

    with st.form("email_form"):

        recipient = st.text_input(
            "Recipient",
            placeholder="Example: HR Manager"
        )

        subject = st.text_input(
            "Email Subject",
            placeholder="Example: Job Application"
        )

        body = st.text_area(
            "Email Details",
            placeholder="Describe the information you want to include...",
            height=120
        )

        purpose = st.text_input(
            "Email Purpose",
            placeholder="Example: Apply for a job"
        )

        tone = st.selectbox(
            "Select Email Tone",
            [
                "Professional",
                "Friendly",
                "Casual",
                "Concise",
                "Formal"
            ]
        )

        generate_button = st.form_submit_button(
            "Generate Email",
            use_container_width=True
        )

    if generate_button:

        if not recipient.strip() or not body.strip() or not purpose.strip():

            st.error(
                "Please fill in the recipient, "
                "email details and email purpose."
            )

        else:

            prompt = f"""
            You are a professional email writing assistant.

            Generate an email using the following information:

            Recipient: {recipient}

            Subject: {subject if subject.strip() else "Suggest an appropriate subject"}

            Email Purpose: {purpose}

            Email Details: {body}

            Tone: {tone}

            Instructions:
            - Write a clear and well-structured email.
            - Include a suitable greeting.
            - Use the requested tone.
            - Include an appropriate closing.
            - Do not invent personal information.
            - Return the subject and email body.
            """

            try:

                with st.spinner("Gemini is generating your email..."):

                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=prompt
                    )

                    generated_email = response.text

                if generated_email and generated_email.strip():

                    st.success("Email generated successfully!")

                    st.subheader("Generated Email")

                    st.text_area(
                        "Your AI-generated email",
                        value=generated_email,
                        height=300
                    )

                else:

                    st.error("Gemini returned an empty response.")

            except Exception as e:

                st.error(f"Email generation failed: {e}")


# =====================================
# 8. Generate Reply
# =====================================

elif menu == "Generate Reply":

    st.title("↩️ Generate Email Reply")

    st.write(
        "Paste an email you received and generate a suitable reply."
    )

    st.divider()

    with st.form("reply_form"):

        received_email = st.text_area(
            "Received Email",
            placeholder="Paste the email you received here...",
            height=200
        )

        reply_purpose = st.text_input(
            "What do you want to communicate?",
            placeholder="Example: Accept the interview invitation"
        )

        reply_tone = st.selectbox(
            "Select Reply Tone",
            [
                "Professional",
                "Friendly",
                "Formal",
                "Concise"
            ]
        )

        reply_button = st.form_submit_button(
            "Generate Reply",
            use_container_width=True
        )

    if reply_button:

        if not received_email.strip() or not reply_purpose.strip():

            st.error(
                "Please provide the received email and reply purpose."
            )

        else:

            prompt = f"""
            You are a professional email reply assistant.

            Read the following email and generate an appropriate reply.

            Received Email:
            {received_email}

            Reply Purpose:
            {reply_purpose}

            Tone:
            {reply_tone}

            Instructions:
            - Write a relevant reply based on the received email.
            - Follow the requested tone.
            - Keep the response clear and professional.
            - Do not invent personal information.
            - Return only the email reply.
            """

            try:

                with st.spinner("Gemini is generating your reply..."):

                    response = client.models.generate_content(
                        model=MODEL_NAME,
                        contents=prompt
                    )

                    generated_reply = response.text

                if generated_reply and generated_reply.strip():

                    st.success("Reply generated successfully!")

                    st.subheader("Generated Reply")

                    st.text_area(
                        "Your AI-generated reply",
                        value=generated_reply,
                        height=250
                    )

                else:

                    st.error("Gemini returned an empty response.")

            except Exception as e:

                st.error(f"Reply generation failed: {e}")


# =====================================
# 9. About
# =====================================

elif menu == "About":

    st.title("About MailGen AI")

    st.write(
        """
        MailGen AI is an AI-powered application that helps
        users write professional emails and generate email
        replies using Google's Gemini AI.
        """
    )

    st.subheader("Technologies Used")

    st.write(
        """
        - Python
        - Streamlit
        - Google Gemini API
        - python-dotenv
        """
    )
