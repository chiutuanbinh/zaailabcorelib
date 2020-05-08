from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zaailabcorelib",
    version="0.1.9.3",
    author="ailabteam",
    include_package_data=True,
    description="A useful tools inside ZAI Lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    tests_require=["pytest", "mock"],
    test_suite="pytest",
)
