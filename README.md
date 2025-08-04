# 🤖 SO-ARM101 Gum Pickup Task with LeRobot

<div align="center">

<a href="https://github.com/CreatorKanata/gum-pickup-so-arm101/blob/main/images/gum-pickup.jpg?raw=true">
<img src="https://github.com/CreatorKanata/gum-pickup-so-arm101/blob/main/images/gum-pickup.jpg?raw=true" width="500">
</a>

**Teaching AI Robot Arm SO-ARM101 to Pick Up Gum (Candy) Using Imitation Learning**

[![Hugging Face Dataset](https://img.shields.io/badge/🤗%20Dataset-gum--pickup--so--arm101-blue)](https://huggingface.co/datasets/CreatorKanata/gum-pickup-so-arm101)
[![Hugging Face Model](https://img.shields.io/badge/🤗%20Model-act--gum--pickup--so--arm101-green)](https://huggingface.co/CreatorKanata/act-gum-pickup-so-arm101)
[![WandB](https://img.shields.io/badge/📊%20WandB-Training%20Logs-orange)](https://wandb.ai/takehide22-hapt-lab-llc/lerobot/runs/afarhran/overview)

</div>

## 🎬 Demo Videos

<table>
<tr>
<td align="center" width="50%">
<b>Run Inference</b><br><br>
<video src="https://github.com/user-attachments/assets/90f59c5c-42e0-4449-a950-ba9a8e1410cc">
</td>
<td align="center" width="50%">
<b>Camera Views</b><br><br>
<video src="https://github.com/user-attachments/assets/3a5870b0-0ad9-4f50-9377-d23be470e271">
</td>
</tr>
</table>

## 🎯 Overview

This repository demonstrates how to train an AI robot arm (SO-ARM101) to perform a gum pickup task using Hugging Face's LeRobot framework. The project covers the complete workflow from data collection through teleoperation to training and autonomous execution.

### Key Features
- 🎮 **Teleoperation**: Intuitive leader-follower configuration for demonstration recording
- 📹 **Multi-camera System**: Dual camera setup with overhead and hand-view perspectives
- 🧠 **Imitation Learning**: Training with ACT (Action Chunking with Transformers) policy
- 📊 **Open Dataset**: Publicly available dataset and model on Hugging Face Hub

## 🛠️ System Requirements

### Hardware
- **Robot**: SO-ARM101 (Leader-Follower configuration)
  - [SO-ARM101 AI Arm Motor Kit Pro](https://jp.seeedstudio.com/SO-ARM101-Low-Cost-AI-Arm-Kit-Pro-p-6427.html) - Motor kit from Seeed Studio
  - [SO-ARM101 3D Printed Parts](https://jp.seeedstudio.com/SO-ARM101-3D-printed-Enclosure-p-6428.html) - 3D printed enclosure from Seeed Studio
- **Cameras**: 
  - USB camera (overhead view)
  - Intel RealSense D435i (hand view with depth sensing)

### Software Environment
- **OS**: Ubuntu 24.0
- **Kernel**: Linux-6.14.0-27-generic-x86_64-with-glibc2.39
- **Python**: 3.10
- **GPU**: NVIDIA GeForce RTX 4070

### System Layout

![System Structure](https://github.com/CreatorKanata/gum-pickup-so-arm101/blob/main/images/system-structure.jpg?raw=true)

### Camera Views

![Camera Visions](https://github.com/CreatorKanata/gum-pickup-so-arm101/blob/main/images/camera-visions.jpg?raw=true)

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Create a Conda environment for LeRobot
conda create -y -n lerobot python=3.10
conda activate lerobot
```

Reference: https://huggingface.co/docs/lerobot/installation

### 2. Robot Arm Calibration

Reference: https://huggingface.co/docs/lerobot/so101

#### Follower Arm (for execution)
```bash
python -m lerobot.calibrate \
  --robot.type=so101_follower \
  --robot.port=/dev/tty.usbserial_lerobot_follower \
  --robot.id=lerobot_follower_arm
```

#### Leader Arm (for teleoperation)
```bash
python -m lerobot.calibrate \
  --teleop.type=so101_leader \
  --teleop.port=/dev/tty.usbserial_lerobot_leader \
  --teleop.id=lerobot_leader_arm
```

#### Test Teleoperation
```bash
python -m lerobot.teleoperate \
  --robot.type=so101_follower \
  --robot.port=/dev/tty.usbserial_lerobot_follower \
  --robot.id=lerobot_follower_arm \
  --teleop.type=so101_leader \
  --teleop.port=/dev/tty.usbserial_lerobot_leader \
  --teleop.id=lerobot_leader_arm
```

### 3. Data Collection

#### Record a dataset
```bash
python kanata_record.py
```
- **Number of episodes**: 10
- **Episode duration**: 20 seconds
- **Reset time**: 10 seconds between episodes
- **Task**: Pick up gum and place it on a white plate

### 4. Model Training

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

### 5. Run Inference

```bash
python kanata_control.py
```

## 📊 Training Results

<div align="center">

**WandB Overview**: https://wandb.ai/takehide22-hapt-lab-llc/lerobot/overview

[![WandB Overview](https://github.com/CreatorKanata/gum-pickup-so-arm101/blob/main/images/wandb-overview.png?raw=true)](https://wandb.ai/takehide22-hapt-lab-llc/lerobot/overview)

**Training Charts**: https://wandb.ai/takehide22-hapt-lab-llc/lerobot/workspace?nw=nwusertakehide22

[![Training Charts](https://github.com/CreatorKanata/gum-pickup-so-arm101/blob/main/images/wandb-train-charts.png?raw=true)](https://wandb.ai/takehide22-hapt-lab-llc/lerobot/workspace?nw=nwusertakehide22)

</div>

## 🤗 Hugging Face Resources

- **Dataset**: [CreatorKanata/gum-pickup-so-arm101](https://huggingface.co/datasets/CreatorKanata/gum-pickup-so-arm101)
- **Trained Model**: [CreatorKanata/act-gum-pickup-so-arm101](https://huggingface.co/CreatorKanata/act-gum-pickup-so-arm101)

## 📁 Project Structure

```
gum-pickup-so-arm101/
├── kanata_record.py      # Data collection script
├── kanata_control.py     # Inference execution script
├── images/              # Documentation images
│   ├── gum-pickup.jpg
│   ├── system-structure.jpg
│   ├── camera-visions.jpg
│   ├── wandb-overview.png
│   ├── wandb-train-charts.png
│   └── huggingface-*.png
├── videos/              # Demo videos
│   ├── run-inference.mp4
│   └── camera-video.mp4
├── CLAUDE.md           # Guidelines for Claude Code
└── README.md           # This file
```

## 🔧 Customization

### Camera Configuration
Adjust in the `camera_config` section of both scripts:
- USB camera index: `index_or_path=6`
- RealSense serial number: `serial_number_or_name="841612072123"`

### Task Parameters
- `NUM_EPISODES`: Number of episodes to record/evaluate
- `EPISODE_TIME_SEC`: Duration of each episode
- `RESET_TIME_SEC`: Reset time between episodes
- `FPS`: Frame rate

## References

- https://huggingface.co/docs/lerobot/so101
- https://huggingface.co/docs/lerobot/il_robots
- https://wiki.seeedstudio.com/ja/lerobot_so100m/
