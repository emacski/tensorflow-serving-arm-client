load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [":status_proto"],
)

proto_library(
    name = "status_proto",
    srcs = ["status.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = ["//proto/tensorflow/core:protos_all"],
)
