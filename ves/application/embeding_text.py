

class InterfaceEmbeddingModel:
    def __init__(self, model):
        self.model = model

    def get_embedding(self, text):
        # output = self.model.generate(text["input_ids"], max_new_tokens=40)
        output = self.model.encode(text)
        return output


if __name__ == '__main__':
    print(InterfaceEmbeddingModel().get_embedding(f'''
        Здравствуйте у меня не работает роутер. Жал на кнопки но онн так и не обновился
    '''))