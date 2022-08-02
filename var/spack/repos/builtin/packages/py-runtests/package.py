# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRuntests(PythonPackage):
    """A simple tools for incrementally building packages,
    then testing against installed version."""

    homepage = "https://github.com/bccp/runtests"
    pypi     = "runtests/runtests-0.0.28.tar.gz"

    version("0.0.28", sha256="add28a6cbbf4cdcfcabb0a8897f154835b7357c0c502e4a389829d30c2dabee4")

    depends_on("py-setuptools", type="build")
