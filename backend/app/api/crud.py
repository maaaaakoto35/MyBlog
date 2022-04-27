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
    summariess = await TextSummary.all().values()
    return summariess

async def get(id: int) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None

async def put(id: int, payload: SummaryPayLoadSchema) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).update(
        summary=payload.summary
    )

    if summary:
        update_summary = await TextSummary.filter(id=id).first().values()
        return update_summary[0]
    return None

async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).delete()
    return summary
