# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPmesh(PythonPackage):
    """pmesh includes a few software components for building
    particle mesh simulations with Python."""

    homepage = "http://rainwoodman.github.io/pmesh"
    pypi     = "pmesh/pmesh-0.1.56.tar.gz"

    version('0.1.56', sha256='8f7a464607c03fec3b5d3c6fad0aa6f82062095fdea2e61443b82366f6531c1a')

    depends_on('py-setuptools', type='build')
    
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-mpi4py', type=('build', 'run'))
    depends_on('py-mpsort', type=('build', 'run'))
    depends_on('py-pfft-python', type=('build', 'run'))
