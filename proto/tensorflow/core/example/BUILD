load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/example",
    strip_import_prefix = "/proto/",
    deps = [
        ":example_parser_configuration_proto",
        ":example_proto",
        ":feature_proto",
    ],
)

proto_library(
    name = "feature_proto",
    srcs = ["feature.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/example",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "example_parser_configuration_proto",
    srcs = ["example_parser_configuration.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/example",
    strip_import_prefix = "/proto/",
    deps = [
        "//proto/tensorflow/core/framework:resource_handle_proto",
        "//proto/tensorflow/core/framework:tensor_proto",
        "//proto/tensorflow/core/framework:tensor_shape_proto",
        "//proto/tensorflow/core/framework:types_proto",
    ],
)

proto_library(
    name = "example_proto",
    srcs = ["example.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/example",
    strip_import_prefix = "/proto/",
    deps = [":feature_proto"],
)
