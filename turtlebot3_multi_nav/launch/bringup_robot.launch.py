from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.launch_context import LaunchContext
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node, SetParameter
from ament_index_python.packages import get_package_share_directory

import os
import xacro
import launch

# https://answers.ros.org/question/382028/ros2-string-repr-of-parameter-within-launch-file/


def launch_setup(ctx, *args, **kwargs):
    # arguments
    model = LaunchConfiguration('model')
    robot_namespace = LaunchConfiguration(
        'robot_namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')
    x_pos = LaunchConfiguration('x_pos')
    y_pos = LaunchConfiguration('y_pos')
    z_pos = LaunchConfiguration('z_pos')

    # real value
    model = model.perform(ctx)
    robot_namespace = robot_namespace.perform(ctx)
    use_sim_time = bool(use_sim_time.perform(ctx))
    x_pos = x_pos.perform(ctx)
    y_pos = y_pos.perform(ctx)
    z_pos = z_pos.perform(ctx)

    # https://answers.ros.org/question/373824/ros2-launch-file-arguments-subsititutions-xacro-and-node-parameters/
    xacro_path = os.path.join(get_package_share_directory('turtlebot3_custom_description'),
                              'urdf', f'turtlebot3_{model}.urdf.xacro')
    urdf_xacro = xacro.process_file(
        xacro_path, mappings={'robot_namespace': robot_namespace})
    urdf_xml = urdf_xacro.toprettyxml()

    # robot_state_publisher
    rsp = Node(package='robot_state_publisher', executable='robot_state_publisher',
               name=f'{robot_namespace}_robot_state_publisher', output='screen',
               parameters=[{'robot_description': urdf_xml,
                            'use_sime_time': use_sim_time}],
               remappings=[('/robot_description', f'/{robot_namespace}_robot_description')])

    # gazebo spawner
    # https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Spawn-and-delete
    # https://gist.github.com/awesomebytes/2595b1dc41831c804a4f
    gr = Node(
        package='gazebo_ros', executable='spawn_entity.py', name=f'{robot_namespace}_spawn_urdf',
        arguments=['-entity', robot_namespace, '-topic', f'/{robot_namespace}_robot_description', '-x', x_pos, '-y', y_pos, '-z', z_pos])

    # setter
    set_model = SetParameter(name="model", value=model)
    set_robot_namespace =SetParameter(name="robot_namespace", value=robot_namespace)
    set_use_sim_time = SetParameter(name="use_sim_time", value=use_sim_time)
    set_x_pos= SetParameter(name="x_pos", value=x_pos)
    set_y_pos= SetParameter(name="y_pos", value=y_pos)
    set_z_pos= SetParameter(name="z_pos", value=z_pos)

    return [
        set_model,
        set_robot_namespace,
        set_use_sim_time,
        set_x_pos,
        set_y_pos,
        set_z_pos,
        rsp,
        gr,
    ]

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument("model"),
        DeclareLaunchArgument("robot_namespace"),
        DeclareLaunchArgument("use_sim_time"),
        DeclareLaunchArgument("x_pos"),
        DeclareLaunchArgument("y_pos"),
        DeclareLaunchArgument("z_pos"),
        OpaqueFunction(function=launch_setup),
    ])
