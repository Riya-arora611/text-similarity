#import libraries
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Function to encode text into BERT embeddings
def bert_encode(text, model, tokenizer):
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**tokens)
    return outputs.last_hidden_state.mean(dim=1)

def process_text(text1, text2):
    doc1_embedding = bert_encode(text1, model, tokenizer)
    doc2_embedding = bert_encode(text2, model, tokenizer)
    similarity_score = cosine_similarity(doc1_embedding, doc2_embedding)
    similarity = similarity_score[0][0]
    return similarity

# Function to find similarity between texts
def similar_docs(text1, text2):
    score = process_text(text1, text2)
    print("score:", score)
    
    if score == 0:
        result = {"matching_score": f"{score :.2f}"}
        return result
    else:
        result = {"matching_score": f"{score :.2f}"}
        return result