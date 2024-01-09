# MLX Phi2 Lora

Cobbled together in response to [this](https://github.com/ml-explore/mlx-examples/issues/135) issue.

Convert your Phi2 weights, I've quantized them here.

```
python3 -m convert --hf-path microsoft/phi-2 --quantize
```

Instantiate training! Sorted.

```
python3 -m lora --train
```