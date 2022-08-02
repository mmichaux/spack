# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCorrfunc(PythonPackage):
    """This package contains a suite of codes to calculate correlation
    functions and other clustering statistics for simulated galaxies in
    a cosmological box (co-moving XYZ) and on observed galaxies with
    on-sky positions (RA, DEC, CZ). """

    homepage = "http://corrfunc.rtfd.io/"
    pypi     = "Corrfunc/Corrfunc-2.4.0.tar.gz"

    version('2.4.0', sha256='7fd177ba245c5aeb3ea5c2006f071a1c6134736d9b25530bd46b321162e7335a')

    depends_on('python@3.4:', type=('build', 'run'))

    depends_on('py-setuptools', type='build')

    depends_on('gmake@3.8:', type='build')
    depends_on('gsl@2.4:', type=('build', 'run'))
    
    depends_on('py-numpy@1.7:', type=('build', 'run'))
