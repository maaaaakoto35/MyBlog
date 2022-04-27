from http.client import HTTPException
import logging
import os

from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from app.api import crud
from app.db import init_db
from app.models.tortoise import SummarySchema
from app.models.pydantic import SummaryPayLoadSchema, SummaryResponseSchema

log = logging.getLogger("uvicorn")

app = FastAPI()

origins = [
    "*",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.on_event("startup")
async def startup_event():
    log.info("Starting up ...")
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

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

@app.get("/summay/{id}", response_model=SummaryResponseSchema)
async def get_summary(id: int = Path(..., gt=0)) -> SummaryResponseSchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary


@app.put("/summary/{id}", response_model=SummarySchema)
async def update_summary(payload: SummaryPayLoadSchema, id: int = Path(..., gt=0)) -> SummarySchema:
    summary = await crud.put(id, payload)

    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    return summary

@app.delete("/summay/{id}", response_model=SummaryResponseSchema)
async def delete_summary(id: int = Path(..., gt=0)) -> SummaryResponseSchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")
    await crud.delete(id)
    return summary
