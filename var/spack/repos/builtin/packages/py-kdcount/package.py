# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKdcount(PythonPackage):
    """kdcount is a simple API for brute force pair counting,
    there is a C interface and a Python interface.
    It uses a KDTree to prune the K-D spatial data;
    for each pair within a given distance D,
    a callback function is called;
    the user-defined callback function does the actual counting."""

    homepage = "https://github.com/rainwoodman/kdcount"
    pypi     = "kdcount/kdcount-0.3.29.tar.gz"

    version('0.3.29', sha256='f93fd9b885f8b9811d16426d80db783442adb4dc1e887a105adf1d7d719e68fe')

    depends_on('py-setuptools', type='build')
    
    depends_on('py-cython', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))
