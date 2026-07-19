from abc import ABC,abstractmethod
from typing import Any
from models.models import ChatRequest,ChatResponse,ToolMetaData,Task
class BaseLLM(ABC):
    @abstractmethod
    async def chat(self,req:ChatRequest) ->ChatResponse:
        pass
"""  @abstractmethod
    async def stream():
        pass
    @abstractmethod
    async def health_check():
        pass
    @abstractmethod
    async def models():
        pass
    @abstractmethod
    async def embed():
        pass"""
class BaseTool(ABC):
    @abstractmethod
    async def execute(self,task:Task,dependencies:dict[str,Any]):
        pass
    @property
    @abstractmethod
    def metadata()->ToolMetaData:
        pass