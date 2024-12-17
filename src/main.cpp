//
// Created by serra on 12/12/2024.
//

#include "../include/gstreamer_video.h"
#include <iostream>

int main() {
    // Initialize the pipeline of GStreamer
    std::cout << "Initializing GStreamer..." << std::endl;
    run_gstreamer_pipeline();
    return 0;
}