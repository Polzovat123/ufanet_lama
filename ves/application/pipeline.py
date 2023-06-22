from ves.adapters.reader_data import InterfaceReaderDialog
from ves.application.embeding_text import InterfaceEmbeddingModel
from ves.application.encoder import InterfaceCyberSecurityEncoder
from ves.application.tokenizer_text import InterfaceTokenizer
from ves.entity.dialog import SafeDialog
from ves.entity.message import *

from InstructorEmbedding import INSTRUCTOR


class InterfacePipeline:
    def __init__(self, resource):
        self.resource = resource
        print(f'wait downloading model:')
        self.model = INSTRUCTOR('hkunlp/instructor-large')

    def execute(self):
        answer = []
        dialogs = InterfaceReaderDialog(self.resource).dialogs

        for dialog in dialogs:
            prompt, key_decode = self._process_text(str(
                f'''
                from: [{dialog.sendler}]
                to:   [{dialog.recipient}]
                '''
            ))
            safe_dialog = SafeDialog(prompt, key_decode)

            for msg in dialog.messages:
                text = msg.text
                encoded_cybersecurity_msg, key_decode = self._process_text(text)
                safe_dialog.add_message(SafeMessage(encoded_cybersecurity_msg, key_decode))
            answer.append(safe_dialog)

        return answer

    def _process_text(self, text):
        encoded_messages = InterfaceTokenizer().encode(text)
        embedded_variable = InterfaceEmbeddingModel(self.model).get_embedding(encoded_messages)
        encoded_cybersecurity, key = InterfaceCyberSecurityEncoder().encode(str(embedded_variable))
        return encoded_cybersecurity, key



    def save(self):
        ...