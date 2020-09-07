load("@rules_proto//proto:defs.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    strip_import_prefix = "/proto",
    deps = [":logging_proto"],
)

proto_library(
    name = "logging_proto",
    srcs = ["logging.proto"],
    strip_import_prefix = "/proto",
    deps = [
        "//proto/tensorflow_serving/apis:model_proto",
        "//proto/tensorflow_serving/config:logging_config_proto",
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
