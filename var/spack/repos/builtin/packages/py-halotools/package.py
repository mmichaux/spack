# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHalotools(PythonPackage):
    """Halotools is a specialized python package for
    building and testing models of the galaxy-halo connection,
    and analyzing catalogs of dark matter halos."""

    homepage = "http://halotools.rtfd.org/"
    pypi     = "halotools/halotools-0.7.tar.gz"
    git      = "https://github.com/astropy/halotools.git"

    version('master', branch='master')
    version('0.7', sha256='a56e0bf32ac02a3bceacdc6669a6e1b7455f6365392ae35d2674558e2e2ab863')

    depends_on('python@3.7:', type=('build', 'run'))

    depends_on('py-setuptools', type='build')

    depends_on('py-numpy@1.9:', type=('build', 'run'))
    depends_on('py-scipy@0.15:', type=('build', 'run'))
    depends_on('py-cython@0.23:', type=('build', 'run'))
    depends_on('py-astropy@4.0:', type=('build', 'run'))
    depends_on('py-beautifulsoup4', type=('build', 'run'))
    depends_on('py-requests', type=('build', 'run'))
    depends_on('py-h5py@2.5:', type=('build', 'run'))
