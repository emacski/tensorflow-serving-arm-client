load("@rules_proto//proto:defs.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    strip_import_prefix = "/proto",
    deps = [
        "//proto/tensorflow_serving/apis:protos_all",
        "//proto/tensorflow_serving/config:protos_all",
        "//proto/tensorflow_serving/core:protos_all",
        "//proto/tensorflow_serving/sources/storage_path:protos_all",
        "//proto/tensorflow_serving/util:protos_all",
    ],
)
