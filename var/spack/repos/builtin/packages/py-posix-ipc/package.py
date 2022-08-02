# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPosixIpc(PythonPackage):
    """posix_ipc is a Python module (written in C)
    that permits creation and manipulation of POSIX inter-process semaphores,
    shared memory and message queues on platforms supporting
    the POSIX Realtime Extensions a.k.a. POSIX 1003.1b-1993.
    This includes nearly all Unices and Windows + Cygwin 1.7."""

    homepage = "http://semanchuk.com/philip/posix_ipc/"
    pypi = "posix_ipc/posix_ipc-1.0.5.tar.gz"

    version('1.0.5', sha256='6cddb1ce2cf4aae383f2a0079c26c69bee257fe2720f372201ef047f8ceb8b97')

    depends_on('python@2.7:', type=('build', 'run'))
