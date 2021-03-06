# launch gazebo

default `world_name` is `house [autorace, autorace2020, stage_[1, 2, 3, 4], world]`.

```bash
roslaunch turtlebot3_nav bringup_world.launch world_name:=house
```

# launch robot

default parameters are `model == burger [burger, waffle, waffle_pi]` , `robot_namespace == burger1` and `slam_method == cartographer [cartographer, gmapping]`.

## launch each robot

```bash
roslaunch turtlebot3_nav sim.launch model:=burger robot_namespace:=burger1 slam_method:=cartographer
roslaunch turtlebot3_path_planner move_base.launch robot_namespace:=burger1
```

## teleop

```bash
roslaunch turtlebot3_nav teleop_robot.launch robot_namespace:=burger1
```

![manual run of burger1 in house](doc/burger1_single_teleop.png)
