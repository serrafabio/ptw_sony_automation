//
// Created by serra on 12/12/2024.
//
#include "../include/gstreamer_video.h"
#include <iostream>
#include <cstdlib>
#include <filesystem>

namespace fs = std::filesystem;  // Alias to use the files


// Function to run the GStreamer pipeline
void run_gstreamer_pipeline() {
    // Retrieve the current GST_PLUGIN_PATH environment variable
    char* gstPluginPathEnv = getenv("GST_PLUGIN_PATH");

    // If GST_PLUGIN_PATH is already set, append the current path to it
    if (gstPluginPathEnv != nullptr) {
        std::string gstPluginPath = fs::current_path().string() + ";" + gstPluginPathEnv;
        _putenv_s("GST_PLUGIN_PATH", gstPluginPath.c_str()); // Update the GST_PLUGIN_PATH
    } else {
        // If not set, initialize GST_PLUGIN_PATH to the current directory
        _putenv_s("GST_PLUGIN_PATH", fs::current_path().string().c_str());
    }

    // Initialize GStreamer
    gst_init(nullptr, nullptr);

    // Create a new GMainLoop for event-driven execution
    GMainLoop *mainLoop = g_main_loop_new(nullptr, FALSE);

    // Define the GStreamer pipeline string
    // This pipeline handles video and audio decoding using OpenGL rendering
    // char *pipeLineString = "esvideosrc name=esvdsrc ! queue ! h264parse ! avdec_h264 ! glupload ! glcolorconvert ! glimagesink name=glsink "
    //                       "esaudiosrc name=esausrc ! queue ! aacparse ! avdec_aac ! audioconvert ! directsoundsink name=ausnk";
    char *pipeLineString = "ksvideosrc device-index=1 ! videoconvert ! autovideosink";

    // Uncomment the following line to test with a webcam pipeline instead
    //char *pipeLineString = "ksvideosrc device-index=0 ! videoconvert ! autovideosink"; // webcam

    // Create the GStreamer pipeline from the string
    GError *error = NULL;
    GstElement *pipeline = gst_parse_launch(pipeLineString, &error);

    // Check if there was an error creating the pipeline
    if (error != nullptr) {
        fprintf(stderr, "Error to create the pipeline: %s\n", error->message);
        g_error_free(error); // Free the error message
        return;
    }

    // Get the bus from the pipeline to listen for messages
    GstBus *bus = gst_element_get_bus(pipeline);
    gst_bus_add_watch(bus, bus_callback, nullptr); // Register a callback for bus messages
    gst_object_unref(bus); // Release the bus object

    // Set the pipeline state to PAUSED, then to PLAYING
    GstStateChangeReturn ret = gst_element_set_state(pipeline, GST_STATE_PAUSED);
    ret = gst_element_set_state(pipeline, GST_STATE_PLAYING);

    // Start the GMainLoop to keep the pipeline running
    g_main_loop_run(mainLoop);

    // Cleanup: Stop the pipeline and release resources
    gst_element_set_state(pipeline, GST_STATE_NULL);
    gst_object_unref(pipeline);
    g_main_loop_unref(mainLoop);
}

// Callback function for GStreamer bus messages
static gboolean bus_callback(GstBus* bus, GstMessage* msg, gpointer data) {
    // Check the type of message received on the bus
    switch (GST_MESSAGE_TYPE(msg)) {
        case GST_MESSAGE_EOS: // End-Of-Stream message
            printf("GST_MESSAGE_EOS\n");
            break;
        case GST_MESSAGE_ERROR: // Error message
            printf("GST_MESSAGE_ERROR\n");
            break;
        default:
            break;  // Ignore other message types
    }
    return TRUE; // Return TRUE to keep watching the bus
}

// Function to register the bus callback for the pipeline
void register_bus_callback(GstElement *pipeline){
    // Get the bus from the pipeline
    GstBus* bus = gst_element_get_bus(pipeline);
    // Add a watch on the bus to handle messages asynchronously
    unsigned int watchId = gst_bus_add_watch(bus, bus_callback, nullptr);
}
