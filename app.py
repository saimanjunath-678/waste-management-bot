import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    system_instruction="""
    You are a Waste Management and Recycling Education Bot.

    Your role is to ONLY explain:
    - Waste segregation rules
    - Recycling processes
    - Composting methods
    - Hazardous waste awareness
    - Environmental best practices

    You MUST NOT:
    - Schedule waste pickups
    - Accept complaints
    - Impose fines or penalties
    - Provide enforcement or legal instructions

    If a user asks for restricted actions, politely refuse and redirect to educational information only.
    """
)

# Streamlit UI
st.set_page_config(page_title="Waste Management Explainer Bot", page_icon="🌍")

st.title("🌱 Waste Management & Recycling Explainer Bot")
st.subheader("Learn how waste is segregated, recycled, and managed responsibly")

user_query = st.text_input("Ask your question about waste management:")

if st.button("Explain"):
    if user_query.strip():
        response = model.generate_content(user_query)
        st.success(response.text)
    else:
        st.warning("Please enter a question.")
