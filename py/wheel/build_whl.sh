#!/bin/bash
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
set -e

PLAT="$1"
OUT_DIR="$2"
TMP_DIR="$(mktemp -d)"
RUNFILES=${BASH_SOURCE[0]}.runfiles
SOURCEFILES=${RUNFILES}/com_github_emacski_tensorflowservingarmclient

cp py/wheel/setup_*.py ${TMP_DIR}/setup.py
cp py/wheel/bazel_build.py ${TMP_DIR}/bazel_build.py
cp py/wheel/stable-status.txt ${TMP_DIR}/stable-status.txt
cp -r ${SOURCEFILES}/py/tensorflow_serving ${TMP_DIR}
cp -r ${SOURCEFILES}/py/tensorflow ${TMP_DIR}

if [ $PLAT = "pure" ]; then
    pushd ${TMP_DIR}
    python3 setup.py bdist_wheel >/dev/null
    popd
else
    # include grpcio and protobuf
    cp -r ${SOURCEFILES}/external/com_google_protobuf/python/google ${TMP_DIR}
    cp -r ${SOURCEFILES}/external/com_github_grpc_grpc/src/python/grpcio/grpc ${TMP_DIR}
    pushd ${TMP_DIR}
    python3 setup.py bdist_wheel --python-tag=cp37 --plat-name=${PLAT} >/dev/null
    popd
fi

cp ${TMP_DIR}/dist/* ${OUT_DIR}
