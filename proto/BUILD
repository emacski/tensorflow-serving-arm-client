load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    strip_import_prefix = "/proto/",
    deps = [
        "//proto/tensorflow:protos_all",
        "//proto/tensorflow_serving:protos_all",
    ],
)
