from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.launch_context import LaunchContext
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import xacro
import launch


def generate_launch_description():
    # arguments
    model = LaunchConfiguration('model', default='burger')
    robot_namespace = LaunchConfiguration(
        'robot_namespace', default="burger1")
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    x = LaunchConfiguration('x', default='-3.0')
    y = LaunchConfiguration('y', default='0.0')
    z = LaunchConfiguration('z', default='0.0')

    # get value
    ctx = LaunchContext()
    model = model.perform(ctx)
    robot_namespace = robot_namespace.perform(ctx)
    use_sim_time = use_sim_time.perform(ctx)
    x = x.perform(ctx)
    y = y.perform(ctx)
    z = z.perform(ctx)

    # https://answers.ros.org/question/373824/ros2-launch-file-arguments-subsititutions-xacro-and-node-parameters/
    xacro_path = os.path.join(get_package_share_directory('turtlebot3_custom_description'),
                              'urdf', f'turtlebot3_{model}.urdf.xacro')
    urdf_xacro = xacro.process_file(
        xacro_path, mappintgs={'robot_namespace': robot_namespace})
    urdf_xml = urdf_xacro.toprettyxml()

    # robot_state_publisher
    rsp = Node(package='robot_state_publisher', executable='robot_state_publisher',
               name=f'{robot_namespace}_robot_state_publisher', output='screen',
               parameters=[{'robot_description': urdf_xml}],
               remappings=[('/robot_description', f'/{robot_namespace}_robot_description')])
    rviz_cfg_dir = os.path.join(get_package_share_directory(
        'turtlebot3_multi_nav'), f'config/sim_{model}.rviz')
    rviz = Node(package='rviz2', executable='rviz2',
                output='screen', arguments=['-d', rviz_cfg_dir])
    # https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Spawn-and-delete
    # https://gist.github.com/awesomebytes/2595b1dc41831c804a4f
    gr = Node(
        package='gazebo_ros', executable='spawn_entity.py', name=f'{robot_namespace}_spawn_urdf',
        arguments=['-entity', robot_namespace, '-topic', f'/{robot_namespace}_robot_description', '-x', x, '-y', y, '-z', z])

    return launch.LaunchDescription([rsp, rviz, gr])
