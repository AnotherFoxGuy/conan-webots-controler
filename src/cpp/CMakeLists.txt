project(CppController CXX)

file(GLOB_RECURSE SOURCE_FILES LIST_DIRECTORIES FALSE "*.hpp" "*.cpp")

include_directories(.)

if(NOT BUILD_C)
	link_libraries("${CMAKE_SOURCE_DIR}/../prebuild/Controller.lib")
endif()

if(NOT BUILD_C)
	add_library(${PROJECT_NAME} ${SOURCE_FILES})
else()
	add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES})
	target_link_libraries(${PROJECT_NAME} PUBLIC Controller)
endif()

install(TARGETS ${PROJECT_NAME}
	LIBRARY DESTINATION lib
	ARCHIVE DESTINATION lib
	PUBLIC_HEADER DESTINATION include
)

install(DIRECTORY "${CMAKE_SOURCE_DIR}/cpp/webots" DESTINATION "include")