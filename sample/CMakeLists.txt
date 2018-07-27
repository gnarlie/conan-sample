cmake_minimum_required( VERSION 3.8 )
project ('example')


add_library(sample SHARED
    sample.cpp)

set_target_properties(sample PROPERTIES
    SOVERSION 1
    PUBLIC_HEADER sample.h)
