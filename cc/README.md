C++ Client
==========

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

Bazel Build Options
```sh
# grpc
--define=grpc_no_ares=true
```

Optional Bazel Build Options
(only required if using the cross-build cc toolchain)
```sh
# enable proper toolchain resolution
--incompatible_enable_cc_toolchain_resolution

# amd64 (x86_64)
--platforms=@com_github_emacski_bazeltools//platform:linux_amd64

# arm64 (aarch64)
--platforms=@com_github_emacski_bazeltools//platform:linux_arm64
# some deps may still require legacy toolchain resolution
--crosstool_top=@com_github_emacski_bazeltools//toolchain/cpp/clang:clang11_crosstool
--cpu=aarch64

# arm (armhf)
--platforms=@com_github_emacski_bazeltools//platform:linux_arm
# some deps still require legacy toolchain resolution
--crosstool_top=@com_github_emacski_bazeltools//toolchain/cpp/clang:clang11_crosstool
--cpu=armhf
```
