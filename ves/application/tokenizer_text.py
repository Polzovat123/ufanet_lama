from transformers import AutoTokenizer

class InterfaceTokenizer:

    def __init__(self, model_token=None):
        self.tokenizer = model_token

        self.text2tokens = {}
        self.tokens2text = {v: k for k, v in self.text2tokens.items()}

    def encode(self, text):
        # inputs = self.tokenizer(text, return_tensors="pt")

        return text