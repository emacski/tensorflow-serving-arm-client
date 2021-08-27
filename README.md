Tensorflow Serving ARM Client
=============================
![](https://github.com/emacski/tensorflow-serving-arm-client/workflows/Build/badge.svg)

**EXPERIMENTAL (anything can change)**

A project for cross building [tensorflow/serving](https://github.com/tensorflow/serving)
standalone grpc api clients targeting popular arm architectures from an x86_64 host.
Currently, client libraries can be cross-built for c++, python and go targeting
`linux_amd64`, `linux_arm64` and `linux_arm`.

## Contents
* [Cross-Building](#cross-building)
* [Project Artifacts](#project-artifacts)
* [Client Examples](#client-examples)
* [Generating Sources](#generating-sources)

## Cross-Building

Using the project's development docker image, all platform specific targets in this
project can be cross-built, from an x86_64 host, for the following platforms by
specifying the corresponding config group when building.

| Config Group | CLI Option |
|--------------|----------|
| `linux_amd64` | `--config=linux_amd64` |
| `linux_arm64` | `--config=linux_arm64` |
| `linux_arm` | `--config=linux_arm` |

Docker Devel Image
```sh
git clone git@github.com:emacski/tensorflow-serving-arm-client.git
cd tensorflow-serving-arm-client
# devel image includes all necessary deps to build and run project targets
docker run --rm -ti \
    -w /tensorflow-serving-arm-client \
    -v $PWD:/tensorflow-serving-arm-client \
    emacski/tensorflow-serving-arm-client:latest-devel /bin/bash
```

Examples
```sh
# build python client library for amd64
bazel build //py:grpc --config=linux_amd64
# build platform wheel for 32-bit arm
bazel run //py/wheel:build_platform --config=linux_arm
# build go client library for arm64
bazel build //go:grpc --config=linux_arm64
```

[Back to Top](#contents)

## Project Artifacts
### Python3 Client Library (Wheels)

Platform specific wheels are published for the current version of python 3
on debian 10 (CPython 3.7) targeting `linux_amd64`, `linux_arm64` and `linux_arm`.
These wheels are full self-contained grpc client libs and include the
`tensorflow_serving`, (protobuf only) `tensorflow`, `grpcio` and `protobuf` py
packages with corresponding extensions where applicable (no compiling or dev-tools
required on the install host).

Additionally, a pure python3 wheel is published that includes the `tensorflow_serving`,
(protobuf only) `tensorflow` packages and depends on external `grpcio` and
`protobuf` python packages.

**Install Wheels with `pip`**
```sh
# on linux_amd64 python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.6.0/tensorflow_serving_arm_client-2.6.0-cp37-none-manylinux2014_x86_64.whl
# on linux_arm64 python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.6.0/tensorflow_serving_arm_client-2.6.0-cp37-none-manylinux2014_aarch64.whl
# on linux_arm python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.6.0/tensorflow_serving_arm_client-2.6.0-cp37-none-manylinux2014_armv7l.whl
# pure python 3 (will require grpcio and protobuf pypi packages)
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.6.0/tensorflow_serving_arm_client-2.6.0-py3-none-any.whl
```

**Building Wheels From Source**
```sh
git clone git@github.com:emacski/tensorflow-serving-arm-client.git
cd tensorflow-serving-arm-client

# Build Environment
docker run --rm -ti \
    -w /tensorflow-serving-arm-client \
    -v $PWD:/tensorflow-serving-arm-client \
    emacski/tensorflow-serving-arm-client:latest-devel /bin/bash
```
By default, wheel artifacts will be output to the workspace root
```sh
# pure python
bazel run //py/wheel:build_pure
# with platform specific deps
bazel run //py/wheel:build_platform --config=linux_amd64
bazel run //py/wheel:build_platform --config=linux_arm64
bazel run //py/wheel:build_platform --config=linux_arm
```

[Back to Top](#contents)

## Client Examples

The client examples are designed to query the same model in the official tensorflow serving example
[TensorFlow Serving with Docker](https://www.tensorflow.org/tfx/serving/docker) using the predict API.

### Model Server Example
Reference instructions for setting up [TensorFlow Serving with Docker](https://www.tensorflow.org/tfx/serving/docker),
substituting the `docker run` command for the one below:
```sh
# this version includes the addition of mapping the grpc port (8500) to the host
docker run -t --rm -p 8501:8501 -p 8500:8500 \
    -v "$TESTDATA/saved_model_half_plus_two_cpu:/models/half_plus_two" \
    -e MODEL_NAME=half_plus_two \
    tensorflow/serving &
```

### gRPC Client Examples
```sh
git clone git@github.com:emacski/tensorflow-serving-arm-client.git
cd tensorflow-serving-arm-client
# devel env image includes all deps to build and run examples
docker run --rm -ti \
    -w /tensorflow-serving-arm-client \
    -v $PWD:/tensorflow-serving-arm-client \
    emacski/tensorflow-serving-arm-client:latest-devel /bin/bash

# client examples accept exactly one command-line argument in the form of:
# <model_server_host>:<model_server_port>

# python
bazel run //py/example:half_plus_two -- host.docker.internal:8500
# or
bazel build //py/example:half_plus_two
./bazel-bin/py/example/half_plus_two host.docker.internal:8500

# cc
bazel run //cc/example:half_plus_two -- host.docker.internal:8500
# or
bazel build //cc/example:half_plus_two
./bazel-bin/cc/example/half_plus_two host.docker.internal:8500

# go
bazel run //go/example:half_plus_two -- host.docker.internal:8500
# or
bazel build //go/example:half_plus_two
./bazel-bin/go/example/half_plus_two host.docker.internal:8500
```

[Back to Top](#contents)

## Generating Sources

Docker Devel Image
```sh
git clone git@github.com:emacski/tensorflow-serving-arm-client.git
cd tensorflow-serving-arm-client
# devel image includes all necessary deps to build and run project targets
docker run --rm -ti \
    -w /tensorflow-serving-arm-client \
    -v $PWD:/tensorflow-serving-arm-client \
    emacski/tensorflow-serving-arm-client:latest-devel /bin/bash
```

Examples
```sh
# py
bazel build //py:grpc_codegen
bazel build //py:protobuf_codegen
# cc
bazel build //cc:grpc_codegen
bazel build //cc:protobuf_codegen
# go
bazel build //go:grpc_codegen
bazel build //go:protobuf_codegen
bazel build //go:tensorflow_core_protobuf_codegen
bazel build //go:tensorflow_example_protobuf_codegen
bazel build //go:tensorflow_framework_protobuf_codegen
```

[Back to Top](#contents)
