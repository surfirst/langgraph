from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from llm_utils import get_llm

# Define state type
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize memory saver and LLM
memory = MemorySaver()
llm = get_llm()

def chatbot(state: State):
    """Chatbot that responds to messages with memory"""
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

# Create and compile graph
graph = (
    StateGraph(State)
    .add_node("chatbot", chatbot)
    .add_edge(START, "chatbot")
    .compile(checkpointer=memory)
)

def chat(thread_id: str = "default"):
    """Run the chat interface with memory"""
    config = {"configurable": {"thread_id": thread_id}}

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
            
        # Process input through graph - memory is handled automatically
        for output in graph.stream({"messages": [("human", user_input)]}, config=config):
            for value in output.values():
                print("Assistant:", value["messages"][-1].content)

if __name__ == "__main__":
    chat() 