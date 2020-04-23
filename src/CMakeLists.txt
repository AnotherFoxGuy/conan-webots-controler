cmake_minimum_required(VERSION 3.5)
project(webots-controller)

option(BUILD_C "C" ON)

include_directories("${CMAKE_SOURCE_DIR}/cpp" "${CMAKE_SOURCE_DIR}/c")


add_subdirectory(c)
add_subdirectory(cpp)
