from src.model.splitter_model import chunks_splitter_model
from embeddings_model import embeddings_model
from src.model.prediction_model import create_prediction_model
from typing import List
import torch


def create_chunks(texts: List) -> List[List[str]]:
    result = []
    splitter = chunks_splitter_model()
    for i in range(len(texts)):
        text = texts[i]
        result.append(splitter.split(text))
    return result


def create_embeddings(text) -> List:
    model = embeddings_model()
    return model.encode(text, normalize_embeddings=True)


def create_prediction(query: str, context: str) -> str:
    model, tokenizer = create_prediction_model()

    prompt = f"Ты - представитель банка России.Ответь на вопрос, основываясь на приведенном ниже контексте.\
Если не знаешь ответа, то просто скажи, что не знаешь, не пытайся выдумывать.\n{context}\n\n\
---\n\nВопрос: {query}\n\
Полезный ответ:"

    lm_text = '<LM>' + prompt

    input_ids = torch.tensor([tokenizer.encode(lm_text, add_special_tokens=True)]).to(device)
    outputs = model.generate(input_ids, eos_token_id=tokenizer.eos_token_id, do_sample=True, max_length=200,
                             repetition_penalty=1.5, temperature=0.5, top_p=0.77)

    return tokenizer.decode(outputs[0][1:])


def passer():
    pass
