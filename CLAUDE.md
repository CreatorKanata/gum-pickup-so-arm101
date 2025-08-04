# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Environment Setup

Set up the conda environment for LeRobot:
```bash
conda create -y -n lerobot python=3.10
conda activate lerobot
```

## Commands

### Calibration
- Follower arm: `python -m lerobot.calibrate --robot.type=so101_follower --robot.port=/dev/tty.usbserial_lerobot_follower --robot.id=lerobot_follower_arm`
- Leader arm: `python -m lerobot.calibrate --teleop.type=so101_leader --teleop.port=/dev/tty.usbserial_lerobot_leader --teleop.id=lerobot_leader_arm`

### Teleoperation
```bash
python -m lerobot.teleoperate --robot.type=so101_follower --robot.port=/dev/tty.usbserial_lerobot_follower --robot.id=lerobot_follower_arm --teleop.type=so101_leader --teleop.port=/dev/tty.usbserial_lerobot_leader --teleop.id=lerobot_leader_arm
```

### Data Collection
```bash
python kanata_record.py
```

### Training
```bash
python -m lerobot.scripts.train \
  --dataset.repo_id=CreatorKanata/gum-pickup-so-arm101 \
  --policy.type=act \
  --output_dir=outputs/train/act-gum-pickup-so-arm101 \
  --job_name=gum-pickup-so-arm101 \
  --policy.device=cuda \
  --wandb.enable=true \
  --policy.repo_id=CreatorKanata/act-gum-pickup-so-arm101
```

### Inference
```bash
python kanata_control.py
```

## Architecture

This is a LeRobot-based project for a gum pickup task using SO-ARM-101 robots:

- **Hardware**: Dual SO-ARM-101 setup with leader-follower configuration, 2 cameras (USB + RealSense D435i)
- **Task**: Pick up gum and place on plate using imitation learning
- **Key Scripts**:
  - `kanata_record.py`: Records demonstration episodes using teleoperation
  - `kanata_control.py`: Runs trained ACT policy for autonomous execution
- **Policy**: ACT (Action Chunking with Transformers) trained on demonstration data
- **Data Flow**: Human demonstrations → LeRobot dataset → ACT training → Autonomous control