from setuptools import find_packages, setup

setup(
    name='postcodelib',
    packages=find_packages(include=['postcodelib']),
    version='0.1.0',
    description='UK postcode validator',
    author='Jack Duggan',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)