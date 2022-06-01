# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyerfa(PythonPackage):
    """PyERFA is the Python wrapper for the ERFA library
    (Essential Routines for Fundamental Astronomy),
    a C library containing key algorithms for astronomy,
    which is based on the SOFA library published by the
    International Astronomical Union (IAU).
    All C routines are wrapped as Numpy universal functions,
    so that they can be called with scalar or array inputs."""

    homepage = "https://pyerfa.readthedocs.io/"
    pypi     = "pyerfa/pyerfa-2.0.0.1.tar.gz"

    version('2.0.0.1', sha256='2fd4637ffe2c1e6ede7482c13f583ba7c73119d78bef90175448ce506a0ede30')

    depends_on('python@3.7:', type=('build', 'run'))

    depends_on('py-setuptools@42:', type='build')
    depends_on('py-setuptools-scm+toml@3.4:', type='build')
    depends_on('py-packaging', type='build')
    depends_on('py-jinja2@2.10.3:', type='build')
    depends_on('py-numpy@1.17:', type=('build', 'run'))

    depends_on('erfa@2.0.0', when='@2.0.0')

    def global_options(self, spec, prefix):
        env['PYERFA_USE_SYSTEM_LIBERFA'] = '1'
        return []
