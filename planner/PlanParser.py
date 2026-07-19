from models.models import Plan
from exceptions import InvalidPlanError
from pydantic import ValidationError
class PlanParser:
    @staticmethod
    def parse(resp)->Plan:
        try:
            return Plan.model_validate_json(resp)
        except ValidationError as e:
            raise InvalidPlanError(
                "This is a Invalid Plan"
            ) from e