# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAsdfStandard(PythonPackage):
    """Standards document describing ASDF,
    Advanced Scientific Data Format."""

    homepage = "https://github.com/asdf-format/asdf-standard"
    pypi     = "asdf_standard/asdf_standard-1.0.2.tar.gz"

    version('1.0.2', sha256='21cfc05dd821559b67dfbc54d03b2bcc0ad8b6cb5cc9d14d7591f73ab3451700')

    depends_on('python@3.8:', type=('build', 'run'))
    depends_on('py-setuptools@42:', type='build')
    depends_on('py-setuptools-scm+toml@3.4:', type='build')
    
    depends_on('py-importlib-resources@3:', when='^python@:3.8', type=('build', 'run'))
