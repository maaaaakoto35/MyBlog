import logging
import os
from urllib import response

from fastapi import FastAPI
from typing import List

from app.api import crud
from app.db import init_db
from app.models.tortoise import SummarySchema
from app.models.pydantic import SummaryPayLoadSchema, SummaryResponseSchema

log = logging.getLogger("uvicorn")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up ...")
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")

@app.post("/summary", response_model = SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayLoadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "summary": payload.summary
    }
    return response_object

@app.get("/summary", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()

@app.get("/")
async def root():
    return {"message": "Hello World!"}