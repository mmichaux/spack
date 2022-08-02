# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAsdf(PythonPackage):
    """The Advanced Scientific Data Format (ASDF) is a next-generation
    interchange format for scientific data. This package contains the Python
    implementation of the ASDF Standard."""

    homepage = "https://github.com/spacetelescope/asdf"
    pypi = "asdf/asdf-2.4.2.tar.gz"

    version("2.12.0", sha256="5914834d077ba3bf68b9aafdc646b9f27ce5e56e1c241167d461dee43b1023e9")
    version("2.11.1", sha256="d6e0d1a12f67c9908b3dd6e20100400e88b0a9a541ce3d4d329657749418a314")
    version("2.10.1", sha256="f7e569f29b3723939efec8164eb2ed7274bdd480b0b283d75833f0f59d108409")
    version("2.9.2", sha256="fb41b8211542541fb8e362951d99611a24786c3fad60e834f71f8bf8f218f3f3")
    version("2.8.3", sha256="de0f70ffb2e0d539461940d6f7529c3548541fa098d8edc37af256af61c09b44")
    version("2.7.5", sha256="66068ea17d185dd6e05648c61180f4697eff403709fa1e572fba40a1d9e9b829")
    version("2.6.0", sha256="6549c3f84d16ad60c17001b1dece76827a9a93c4aee7e0a98dd4da2b7bada9fa")
    version("2.5.2", sha256="1e85178ba228976ed96869322bab9410dc87eeb71b0e5c1d6601ab4685a1252a")
    version("2.4.2", sha256="6ff3557190c6a33781dae3fd635a8edf0fa0c24c6aca27d8679af36408ea8ff2")

    variant("extras", default=False, description="Enable extra functionality")

    depends_on("python@3.7:", when="@2.9:", type=("build", "run"))
    depends_on("python@3.6:", when="@2.8:", type=("build", "run"))
    depends_on("python@3.5:", when="@2.6:", type=("build", "run"))
    depends_on("python@3.3:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-semantic-version@2.8:", when="@2.5:", type=("build", "run"))
    depends_on("py-semantic-version@2.3.1:2.6.0", when="@:2.4", type=("build", "run"))
    depends_on("py-pyyaml@3.10:", type=("build", "run"))
    depends_on("py-jsonschema@4.0.1:", when="@2.11:", type=("build", "run"))
    depends_on("py-jsonschema@3.0.2:3.2.0", when="@2.7:2.10", type=("build", "run"))
    depends_on("py-jsonschema@2.3:3", when="@:2.6", type=("build", "run"))
    depends_on("py-six@1.9.0:", type=("build", "run"))
    depends_on("py-numpy@1.10:", when="@2.7:", type=("build", "run"))
    depends_on("py-numpy@1.8:", type=("build", "run"))
    depends_on("py-importlib-resources@3:", when="@2.8: ^python@:3.8", type=("build", "run"))
    depends_on("py-jmespath@0.6.2:", when="@2.8:", type=("build", "run"))
    depends_on("py-packaging@16:", when="@2.8:", type=("build", "run"))
    depends_on("py-asdf-standard@1.0.1:", when="@2.10.1:", type=("build", "run"))
    depends_on("py-asdf-standard@1:", when="@2.10:", type=("build", "run"))
    depends_on("py-asdf-transform-schemas@0.2.2:", when="@2.10.1:", type=("build", "run"))
    depends_on("py-asdf-transform-schemas@0.2:", when="@2.10:", type=("build", "run"))

    depends_on("py-lz4@0.10:", when="+extras", type=("build", "run"))
