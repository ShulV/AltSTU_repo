cmake_minimum_required(VERSION 3.0)

project(lab1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)


add_subdirectory(thirdparty/SDL2)
add_subdirectory(thirdparty/glm)

add_executable(lab1 main.cpp Window.h Window.cpp
    core/Vector3D.hpp core/Matrix.hpp core/MatrixTransform.hpp core/Vector4D.hpp
    figure.h figure.cpp)


target_link_libraries(lab1 SDL2)
target_link_libraries(lab1 glm)

