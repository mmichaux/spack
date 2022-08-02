# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNbodykit(PythonPackage):
    """nbodykit is an open source project and Python package providing
    a set of algorithms useful in the analysis of cosmological datasets
    from N-body simulations and large-scale structure surveys."""

    homepage = "http://nbodykit.rtfd.io/"
    pypi     = "nbodykit/nbodykit-0.3.15.tar.gz"

    version('0.3.15', sha256='77443dd0dc8bba6a89fa12223af0e9ed05a6226080896d2f5931d7383ebde0c3')

    depends_on('python@3.5:', type=('build', 'run'))

    depends_on('py-setuptools', type='build')

    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-astropy', type=('build', 'run'))
    depends_on('py-pyerfa', type=('build', 'run'))
    depends_on('py-mpi4py', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-runtests', type=('build', 'run'))
    depends_on('py-pmesh', type=('build', 'run'))
    depends_on('py-kdcount', type=('build', 'run'))
    depends_on('py-mpsort', type=('build', 'run'))
    depends_on('py-bigfile', type=('build', 'run'))
    depends_on('py-pandas', type=('build', 'run'))
    depends_on('py-dask@0.14.2:', type=('build', 'run'))
    depends_on('py-cachey', type=('build', 'run'))
    depends_on('py-sympy', type=('build', 'run'))
    depends_on('py-numexpr', type=('build', 'run'))
    depends_on('py-corrfunc', type=('build', 'run'))
    depends_on('py-mcfit', type=('build', 'run'))
    depends_on('py-classylss@0.2:', type=('build', 'run'))

    depends_on('py-halotools@master', type=('build', 'run'))
    depends_on('py-h5py', type=('build', 'run'))
    depends_on('py-fitsio', type=('build', 'run'))

    conflicts('py-sympy@1.6.0:1.6.1')
