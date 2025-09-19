from transformers import AutoTokenizer, AutoModel
import torch
from tokenizers import Tokenizer

tokenizer = AutoTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
model = AutoModel.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")

inputs = tokenizer("CCO", return_tensors="pt")
print(f"Inputs: {inputs}")

with torch.no_grad():
    outputs = model(**inputs)

embedding = outputs.last_hidden_state
print(f"Embedding CCO: {embedding}")



# embeddings/embedder_de_chembert.py

class ChemBERTaEmbedder:
    def __init__(self, model_name="seyonec/ChemBERTa-zinc-base-v1", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()

    def encode(self, smiles: str):
        """Devuelve embeddings para una molécula en formato SMILES"""
        inputs = self.tokenizer(smiles, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return outputs.last_hidden_state  # (batch, seq_len, hidden_dim)
