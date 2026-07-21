from models.models import Plan
from exceptions import InvalidPlanError
from pydantic import ValidationError
import logging
logger = logging.getLogger(__name__)
class PlanParser:
    @staticmethod
    def parse(resp)->Plan:
        try:
            res = Plan.model_validate_json(resp)
            logger.info("Created %d Tasks",len(res.tasks))
            return res
        except ValidationError as e:
            logger.exception("Invalid Plan Created by Planner")
            raise InvalidPlanError(
                "This is a Invalid Plan"
            ) from e