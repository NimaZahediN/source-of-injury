## Objective

The `source-of-injury` project aims to identify the source injuries based on textual descriptions. The model is able to understand and analyze the context of the injury description and provide a concise and accurate classification of the source or cause.

## Use Cases

Some potential use cases for the `source-of-injury` model include:

1. **Healthcare**: Assist medical professionals in quickly identifying the source of an injury, which can aid in providing appropriate treatment and preventive measures and/or labeling the incident for downstream analysis.

2. **Insurance**: Enable insurance companies to efficiently process injury claims by automatically determining the source of the injury, streamlining the claims process.

3. **Accident Reporting**: Facilitate accurate and consistent reporting of accidents by automatically classifying the source of injuries based on textual descriptions.

4. **Research and Analysis**: Provide a tool for researchers and analysts to study patterns and trends in injury causes, enabling better prevention strategies and resource allocation.

## Approach

The `source-of-injury` project leverages the power of large language models and fine-tuning techniques to adapt a pre-trained LLM to the specific task of injury source classification. The project utilizes the Mistral-7B-v0.1 model from MistralAI as the base model and fine-tunes it on a custom dataset of injury descriptions and their corresponding sources.

The fine-tuning process involves training the model on a curated synthehtic dataset. The project employs the Axolotl framework, which provides a streamlined and efficient approach to fine-tuning large language models.

## Important hyperparameters, optimizers, and training parameters

- base_model: mistralai/Mistral-7B-v0.1
- adapter: qlora
- lora_r: 32
- lora_alpha: 16
- lora_dropout: 0.05
- sequence_len: 896
- micro_batch_size: 16
- eval_batch_size: 16
- num_epochs: 3
- optimizer: adamw_bnb_8bit
- lr_scheduler: cosine
- learning_rate: 0.0002
- max_grad_norm: 1.0
- adam_beta2: 0.95
- adam_epsilon: 0.00001
- gradient_accumulation_steps: 4
- warmup_steps: 20
- gradient_checkpointing: true
- bf16: true
- loss_watchdog_threshold: 5.0
- loss_watchdog_patience: 3
- evals_per_epoch: 4
- saves_per_epoch: 6
- weight_decay: 0.0
- special_tokens:
    ``` txt
    bos_token: "<s>"
    eos_token: "</s>" 
    unk_token: "<unk>"
    ```
- save_safetensors: true


[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 2.0189        | 0.1481 | 1    | 2.0511          |
| 2.0285        | 0.2963 | 2    | 2.0442          |
| 1.9559        | 0.5926 | 4    | 1.9259          |
| 1.802         | 0.8889 | 6    | 1.6212          |
| 1.4115        | 1.1852 | 8    | 1.2261          |
| 1.1171        | 1.4815 | 10   | 1.0004          |
| 0.9691        | 1.7778 | 12   | 0.8657          |
| 0.747         | 2.0741 | 14   | 0.7082          |
| 0.6407        | 2.3704 | 16   | 0.6205          |
| 0.6101        | 2.6667 | 18   | 0.5867          |


Training Loss Curve:

![Training Loss Curve](/pics/Image.png)
[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/uqam/source_of_injury/runs/2q7kaw2k)


### Framework versions

- PEFT 0.11.1
- Transformers 4.42.3
- Pytorch 2.1.2+cu118
- Datasets 2.19.1
- Tokenizers 0.19.1

