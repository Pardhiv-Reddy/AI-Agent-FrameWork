from llm.ollama import OllamaLLM
from typing import Any
from llm.base import BaseTool
from models.models import ToolMetaData,ChatRequest,Message,Task
import httpx
import json
class LLM(BaseTool):
    def __init__(self,llm:httpx.AsyncClient):
        self.llm = llm
    async def execute(self,task:Task,dep:dict[str,Any])->str:
        sum_prompt = '''
        You are an summarizer assistant.
        summarize the following task result ACCURATELY.

        Requirements:
        Do NOT invent information.

        Be concise and factual.
        NEVER Hallucinate.

        Do Not explain your reasoning.

        Do Not use lists or bullet points.
        '''
        ans_prompt = '''
        You are an helpful AI Assitant
        '''
        if task.action.lower() == "summarize":
            req = ChatRequest(
                model="qwen3.5:9b",
                messages=[
                    Message(
                        role="system",
                        content=sum_prompt
                    ),
                    Message(
                        role="user",
                        content=json.dumps(list(dep.values()),indent=2)
                    )
                ],
            )
        elif task.action.lower() == "answer":
            req = ChatRequest(
                model="qwen3.5:9b",
                messages=[
                    Message(
                        role="system",
                        content=ans_prompt
                    ),
                    Message(
                        role="user",
                        content=task.arguments["query"]
                    )
                ],
            )
        else:
            print("")
        response = await self.llm.chat(req)
        return response.content
    @property
    def metadata(self):
        return ToolMetaData(
            name ="llm",
            description="General-purpose language model for answering questions and summarizing task results.",
            actions=["summarize","answer"],
            parameters=[]
        )