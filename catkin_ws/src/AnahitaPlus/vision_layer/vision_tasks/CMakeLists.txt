cmake_minimum_required(VERSION 2.8.3)
project(vision_tasks)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  roscpp
  rospy
  sensor_msgs
  std_msgs
  dynamic_reconfigure
  image_transport
  message_generation
  geometry_msgs
)

find_package(Boost REQUIRED COMPONENTS system)
find_package(OpenCV REQUIRED)
find_package(vision_commons REQUIRED)

add_service_files (
    FILES
    ContourCenter.srv
)

generate_messages (
    DEPENDENCIES
    std_msgs   
)

catkin_package(LIBRARIES vision_commons)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${dynamic_reconfigure_PACKAGE_PATH}/cmake/cfgbuild.cmake 
  ${vision_commons_INCLUDE_DIRS}
  include/
)

add_library(base_class SHARED src/base_class.cpp include/base_class.h)
add_dependencies(base_class ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(base_class ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

# add_library(torpedo_task SHARED src/torpedo.cpp include/torpedo.h include/base_class.h)
# add_dependencies(torpedo_task base_class ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
# target_link_libraries(torpedo_task base_class ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(gate_task SHARED src/gate.cpp include/gate.h include/base_class.h)
add_dependencies(gate_task base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(gate_task base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

# add_library(cruc_task SHARED src/cruc.cpp include/cruc.h include/base_class.h)
# add_dependencies(cruc_task base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
# target_link_libraries(cruc_task base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(path_marker SHARED src/path_marker.cpp include/path_marker.h include/base_class.h)
add_dependencies(path_marker base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(path_marker base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(marker SHARED src/marker.cpp include/marker.h include/base_class.h)
add_dependencies(marker base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(marker base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(crucifix_task SHARED src/crucifix.cpp include/crucifix.h include/base_class.h)
add_dependencies(crucifix_task base_class ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(crucifix_task base_class ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons)

#add_library(grabber_test SHARED src/grabber.cpp include/grabber.h include/base_class.h)
#add_dependencies(grabber_test base_class ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
#target_link_libraries(grabber_test base_class ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons)

add_library(start_gate SHARED src/start_gate.cpp include/start_gate.h include/base_class.h)
add_dependencies(start_gate base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(start_gate base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(pinger SHARED src/pinger.cpp include/pinger.h include/base_class.h)
add_dependencies(pinger base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(pinger base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(startgate SHARED src/testgate.cpp include/testgate.h include/base_class.h)
add_dependencies(startgate base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(startgate base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(md SHARED src/marker_dropper.cpp include/marker_dropper.h include/base_class.h)
add_dependencies(md base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(md base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_library(triangular_buoy SHARED src/triangular_buoy.cpp include/triangular_buoy.h include/base_class.h)
add_dependencies(triangular_buoy base_class  ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(triangular_buoy base_class  ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} vision_commons )

add_executable(vision_node src/vision_node.cpp)
add_dependencies(vision_node ${vision_tasks_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(vision_node 
  ${catkin_LIBRARIES} 
  ${OpenCV_LIBRARIES} 
  vision_commons 
  gate_task 
  path_marker
  marker
  # torpedo_task
  triangular_buoy
  crucifix_task
  #grabber_test
  startgate
  # cruc_task
)
