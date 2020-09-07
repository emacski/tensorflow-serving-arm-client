load("@rules_proto//proto:defs.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    strip_import_prefix = "/proto",
    deps = [
        ":log_collector_config_proto",
        ":logging_config_proto",
        ":model_server_config_proto",
    ],
)

proto_library(
    name = "log_collector_config_proto",
    srcs = ["log_collector_config.proto"],
    strip_import_prefix = "/proto",
    deps = [
        "@com_google_protobuf//:any_proto",
        "@com_google_protobuf//:api_proto",
        "@com_google_protobuf//:compiler_plugin_proto",
        "@com_google_protobuf//:descriptor_proto",
        "@com_google_protobuf//:duration_proto",
        "@com_google_protobuf//:empty_proto",
        "@com_google_protobuf//:field_mask_proto",
        "@com_google_protobuf//:source_context_proto",
        "@com_google_protobuf//:struct_proto",
        "@com_google_protobuf//:timestamp_proto",
        "@com_google_protobuf//:type_proto",
        "@com_google_protobuf//:wrappers_proto",
    ],
)

proto_library(
    name = "logging_config_proto",
    srcs = ["logging_config.proto"],
    strip_import_prefix = "/proto",
    deps = [
        ":log_collector_config_proto",
        "@com_google_protobuf//:any_proto",
        "@com_google_protobuf//:api_proto",
        "@com_google_protobuf//:compiler_plugin_proto",
        "@com_google_protobuf//:descriptor_proto",
        "@com_google_protobuf//:duration_proto",
        "@com_google_protobuf//:empty_proto",
        "@com_google_protobuf//:field_mask_proto",
        "@com_google_protobuf//:source_context_proto",
        "@com_google_protobuf//:struct_proto",
        "@com_google_protobuf//:timestamp_proto",
        "@com_google_protobuf//:type_proto",
        "@com_google_protobuf//:wrappers_proto",
    ],
)

proto_library(
    name = "model_server_config_proto",
    srcs = ["model_server_config.proto"],
    strip_import_prefix = "/proto",
    deps = [
        ":logging_config_proto",
        "//proto/tensorflow_serving/sources/storage_path:file_system_storage_path_source_proto",
        "@com_google_protobuf//:any_proto",
        "@com_google_protobuf//:api_proto",
        "@com_google_protobuf//:compiler_plugin_proto",
        "@com_google_protobuf//:descriptor_proto",
        "@com_google_protobuf//:duration_proto",
        "@com_google_protobuf//:empty_proto",
        "@com_google_protobuf//:field_mask_proto",
        "@com_google_protobuf//:source_context_proto",
        "@com_google_protobuf//:struct_proto",
        "@com_google_protobuf//:timestamp_proto",
        "@com_google_protobuf//:type_proto",
        "@com_google_protobuf//:wrappers_proto",
    ],
)
