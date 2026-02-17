
from langchain.chat_models import ChatOpenAI

def scheduling_agent():
    llm = ChatOpenAI(model="gpt-4")
    return llm
