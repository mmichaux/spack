# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFitsio(PythonPackage):
    """This is a python extension written in C and python.
    Data are read into numerical python arrays."""

    homepage = "https://github.com/esheldon/fitsio"
    pypi = "fitsio/fitsio-1.1.7.tar.gz"

    version("1.1.7", sha256="be870a568a21081789d390eb903777c4c1090d7cf246bfb1957526ed658c1a61")

    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.11:", type=("build", "run"))

    depends_on("bzip2", type=("build", "link", "run"))
    depends_on("curl", type=("build", "link", "run"))
