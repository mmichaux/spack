# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAsdfTransformSchemas(PythonPackage):
    """This package provides ASDF schemas for validating transform tags."""

    homepage = "https://github.com/asdf-format/asdf-transform-schemas"
    pypi     = "asdf_transform_schemas/asdf_transform_schemas-0.2.2.tar.gz"

    version('0.2.2', sha256='f71a9309ed3ebd09b1937ae857c94cec92887870440eb3e9868bbbed72656b15')

    depends_on('python@3.6:', type=('build', 'run'))
    depends_on('py-setuptools@42:', type='build')
    depends_on('py-setuptools-scm+toml@3.4:', type='build')

    depends_on('py-importlib-resources@3:', when='^python@:3.8', type=('build', 'run'))
    depends_on('py-asdf-standard@1.0.1:', type=('build', 'run'))