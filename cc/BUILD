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
    "@com_github_emacski_bazeltools//protobuf:cc.bzl",
    "cc_grpc_library",
    "cc_proto_library",
)

package(default_visibility = ["//visibility:public"])

cc_grpc_library(
    name = "grpc",
    srcs = ["//proto/tensorflow_serving/apis:protos_grpc_all"],
    deps = [":protos"],
)

cc_proto_library(
    name = "protos",
    deps = ["//proto:protos_all"],
)
