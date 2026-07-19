from llm.base import BaseLLM
import httpx
from models.models import ChatRequest,ChatResponse
from exceptions import ConnectionError,InvalidResponseError,TimeoutError
class OllamaLLM(BaseLLM):
    def __init__(self,client : httpx.AsyncClient,url : str = "http://localhost:11434"):
        self.base_url = url
        self.client = client
    async def chat(self,request : ChatRequest)->ChatResponse:
        try:
            payload = request.model_dump()
            response = await self.client.post(f"{self.base_url}/api/chat",json=payload)
            response.raise_for_status()
            response_data = response.json()
            return ChatResponse(
                model= response_data["model"],
                content = response_data["message"]["content"]
            )
        except httpx.ConnectError as e:
            raise ConnectionError(
                "Unable to Connect to LLM"
            )from e
        except KeyError as e:
            raise InvalidResponseError(
                "The LLM didnt give correct response"
            )from e
        except httpx.ConnectTimeout as e:
            raise TimeoutError(
                "Timeout Error !"
            )from e