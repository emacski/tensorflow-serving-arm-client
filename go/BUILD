# Copyright 2021 Erik Maciejewski
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

load(
    "@com_github_emacski_bazeltools//protobuf:go.bzl",
    "go_grpc_library",
    "go_proto_library",
)

package(default_visibility = ["//visibility:public"])

go_grpc_library(
    name = "tensorflow_serving",
    srcs = ["//proto/tensorflow_serving/apis:protos_grpc_all"],
    importpath = "github.com/tensorflow-serving-arm-client/go/tensorflow_serving",
    deps = [":tensorflow_serving_protobuf"],
)

go_proto_library(
    name = "tensorflow_serving_protobuf",
    importpath = "github.com/tensorflow-serving-arm-client/go/tensorflow_serving",
    proto = ["//proto/tensorflow_serving:protos_all"],
    deps = [
        ":tensorflow_core_proto",
        ":tensorflow_example_proto",
        ":tensorflow_framework_proto",
    ],
)

go_proto_library(
    name = "tensorflow_core_proto",
    importpath = "github.com/tensorflow-serving-arm-client/go/tensorflow/core",
    proto = ["//proto/tensorflow/core:protos_all"],
    deps = [":tensorflow_framework_proto"],
)

go_proto_library(
    name = "tensorflow_framework_proto",
    importpath = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    proto = ["//proto/tensorflow/core/framework:protos_all"],
)

go_proto_library(
    name = "tensorflow_example_proto",
    importpath = "github.com/tensorflow-serving-arm-client/go/tensorflow/core/example",
    proto = ["//proto/tensorflow/core/example:protos_all"],
    deps = [":tensorflow_framework_proto"],
)
