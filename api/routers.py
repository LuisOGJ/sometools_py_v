from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from api.schemas import GenPassEntity
from core.services import *

router = APIRouter(prefix="/passGenerator")

@router.get("/", tags=["passGenerator"])
def generatePass(valuesOptions: GenPassEntity):
    mayus = valuesOptions.mayus
    special = valuesOptions.special
    numbers = valuesOptions.numbers
    dist = valuesOptions.dist
    passDTO = generatePassService(mayus, special, numbers, dist)
    return passDTO


@router.get("/1", tags=["passGenerator"])
def generatePass1():
    return 5