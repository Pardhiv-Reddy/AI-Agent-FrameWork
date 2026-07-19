**Output Schema:**
*Return a JSON object using the following schema*
{
    "tasks": [
        {
            "id": 1,
            "tool": "github",
            "action": "search",
            "depends_on": [],
            "arguments": {
                "q": "Machine Learning"
            }
        }
    ]
}
**Field Types**
- id : int
- tool : string(must be one of the available tools)
- action : string(must be one of the available actions)
- depends_on : array of integers(empty array if no dependency)
- arguments : JSON object containing the parameters required by the selected tool and action