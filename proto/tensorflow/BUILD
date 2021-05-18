load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    strip_import_prefix = "/proto/",
    deps = [
        "//proto/tensorflow/core:protos_all",
        "//proto/tensorflow/core/example:protos_all",
        "//proto/tensorflow/core/framework:protos_all",
        "//proto/tensorflow/core/grappler/costs:protos_all",
        "//proto/tensorflow/core/lib/core:protos_all",
        "//proto/tensorflow/core/profiler:protos_all",
        "//proto/tensorflow/core/profiler/protobuf:protos_all",
        "//proto/tensorflow/core/util:protos_all",
    ],
)
