cmake_minimum_required(VERSION 3.10)
project(SampleProject)

add_executable(sample_project src/main.cpp src/utils.cpp)

target_include_directories(sample_project PUBLIC
    include
)
