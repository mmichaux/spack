# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyPygad(PythonPackage):
    """PyGAD is an open-source easy-to-use Python 3 library for building
    the genetic algorithm and optimizing machine learning algorithms.
    It supports Keras and PyTorch."""

    homepage = "https://pygad.readthedocs.io/"
    pypi = "pygad/pygad-2.16.3.tar.gz"

    version("2.16.3", sha256="db8322bcdfc41f3553f77f1ac099d07f7a89f31bf87c0f23bd5fb4a5b7c1bbf4")

    variant("torch", default=False, description="Enable the pygad.torchga module")
    variant("keras", default=False, description="Enable the pygad.kerasga module")

    depends_on("python@3.7.3:", type=("build", "run"))

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.16.4:", type="run")
    depends_on("py-matplotlib@3.1.0:", type="run")
    depends_on("py-torch", type="run", when="+torch")
    depends_on("py-keras", type="run", when="+keras")
    depends_on("py-tensorflow", type="run", when="+keras")
