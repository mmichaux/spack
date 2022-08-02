# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyClassylss(PythonPackage):
    """A lightweight Python binding of the CMB Boltzmann code CLASS,
    with an emphasis on the routines that are important for
    large-scale structure calculations. The main modules
    of the CLASS code are exposed to the user via a Cython wrapper."""

    homepage = "https://github.com/nickhand/classylss"
    pypi     = "classylss/classylss-0.2.9.tar.gz"

    version('0.2.9', sha256='1a8521d2bf9da3d2572245e801e243fcf76f7518b59cbe525a31aa80a884dd86')

    depends_on('py-setuptools', type='build')

    depends_on('py-numpy', type=('build', 'run'))
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-six', type=('build', 'run'))
    depends_on('py-runtests', type=('build', 'run'))
    depends_on('py-astropy', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
