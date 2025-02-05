from transformers import AutoTokenizer, AutoModelForCausalLM

class BloomLLM:
    def __init__(self, model_name='bigscience/bloom-560m'):
        print("Loading Bloom-560m model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        print("Bloom-560m model loaded successfully.")

    def generate_response(self, prompt, max_new_tokens=80):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_new_tokens=max_new_tokens)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
