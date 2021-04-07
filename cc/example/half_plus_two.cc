// Copyright 2021 Erik Maciejewski
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include <iostream>
#include <string>
#include <vector>

#include "grpcpp/grpcpp.h"
#include "tensorflow/core/framework/types.pb.h"
#include "tensorflow/core/framework/tensor.pb.h"
#include "tensorflow_serving/apis/prediction_service.grpc.pb.h"

using namespace tensorflow::serving;

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "error: only 1 argument accepted" << std::endl;
        return 1;
    }

    const std::string server_host_port = argv[1];

    std::unique_ptr<PredictionService::Stub> stub;
    stub = PredictionService::NewStub(grpc::CreateChannel(
      server_host_port, grpc::InsecureChannelCredentials()));

    // same example inputs from https://www.tensorflow.org/tfx/serving/docker
    std::vector<float> inputs = {1.0, 2.0, 5.0};

    std::unique_ptr<tensorflow::TensorProto> input_tensor;
    input_tensor = std::make_unique<tensorflow::TensorProto>();

    input_tensor->mutable_tensor_shape()->add_dim()->set_size(inputs.size());
    input_tensor->set_dtype(tensorflow::DataType::DT_FLOAT);

    for (auto i = inputs.begin(); i != inputs.end(); i++) {
        input_tensor->add_float_val(*i);
    }

    std::unique_ptr<PredictRequest> req = std::make_unique<PredictRequest>();

    req->mutable_model_spec()->set_name("half_plus_two");
    req->mutable_model_spec()->set_signature_name("serving_default");
    (*req->mutable_inputs())["x"] = *input_tensor;

    PredictResponse res;
    grpc::ClientContext ctx;

    grpc::Status status = stub->Predict(&ctx, *req, &res);

    if (status.ok()) {
        std::cout << res.DebugString() << std::endl;
    } else {
        std::cout << status.error_code() << ": " << status.error_message() << std::endl;
    }

    return 0;
}
