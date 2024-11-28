from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from llm_utils import get_llm

# Define state type
class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    """Simple chatbot that responds to messages"""
    llm = get_llm()
    return {"messages": [llm.invoke(state["messages"])]}

# Create and compile graph
graph = (
    StateGraph(State)
    .add_node("chatbot", chatbot)
    .add_edge(START, "chatbot")
    .compile()
)

def chat():
    """Run the chat interface"""
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
            
        # Process input through graph
        for output in graph.stream({"messages": [("user", user_input)]}, {}):
            for value in output.values():
                print("Assistant:", value["messages"][-1].content)

if __name__ == "__main__":
    chat() 