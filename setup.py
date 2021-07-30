import setuptools

with open("README.md", "r") as file_handler:
    long_description = file_handler.read()


setuptools.setup(
    name="kollet-io-python",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license='MIT',
    author="Kollet",
    author_email="",
    description="Python API wrapper for the Kollet Merchant API",
    long_description=long_description,
    url="https://github.com/kollet-io/kollet-python-api-wrapper.git",
    keywords="",
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)