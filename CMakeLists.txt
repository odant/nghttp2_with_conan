cmake_minimum_required(VERSION 3.0)
project(nghttp2_with_conan C CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(vendor/cmake-conan/conan.cmake)
conan_cmake_run(
    CONANFILE conanfile.py
    BASIC_SETUP CMAKE_TARGETS
)

set(ENABLE_ASIO_LIB ON)
set(ENABLE_APP OFF)
set(ENABLE_EXAMPLES OFF)
set(ENABLE_PYTHON_BINDINGS OFF)
set(WITH_LIBXML2 OFF)
set(WITH_SPDYLAY OFF)
set(WITH_MRUBY OFF)
set(WITH_NEVERBLEED OFF)
set(ENABLE_PYTHON_BINDINGS OFF)

if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(ENABLE_DEBUG ON)
endif()

add_subdirectory(vendor/nghttp2)
