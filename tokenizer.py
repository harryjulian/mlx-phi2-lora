from transformers import AutoTokenizer
import sentencepiece as spm

if __name__ == "__main__":

    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
    vocab = tokenizer.get_vocab()
    with open("vocab.txt", "w", encoding="utf-8") as file:
        for token in vocab:
            file.write(token + "\n")
    import sentencepiece as spm

    # Train SentencePiece model
    spm.SentencePieceTrainer.train(input='vocab.txt', model_prefix='tokenizer', vocab_size=25502)
