cmake_minimum_required(VERSION 3.14)
project(Figuras LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# -------- GoogleTest via FetchContent --------
include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG v1.14.0
  DOWNLOAD_EXTRACT_TIMESTAMP ON
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# -------- Librería con la lógica de figuras --------
add_library(figuraslib
    Esfera.cpp
    Cuadrado.cpp
    Circulo.cpp
    Cubo.cpp
)
target_include_directories(figuraslib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# -------- Ejecutable principal --------
add_executable(Figuras
    Main.cpp
    Gestionar.cpp
)
target_link_libraries(Figuras PRIVATE figuraslib)

# (Opcional) salida a bin/
set_target_properties(Figuras PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# -------- Tests con GoogleTest (opcional si existe el archivo) --------
set(TEST_FILE "${CMAKE_CURRENT_SOURCE_DIR}/test_figuras.cpp")

if(EXISTS "${TEST_FILE}")
    add_executable(tests_figuras "${TEST_FILE}")
    target_link_libraries(tests_figuras PRIVATE figuraslib gtest_main)
    target_include_directories(tests_figuras PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})
    set_target_properties(tests_figuras PROPERTIES
        RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    )
    enable_testing()
    add_test(NAME all_tests COMMAND $<TARGET_FILE:tests_figuras>)
else()
    message(WARNING "No se encontró ${TEST_FILE}. Se omiten los tests.")
endif()
