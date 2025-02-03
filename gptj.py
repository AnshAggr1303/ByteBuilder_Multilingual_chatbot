from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Authenticate with Hugging Face (if not already done)
from huggingface_hub import login
login(token='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')

# Load GPT-2 model and tokenizer
model_name = "gpt2"  # You can use "gpt2-medium", "gpt2-large", or "gpt2-xl" if needed
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)