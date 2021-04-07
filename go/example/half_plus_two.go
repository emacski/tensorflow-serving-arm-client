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

package main

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/emacski/tensorflow-serving-arm-client/go/tensorflow/core/framework"
	"github.com/emacski/tensorflow-serving-arm-client/go/tensorflow_serving"
	"google.golang.org/grpc"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("error: only 1 argument accepted");
		os.Exit(1)
	}

	conn, err := grpc.Dial(os.Args[1], grpc.WithInsecure())
	if err != nil {
		fmt.Printf("fail to dial: %v\n", err)
		os.Exit(1)
	}
	defer conn.Close()

	client := tensorflow_serving.NewPredictionServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	// same example inputs from https://www.tensorflow.org/tfx/serving/docker
	inputs := []float32{1.0, 2.0, 5.0}

	input_tensor := &framework.TensorProto{
		Dtype: framework.DataType_DT_FLOAT,
		TensorShape: &framework.TensorShapeProto{
			Dim: []*framework.TensorShapeProto_Dim{
				&framework.TensorShapeProto_Dim{Size: int64(len(inputs))},
			},
		},
		FloatVal: inputs,
	}

	req := &tensorflow_serving.PredictRequest{
		ModelSpec: &tensorflow_serving.ModelSpec{Name: "half_plus_two"},
		Inputs:    map[string]*framework.TensorProto {"x": input_tensor},
	}

	res, err := client.Predict(ctx, req)
	if err != nil {
		fmt.Printf("%v\n", err)
		os.Exit(1)
	}

	fmt.Printf("%s", res.String())
	os.Exit(0)
}
