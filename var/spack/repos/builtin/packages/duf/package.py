# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Duf(Package):
    """Disk Usage/Free Utility"""

    homepage = 'https://github.com/muesli/duf'
    url = 'https://github.com/muesli/duf/archive/refs/tags/v0.8.1.tar.gz'

    phases = ['build', 'install']

    version('0.8.1', sha256='ebc3880540b25186ace220c09af859f867251f4ecaef435525a141d98d71a27a')

    depends_on('go@1.12:', type='build')

    def build(self, spec, prefix):
        go = which('go')
        go('build')

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install('duf', prefix.bin)
