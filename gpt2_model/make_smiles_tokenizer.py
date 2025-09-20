# IA-MOLGEN/gpt2_model/make_smiles_tokenizer.py
from transformers import PreTrainedTokenizerFast

# Carga el JSON BPE que copiaste
tok = PreTrainedTokenizerFast(
    tokenizer_file="IA-MOLGEN/gpt2_model/smiles_tokenizer.json",
    padding_side="right",
    bos_token="[BOS]",
    eos_token="[EOS]",
    unk_token="[UNK]",
    pad_token="[PAD]",
    cls_token="[CLS]",
    sep_token="[SEP]",
    mask_token="[MASK]",
)

# Lo guarda en formato HuggingFace (carpeta con tokenizer_config.json, etc.)
tok.save_pretrained("IA-MOLGEN/gpt2-smiles-tokenizer")
print("[OK] Guardado en IA-MOLGEN/gpt2-smiles-tokenizer")
