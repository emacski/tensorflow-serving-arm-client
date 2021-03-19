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

load("@rules_python//python:defs.bzl", "py_binary")

package(default_visibility = ["//visibility:public"])

genrule(
    name = "stable_status",
    outs = ["stable-status.txt"],
    cmd = "cp bazel-out/stable-status.txt $@",
    stamp = 1,
)

[py_binary(
    name = "setup_" + whl_type,
    srcs = [
        "setup_" + whl_type + ".py",
        "bazel_build.py",
    ],
    data = [":stable-status.txt"],
    deps = ["//py:tensorflow_serving"],
) for whl_type in ("pure", "platform")]

sh_binary(
    name = "build_pure",
    srcs = ["build_whl.sh"],
    args = [
        "pure",
        "/tensorflow-serving-arm-client",
    ],
    data = [":setup_pure"],
)

[config_setting(
    name = "is_linux_" + bazel_cpu,
    constraint_values = [
        "@platforms//os:linux",
        "@platforms//cpu:" + bazel_cpu,
    ],
) for bazel_cpu in ("arm", "aarch64", "x86_64")]

sh_binary(
    name = "build_platform",
    srcs = ["build_whl.sh"],
    args = select({
        ":is_linux_arm": ["manylinux2014_armv7l"],
        ":is_linux_aarch64": ["manylinux2014_aarch64"],
        ":is_linux_x86_64": ["manylinux2014_x86_64"],
    }) + ["/tensorflow-serving-arm-client"],
    data = [":setup_platform"],
)
