import pkgutil
import inspect
import importlib
import tools
import logging
from toolregistry import ToolRegistry
from llm.base import BaseTool
from llm.ollama import OllamaLLM
from tools.llm import LLM
logger = logging.getLogger(__name__)
class AutoRegister:
    @staticmethod
    def auto_register(registry:ToolRegistry,llm:OllamaLLM):
        for module in pkgutil.iter_modules(tools.__path__):
            imported = importlib.import_module(f"tools.{module.name}")
            classes = inspect.getmembers(imported,inspect.isclass)
            for name,cls in classes:
                if(issubclass(cls,BaseTool)):
                    if cls is BaseTool:
                        continue
                    if cls is LLM:
                        tool = cls(llm)
                    else:
                        tool = cls()
                    registry.register(tool)
                    logger.info("%s tool has been register successfully",name)             