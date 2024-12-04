# LangGraph 聊天机器人示例

本仓库包含了使用 LangGraph 和 LangChain 构建的各种聊天机器人示例。

## 环境要求

- Python 3.8+
- pip（Python 包管理器）

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/langgraph.git
cd langgraph
```

2. 创建并激活虚拟环境（推荐）：
```bash
python -m venv venv
source venv/bin/activate  # Windows系统使用: venv\Scripts\activate
```

3. 安装依赖包：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
```bash
cp .env.example .env
```
然后编辑 `.env` 文件，添加以下 API 密钥：
- GOOGLE_API_KEY：Google 生成式 AI 的 API 密钥
- TAVILY_API_KEY：Tavily 搜索功能的 API 密钥
- OPENAI_API_KEY：OpenAI 的 API 密钥（如果使用 OpenAI 模型）

## 示例程序

1. `simple_chatbot.py`：基础聊天机器人实现
2. `memory_chatbot.py`：带有对话记忆功能的聊天机器人
3. `chatbot-without-memory.py`：无记忆功能的简单聊天机器人
4. `chatbot-with-human.py`：有人类干预的聊天机器人
5. `chatbot-with-tools-n-memory.py`：带有工具和记忆功能的高级聊天机器人

## 运行示例

要运行任何示例聊天机器人，使用 Python 执行相应的脚本：

```bash
python simple_chatbot.py
# 或者
python memory_chatbot.py
# 或者其他示例脚本
```

每个示例都展示了 LangGraph 和 LangChain 集成的不同功能和特性。

## 许可证

本项目遵循仓库中 LICENSE 文件的条款。