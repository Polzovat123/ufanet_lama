from transformers import AutoModelForCausalLM, AutoTokenizer

class RWKVChatModel:
    def __init__(self, prompt):
        self.prompt = f'Imageine that youre are software engineer, {prompt}'
        self.model = AutoModelForCausalLM.from_pretrained("RWKV/rwkv-raven-14b")
        self.tokenizer = AutoTokenizer.from_pretrained("RWKV/rwkv-raven-14b")

    def speak(self, text):
        request_text = self.prompt + text

        inputs = self.tokenizer(request_text, return_tensors="pt")
        output = self.model.generate(inputs["input_ids"], max_new_tokens=40)
        return self.tokenizer.decode(output[0].tolist(), skip_special_tokens=True)
        # return 'all work'