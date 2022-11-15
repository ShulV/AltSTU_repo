


enable_testing()


add_executable(Matrix_Test Matrix_Test.cpp)
target_link_libraries(Matrix_Test ${Boost_LIBRARIES})

include_directories(${Boost_INCLUDE_DIRS})

add_test(NAME Matrix_Test COMMAND Matrix_Test)


add_executable(Transform_Test Transform_Test.cpp)
target_link_libraries(Transform_Test ${Boost_LIBRARIES})

add_test(NAME Transform_Test COMMAND Transform_Test)
