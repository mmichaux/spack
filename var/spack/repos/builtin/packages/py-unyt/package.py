# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyUnyt(PythonPackage):
    """A package for handling numpy arrays with units."""

    homepage = "https://unyt.readthedocs.io/"
    pypi = "unyt/unyt-2.8.0.tar.gz"

    version("2.8.0", sha256="6a17f849af0ec376fccb111c26b767022189d157d416f0fe5078f31b6b01a22e")

    depends_on("python@3.8:", type=("build", "run"))

    depends_on("py-numpy@1.17.5:", type=("build", "run"))
    depends_on("py-sympy@1.5:", type=("build", "run"))
