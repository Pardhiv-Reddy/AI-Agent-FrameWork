from toolregistry import ToolRegistry
from models.models import Plan
from exceptions import CircularDependencyError
import asyncio
import logging
logger = logging.getLogger(__name__)
class Executor:
    def __init__(self,register : ToolRegistry):
        self.register = register
    async def execute(self,plan:Plan):
        results = {}
        rem_tasks = plan.tasks.copy()
        used = set()
        logger.info("Executing Plan with %d Tasks",len(plan.tasks))
        while rem_tasks:
            runnable_tasks = []
            for task in rem_tasks:
                used.update(task.depends_on)
                if all(dep in results for dep in task.depends_on):
                    dep_res = {dep: results[dep] for dep in task.depends_on}
                    runnable_tasks.append((task,dep_res))
            logger.info("Executing %d runnable Task(s)",len(runnable_tasks))
            if not runnable_tasks:
                logger.error("Circular Dependency Detected in Plan")
                raise CircularDependencyError(
                    "There is a Circular Dependency"
                )
            coroutines = [
                self.register.get(task.tool).execute(task,dep_res) for task, dep_res in runnable_tasks
            ]
            res = await asyncio.gather(*coroutines,return_exceptions=True)
            for (task,_), result in zip(runnable_tasks,res):
                if isinstance(result,Exception):
                    logger.exception("Task %d has failed !",task.id)
                else :
                    logger.info("Task %d has Executed Successfully",task.id)
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
        if final is None :
            logger.warning("No Leaf Task Found")
        logger.info("Plan Execution Completed")
        return results,final