load("@rules_proto//proto:defs.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    strip_import_prefix = "/proto",
    deps = [
        "//proto/tensorflow_serving:protos_all",
        "@org_tensorflow//tensorflow/core:protos_all",
    ],
)
