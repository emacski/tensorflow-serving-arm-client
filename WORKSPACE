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

workspace(name = "com_github_emacski_tensorflowservingarmclient")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "com_github_emacski_bazeltools",
    sha256 = "6f3c9b725b2222ea16e6eabfb8f2a9ec267567f0c05c9c4f36cbd641cd02ff39",
    strip_prefix = "bazel-tools-74b14ec277cbc79c328142c561d1edd69e05d3b4",
    urls = ["https://github.com/emacski/bazel-tools/archive/74b14ec277cbc79c328142c561d1edd69e05d3b4.tar.gz"],
)

register_toolchains("@com_github_emacski_bazeltools//toolchain/cpp/clang:all")

http_archive(
    name = "rules_python",
    sha256 = "afe33d4a8091452cb785108f237c7f3dcef56345952aad124954a96d89c4aab6",
    strip_prefix = "rules_python-0d23d579fd93b72fe94b27b0077fbf3dc8680724",
    urls = ["https://github.com/bazelbuild/rules_python/archive/0d23d579fd93b72fe94b27b0077fbf3dc8680724.tar.gz"],
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()

load("@rules_python//python:pip.bzl", "pip_repositories")

pip_repositories()

# tensorflow 2.2.0
# https://github.com/tensorflow/tensorflow
http_archive(
    name = "org_tensorflow",
    sha256 = "b3d7829fac84e3a26264d84057367730b6b85b495a0fce15929568f4b55dc144",
    strip_prefix = "tensorflow-2b96f3662bd776e277f86997659e61046b56c315",
    urls = [
        "https://github.com/tensorflow/tensorflow/archive/2b96f3662bd776e277f86997659e61046b56c315.tar.gz",
    ],
)

# see tensorflow/serving/WORKSPACE and tensorflow/tensorflow/WORKSPACE
http_archive(
    name = "io_bazel_rules_closure",
    sha256 = "5b00383d08dd71f28503736db0500b6fb4dda47489ff5fc6bed42557c07c6ba9",
    strip_prefix = "rules_closure-308b05b2419edb5c8ee0471b67a40403df940149",
    urls = [
        "https://github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz",
    ],
)

# see tensorflow/serving/WORKSPACE and tensorflow/tensorflow/WORKSPACE
http_archive(
    name = "bazel_skylib",
    sha256 = "1dde365491125a3db70731e25658dfdd3bc5dbdfd11b840b3e987ecf043c7ca0",
    urls = [
        "https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/bazel-skylib/releases/download/0.9.0/bazel_skylib-0.9.0.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/0.9.0/bazel_skylib-0.9.0.tar.gz",
    ],
)

# see tensorflow/serving/WORKSPACE
http_archive(
    name = "rules_pkg",
    sha256 = "f8bf72e76a15d045f786ef0eba92e073a50bbdbd807d237a43a759d36b1b1e2c",
    strip_prefix = "rules_pkg-0.2.5/pkg",
    urls = ["https://github.com/bazelbuild/rules_pkg/archive/0.2.5.tar.gz"],
)

# https://github.com/tensorflow/serving
http_archive(
    name = "tf_serving",
    sha256 = "946c1a58d677686e6b986634b51f4bc19486230c7fc2ab669c8492b0662ad4cc",
    strip_prefix = "serving-d22fc192c7ad7b48d9a81346224aff637b8988f1",
    urls = [
        "https://github.com/tensorflow/serving/archive/d22fc192c7ad7b48d9a81346224aff637b8988f1.tar.gz",
    ],
)

load("@tf_serving//tensorflow_serving:workspace.bzl", "tf_serving_workspace")

tf_serving_workspace()

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@upb//bazel:repository_defs.bzl", "bazel_version_repository")

bazel_version_repository(name = "bazel_version")
