# AgentFlow
> A lightweight asynchronous AI agent framework built from scratch in Python that uses planning, dependency-aware execution, and pluggable tools to solve user requests.

---

## Features
-  LLM-based task planner
-  Dependency-aware asynchronous executor
-  Parallel execution of independent tasks
-  Pluggable tool architecture
-  Automatic tool discovery & registration
-  Conversation memory
-  Structured planning using Pydantic models
-  Custom exception handling
-  Extensible tool ecosystem

---

# Architecture
```
                 User Query
                      │
                      ▼
              Conversation Manager
                      │
                      ▼
                  Planner (LLM)
                      │
                      ▼
                 Structured Plan
                      │
                      ▼
          Dependency-Aware Executor
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
   GitHub Tool                 LLM Tool
        │                           │
        └─────────────┬─────────────┘
                      ▼
               Final Response
```

---

# Example Workflow

### User

```
Find the top GitHub repositories for LangGraph and summarize them.
```

### Planner Output
```json
{
  "tasks": [
    {
      "id": 1,
      "tool": "github",
      "action": "search",
      "depends_on": [],
      "arguments": {
        "q": "LangGraph",
        "sort": "stars"
      }
    },
    {
      "id": 2,
      "tool": "llm",
      "action": "summarize",
      "depends_on": [1],
      "arguments": {}
    }
  ]
}
```

### Execution Graph

```
GitHub Search
      │
      ▼
LLM Summarize
```

---

# Parallel Execution
The executor automatically detects tasks that have no unresolved dependencies and executes them concurrently.

Example:

```
Task1 → GitHub Search (Machine Learning)

Task2 → GitHub Search (Blockchain)

Task3 → Summarize Results
```

Execution graph

```
      Task1 ──┐
              │
              ▼
           Task3
              ▲
              │
      Task2 ──┘
```

Both GitHub searches execute simultaneously before the summarization task begins.

---

# Project Structure
```
AgentFlow/

├── Conversation/
├── Executor/
├── Planner/
├── Tools/
├── Utils/
├── llm/
├── models/
├── exceptions.py
├── main.py
└── README.md
```

---

# Built-in Components
*Component : Purpose*
- Planner : Converts natural language into executable plans 
- Executor : Executes dependency graphs asynchronously 
- Conversation : Maintains conversation history 
- Tool Registry : Stores available tools 
- Auto Register : Automatically discovers tools 
- Prompt Builder : Dynamically builds planner prompts 
- Ollama Wrapper : Handles local LLM communication 

---

# Built-in Tools
- GitHub Repository Search
- LLM Answering
- LLM Summarization
Adding new tools only requires inheriting from `BaseTool`.

---

# Creating a Tool
```python
class MyTool(BaseTool):
    async def execute(self, task, dependencies):
        ...
    @property
    def metadata(self):
        ...
```
The framework automatically discovers and registers tools during startup.
---
# Technologies
- Python 3.14
- asyncio
- httpx
- Ollama
- Pydantic

---

# Current Limitations
- LLM execution tools currently operate only on task dependency results and do not yet receive full conversation context.
- Tool execution retries are not implemented.
- Streaming responses are not yet supported.

---

# Planned Improvements
- Conversation-aware tool execution
- Retry policies
- Streaming LLM responses
- Additional tools
- Better planner optimization

---

# Why This Project?
Most AI agent projects rely heavily on existing frameworks.
This project was built from scratch to understand and implement the core building blocks of an AI agent system, including planning, dependency resolution, asynchronous execution, tool orchestration, and conversation management.
The goal is to provide a lightweight, extensible framework that can serve as a foundation for building more capable AI applications.

---

# License
MIT License
