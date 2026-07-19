from models.models import Plan,ChatRequest,ChatResponse
from llm.base import BaseLLM
class Planner:
    def __init__(self,llm:BaseLLM):
        self.llm = llm
    async def plan(self,req : ChatRequest)->ChatResponse:
        return await self.llm.chat(req)