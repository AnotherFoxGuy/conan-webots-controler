project(CppController CXX)

file(GLOB_RECURSE SOURCE_FILES LIST_DIRECTORIES FALSE "*.hpp" "*.cpp")

include_directories(.)

add_library(${PROJECT_NAME} ${SOURCE_FILES})

install(TARGETS ${PROJECT_NAME}
	LIBRARY DESTINATION lib
	ARCHIVE DESTINATION lib
	PUBLIC_HEADER DESTINATION include
)
install(DIRECTORY "${CMAKE_SOURCE_DIR}/cpp/webots" DESTINATION "include")