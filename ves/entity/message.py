from datetime import datetime


class Message:
    def __init__(self, data, text):
        self.data = data
        self.text = text


class SafeMessage:
    def __init__(self, encode_text, key):
        self.key = key
        self.text = encode_text

if __name__ == "__main__":
    print(Message('01.01.2023', 'Today is good day'))