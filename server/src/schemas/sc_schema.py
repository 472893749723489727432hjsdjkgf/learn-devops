from pydantic import BaseModel,Field


class ScUrlSchema(BaseModel):
    url : str = Field(min_length=15,max_length=1500)