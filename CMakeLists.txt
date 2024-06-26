cmake_minimum_required(VERSION 3.5.0)
project(phantomjs)

set (CMAKE_CXX_STANDARD 11)

find_package(Qt5 COMPONENTS Core Network Widgets REQUIRED)
find_package(Threads REQUIRED)

if(NOT DEFINED Qt5WebKit_DIR)
    set(Qt5WebKit_DIR "/home/ubuntu/webkit-master")
endif()

message("Using Qt version ${Qt5Core_VERSION}")
if (Qt5Core_VERSION VERSION_LESS 5.5.0)
  message(FATAL_ERROR "This version of Qt is not supported. Please use Qt 5.5 or later")
endif()

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

file(GLOB_RECURSE PHANTOMJS_SOURCES src/*.cpp)
include_directories(src)
set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(THIRDPARTY_SOURCES src/mongoose/mongoose.c src/qcommandline/qcommandline.cpp src/linenoise/src/linenoise.c)
include_directories(src/linenoise/src)
include_directories(src/mongoose)
include_directories(src/qcommandline)
include_directories(${Qt5WebKit_DIR}/include)
include_directories(${Qt5WebKit_DIR}/include/QtWebKit)
include_directories(${Qt5WebKit_DIR}/include/QtWebKitWidgets)
link_directories(${Qt5WebKit_DIR}/lib)

if (WIN32)
  set(EXTRA_LIBS ws2_32)
  add_definitions(-DQCOMMANDLINE_STATIC)
else()
  set(EXTRA_LIBS dl)
endif()

add_executable(${PROJECT_NAME} src/phantomjs.qrc ${PHANTOMJS_SOURCES} ${THIRDPARTY_SOURCES})
target_link_libraries(${PROJECT_NAME} ${EXTRA_LIBS} Qt5::Core Qt5::Network Qt5::Widgets Qt5WebKitWidgets Qt5WebKit Threads::Threads)
install(TARGETS ${PROJECT_NAME} DESTINATION bin)

add_custom_target(check COMMAND python test/run-tests.py -v)
