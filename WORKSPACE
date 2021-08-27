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
    sha256 = "dba9e8f0613401ed3c052d6fe79b3517197a7747046659845309fb17e9b3038d",
    strip_prefix = "bazel-tools-17a0d8b9ae66bc542853a72365ef1aeb85086827",
    urls = ["https://github.com/emacski/bazel-tools/archive/17a0d8b9ae66bc542853a72365ef1aeb85086827.tar.gz"],
)

load(
    "@com_github_emacski_bazeltools//toolchain/cpp/clang:defs.bzl",
    "register_clang_cross_toolchains",
)

register_clang_cross_toolchains(clang_version = "11")

# python client deps

http_archive(
    name = "rules_python",
    sha256 = "4feecd37ec6e9941a455a19e7392bed65003eab0aa6ea347ca431bce2640e530",
    strip_prefix = "rules_python-0.3.0",
    urls = ["https://github.com/bazelbuild/rules_python/archive/0.3.0.tar.gz"],
)

# go client deps

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "8e968b5fcea1d2d64071872b12737bbb5514524ee5f0a4f54f5920266c261acb",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.28.0/rules_go-v0.28.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.28.0/rules_go-v0.28.0.zip",
    ],
)

http_archive(
    name = "bazel_gazelle",
    sha256 = "62ca106be173579c0a167deb23358fdfe71ffa1e4cfdddf5582af26520f1c66f",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-gazelle/releases/download/v0.23.0/bazel-gazelle-v0.23.0.tar.gz",
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.23.0/bazel-gazelle-v0.23.0.tar.gz",
    ],
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.17")

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies", "go_repository")

gazelle_dependencies()

go_repository(
    name = "org_golang_google_grpc",
    commit = "41e044e1c82fcf6a5801d6cbd7ecf952505eecb1",  # 1.40.0
    importpath = "google.golang.org/grpc",
)

go_repository(
    name = "org_golang_x_net",
    importpath = "golang.org/x/net",
    sum = "h1:LO7XpTYMwTqxjLcGWPijK3vRXg1aWdlNOVOHRq45d7c=",
    version = "v0.0.0-20210813160813-60bc85c4be6d",
)

go_repository(
    name = "org_golang_x_text",
    importpath = "golang.org/x/text",
    sum = "h1:olpwvP2KacW1ZWvsR7uQhoyTYvKAupfQrRGBFM352Gk=",
    version = "v0.3.7",
)

# protobuf / grpc deps

http_archive(
    name = "com_google_protobuf",
    sha256 = "c6003e1d2e7fefa78a3039f19f383b4f3a61e81be8c19356f85b6461998ad3db",
    strip_prefix = "protobuf-3.17.3",
    urls = [
        "https://github.com/protocolbuffers/protobuf/archive/v3.17.3.tar.gz",
    ],
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

http_archive(
    name = "com_github_grpc_grpc",
    sha256 = "024118069912358e60722a2b7e507e9c3b51eeaeee06e2dd9d95d9c16f6639ec",
    strip_prefix = "grpc-1.39.1",
    urls = [
        "https://github.com/grpc/grpc/archive/v1.39.1.tar.gz"
    ],
)

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")

grpc_extra_deps()
