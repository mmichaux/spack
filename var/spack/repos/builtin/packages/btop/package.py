# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Btop(MakefilePackage):
    """Resource monitor that shows usage and stats for processor,
    memory, disks, network and processes.
    C++ version and continuation of bashtop and bpytop."""

    homepage = "https://github.com/aristocratos/btop"
    url      = "https://github.com/aristocratos/btop/archive/refs/tags/v1.2.8.tar.gz"

    version('1.2.8', sha256='7944b06e3181cc1080064adf1e9eb4f466af0b84a127df6697430736756a89ac')

    def setup_build_environment(self, env):
        env.set('PREFIX', self.prefix)
        env.set('ARCH', self.spec.architecture.target)
        env.set('STRIP', 'true')

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            make()

    def install(self, spec, prefix):
        with working_dir(self.build_directory):
            make('install')
