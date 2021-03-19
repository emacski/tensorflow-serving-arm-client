load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core",
    strip_import_prefix = "/proto/",
    deps = [
        ":core_protos",
        ":error_codes_proto_impl",
    ],
)

proto_library(
    name = "core_protos",
    srcs = [
        "protobuf/bfc_memory_map.proto",
        "protobuf/cluster.proto",
        "protobuf/config.proto",
        "protobuf/control_flow.proto",
        "protobuf/data/experimental/snapshot.proto",
        "protobuf/debug.proto",
        "protobuf/debug_event.proto",
        "protobuf/device_filters.proto",
        "protobuf/device_properties.proto",
        "protobuf/graph_debug_info.proto",
        "protobuf/meta_graph.proto",
        "protobuf/named_tensor.proto",
        "protobuf/queue_runner.proto",
        "protobuf/remote_tensor_handle.proto",
        "protobuf/rewriter_config.proto",
        "protobuf/saved_model.proto",
        "protobuf/saved_object_graph.proto",
        "protobuf/saver.proto",
        "protobuf/struct.proto",
        "protobuf/tensor_bundle.proto",
        "protobuf/tensorflow_server.proto",
        "protobuf/trackable_object_graph.proto",
        "protobuf/transport_options.proto",
        "protobuf/verifier_config.proto",
    ],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core",
    strip_import_prefix = "/proto/",
    deps = [
        ":error_codes_proto_impl",
        "//proto/tensorflow/core/example:protos_all",
        "//proto/tensorflow/core/framework:protos_all",
        "//proto/tensorflow/core/lib/core:protos_all",
        "//proto/tensorflow/core/profiler:protos_all",
        "//proto/tensorflow/core/profiler/protobuf:protos_all",
        "//proto/tensorflow/core/util:protos_all",
    ],
)

proto_library(
    name = "error_codes_proto_impl",
    srcs = ["protobuf/error_codes.proto"],
    go_package = "github.com/tensorflow-serving-arm-client/go/tensorflow/core",
    strip_import_prefix = "/proto/",
)
