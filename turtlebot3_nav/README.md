# launch gazebo

```
roslaunch turtlebot3_nav bringup_world.launch
```

# launch robot

default is `model == burger [burger, waffle, waffle_pi]` and `robot_namespace == burger1`.

## launch each robot

```
roslaunch turtlebot3_nav sim.launch model:=burger robot_namespace:=burger1
```
## teleop

```
roslaunch turtlebot3_nav teleop_robot.launch robot_namespace:=burger1
```
