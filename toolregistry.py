from llm.base import BaseTool
from exceptions import ToolNotFoundError
class ToolRegistry():
    def __init__(self):
        self._tools = {}
    def register(self,tool:BaseTool):
        self._tools[tool.metadata.name] = tool 
    def get(self,name:str)->BaseTool:
        if name not in self._tools:
            raise ToolNotFoundError(
                f"{name} is not found in the registry"
            )
        return self._tools[name]
    def tools(self)->list[BaseTool]:
        return list(self._tools.values())