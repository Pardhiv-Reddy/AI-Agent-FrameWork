import asyncio
import httpx
from llm.ollama import OllamaLLM
from conversation.conversation import Conversation
from models.models import ChatRequest
from planner.planner import Planner
from planner.PlanParser import PlanParser
from toolregistry import ToolRegistry
from executor.executor import Executor
from utils.Builder import Builder
from utils.auto_register import AutoRegister
from utils.logger import setup_logging
async def main():
    setup_logging()
    async with httpx.AsyncClient(timeout=None) as client:
        llm = OllamaLLM(client)
        planner = Planner(llm)
        registry = ToolRegistry()
        AutoRegister.auto_register(registry,llm)
        prompt = Builder.build_prompt(registry)
        conv = Conversation(prompt,25)
        executor = Executor(registry)
        try:
            while True:
                inp = input("Chat : ")
                if(inp.lower().strip() == "bye"):
                    print("Until we Meet Again")
                    return
                conv.add_user(inp)
                req = ChatRequest(
                model="qwen3.5:9b",
                messages=conv.build_messages()
                )
                plan_response = await planner.plan(req)
                plan = PlanParser.parse(plan_response.content)
                result,final = await executor.execute(plan)
                if final is None:
                    raise RuntimeError(
                        "No final task found."
                    )
                for task in plan.tasks:
                    print(f"\n[{task.tool.upper()} - {task.action}]")
                    print(result[task.id])
                conv.add_assistant(result[final])
        except Exception as e:
            print(e)
asyncio.run(main())