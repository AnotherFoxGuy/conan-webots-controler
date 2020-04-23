from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool


class WebotscontrollerConan(ConanFile):
    name = "webots-controller"
    version = "R2020a-rev1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Webotscontroller here>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = ["src/*", "prebuild/*"]

    def build(self):
        cmake = CMake(self)
        if tools.os_info.is_windows and self.settings.compiler == "Visual Studio":
            cmake.definitions['BUILD_C'] = 'OFF'
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
        if tools.os_info.is_windows and self.settings.compiler == "Visual Studio":
            self.copy("*.lib", dst="lib", keep_path=False)
            self.copy("*.dll", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
