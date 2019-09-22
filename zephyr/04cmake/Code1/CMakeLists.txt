
#cmake_minimum_required (VERSION 2.6)
cmake_minimum_required(VERSION 3.13.1)
message(STATUS "test code")
include(boilerplate.cmake)
project(HELLO)
set(SRC_LIST main.c)
add_executable(hello ${SRC_LIST})