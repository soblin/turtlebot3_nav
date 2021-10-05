# launch gazebo

```
roslaunch turtlebot3_nav bringup_world.launch
```

# launch robot

default parameters are `model == burger [burger, waffle, waffle_pi]` , `robot_namespace == burger1` and `slam_method == cartographer [cartographer, gmapping]`.

## launch each robot

```
roslaunch turtlebot3_nav sim.launch model:=burger robot_namespace:=burger1 slam_method:=cartographer
```
## teleop

```
roslaunch turtlebot3_nav teleop_robot.launch robot_namespace:=burger1
```
