import logging

from fastapi import FastAPI

from nalma.adapters.route_adadpters import JSONASKAdapter
from nalma.application.api_structure import ResponseChat, AskChat
from nalma.application.ml_models.rwkv import RWKVChatModel
from nalma.application.promt_builder import BuildPrompt

app = FastAPI(title='MLSER')
logger = logging.getLogger("uvicorn.error")


@app.post('/ask', response_model=ResponseChat)
def chat(request: AskChat):
    id_chat, sendler, question, type_ask = JSONASKAdapter().parse(request)
    prompt = BuildPrompt().build(type_ask)

    chatbot = RWKVChatModel(prompt)

    return ResponseChat(
        text=chatbot.speak(question)
    )
