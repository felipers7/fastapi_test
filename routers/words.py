from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/words",tags=["Words"])


class Word(BaseModel):
    id: int
    word_en: str
    word_uk: str


word_list = [
        Word(id=0,word_en="word1",word_uk="meaning1"),
        Word(id=1,word_en="word2",word_uk="meaning2")
        ]
@router.get("/")
async def root():
    return Word(id=1,word_en="word",word_uk="meaning")

@router.get("/{id}")
async def get_word(id: int):
    try:
        return word_list[id]
    except:
        return ""

#if is not defined in the route is a query param
@router.get("/")
async def get_word(id: int):
    try:
        return word_list[id]
    except:
        raise HTTPException(status_code=404,detail="Not found") 

@router.get("/")
async def get_words_list():
    return word_list 

@router.post("/", response_model=Word)
async def post_word(word: Word):
    word_list.append(word)
    return word
