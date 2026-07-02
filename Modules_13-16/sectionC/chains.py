from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI

from tools import get_delivery_estimate

memory = ConversationBufferMemory(
    memory_key="history",
    return_messages=True
)

llm=Ollama(
    model="llama3.1",
    temperature=0
)

agent = initialize_agent(
    tools=[get_delivery_estimate],
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)