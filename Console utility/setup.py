from setuptools import setup
from setuptools import find_packages

setup(
    name='convert',
    packages=[
        'packager',
        'packager/creator',
        'packager/object_inspector',
        'packager/packer',
        'packager/unpacker',
        'factory',
        'parsers',
        'parsers/base_parser',
        'parsers/json_parser',
        'parsers/yaml_parser',
    ],
    # version='0.2.0',
    description='Custom serializer',
    author='Stanislav Korenevsky',
    install_requires=[],
    # setup_requires=['pytest-runner'],
    # maybe version
    # tests_require=['pytest'],
    # test_suite='tests',
    scripts=['bin/convert']
)