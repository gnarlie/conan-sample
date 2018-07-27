from conans import ConanFile, CMake, tools

import os

class SampleConan(ConanFile):

    name = 'sample'
    version = '1.0.0'
    exports_sources = 'sample/*'

    def build(self):
        try:
            os.makedirs('./sample/build')
        except:
            pass
        cmake = CMake(self)
        cmake.configure(source_dir='..', build_dir='sample/build')
        cmake.build()

    def package(self):
        self.copy( '*.dylib*', dst='lib', src='sample/build', symlinks=True )
        self.copy( '*.so*', dst='lib', src='sample/build', symlinks=True )
        self.copy( '*.h', dst='include', src='sample/sample.h')

    def package_info(self):
        self.cpp_info.libs = ['sample']
