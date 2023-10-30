import os
from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    config = os.path.join(
            get_package_share_directory("ros2_kitti_publishers"),
            "config",
            "kitti_config.yaml"
            )
    
    node = Node(package = "ros2_kitti_publishers",
                name = "publisher_node",
                executable="kitti_publishers",
                parameters=[config]
                )

    ld.add_action(node);
    return ld;

