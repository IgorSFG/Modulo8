from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="turtlebot3_gazebo",
            executable="turtlebot3_world.launch.py",
        ),
        Node(
            package="turtlebot3_teleop",
            executable="teleop_keyboard",
        ),
        Node(
            package="turtlebot3_cartographer",
            executable="cartographer.launch.py",
            name="cartographer",
            parameters=[
                {"use_sim_time": True},
            ]
        ),
    ])