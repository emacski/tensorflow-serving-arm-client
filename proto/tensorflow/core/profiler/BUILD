load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/profiler",
    strip_import_prefix = "/proto/",
    deps = [":profiler_options_proto"],
)

proto_library(
    name = "profiler_options_proto",
    srcs = ["profiler_options.proto"],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/profiler",
    strip_import_prefix = "/proto/",
)
