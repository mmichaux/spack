# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Healpix(Package):
    """Software for pixelization, hierarchical indexation,
    synthesis, analysis, and visualization of data on the sphere."""

    homepage = "http://healpix.sourceforge.net/"
    url = "https://sourceforge.net/projects/healpix/files/Healpix_3.81/Healpix_3.81_2022Jan25.tar.gz/download"

    version('3.81', sha256='82d92bb21626371f9d280e59e82ad0f47d9ae62c70d86ccd1026e0310f193551')

    phases = ['configure', 'build', 'install']

    variant('c', default=True, description='Builds the C library')
    variant('cxx', default=True, description='Builds the C++ library')
    variant('shared', default=True, description='Also build the shared library')
    variant('f90', default=False, description='Builds the Fortran 90 library')

    depends_on('cfitsio', when='+c')

    def configure_args(self, spec):
        args = list()
        languages = list()

        args += ['-L']

        if spec.satisfies('+c'):
            languages += ['c']

        if spec.satisfies('+cxx'):
            languages += ['cxx']

        if spec.satisfies('+f90'):
            languages += ['f90']

        args += ['--auto={}'.format(','.join(languages))]
        return args

    def configure(self, spec, prefix):
        cfitsio = spec['cfitsio']
        env['FITSDIR'] = f'{cfitsio.prefix}/lib'
        env['FITSINC'] = f'{cfitsio.prefix}/include'
        if spec.satisfies('+shared'):
            env['C_SHARED'] = '1'
        configure = Executable('./configure')
        configure(*self.configure_args(spec))

    def build(self, spec, prefix):
        make()

    def install(self, spec, prefix):
        if spec.satisfies('+c'):
            filter_file(r'prefix=[a-zA-Z0-9/.-]+', f'prefix={prefix}', 'lib/pkgconfig/chealpix.pc')

        if spec.satisfies('+cxx'):
            filter_file(r'prefix=[a-zA-Z0-9/.-]+', f'prefix={prefix}', 'lib/pkgconfig/healpix_cxx.pc')
            filter_file(r'-I[a-zA-Z0-9/.-]+healpix[a-zA-Z0-9/.-]+', f'-I{prefix}', 'lib/pkgconfig/healpix_cxx.pc')
            filter_file(r'prefix=[a-zA-Z0-9/.-]+', f'prefix={prefix}', 'lib/pkgconfig/libsharp.pc')

        install_tree('bin', prefix.bin)
        install_tree('include', prefix.include)
        install_tree('lib', prefix.lib)

    @run_after('install')
    @on_package_attributes(run_tests=True)
    def test(self):
        if self.spec.satisfies('+c'):
            make('c-test')
