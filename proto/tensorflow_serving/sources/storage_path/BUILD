load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [":file_system_storage_path_source_proto"],
)

proto_library(
    name = "file_system_storage_path_source_proto",
    srcs = ["file_system_storage_path_source.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
)
