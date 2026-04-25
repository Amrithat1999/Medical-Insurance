from pydantic import BaseModel

class FormatData(BaseModel):
    age: int
    sex: str
    bmi: float
    children: int
    smoker: str
    region: str


