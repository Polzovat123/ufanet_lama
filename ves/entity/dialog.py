class Dialog:
    def __init__(self, sendler, recipient):
        self.messages = []
        self.sendler = sendler
        self.recipient = recipient

    def add_message(self, msg):
        self.messages.append(msg)


class SafeDialog:
    def __init__(self, encoded_input_params, key_decode):
        self.prompt = encoded_input_params
        self.key_decode = key_decode
        self.messages = []

    def add_message(self, msg):
        self.messages.append(msg)