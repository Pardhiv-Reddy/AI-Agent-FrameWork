from pydantic import BaseModel,Field,field_validator
from typing import Literal,Any
class Message(BaseModel):
    role : Literal["assistant","user","system"]
    content : object
class ChatRequest(BaseModel):
    model : str
    messages : list[Message] = Field(default_factory=list)
    #tokens : int
    temperature : float = Field(ge=0,le=2,default=0.2)
    stream : bool = False
class ChatResponse(BaseModel):
    model : str
    content : str
class Task(BaseModel):
    id : int = Field(ge=0)
    tool : Literal["llm","github","wikipedia","arvix","weather","echo","email"]
    action : Literal["answer","summarize","search","formal writing"]
    depends_on : list[int]
    arguments : dict[str,Any] = Field(default_factory=dict)
    @field_validator("tool",mode="before")
    @classmethod
    def validate_name(cls,value):
        return value.lower()
    @field_validator("action",mode="before")
    @classmethod
    def validate(cls,value):
        return value.lower()
class Plan(BaseModel):
    tasks : list[Task]
class Parameter(BaseModel):
    name : str
    description : str
    required : bool = Field(default=True)
class ToolMetaData(BaseModel):
    name : str
    description : str
    actions : list[str]
    parameters : list[Parameter]
class GitResult(BaseModel):
    name : str
    url : str
    stars : int