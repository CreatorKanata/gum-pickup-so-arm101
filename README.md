# gum-pickup-so-arm101

![](https://github.com/CreatorKanata/gum-pickup-so-arm101/blob/main/images/gum-pickup.jpg?raw=true)

## Software/Hardware spec

- OS: Ubuntu 24.0
- Kernel: Linux-6.14.0-27-generic-x86_64-with-glibc2.39
- Python: 3.10
- GPU: NVIDIA GeForce RTX 4070

## Dataset & Models

- Hugging Face
  - Dataset: https://huggingface.co/datasets/CreatorKanata/gum-pickup-so-arm101
  - Model: https://huggingface.co/CreatorKanata/act-gum-pickup-so-arm101
- Wandb: https://wandb.ai/takehide22-hapt-lab-llc/lerobot/runs/afarhran/overview

## Commands

Installation lerobot

```
conda create -y -n lerobot python=3.10
conda activate lerobot
```

Follower arm calibration

```
python -m lerobot.calibrate --robot.type=so101_follower --robot.port=/dev/tty.usbserial_lerobot_follower --robot.id=lerobot_follower_arm
```

Leader arm calibration

```
python -m lerobot.calibrate --teleop.type=so101_leader --teleop.port=/dev/tty.usbserial_lerobot_leader --teleop.id=lerobot_leader_arm
```

Tele-operation

```
python -m lerobot.teleoperate --robot.type=so101_follower --robot.port=/dev/tty.usbserial_lerobot_follower --robot.id=lerobot_follower_arm --teleop.type=so101_leader --teleop.port=/dev/tty.usbserial_lerobot_leader --teleop.id=lerobot_leader_arm
```

Record dataset

```
python kanata-record.py
```

Train

```
python -m lerobot.scripts.train \
  --dataset.repo_id=CreatorKanata/gum-pickup-so-arm101 \
  --policy.type=act \
  --output_dir=outputs/train/act-gum-pickup-so-arm101 \
  --job_name=gum-pickup-so-arm101 \
  --policy.device=cuda \
  --wandb.enable=true \
  --policy.repo_id=CreatorKanata/act-gum-pickup-so-arm101
```

