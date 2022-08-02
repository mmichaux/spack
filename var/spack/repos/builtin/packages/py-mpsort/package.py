# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMpsort(PythonPackage):
    """A Massively Parallel Sorting Library.
    The library implements a histogram sort."""

    homepage = "https://github.com/rainwoodman/MP-sort"
    pypi = "mpsort/mpsort-0.1.17.tar.gz"

    version("0.1.17", sha256="28793fc9fef8fc3fbd92f81d3b056128d6d46d7171f3c6daa067aee8c4448d3d")

    depends_on("py-setuptools", type="build")

    depends_on("py-mpi4py", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))

    depends_on("mpi", type=("build", "run"))
