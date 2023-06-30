import pydantic
from pydantic import BaseModel


class AskChat(BaseModel):
    id_chat: str
    type_question: str
    sendler: str
    date: str
    text: str


class ResponseChat(BaseModel):
    text: str