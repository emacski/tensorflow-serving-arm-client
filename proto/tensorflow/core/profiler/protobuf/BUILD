load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/profiler/protobuf",
    strip_import_prefix = "/proto/",
    deps = [":xplane_proto"],
)

proto_library(
    name = "xplane_proto",
    srcs = ["xplane.proto"],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/profiler/protobuf",
    strip_import_prefix = "/proto/",
)
