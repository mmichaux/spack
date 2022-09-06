# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Lsd(Package):
    """This project is a rewrite of GNU ls with lot of added features like
    colors, icons, tree-view, more formatting options etc.
    The project is heavily inspired by the super colorls project."""

    homepage = "https://github.com/Peltoche/lsd"
    url = "https://github.com/Peltoche/lsd/archive/refs/tags/0.23.0.tar.gz"

    version("0.23.0", sha256="0ce6582745b5364fdb4052954d24f6a211af616061d1454583e68f3366f6496e")

    depends_on("rust")

    def install(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--root", prefix, "--path", ".")
