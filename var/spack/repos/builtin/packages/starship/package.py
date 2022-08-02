# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Starship(Package):
    """The minimal, blazing-fast, and infinitely
    customizable prompt for any shell!"""

    homepage = "https://starship.rs/"
    url = "https://github.com/starship/starship/archive/refs/tags/v1.6.3.tar.gz"

    version('1.9.1', sha256='2b54bee07bf67504a1bb170d37dc8d6accab4594d35731bbdf0e8a631c8d1585')
    version('1.8.0', sha256='398bf5b413ce5dfe4d3c5acceb0025f773478f28016609869821cf385448dcf5')
    version('1.7.1', sha256='364b8222e097a8c671a9d03788ffc745982f4e62ee59e75687eb75310fae64e0')
    version('1.6.3', sha256='a6219189eb1e9182eb092213ce4cdd5fba84ae148cb9c4188610a907231a77c7')

    depends_on('rust')

    def install(self, spec, prefix):
        cargo = which('cargo')
        cargo('install', '--root', prefix, '--path', '.')
