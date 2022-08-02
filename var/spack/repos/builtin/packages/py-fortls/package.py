# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFortls(PythonPackage):
    """fortls is an implementation of the Language Server Protocol (LSP) for Fortran using Python"""

    homepage = "https://gnikit.github.io/fortls/"
    pypi     = "fortls/fortls-2.11.0.tar.gz"

    version('2.11.0', sha256='11d267bc8f8c06ba4fa8b3cd0f0f3b6cacf0bd71f1f5b8746f7d01de70ca0774')

    depends_on('python@3.7:', type=('build', 'run'))

    depends_on('py-wheel', type='build')
    depends_on('py-setuptools@45:', type='build')
    depends_on('py-setuptools-scm@6.2: +toml', type='build')
    depends_on('py-setuptools-scm-git-archive', type='build')

    depends_on('py-json5', type=('build', 'run'))
    depends_on('py-packaging', type=('build', 'run'))
    depends_on('py-importlib-metadata', when='^python@:3.7', type=('build', 'run'))
    depends_on('py-typing-extensions', when='^python@:3.7', type=('build', 'run'))
