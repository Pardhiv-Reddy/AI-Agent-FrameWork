from .loader import Loader
from toolregistry import ToolRegistry
class Builder:
    @staticmethod
    def build_prompt(register:ToolRegistry)->str:
        text = "##Available  Tools\n\n"
        for tool in register.tools():
            meta = tool.metadata
            text += f"### {meta.name}\n"
            text += f"Description:\n{meta.description}\n\n"
            text += "Actions:\n"
            for action in meta.actions:
                text += f"- {action}\n"
            text += "\nParameters:\n"
            for param in meta.parameters:
                text += f"- {param}\n"
            text += "\n"
        return "\n\n".join(
            [
                Loader.load("role.md"),
                Loader.load("rules.md"),
                text,
                Loader.load("schema.md"),
                Loader.load("examples.md")
            ]
        )