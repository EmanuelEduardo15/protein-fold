# rosetta_plugin/CMakeLists.txt  
add_library(curvometry_energy SHARED CurvometryEnergy.cc)  
target_link_libraries(curvometry_energy PUBLIC rosetta_core)
