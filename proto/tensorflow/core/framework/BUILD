load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":allocation_description_proto",
        ":api_def_proto",
        ":attr_value_proto",
        ":cost_graph_proto",
        ":dataset_options_proto",
        ":device_attributes_proto",
        ":full_type_proto",
        ":function_proto",
        ":graph_proto",
        ":graph_transfer_info_proto",
        ":kernel_def_proto",
        ":log_memory_proto",
        ":model_proto",
        ":node_def_proto",
        ":op_def_proto",
        ":reader_base_proto",
        ":resource_handle_proto",
        ":step_stats_proto",
        ":summary_proto",
        ":tensor_description_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":tensor_slice_proto",
        ":types_proto",
        ":variable_proto",
        ":versions_proto",
    ],
)

proto_library(
    name = "versions_proto",
    srcs = ["versions.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "variable_proto",
    srcs = ["variable.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "types_proto",
    srcs = ["types.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "tensor_slice_proto",
    srcs = ["tensor_slice.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "tensor_shape_proto",
    srcs = ["tensor_shape.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "tensor_description_proto",
    srcs = ["tensor_description.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":allocation_description_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "tensor_proto",
    srcs = ["tensor.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":resource_handle_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "summary_proto",
    srcs = ["summary.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "step_stats_proto",
    srcs = ["step_stats.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":allocation_description_proto",
        ":tensor_description_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "resource_handle_proto",
    srcs = ["resource_handle.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "reader_base_proto",
    srcs = ["reader_base.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "op_def_proto",
    srcs = ["op_def.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":attr_value_proto",
        ":full_type_proto",
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "node_def_proto",
    srcs = ["node_def.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":attr_value_proto",
        ":full_type_proto",
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "model_proto",
    srcs = ["model.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "log_memory_proto",
    srcs = ["log_memory.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":allocation_description_proto",
        ":tensor_description_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "kernel_def_proto",
    srcs = ["kernel_def.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":attr_value_proto",
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "graph_transfer_info_proto",
    srcs = ["graph_transfer_info.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [":types_proto"],
)

proto_library(
    name = "graph_proto",
    srcs = ["graph.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":attr_value_proto",
        ":full_type_proto",
        ":function_proto",
        ":node_def_proto",
        ":op_def_proto",
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
        ":versions_proto",
    ],
)

proto_library(
    name = "function_proto",
    srcs = ["function.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":attr_value_proto",
        ":full_type_proto",
        ":node_def_proto",
        ":op_def_proto",
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "full_type_proto",
    srcs = ["full_type.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "device_attributes_proto",
    srcs = ["device_attributes.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "dataset_options_proto",
    srcs = ["dataset_options.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "cost_graph_proto",
    srcs = ["cost_graph.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "attr_value_proto",
    srcs = ["attr_value.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "api_def_proto",
    srcs = ["api_def.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
    deps = [
        ":attr_value_proto",
        ":resource_handle_proto",
        ":tensor_proto",
        ":tensor_shape_proto",
        ":types_proto",
    ],
)

proto_library(
    name = "allocation_description_proto",
    srcs = ["allocation_description.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    strip_import_prefix = "/proto/",
)
