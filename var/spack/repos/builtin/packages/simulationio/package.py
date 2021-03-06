# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Simulationio(CMakePackage):
    """SimulationIO: Efficient and convenient I/O for large PDE simulations"""

    homepage = "https://github.com/eschnett/SimulationIO"
    url      = "https://github.com/eschnett/SimulationIO/archive/version/0.1.0.tar.gz"
    git      = "https://github.com/eschnett/SimulationIO.git"

    version('develop', branch='master')
    version('1.0.0', '5cbf1d0084eb436d861ffcdd297eaa08')
    version('0.1.0', '00f7dabc08ed1ab77858785ce0809f50')

    variant('julia', default=False)
    variant('python', default=True)

    variant('pic', default=True,
            description="Produce position-independent code")

    depends_on('hdf5 +cxx @:1.10.0-patch1')
    depends_on('julia', when='+julia', type=('build', 'run'))
    depends_on('py-h5py', when='+python', type=('build', 'run'))
    depends_on('py-numpy', when='+python', type=('build', 'run'))
    depends_on('python@2.7:2.8', when='+python', type=('build', 'run'))
    depends_on('swig', type='build')

    extends('python')

    def cmake_args(self):
        spec = self.spec
        options = []
        if '+pic' in spec:
            options.append("-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=true")
        return options

    def check(self):
        with working_dir(self.build_directory):
            make("test", "CTEST_OUTPUT_ON_FAILURE=1")
