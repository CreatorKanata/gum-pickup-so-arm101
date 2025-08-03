#!/usr/bin/env python3

from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.cameras.realsense.configuration_realsense import RealSenseCameraConfig
from lerobot.cameras.realsense.camera_realsense import RealSenseCamera
from lerobot.cameras.configs import ColorMode, Cv2Rotation
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.datasets.utils import hw_to_dataset_features
from lerobot.policies.act.modeling_act import ACTPolicy
from lerobot.robots.so101_follower import SO101Follower, SO101FollowerConfig
from lerobot.utils.control_utils import init_keyboard_listener
from lerobot.utils.utils import log_say
from lerobot.utils.visualization_utils import _init_rerun
from lerobot.record import record_loop

NUM_EPISODES = 10
FPS = 30
EPISODE_TIME_SEC = 20
RESET_TIME_SEC = 10
TASK_DESCRIPTION = "Pick up a piece of gum and place it on the plate"

# Create the robot and teleoperator configurations
camera_config = {
    "top": OpenCVCameraConfig(index_or_path=6, width=640, height=480, fps=FPS),
    "front": RealSenseCameraConfig(
        serial_number_or_name="841612072123",
        fps=FPS,
        width=640,
        height=480,
        color_mode=ColorMode.RGB,
        use_depth=True,
        rotation=Cv2Rotation.NO_ROTATION
    )
}
robot_config = SO101FollowerConfig(
    port="/dev/tty.usbserial_lerobot_follower",
    id="lerobot_follower_arm",
    cameras=camera_config
)

# Initialize the robot and teleoperator
robot = SO101Follower(robot_config)

# Initialize the policy
policy = ACTPolicy.from_pretrained("CreatorKanata/act-gum-pickup-so-arm101")

# Configure the dataset features
action_features = hw_to_dataset_features(robot.action_features, "action")
obs_features = hw_to_dataset_features(robot.observation_features, "observation")
dataset_features = {**action_features, **obs_features}

# Create the dataset
dataset = LeRobotDataset.create(
    repo_id="CreatorKanata/eval-gum-pickup-so-arm101",
    fps=FPS,
    features=dataset_features,
    robot_type=robot.name,
    use_videos=True,
    image_writer_threads=4,
)

# Initialize the keyboard listener and rerun visualization
_, events = init_keyboard_listener()
_init_rerun(session_name="recording")

# Connect the robot and teleoperator
robot.connect()

for episode_idx in range(NUM_EPISODES):
    log_say(f"Running inference, recording eval episode {episode_idx + 1} of {NUM_EPISODES}")

    # Run the policy inference loop
    record_loop(
        robot=robot,
        events=events,
        fps=FPS,
        policy=policy,
        dataset=dataset,
        control_time_s=EPISODE_TIME_SEC,
        single_task=TASK_DESCRIPTION,
        display_data=True,
    )

    dataset.save_episode()

# Clean up
log_say("Stop recording")
robot.disconnect()
dataset.push_to_hub()

