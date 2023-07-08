cmake_minimum_required(VERSION 3.17)
project(Lab1_C__)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Lab1_C__
        edge.cpp
        edge.h graph.cpp graph.h vectorIterator.cpp vectorIterator.h vertexIterator.cpp vertexIterator.h customHash.cpp customHash.h wgraph.cpp wgraph.h main.cpp)
