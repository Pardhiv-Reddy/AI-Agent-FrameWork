from toolregistry import ToolRegistry
from models.models import Plan
from exceptions import CircularDependencyError
import asyncio
class Executor:
    def __init__(self,register : ToolRegistry):
        self.register = register
    async def execute(self,plan:Plan):
        results = {}
        rem_tasks = plan.tasks.copy()
        used = set()
        while rem_tasks:
            runnable_tasks = []
            for task in rem_tasks:
                used.update(task.depends_on)
                if all(dep in results for dep in task.depends_on):
                    dep_res = {dep: results[dep] for dep in task.depends_on}
                    runnable_tasks.append((task,dep_res))
            if not runnable_tasks:
                raise CircularDependencyError(
                    "There is a Circular Dependency"
                )
            coroutines = [
                self.register.get(task.tool).execute(task,dep_res) for task, dep_res in runnable_tasks
            ]
            res = await asyncio.gather(*coroutines,return_exceptions=True)
            for (task,_), result in zip(runnable_tasks,res):
                results[task.id] = result
            completed_ids = {task.id for task,_ in runnable_tasks}
            rem_tasks= [
                task for task in rem_tasks
                if task.id not in completed_ids
            ]
            final = None
        for task in plan.tasks:
            if task.id not in used:
                final = task.id
                break
        return results,final