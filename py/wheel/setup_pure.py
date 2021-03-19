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
"""TensorFlow Serving Standalone Client Library (Experimental)

Experimental standalone client library extracted from the TensorFlow Serving
APIs removing the dependency on the full tensorflow python library. Platform
specific wheels include grpcio and protobuf packages with precompiled extensions.
"""
import sys

from setuptools import find_packages
from setuptools import setup
from bazel_build import bazel_info

PROJECT_NAME = "tensorflow-serving-arm-client"

VERSION = bazel_info["BUILD_EMBED_LABEL"]

DOCLINES = __doc__.split("\n")

INSTALL_REQUIRES = [
    "grpcio>=1.0<2",
    "protobuf>=3.6.0",
]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    packages=find_packages(exclude=["bazel_build.py"]),
    python_requires=">=3.4",
    install_requires=INSTALL_REQUIRES,

    author="Erik Maciejewski",
    author_email="mr.emacski@gmail.com",
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    license="Apache 2.0",
    keywords="tensorflow serving machine learning client api libraries",
    url='http://github.com/emacski/tensorflow-serving-client',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
