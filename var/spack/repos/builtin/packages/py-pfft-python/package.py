# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPfftPython(PythonPackage):
    """Python binding of PFFT."""

    homepage = "https://github.com/rainwoodman/pfft-python"
    pypi     = "pfft-python/pfft-python-0.1.21.tar.gz"

    version('0.1.21', sha256='2c5bf26170dffbe06c897f1edbbcf35961baf48fb3a383eedcc3103648e4d334')

    depends_on('py-setuptools', type='build')

    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-mpi4py', type=('build', 'run'))
    
    depends_on('mpi', type='build')
