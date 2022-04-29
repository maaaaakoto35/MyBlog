from ctypes import Union
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
    summaries = await TextSummary.all().values()
    return summaries

async def get(id: int) -> TextSummary:
    summary = await TextSummary.filter(id=id).first()
    if summary:
        return summary
    return None

async def put(id: int, payload: SummaryPayLoadSchema) -> TextSummary:
    summary = await TextSummary.filter(id=id).update(
        summary=payload.summary
    )

    if summary:
        update_summary = await TextSummary.filter(id=id).first()
        return update_summary
    return None

async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).delete()
    return summary
