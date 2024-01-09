# MLX Phi2 Lora

Cobbled together in response to [this](https://github.com/ml-explore/mlx-examples/issues/135) issue.

Convert your Phi2 weights, I've quantized them here.

```
python3 -m convert --hf-path microsoft/phi-2 --quantize
```

Use tokenizer.py to get the tokenizer.model files required for sentencepiece.

```
python3 -m tokenizer 
```

Copy them into the model dir. 

Instantiate training! Sorted.

```
python3 -m lora --train
```