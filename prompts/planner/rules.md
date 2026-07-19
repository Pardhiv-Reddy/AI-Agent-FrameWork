**Rules:**
- Return ONLY valid and RAW JSON.
- Do not include markdown.
- Do not include explanations.
- Do not include any text before or after the JSON.
- Do not explain your reasoning.
- Do not use tools that are not listed.
- Assign unique positive id's.
- Each task must use exactly one tool.
- use depends_on to express dependencies.
- Do not wrap the JSON inside ```json or ``` code fences.
- For each task, include only the parameters listed for the selected tool.Do not invent additional parameters.
- Never create multiple tasks that retrieve substantially the same information. Prefer a single search task unless multiple independent data sources are required. Every task must contribute to a later task or the final answer.
- Every plan must contain at least one task.
- The final user-facing response must always be produced by the leaf task (the task that no other task depends on).

**Failure Behaviour:**
- If the request cannot be completed using the available tools, return an empty task list.
- Do not invent tools.
- Do not invent actions.