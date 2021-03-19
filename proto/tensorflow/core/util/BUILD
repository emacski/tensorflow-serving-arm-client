load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/util",
    strip_import_prefix = "/proto/",
    deps = [
        ":event_proto",
        ":memmapped_file_system_proto",
        ":saved_tensor_slice_proto",
        ":test_log_proto",
    ],
)

proto_library(
    name = "test_log_proto",
    srcs = ["test_log.proto"],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/util",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "saved_tensor_slice_proto",
    srcs = ["saved_tensor_slice.proto"],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/util",
    strip_import_prefix = "/proto/",
    deps = [
        "//proto/tensorflow/core/framework:resource_handle_proto",
        "//proto/tensorflow/core/framework:tensor_proto",
        "//proto/tensorflow/core/framework:tensor_shape_proto",
        "//proto/tensorflow/core/framework:tensor_slice_proto",
        "//proto/tensorflow/core/framework:types_proto",
        "//proto/tensorflow/core/framework:versions_proto",
    ],
)

proto_library(
    name = "memmapped_file_system_proto",
    srcs = ["memmapped_file_system.proto"],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/util",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "event_proto",
    srcs = ["event.proto"],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/util",
    strip_import_prefix = "/proto/",
    deps = [
        "//proto/tensorflow/core/framework:resource_handle_proto",
        "//proto/tensorflow/core/framework:summary_proto",
        "//proto/tensorflow/core/framework:tensor_proto",
        "//proto/tensorflow/core/framework:tensor_shape_proto",
        "//proto/tensorflow/core/framework:types_proto",
    ],
)
