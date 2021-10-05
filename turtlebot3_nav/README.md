# launch gazebo

```
roslaunch turtlebot3_nav bringup_world.launch
```

# launch robot

default is `model == burger [burger, waffle, waffle_pi]` and `robot_namespace == burger1`.

`slam_method` is `gmapping` by default as of now.

## launch each robot

```
roslaunch turtlebot3_nav sim.launch model:=burger robot_namespace:=burger1 slam_method:=gmapping
```
## teleop

```
roslaunch turtlebot3_nav teleop_robot.launch robot_namespace:=burger1
```
