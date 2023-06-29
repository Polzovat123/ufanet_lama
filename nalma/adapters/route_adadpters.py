import json
import ast

class JSONASKAdapter:
    def parse(self, json_input):
        dict_ask = ast.literal_eval(json_input.json())

        chat_id = dict_ask['id_chat']
        sendler = dict_ask['sendler']

        text = dict_ask['text']
        type_ask = dict_ask['type_question']
        return chat_id, sendler, text, type_ask