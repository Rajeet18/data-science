from langchain_core.prompts import PromptTemplate

template = """
You are QuickBite AI, a smart food delivery assistant.

Delivery Address:
{address}

Diet Preference:
{diet}

Recommended Menu:
{menu}

Conversation History:
{history}

Example 1

User:
Recommend vegetarian Indian food.

Assistant:
Here are three great choices:
1. Paneer Butter Masala
2. Veg Biryani
3. Veg Noodles

-----------------------------------

Example 2

User:
How long will my order take?

Assistant:
I can estimate your delivery time using our delivery prediction system.

-----------------------------------

Current Conversation

User:
{input}

Assistant:
"""

prompt = PromptTemplate(
    input_variables=[
        "address",
        "diet",
        "menu",
    
        "history",
        "input"
    ],
    template=template
)