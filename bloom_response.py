from transformers import AutoTokenizer, AutoModelForCausalLM

class BloomLLM:
    def __init__(self, model_name='bigscience/bloom-560m'):
        # Initialize the tokenizer and model
        print("Loading Bloom-560m model...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        print("Bloom-560m model loaded successfully.")

    def generate_response(self, prompt, max_new_tokens=100):
        """
        Generate a response using Bloom.
        :param prompt: The input prompt to Bloom.
        :param max_new_tokens: Maximum number of new tokens to generate.
        :return: The generated response.
        """
        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        # Generate response with limited new tokens
        outputs = self.model.generate(inputs["input_ids"], max_new_tokens=max_new_tokens)
        
        # Decode and return the response
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test Bloom-560m response generation
if __name__ == "__main__":
    bloom = BloomLLM()
    prompt = "Explain how a chatbot can help with health queries."
    response = bloom.generate_response(prompt)
    print("Bloom Response:")
    print(response)
