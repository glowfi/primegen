from pydantic import BaseModel, Field
from datetime import datetime


# Data send as post request
class InputData(BaseModel):
    algo: str
    upperBound: int
    lowerBound: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"algo": "V1", "lowerBound": 30, "upperBound": 100},
                {"algo": "V1", "lowerBound": 40, "upperBound": 1000},
                {"algo": "V1", "lowerBound": 500, "upperBound": 1000},
            ]
        }
    }


# Data send as response
class OutputData(BaseModel):
    id: int
    algo: str = Field(
        default="V1",
        description="Valid Inputs are V1 V2 V3",
        examples=["V1", "V2", "V3"],
    )
    upperBound: int = Field(
        gt=0, description="Number must be greater than 0", examples=[10, 20, 30]
    )
    lowerBound: int = Field(
        gt=0, description="Any postitive number", examples=[100, 200, 300]
    )
    timeElapsed: float
    primeLength: int
    result: str
    createdAt: datetime

    class Config:
        from_attributes = True
