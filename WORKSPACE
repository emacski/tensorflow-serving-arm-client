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
    sha256 = "ac040d00f7f00c9947d61c7b8970a877d907c92e088966c24a0eaeeba5551b19",
    strip_prefix = "bazel-tools-250e4a98908fa0c6631ebccdeae930a60fd4c0d5",
    urls = ["https://github.com/emacski/bazel-tools/archive/250e4a98908fa0c6631ebccdeae930a60fd4c0d5.tar.gz"],
)

register_toolchains("@com_github_emacski_bazeltools//toolchain/cpp/clang:all")

# python client deps

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

# go client deps

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "7904dbecbaffd068651916dce77ff3437679f9d20e1a7956bff43826e7645fcc",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.25.1/rules_go-v0.25.1.tar.gz",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.25.1/rules_go-v0.25.1.tar.gz",
    ],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "222e49f034ca7a1d1231422cdb67066b885819885c356673cb1f72f748a3c9d4",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.22.3/bazel-gazelle-v0.22.3.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.22.3/bazel-gazelle-v0.22.3.tar.gz",
    ],
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.16")

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies", "go_repository")

gazelle_dependencies()

go_repository(
    name = "org_golang_google_grpc",
    commit = "f74f0337644653eba7923908a4d7f79a4f3a267b",  # 1.36.0
    importpath = "google.golang.org/grpc",
)

go_repository(
    name = "org_golang_x_net",
    importpath = "golang.org/x/net",
    sum = "h1:oWX7TPOiFAMXLq8o0ikBYfCJVlRHBcsciT5bXOrH628=",
    version = "v0.0.0-20190311183353-d8887717615a",
)

go_repository(
    name = "org_golang_x_text",
    importpath = "golang.org/x/text",
    sum = "h1:g61tztE5qeGQ89tm6NTjjM9VPIm088od1l6aSorWRWg=",
    version = "v0.3.0",
)

# protobuf / grpc deps

http_archive(
    name = "com_github_grpc_grpc",
    patches = [
        "@com_github_emacski_tensorflowservingarmclient//third_party/grpc:cython_library.patch",
    ],
    sha256 = "bb6de0544adddd54662ba1c314eff974e84c955c39204a4a2b733ccd990354b7",
    strip_prefix = "grpc-1.36.3",
    urls = ["https://github.com/grpc/grpc/archive/v1.36.3.tar.gz"],
)

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")

grpc_extra_deps()
