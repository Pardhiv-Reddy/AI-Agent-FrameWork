from llm.base import BaseTool
import httpx
from typing import Any
from models.models import ToolMetaData,GitResult,Task,Parameter
import logging
logger = logging.getLogger(__name__)
class GithubTool(BaseTool):
    def __init__(self,url:str = "https://api.github.com/search/repositories"):
        super().__init__()
        self.url = url
        self.client = httpx.AsyncClient()
    async def execute(self,task:Task,dep:dict[str,Any])->list[dict[str,Any]]:
        res = await self.client.get(self.url,params = task.arguments)
        res.raise_for_status()
        logger.error("Error in Github")
        response = res.json()
        logger.info("Github Fetched Successfully")
        return [
            GitResult(
                name=repo["name"],
                url=repo["html_url"],
                stars=repo["stargazers_count"]
            ).model_dump()
            for repo in response["items"][:10]
        ]
    @property
    def metadata(self)->ToolMetaData:
        return ToolMetaData(
            name="github",
            description="search github repositories",
            actions=["search"],
            parameters=[
                Parameter(
                    name = "q",
                    description="GitHub repository search query. Use valid GitHub repository search syntax. Examples: 'blockchain', 'blockchain stars:>1000', 'machine learning language:python', 'topic:blockchain language:solidity', 'user:openai'. Combine qualifiers with spaces. Do not include sort, order, or per_page in this parameter."
                ),
                Parameter(
                    name="sort",
                    description="it is the criteria used to sort the result. Allowed qualifiers : star, fork, updated."
                ),
                Parameter(
                    name="order",
                    description="The Order of Sorting The Result. Allowed qualifiers : desc, asc."
                )
            ]
        )