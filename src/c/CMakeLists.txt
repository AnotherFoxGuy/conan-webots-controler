project(Controller C)

file(GLOB_RECURSE SOURCE_FILES LIST_DIRECTORIES FALSE "*.h" "*.c")

include_directories("${CMAKE_SOURCE_DIR}/c")

if(BUILD_C)
	add_library(${PROJECT_NAME} SHARED ${SOURCE_FILES})

	install(TARGETS ${PROJECT_NAME} 
		LIBRARY DESTINATION lib
		ARCHIVE DESTINATION lib
		PUBLIC_HEADER DESTINATION include
	)
endif()

install(DIRECTORY "${CMAKE_SOURCE_DIR}/c/webots" DESTINATION "include")