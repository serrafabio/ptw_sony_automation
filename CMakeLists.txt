cmake_minimum_required(VERSION 3.10)
project(GStreamerExample)

# Defina a versão do C++
set(CMAKE_CXX_STANDARD 17)

# Adicione o diretório de cabeçalhos do GStreamer
include_directories("C:/gstreamer/1.0/msvc_x86_64/include/gstreamer-1.0")
include_directories("C:/gstreamer/1.0/msvc_x86_64/include/glib-2.0")
include_directories("C:/gstreamer/1.0/msvc_x86_64/lib/gstreamer-1.0/include")
include_directories("C:/gstreamer/1.0/msvc_x86_64/lib/glib-2.0/include")
include_directories(${CMAKE_SOURCE_DIR}/include)

# Adicione os diretórios das bibliotecas
link_directories("C:/gstreamer/1.0/msvc_x86_64/lib")

# Use o pkg-config para garantir que os caminhos estão corretos
find_package(PkgConfig REQUIRED)
pkg_check_modules(GSTREAMER REQUIRED gstreamer-1.0)

# Encontra os arquivos fonte do projeto
file(GLOB SOURCES "src/*.cpp")

# Adicione o executável
add_executable(GStreamerExample  ${SOURCES})

# Linke o GStreamer ao projeto
target_link_libraries(GStreamerExample gstreamer-1.0 glib-2.0 gobject-2.0)