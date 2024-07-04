# source-of-injury
---
base_model: mistralai/Mistral-7B-v0.1
library_name: peft
license: apache-2.0
tags:
- axolotl
- generated_from_trainer
model-index:
- name: source_of_injury
  results: []
language:
- en
pipeline_tag: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

[<img src="https://raw.githubusercontent.com/OpenAccess-AI-Collective/axolotl/main/image/axolotl-badge-web.png" alt="Built with Axolotl" width="200" height="32"/>](https://github.com/OpenAccess-AI-Collective/axolotl)
<details><summary>See axolotl config</summary>

axolotl version: `0.4.1`
```yaml
base_model: mistralai/Mistral-7B-v0.1
model_type: MistralForCausalLM
tokenizer_type: LlamaTokenizer
is_mistral_derived_model: true

load_in_8bit: false
load_in_4bit: true
strict: false

lora_fan_in_fan_out: false
data_seed: 49
seed: 49

datasets:
  - path: NimaZahedinameghi/source_injury
    type: alpaca

dataset_prepared_path: last_run_prepared
val_set_size: 0.1
output_dir: ./qlora-alpaca-out
hub_model_id: NimaZahedinameghi/source_of_injury

adapter: qlora
lora_model_dir:

sequence_len: 896
sample_packing: false
pad_to_sequence_len: true

lora_r: 32
lora_alpha: 16
lora_dropout: 0.05
lora_target_linear: true
lora_fan_in_fan_out:
lora_target_modules:
  - gate_proj
  - down_proj
  - up_proj
  - q_proj
  - v_proj
  - k_proj
  - o_proj

wandb_project: source_of_injury
wandb_entity: uqam

gradient_accumulation_steps: 4
micro_batch_size: 16
eval_batch_size: 16
num_epochs: 3
optimizer: adamw_bnb_8bit
lr_scheduler: cosine
learning_rate: 0.0002
max_grad_norm: 1.0
adam_beta2: 0.95
adam_epsilon: 0.00001
save_total_limit: 12

train_on_inputs: false
group_by_length: false
bf16: true
fp16: false
tf32: false

gradient_checkpointing: true
early_stopping_patience:
resume_from_checkpoint:
local_rank:
logging_steps: 1
xformers_attention:
flash_attention: true

loss_watchdog_threshold: 5.0
loss_watchdog_patience: 3

warmup_steps: 20
evals_per_epoch: 4
eval_table_size:
eval_table_max_new_tokens: 128
saves_per_epoch: 6
debug:
weight_decay: 0.0
fsdp:
fsdp_config:
special_tokens:
  bos_token: "<s>"
  eos_token: "</s>"
  unk_token: "<unk>"
save_safetensors: true
```

</details><br>

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="200" height="32"/>](https://wandb.ai/uqam/source_of_injury/runs/2q7kaw2k)

# Run Summary

## Training Information
- **Author:** nima-zahedinameghi-1
- **Training Duration:** 7m 15s

## Environment Details
- **OS:** Linux-5.15.0-89-generic-x86_64-with-glibc2.35

## Command Executed
```bash
-m axolotl.cli.train examples/openllama-3b/lora.yml
```
# source_of_injury

This model is built by [Nima Zahedinameghi](https://www.linkedin.com/in/nima-zahedi-nameghi-ph-d-3b7061146/). It's a fine-tuned version of [mistralai/Mistral-7B-v0.1](https://huggingface.co/mistralai/Mistral-7B-v0.1) on the [source_injury](https://huggingface.co/datasets/NimaZahedinameghi/source_injury) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5867, after 3 epochs.

## Dependencies
Please pip install all the required dependencies
``` txt
transformers==4.36.2
datasets==2.15.0
peft==0.6.0
accelerate==0.24.1
bitsandbytes==0.41.3.post2
safetensors==0.4.1
scipy==1.11.4
sentencepiece==0.1.99
protobuf==4.23.4 --upgrade
```

## Model description

the model is fine tuned on a small dataset with 4bit precision. 

## Intended uses & limitations

Further testing is required to evaluate the model performance on custome evaluations

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 16
- seed: 49
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.95) and epsilon=1e-05
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 20
- num_epochs: 3

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


### Framework versions

- PEFT 0.11.1
- Transformers 4.42.3
- Pytorch 2.1.2+cu118
- Datasets 2.19.1
- Tokenizers 0.19.1
