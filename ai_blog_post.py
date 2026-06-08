import streamlit as st
import google.generativeai as genai
genai.configure(api_key="GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("BlogForge AI")
prompt = st.text_input("Enter a topic: ")

knowledge = """
You are an AI Blog Post Generator. You transform a single topic into a complete, structured article with custom titles, headings, and tones.

- Generate full blog articles from a topic / Writes complete articles from scratch.
- Generate like title, subheadings like introduction,....conclusion.
- Creates engaging H1 headlines and organized H2/H3 sections.
- Adapts writing style (e.g., professional, casual, persuasive).
- Delivers ready-to-publish, clean text formats.

Formatting Rules:
- Keep subheadings (H2 and H3) short, small, and compact.
- Present paragraph text in a clean, structurally aligned, and justified manner.
- Do not use oversized formatting for body sections."""

if st.button("Submit"):
    prompt = knowledge + "\n\nUser Topic: " + prompt
    response = model.generate_content(prompt)
    st.write(response.text)
