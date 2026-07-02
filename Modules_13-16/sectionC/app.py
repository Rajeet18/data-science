import streamlit as st
from chains import agent, memory
from utils import search_menu

st.set_page_config(page_title="QuickBite AI")

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
st.sidebar.title("QuickBite Settings")

address = st.sidebar.text_input("Delivery Address")
diet = st.sidebar.selectbox(
    "Diet Preference",
    ["Vegetarian", "Non-Vegetarian"]
)

st.session_state["address"] = address
st.session_state["diet"] = diet

# Clear Chat
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    memory.clear()
    st.rerun()

st.title("🍔 QuickBite AI")

# Display Chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User Input
user_input = st.chat_input("Ask about food or delivery...")

if user_input:

    # Display User Message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Search Menu
    menu = search_menu(
        st.session_state["diet"],
        user_input
    )

    menu_text = "\n".join(
        [
            f"{i['name']} - ₹{i['price']}"
            for i in menu
        ]
    )

    # Prompt
    prompt = f"""
Delivery Address:
{st.session_state['address']}

Diet:
{st.session_state['diet']}

Recommended Menu:
{menu_text}

User:
{user_input}
"""

    # LangChain Agent
    response = agent.run(prompt)

    # Display Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)