# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPynbody(PythonPackage):
    """Pynbody is an analysis framework for N-body and hydrodynamic
    astrophysical simulations supporting PKDGRAV/Gasoline,
    Gadget, Gadget4/Arepo, N-Chilada and RAMSES AMR outputs."""

    homepage = "https://pynbody.github.io/pynbody/"
    pypi = "pynbody/pynbody-1.2.3.tar.gz"

    version("1.2.3", sha256="7dba913c7be137a44e9c01dd7e109481ce001a3d928aa9fcb63f7c4cb498bccb")

    depends_on("python@3.5:", type=("build", "run"))

    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-cython@0.20:", type=("build", "run"))
    depends_on("py-h5py@2.10:", type=("build", "run"))
    depends_on("py-matplotlib@3:", type=("build", "run"))
    depends_on("py-numpy@1.14:", type=("build", "run"))
    depends_on("py-posix-ipc@0.8:", type=("build", "run"))
    depends_on("py-scipy@1:", type=("build", "run"))
