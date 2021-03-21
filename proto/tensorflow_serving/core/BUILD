load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [":logging_proto"],
)

proto_library(
    name = "logging_proto",
    srcs = ["logging.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        "//proto/tensorflow_serving/apis:model_proto",
        "//proto/tensorflow_serving/config:logging_config_proto",
    ],
)
