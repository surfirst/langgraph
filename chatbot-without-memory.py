from typing import Annotated, TypedDict
from langgraph.graph import Graph
from langchain_core.messages import HumanMessage, AIMessage
from llm_utils import get_llm
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 定义状态类型
class AgentState(TypedDict):
    messages: Annotated[list[HumanMessage | AIMessage], "对话历史"]

# 使用 get_llm() 获取 LLM
model = get_llm()

# 定义处理用户输入的函数
def call_model(state: AgentState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": messages + [response]}

# 创建工作流程图
workflow = Graph()

# 添加节点
workflow.add_node("chat", call_model)

# 设置工作流程
workflow.set_entry_point("chat")
workflow.set_finish_point("chat")

# 编译工作流程
chain = workflow.compile()

# 使用示例
messages = [HumanMessage(content="你好！")]
result = chain.invoke({"messages": messages})
print(result["messages"][-1].content)
