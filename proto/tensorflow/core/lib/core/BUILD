load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/lib/core",
    strip_import_prefix = "/proto/",
    deps = [":error_codes_proto"],
)

proto_library(
    name = "error_codes_proto",
    srcs = ["error_codes.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/lib/core",
    strip_import_prefix = "/proto/",
    deps = ["//proto/tensorflow/core:error_codes_proto_impl"],
)
