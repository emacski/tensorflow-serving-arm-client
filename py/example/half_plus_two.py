# Copyright 2021 Erik Maciejewski
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

import sys
import grpc
from google.protobuf import text_format
from tensorflow.core.framework import tensor_shape_pb2, tensor_pb2, types_pb2
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2_grpc


def main():
    if len(sys.argv) != 2:
        print("error: only 1 argument accepted")
        sys.exit(1)

    ch = grpc.insecure_channel(sys.argv[1])
    stub = prediction_service_pb2_grpc.PredictionServiceStub(ch)

    # same example inputs from https://www.tensorflow.org/tfx/serving/docker
    inputs = [1.0, 2.0, 5.0]

    input_tensor = tensor_pb2.TensorProto(
        dtype=types_pb2.DT_FLOAT,
        tensor_shape=tensor_shape_pb2.TensorShapeProto(
            dim = [tensor_shape_pb2.TensorShapeProto.Dim(
                size=len(inputs),
            )]
        ),
        float_val=inputs,
    )

    req = predict_pb2.PredictRequest()
    req.model_spec.name = "half_plus_two"
    req.model_spec.signature_name = "serving_default"
    req.inputs["x"].CopyFrom(input_tensor)

    res = stub.Predict(req)

    print(text_format.MessageToString(res))
    sys.exit(0)


if __name__ == "__main__":
    main()
