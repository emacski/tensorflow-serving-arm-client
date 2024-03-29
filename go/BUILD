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
    name = "grpc",
    srcs = ["//proto/tensorflow_serving/apis:protos_grpc_all"],
    importpath = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    deps = [":protos"],
)

go_proto_library(
    name = "protos",
    importpath = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving",
    proto = ["//proto/tensorflow_serving:protos_all"],
    deps = [
        ":tensorflow_core_protos",
        ":tensorflow_example_protos",
        ":tensorflow_framework_protos",
    ],
)

go_proto_library(
    name = "tensorflow_core_protos",
    importpath = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core",
    proto = ["//proto/tensorflow/core:protos_all"],
    deps = [":tensorflow_framework_protos"],
)

go_proto_library(
    name = "tensorflow_example_protos",
    importpath = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/example",
    proto = ["//proto/tensorflow/core/example:protos_all"],
    deps = [":tensorflow_framework_protos"],
)

go_proto_library(
    name = "tensorflow_framework_protos",
    importpath = "github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework",
    proto = ["//proto/tensorflow/core/framework:protos_all"],
)
