from app.models.pydantic import SummaryPayLoadSchema
from app.models.tortoise import TextSummary
from typing import List

async def post(payload: SummaryPayLoadSchema) -> int:
    summary = TextSummary(
        summary=payload.summary,
    )
    await summary.save()
    return summary.id

async def get_all() -> List:
    summarys = await TextSummary.all().values()
    return summarys
