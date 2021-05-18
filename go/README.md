Go Client
=========

## Bazel Workspace

`WORKSPACE` Dependencies
```python
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
# OPTIONAL: only required if using the cross-build cc toolchain
register_clang_cross_toolchains(clang_version = "11")

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
    importpath = "google.golang.org/grpc",
    commit = "f74f0337644653eba7923908a4d7f79a4f3a267b",  # 1.36.0
)

# required by google.golang.org/grpc
go_repository(
    name = "org_golang_x_net",
    importpath = "golang.org/x/net",
    sum = "h1:oWX7TPOiFAMXLq8o0ikBYfCJVlRHBcsciT5bXOrH628=",
    version = "v0.0.0-20190311183353-d8887717615a",
)

# required by golang.org/x/net
go_repository(
    name = "org_golang_x_text",
    importpath = "golang.org/x/text",
    sum = "h1:g61tztE5qeGQ89tm6NTjjM9VPIm088od1l6aSorWRWg=",
    version = "v0.3.0",
)

http_archive(
    name = "com_github_emacski_tensorflowservingarmclient",
    sha256 = "[BAZEL_HTTP_ARCHIVE_SHA]",
    strip_prefix = "tensorflow-serving-arm-client-[GIT_COMMIT_SHA]",
    urls = ["https://github.com/emacski/tensorflow-serving-arm-client/archive/[GIT_COMMIT_SHA].tar.gz"],
)

http_archive(
    name = "com_github_grpc_grpc",
    sha256 = "bb6de0544adddd54662ba1c314eff974e84c955c39204a4a2b733ccd990354b7",
    strip_prefix = "grpc-1.36.3",
    urls = ["https://github.com/grpc/grpc/archive/v1.36.3.tar.gz"],
)

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")

grpc_deps()

load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")

grpc_extra_deps()
```

Optional Bazel Build Options
(only required if cross-building)
```sh
# enable proper toolchain resolution
--incompatible_enable_cc_toolchain_resolution

# amd64 (x86_64)
--platforms=@com_github_emacski_bazeltools//platform:linux_amd64
# or
--platforms=@io_bazel_rules_go//go/toolchain:linux_amd64

# arm64 (aarch64)
--platforms=@com_github_emacski_bazeltools//platform:linux_arm64
# or
--platforms=@io_bazel_rules_go//go/toolchain:linux_arm64

# arm (armhf)
--platforms=@com_github_emacski_bazeltools//platform:linux_arm
# or
--platforms=@io_bazel_rules_go//go/toolchain:linux_arm
```
