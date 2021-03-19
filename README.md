Tensorflow Serving ARM Client
=============================
![](https://github.com/emacski/tensorflow-serving-arm-client/workflows/Build/badge.svg)

**EXPERIMENTAL (anything can change)**

A project for cross building [tensorflow/serving](https://github.com/tensorflow/serving)
standalone grpc api clients targeting popular arm architectures from an x86_64 host.
Currently, client libraries can be cross-built for c++, python and go targeting
`linux_amd64`, `linux_arm64` and `linux_arm`.

## Project Artifacts
### Python3 Client Library (Wheels)

Currently, platform specific wheels are published for CPython 3.7 on
`linux_amd64`, `linux_arm64` and `linux_arm`. These wheels are full self-contained
grpc client libs and include the `tensorflow_serving`, (protobuf only) `tensorflow`,
`grpcio` and `protobuf` py packages with corresponding extensions where applicable
(no compiling or dev-tools required on the install host).

Additionally, a pure python3 wheel is published that includes the `tensorflow_serving`,
(protobuf only) `tensorflow` packages and depends on external `grpcio` and
`protobuf` python packages.

**Install Wheels with `pip`**
```sh
# on linux_amd64 python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.3.0/tensorflow_serving_arm_client-2.3.0-cp37-none-manylinux2014_x86_64.whl
# on linux_arm64 python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.3.0/tensorflow_serving_arm_client-2.3.0-cp37-none-manylinux2014_aarch64.whl
# on linux_arm python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.3.0/tensorflow_serving_arm_client-2.3.0-cp37-none-manylinux2014_armv7l.whl
# pure python 3 (will also install grpcio and protobuf pypi packages)
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.3.0/tensorflow_serving_arm_client-2.3.0-py3-none-any.whl
```

**Building Wheels From Source**
```sh
git clone git@github.com:emacski/tensorflow-serving-arm-client.git
cd tensorflow-serving-arm-client

# Build Environment
docker run --rm -ti \
    -w /tensorflow-serving-arm-client \
    -v $PWD:/tensorflow-serving-arm-client \
    emacski/tensorflow-serving:latest-devel /bin/bash
```
By default, wheel artifacts will be output to the workspace root
```sh
# pure python
bazel run //py/wheel:build_pure
# with extension
bazel run //py/wheel:build_platform --config=linux_amd64
bazel run //py/wheel:build_platform --config=linux_arm64
bazel run //py/wheel:build_platform --config=linux_arm
```
