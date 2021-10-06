#include <costmap_2d/costmap_2d_ros.h>
#include <ros/ros.h>
#include <tf2_ros/transform_listener.h>

int main(int argc, char** argv) {
  ros::init(argc, argv, "costmap");

  ros::NodeHandle nh;

  tf2_ros::Buffer tf_buf;

  costmap_2d::Costmap2DROS costmap("costmap", tf_buf);

  costmap.start();

  ros::spin();

  return 0;
}
