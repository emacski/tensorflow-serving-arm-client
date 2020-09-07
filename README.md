Tensorflow Serving ARM Client
=============================
![](https://github.com/emacski/tensorflow-serving-arm-client/workflows/Build/badge.svg)

**EXPERIMENTAL (anything can change)**

A project for cross building [tensorflow/serving](https://github.com/tensorflow/serving)
grpc api clients targeting popular arm architectures from an x86_64 host.
Additionally, this includes an experimental multi-arch standalone python3 client
(it doesn't depend on the core tensorflow python package).

## Python3 Client

### Wheels

A pure python3 wheel is maintained that depends on `grpcio` and `protobuf`
python packages.

Currently, platform specific wheels are maintained for CPython 3.7 on
`linux_amd64`, `linux_arm64` and `linux_arm`. These wheels are full
self-contained grpc client libs and include the `tensorflow_serving`,
`tensorflow`, `grpcio` and `protobuf`, python packages with corresponding
compiled extensions where applicable.

**Install with `pip`**
```sh
# on linux_amd64 python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.2.0/tensorflow_serving_arm_client-2.2.0-cp37-none-manylinux2014_x86_64.whl
# on linux_arm64 python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.2.0/tensorflow_serving_arm_client-2.2.0-cp37-none-manylinux2014_aarch64.whl
# on linux_arm python 3.7
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.2.0/tensorflow_serving_arm_client-2.2.0-cp37-none-manylinux2014_armv7l.whl
# pure python 3 (depends on grpcio and protobuf)
pip install https://github.com/emacski/tensorflow-serving-arm-client/releases/download/2.2.0/tensorflow_serving_arm_client-2.2.0-py3-none-any.whl
```
