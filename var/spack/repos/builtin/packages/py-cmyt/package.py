# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCmyt(PythonPackage):
    """Matplotlib colormaps from the yt project !"""

    homepage = "https://yt-project.org/"
    pypi = "cmyt/cmyt-1.0.4.tar.gz"

    version('1.0.4', sha256='ae5157d37e733ae55df12bad1e8aedb3eb2f3b45e829e25c83df023dcefd5926')

    depends_on('python@3.6:', type=('build', 'run'))

    depends_on('py-setuptools@40.9:', type='build')

    depends_on('py-colorspacious@1.1.2:', type=('build', 'run'))
    depends_on('py-matplotlib@2.1:', type=('build', 'run'))
    depends_on('py-more-itertools@8.4:', type=('build', 'run'))
    depends_on('py-numpy@1.13.3:', type=('build', 'run'))
    depends_on('py-typing-extensions@3.10.0.2:', type=('build', 'run'))
