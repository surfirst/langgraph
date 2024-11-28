from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Load environment variables
load_dotenv()

def get_llm():
    """根据环境变量选择使用的LLM"""
    model_type = os.getenv("MODEL_TYPE", "").lower()  # 默认为空字符串
    print("model_type:", model_type)
    
    if model_type == "azure":
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION")
        
        print(f"Azure OpenAI Configuration:")
        print(f"Endpoint: {endpoint}")
        print(f"Deployment Name: {deployment_name}")
        print(f"API Version: {api_version}")
        print(f"API Key: {api_key[:6]}..." if api_key else "API Key: None")
        
        return AzureChatOpenAI(
            openai_api_key=api_key,
            azure_endpoint=endpoint,
            deployment_name=deployment_name,
            openai_api_version=api_version,
            temperature=0
        )
    elif model_type == "gemini":
        api_key = os.getenv("GOOGLE_API_KEY")
        model_name = os.getenv("GEMINI_MODEL", "gemini-pro")
        
        print(f"Gemini Configuration:")
        print(f"Model: {model_name}")
        print(f"API Key: {api_key[:6]}..." if api_key else "API Key: None")
        
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=0
        )
    else:  # OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        api_base = os.getenv("OPENAI_API_BASE")
        model_name = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
        
        print(f"OpenAI Configuration:")
        print(f"Model: {model_name}")
        print(f"API Base: {api_base}")
        print(f"API Key: {api_key[:6]}..." if api_key else "API Key: None")
        
        return ChatOpenAI(
            model=model_name,
            openai_api_key=api_key,
            openai_api_base=api_base,
            temperature=0
        )