from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    try:
        input_ids = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")
        repsonse_ids = model.generate(input_ids,max_length = 50,pad_token_id = tokenizer.eos_token_id)
        response_text = tokenizer.decode(repsonse_ids[:,input_ids.shape[-1]:][0],skip_special_tokens=True)
        return response_text
    except Exception as e:
        print("Error generating response",e)
        return "Sorry couldnt generate response"