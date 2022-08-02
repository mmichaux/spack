# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMcfit(PythonPackage):
    """Multiplicatively Convolutional Fast Integral Transforms"""

    homepage = "https://github.com/eelregit/mcfit"
    pypi     = "mcfit/mcfit-0.0.17.tar.gz"

    version('0.0.17', sha256='2d4f09843589d5f6c50fd008cfb326c6e533f1c193929b5abb45520369fa9f76')

    depends_on('py-setuptools', type='build')

    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-mpmath', type=('build', 'run'))
