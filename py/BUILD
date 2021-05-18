# Copyright 2020 Erik Maciejewski
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
    "@com_github_emacski_bazeltools//protobuf:py.bzl",
    "py_grpc_library",
    "py_proto_library",
)

package(default_visibility = ["//visibility:public"])

py_grpc_library(
    name = "grpc",
    srcs = ["//proto/tensorflow_serving/apis:protos_grpc_all"],
    srcs_version = "PY3",
    deps = [":protobuf"],
)

py_proto_library(
    name = "protobuf",
    srcs_version = "PY3",
    deps = ["//proto:protos_all"],
)
