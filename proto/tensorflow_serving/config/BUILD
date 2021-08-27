load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":file_system_storage_path_source_proto",
        ":log_collector_config_proto",
        ":logging_config_proto",
        ":model_server_config_proto",
    ],
)

proto_library(
    name = "model_server_config_proto",
    srcs = ["model_server_config.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":file_system_storage_path_source_proto",
        ":logging_config_proto",
    ],
)

proto_library(
    name = "file_system_storage_path_source_proto",
    srcs = ["file_system_storage_path_source.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "logging_config_proto",
    srcs = ["logging_config.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [":log_collector_config_proto"],
)

proto_library(
    name = "log_collector_config_proto",
    srcs = ["log_collector_config.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
)
