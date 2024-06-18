from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException

router = APIRouter(prefix="/passGenerator")

@router.get("/", tags=["passGenerator"])
def generatePass():
    return 5


@router.get("/1", tags=["passGenerator"])
def generatePass1():
    return 5