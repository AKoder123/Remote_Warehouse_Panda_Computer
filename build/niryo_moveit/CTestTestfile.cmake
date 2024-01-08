# CMake generated Testfile for 
# Source directory: /home/hrigroup2/mrtele_ws/src/niryo_moveit
# Build directory: /home/hrigroup2/mrtele_ws/build/niryo_moveit
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_niryo_moveit_roslaunch-check_launch "/home/hrigroup2/mrtele_ws/build/niryo_moveit/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/hrigroup2/mrtele_ws/build/niryo_moveit/test_results/niryo_moveit/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/hrigroup2/mrtele_ws/build/niryo_moveit/test_results/niryo_moveit" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/hrigroup2/mrtele_ws/build/niryo_moveit/test_results/niryo_moveit/roslaunch-check_launch.xml\" \"/home/hrigroup2/mrtele_ws/src/niryo_moveit/launch\" ")
subdirs("gtest")
