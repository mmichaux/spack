# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyCmakelang(PythonPackage):
    """The cmake-format project provides Quality Assurance (QA) tools for cmake."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://cmake-format.readthedocs.io/"
    url = "https://github.com/cheshirekow/cmake_format/archive/refs/tags/v0.6.13.tar.gz"

    version('0.6.13', sha256='b67dd150380d9223036a12f82126a7a9b18e77db4a8d7240f993ee090884e4bf')

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-pip@X.Y:', type='build')
    # depends_on('py-wheel@X.Y:', type='build')

    depends_on('py-setuptools', type='build')
    depends_on('py-pyyaml@5.3:', type=('build', 'run'))
    depends_on('py-jinja2@2.10.3:', type=('build', 'run'))
    depends_on('py-six@1.13.0:', type=('build', 'run'))

    patch('0001-Fixed-setup.py.patch')

    # depends_on('py-astroid', type=('build', 'run'))
    # depends_on('py-autopep8', type=('build', 'run'))
    # depends_on('py-flake8', type=('build', 'run'))
    # depends_on('py-jinja2', type=('build', 'run'))
    # depends_on('py-keyring', type=('build', 'run'))
    # depends_on('py-packaging', type=('build', 'run'))
    # depends_on('py-pycodestyle', type=('build', 'run'))
    # depends_on('py-pylint', type=('build', 'run'))
    # depends_on('py-pyyaml', type=('build', 'run'))
    # depends_on('py-pgpy', type=('build', 'run'))
    # depends_on('py-pygithub', type=('build', 'run'))
    # depends_on('py-magic', type=('build', 'run'))
    # depends_on('py-', type=('build', 'run'))
    # depends_on('py-twine', type=('build', 'run'))
