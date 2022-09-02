# launch gazebo

default `world_name` is `house [house, dqn_stage[1, 2, 3, 4], world]`.

```bash
ros2 launch turtlebot3_mulit_nav bringup_world.launch.xml
```

# launch robot

default parameters are `model == burger [burger, waffle, waffle_pi]` , `robot_namespace == burger1`.

## launch each robot

```bash
ros2 launch turtlebot3_multi_nav bringup_robot.launch.py
```

## teleop

```bash
ros2 run turtlebot3_multi_nav teleop_keyborad.py --ros-args -p robot_namespace:=burger1
```

![manual run of burger1 in house](doc/burger1_single_teleop.png)
