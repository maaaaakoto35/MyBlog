from pydantic import BaseModel

class SummaryPayLoadSchema(BaseModel):
    summary: str

class SummaryResponseSchema(SummaryPayLoadSchema):
    id: int
