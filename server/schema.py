from typing import Literal
from pydantic import BaseModel, Field


# Data send as post request
class InputData(BaseModel):

    # Input fields allowed
    algo: Literal["V1", "V2", "V3", "v1", "v2", "v3"]
    upperBound: int = Field(
        gt=1, description="Number must be greater than 0", examples=[10, 20, 30]
    )
    lowerBound: int = Field(
        gt=1, description="Any postitive number", examples=[100, 200, 300]
    )
