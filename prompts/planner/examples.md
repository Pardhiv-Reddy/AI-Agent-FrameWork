**EXAMPLES:**
**Example 1- Independent Task:**
{
    "tasks": [
        {
            "id": 1,
            "tool": "github",
            "action": "search",
            "depends_on": [],
            "arguments": {
                "q": "LangGraph"
            }
        }
    ]
}
**Example 2 - Dependent Task:**
User: Find the top GitHub repositories for LangGraph and summarize them.
{
    "tasks": [
        {
            "id": 1,
            "tool": "github",
            "action": "search",
            "depends_on": [],
            "arguments": {
                "q": "LangGraph",
                "sort":"stars"
            }
        },
        {
            "id": 2,
            "tool":"llm",
            "action":"summarize",
            "depends_on":[1],
            "arguments":{}
        }
    ]
}
User : Find the top Github repositories of machine learning and blockchain and summarize them for me.
Reasoning:
- Search for machine learning repositories.
- Search for blockchain repositories.
- Summarize both search results.
{
    "tasks":[
        {
            "id":1,
            "tool":"github",
            "action":"search",
            "depends_on":[],
            "arguments":{
                "q":"machine learning",
                "sort":"stars"
            }
        },
        {
            "id":2,
            "tool":"github",
            "action":"search",
            "depends_on":[],
            "arguments":{
                "q":"blockchain",
                "sort":"stars"
            }
        },
        {
            "id":3,
            "tool":"llm",
            "action":"summarize",
            "depends_on":[1,2],
            "arguments":{}
        }
    ]
}
User: Find the GitHub repository for LangGraph, find what Wikipedia says about it, then give me a concise summary.
{
    "tasks": [
        {
            "id": 1,
            "tool": "github",
            "action": "search",
            "depends_on": [],
            "arguments": {
                "q": "LangGraph"
            }
        },
        {
            "id": 2,
            "tool": "wikipedia",
            "action": "search",
            "depends_on": [],
            "arguments": {
                "q": "LangGraph"
            }
        },
        {
            "id": 3,
            "tool": "llm",
            "action": "summarize",
            "depends_on": [1, 2],
            "arguments": {}
        }
    ]
}
**Example 3 - Simple User Query:**
{
    "tasks": [
        {
            "id":1,
            "tool":"llm",
            "action":"answer",
            "depends_on":[],
            "arguments":{
                "query":"what is Asyncio"
            }
        }
    ]
}