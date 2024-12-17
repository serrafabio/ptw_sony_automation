//
// Created by serra on 12/12/2024.
//

#ifndef GSTREAMER_VIDEO_H
#define GSTREAMER_VIDEO_H

#include <gst/gst.h>

// Função principal para rodar o pipeline do GStreamer
void run_gstreamer_pipeline();

// Função de callback para lidar com mensagens do GStreamer
static gboolean bus_callback(GstBus* bus, GstMessage* msg, gpointer data);

// Registrar o callback do bus
void register_bus_callback(GstElement* pipeline);

#endif // GSTREAMER_VIDEO_H