from transformers import GPT2Tokenizer, T5ForConditionalGeneration
import torch


def prediction_model():
    tokenizer = GPT2Tokenizer.from_pretrained('ai-forever/FRED-T5-1.7B', eos_token='</s>')
    model = T5ForConditionalGeneration.from_pretrained('ai-forever/FRED-T5-1.7B')
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model.to(device)

    return model, tokenizer
