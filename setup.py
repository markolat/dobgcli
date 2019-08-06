import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dobg",
    install_requires=['requests', 'python-digitalocean>=1.14.0'],
    version="0.0.22",
    entry_points = {
        "console_scripts": ['dobg = dobg.dobg:main']
        },
    author="Marko Latinovic",
    author_email="markolat@outlook.com",
    description="Digital Ocean CLI tool for managing Droplets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markolat/dobgcli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
    ],
)