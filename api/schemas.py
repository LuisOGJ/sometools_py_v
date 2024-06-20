from fastapi import FastAPI
from pydantic import BaseModel

class GenPassEntity(BaseModel):
    mayus: bool
    special: bool
    numbers: bool
    dist: int
