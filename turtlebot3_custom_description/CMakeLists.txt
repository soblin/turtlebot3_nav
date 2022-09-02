cmake_minimum_required(VERSION 3.8)
project(turtlebot3_custom_description)

find_package(ament_cmake_auto REQUIRED)

ament_auto_package(INSTALL_TO_SHARE
  urdf
  meshes
  models
)
