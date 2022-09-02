cmake_minimum_required(VERSION 3.8)
project(turtlebot3_multi_nav)

find_package(ament_cmake_auto REQUIRED)

install(
  PROGRAMS
  scripts/teleop_keyboard.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_auto_package(INSTALL_TO_SHARE
  launch
  config
)
