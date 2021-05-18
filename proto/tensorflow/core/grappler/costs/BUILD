load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/grappler/costs",
    strip_import_prefix = "/proto/",
    deps = [":op_performance_data_proto"],
)

proto_library(
    name = "op_performance_data_proto",
    srcs = ["op_performance_data.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/grappler/costs",
    strip_import_prefix = "/proto/",
    deps = [
        "//proto/tensorflow/core:error_codes_proto_impl",
        "//proto/tensorflow/core/framework:allocation_description_proto",
        "//proto/tensorflow/core/framework:api_def_proto",
        "//proto/tensorflow/core/framework:attr_value_proto",
        "//proto/tensorflow/core/framework:cost_graph_proto",
        "//proto/tensorflow/core/framework:dataset_options_proto",
        "//proto/tensorflow/core/framework:device_attributes_proto",
        "//proto/tensorflow/core/framework:function_proto",
        "//proto/tensorflow/core/framework:graph_proto",
        "//proto/tensorflow/core/framework:graph_transfer_info_proto",
        "//proto/tensorflow/core/framework:kernel_def_proto",
        "//proto/tensorflow/core/framework:log_memory_proto",
        "//proto/tensorflow/core/framework:model_proto",
        "//proto/tensorflow/core/framework:node_def_proto",
        "//proto/tensorflow/core/framework:op_def_proto",
        "//proto/tensorflow/core/framework:reader_base_proto",
        "//proto/tensorflow/core/framework:resource_handle_proto",
        "//proto/tensorflow/core/framework:step_stats_proto",
        "//proto/tensorflow/core/framework:summary_proto",
        "//proto/tensorflow/core/framework:tensor_description_proto",
        "//proto/tensorflow/core/framework:tensor_proto",
        "//proto/tensorflow/core/framework:tensor_shape_proto",
        "//proto/tensorflow/core/framework:tensor_slice_proto",
        "//proto/tensorflow/core/framework:types_proto",
        "//proto/tensorflow/core/framework:variable_proto",
        "//proto/tensorflow/core/framework:versions_proto",
    ],
)
