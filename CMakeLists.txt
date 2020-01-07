cmake_minimum_required(VERSION 2.8.3)
project(mixing_py2_py3_ros)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS
  scripts/py2.py
  scripts/py3.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

