cmake_minimum_required(VERSION 3.5)
project(nav2_bringup)

find_package(ament_cmake REQUIRED)
find_package(nav2_common REQUIRED)
find_package(navigation2 REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(livox_ros_driver2 REQUIRED)
find_package(pcl_conversions REQUIRED)
find_package(PCL REQUIRED)
find_package(autoaim_interfaces REQUIRED)
include_directories(
    ${EIGEN3_INCLUDE_DIR}
    ${PCL_INCLUDE_DIRS}
)
add_executable(livox_repub src/livox_repub.cpp)
ament_target_dependencies(livox_repub
    rclcpp
    sensor_msgs
    nav_msgs
    geometry_msgs
    std_msgs
    pcl_conversions
    tf2_ros
    livox_ros_driver2
)
target_link_libraries(livox_repub
    ${PCL_LIBRARIES}
    ${OpenCV_LIBS}
)

add_executable(send_goals src/send_goals.cpp)
ament_target_dependencies(send_goals rclcpp rclcpp_action nav2_msgs)

add_executable(when_to_go_node src/when_to_go.cpp)
ament_target_dependencies(when_to_go_node rclcpp rclcpp_action nav2_msgs)

add_executable(send_goal_num_node src/send_goal_num.cpp)
ament_target_dependencies(send_goal_num_node rclcpp std_msgs)

add_executable(virtual_chassis src/virtual_chassis.cpp)
ament_target_dependencies(virtual_chassis rclcpp std_msgs geometry_msgs tf2_ros tf2 autoaim_interfaces)

# add_executable(cmd_vel_repub_node src/cmd_vel_repub.cpp)
# ament_target_dependencies(cmd_vel_repub_node rclcpp geometry_msgs)

nav2_package()

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY maps DESTINATION share/${PROJECT_NAME})
install(DIRECTORY rviz DESTINATION share/${PROJECT_NAME})
install(DIRECTORY worlds DESTINATION share/${PROJECT_NAME})
install(DIRECTORY params DESTINATION share/${PROJECT_NAME})
install(DIRECTORY urdf DESTINATION share/${PROJECT_NAME})
install(TARGETS
  send_goals
  when_to_go_node
  send_goal_num_node
  virtual_chassis
  # cmd_vel_repub_node
  livox_repub
  DESTINATION lib/${PROJECT_NAME}
)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
