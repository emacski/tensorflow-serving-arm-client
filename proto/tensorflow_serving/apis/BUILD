load("@com_github_emacski_bazeltools//protobuf:proto.bzl", "proto_library")

package(default_visibility = ["//visibility:public"])

proto_library(
    name = "protos_all",
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":classification_proto",
        ":get_model_metadata_proto",
        ":get_model_status_proto",
        ":inference_proto",
        ":input_proto",
        ":logging_proto",
        ":model_management_proto",
        ":model_proto",
        ":model_service_proto",
        ":predict_proto",
        ":prediction_log_proto",
        ":prediction_service_proto",
        ":regression_proto",
        ":session_service_proto",
        ":status_proto",
    ],
)

proto_library(
    name = "protos_grpc_all",
    srcs = [
        "model_service.proto",
        "prediction_service.proto",
    ],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":classification_proto",
        ":get_model_metadata_proto",
        ":get_model_status_proto",
        ":inference_proto",
        ":model_management_proto",
        ":predict_proto",
        ":regression_proto",
    ],
)

proto_library(
    name = "prediction_service_proto",
    srcs = ["prediction_service.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":classification_proto",
        ":get_model_metadata_proto",
        ":inference_proto",
        ":predict_proto",
        ":regression_proto",
    ],
)

proto_library(
    name = "prediction_log_proto",
    srcs = ["prediction_log.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":classification_proto",
        ":inference_proto",
        ":logging_proto",
        ":predict_proto",
        ":regression_proto",
        ":session_service_proto",
    ],
)

proto_library(
    name = "session_service_proto",
    srcs = ["session_service.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":model_proto",
        "//proto/tensorflow/core:protos_all",
    ],
)

proto_library(
    name = "predict_proto",
    srcs = ["predict.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":model_proto",
        "//proto/tensorflow/core/framework:tensor_proto",
    ],
)

proto_library(
    name = "model_service_proto",
    srcs = ["model_service.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":get_model_status_proto",
        ":model_management_proto",
    ],
)

proto_library(
    name = "model_management_proto",
    srcs = ["model_management.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":status_proto",
        "//proto/tensorflow_serving/config:model_server_config_proto",
    ],
)

proto_library(
    name = "logging_proto",
    srcs = ["logging.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":model_proto",
        "//proto/tensorflow_serving/config:logging_config_proto",
    ],
)

proto_library(
    name = "inference_proto",
    srcs = ["inference.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":classification_proto",
        ":input_proto",
        ":model_proto",
        ":regression_proto",
    ],
)

proto_library(
    name = "regression_proto",
    srcs = ["regression.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":input_proto",
        ":model_proto",
    ],
)

proto_library(
    name = "get_model_status_proto",
    srcs = ["get_model_status.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":model_proto",
        ":status_proto",
    ],
)

proto_library(
    name = "status_proto",
    srcs = ["status.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = ["//proto/tensorflow/core:protos_all"],
)

proto_library(
    name = "get_model_metadata_proto",
    srcs = ["get_model_metadata.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":model_proto",
        "//proto/tensorflow/core:protos_all",
    ],
)

proto_library(
    name = "classification_proto",
    srcs = ["classification.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = [
        ":input_proto",
        ":model_proto",
    ],
)

proto_library(
    name = "model_proto",
    srcs = ["model.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
)

proto_library(
    name = "input_proto",
    srcs = ["input.proto"],
    go_package = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    strip_import_prefix = "/proto/",
    deps = ["//proto/tensorflow/core/example:example_proto"],
)
