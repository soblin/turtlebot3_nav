# turtlebot3_custom_description

## Why we cannot use default turtlebot3_description

Cartographer does not accept topic/tf with namespacing like `burger1/base_footprint`, `/burger1/scan`, `/burger1/odom` (the prefix is ignored even if you specified it). This is problematic in multi-robot settings because cartographer node on each robot cannot separate topic/tf of other robots, leading to interferances.

The urdf files of this package take `robot_namespace` (like burger1) as a parameter when being loaded as `robot_description`, and expands tf link with the form of `<robot_namespace>_base_link`.

```xml
<param name="$(arg robot_namespace)_robot_description"
       command="$(find xacro)/xacro --inorder $(find turtlebot3_custom_description)/urdf/turtlebot3_$(arg model).urdf.xacro robot_namespace:=$(arg robot_namespace)"
/>
```

In this way we do not need to specify `tf_prerix` in `robot_state_publisher`, therefore can avoid the usage of `/` for `robot_description`. Also `*.gazebo.urdf` files are also customized to publish `${prefix}_{odom, scan, etc..}` instead of `${prefix}/{odom, scan, etc..}`.

```xml
<node name="$(arg robot_namespace)_robot_state_publisher"
      type="robot_state_publisher"
      pkg="robot_state_publisher">
   <remap from="robot_description" to="$(arg robot_namespace)_robot_description"/>
</node>
```

The drawback of this approach is that we have to migrate most of the topic names from `/` to `_` prefixing, resulting in a lot of remappings in launch files.
