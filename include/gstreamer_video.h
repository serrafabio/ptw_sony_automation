//
// Created by serra on 12/12/2024.
//

#ifndef GSTREAMER_VIDEO_H
#define GSTREAMER_VIDEO_H

#include <gst/gst.h>

// Main function to run the GStreamer
void run_gstreamer_pipeline();

// Callback function to handle with the messages
static gboolean bus_callback(GstBus* bus, GstMessage* msg, gpointer data);

// Callback function to the bus
void register_bus_callback(GstElement* pipeline);

#endif // GSTREAMER_VIDEO_H