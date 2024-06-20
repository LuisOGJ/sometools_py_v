from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from core.services import *

router = APIRouter(prefix="/passGenerator")

@router.get("/", tags=["passGenerator"])
def generatePass():
    passDTO = generatePassService(True, True, True, 20)
    return passDTO


@router.get("/1", tags=["passGenerator"])
def generatePass1():
    return 5