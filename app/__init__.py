from .main import (
    SourceCode,
    Table,
    MarkdownDocument,
    parse_yaml_metadata,
    parse_table,
    parse_python_script,
    parse_markdown_content,
    SourceCodePromptTemplate,
    MarkdownDocumentPromptTemplate,
    PythonScriptPromptTemplate,
    agent_logic,
    agent_executor
)

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langsmith import traceable

from minio import Minio
from minio.error import S3Error

# Load environment variables from .env file
load_dotenv()

# Set LangChain and LangSmith environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "cda")

# Example LangChain usage with traceable decorator
# @traceable(run_type="llm")
# def call_openai(data):
#     openai_api_key = os.getenv("OPENAI_API_KEY")
#     return ChatOpenAI(api_key=openai_api_key).predict(data)

__all__ = [
    "SourceCode",
    "Table",
    "MarkdownDocument",
    "parse_yaml_metadata",
    "parse_table",
    "parse_python_script",
    "parse_markdown_content",
    "SourceCodePromptTemplate",
    "MarkdownDocumentPromptTemplate",
    "PythonScriptPromptTemplate",
    "agent_logic",
    "agent_executor"
]
