from models.models import Plan,ChatRequest,ChatResponse
from llm.base import BaseLLM
import logging
logger = logging.getLogger(__name__)
class Planner:
    def __init__(self,llm:BaseLLM):
        self.llm = llm
    async def plan(self,req : ChatRequest)->ChatResponse:
        logger.info("Planner Started")
        try :
            res =  await self.llm.chat(req)
            logger.info("Plan Created Successfully")
            return res
        except Exception :
            logger.exception("Planner Failed")
            raise