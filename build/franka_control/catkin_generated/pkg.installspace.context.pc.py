# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/include".split(';') if "${prefix}/include;/usr/include" != "" else []
PROJECT_CATKIN_DEPENDS = "controller_interface;franka_hw;franka_msgs;geometry_msgs;pluginlib;realtime_tools;roscpp;sensor_msgs;tf2_msgs".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lfranka_state_controller;/usr/lib/libfranka.so.0.7.1".split(';') if "-lfranka_state_controller;/usr/lib/libfranka.so.0.7.1" != "" else []
PROJECT_NAME = "franka_control"
PROJECT_SPACE_DIR = "/home/hrigroup2/mrtele_ws/install"
PROJECT_VERSION = "0.7.1"
