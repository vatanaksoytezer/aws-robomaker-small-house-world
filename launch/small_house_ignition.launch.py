import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # Ignition gazebo
    pkg_ros_ign_gazebo = get_package_share_directory('ros_ign_gazebo')
    pkg_stretch_ignition = get_package_share_directory('aws_robomaker_small_house_world')
    # TODO: Make world argument modular with bridge
    world_dir = os.path.join(pkg_stretch_ignition, 'worlds', 'small_house.sdf')
    world_str = "-r " + world_dir
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_ign_gazebo, 'launch', 'ign_gazebo.launch.py')),
        launch_arguments={'ign_args': world_str}.items(),
    )

    return LaunchDescription(
        [
            # Nodes and Launches
            gazebo,
        ]
    )
