from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename)]

setup(
    name="Eniato",
    version="0.0.1",
    description='Bora ficar rico Ro',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_requires={'dev': read("requirements-dev.txt")}
)

#Descrições e instala requerimentos