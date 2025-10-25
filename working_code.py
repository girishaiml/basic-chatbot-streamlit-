import streamlit as st
from datetime import datetime

# Page setup
st.set_page_config(page_title="AI Lab Chatbot - Group 8", page_icon="🤖")

# Title
st.title("🤖 AI Lab Chatbot - Group 8")
st.write("Welcome to our AI Assistant project for the Machine Learning Fundamentals Lab (AIML-500).")

# Chat history setup
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past messages
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
prompt = st.chat_input("Ask me anything about AI or ML!")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Simple AI logic ---
    text = prompt.strip().lower()
    if text in {"hi", "hello", "hey", "yo", "hola"}:
        response = "Hey there! 👋 I’m your Group 8 AI Assistant — ready to chat about Machine Learning, AI tools, and ideas!"
    elif "group" in text:
        response = "This chatbot was proudly built by **Group 8** members: **Girish**, **Tesleem**, **Nathan**, and **Mohsin** 🎯"
    elif "who made you" in text or "your team" in text:
        response = "I was created by Group 8 — Girish, Tesleem, Nathan, and Mohsin — as part of our Machine Learning Fundamentals Lab project."
    else:
        response = (
            f"I'm glad you asked about **{prompt}**! 🤓 I'm a simple AI assistant designed using Streamlit "
            "to demonstrate generative AI capabilities. I can discuss AI concepts, give definitions, "
            "and help brainstorm ideas for projects or research."
        )

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state["messages"].append(
        {"role": "assistant", "content": response})

# Sidebar details
st.sidebar.header("📘 About this Project")
st.sidebar.write(f"""
**Course:** Machine Learning Fundamentals (AIML-500)  
**Project:** AI Lab - Chatbot (Group 8)  
**Team Members:**  
- Girish  
- Tesleem  
- Nathan  
- Mohsin  

**Goal:** Build and deploy a simple AI chatbot using Streamlit.  
**Tech Stack:** Streamlit (Python)  
**Created:** {datetime.now().strftime("%B %d, %Y")}
""")
