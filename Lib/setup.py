from setuptools import setup

setup(
    name='Serializer',
    packages=[
        'Serializer',
        'Serializer/factory',
        'Serializer/packager',
        'Serializer/parsers',
    ],
    version='3.1.3',
    description='Serializer library',
    author='Stanislav Korenevsky',
    install_requires=['pyyaml'],
    python_requires='>=3.8',
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],
    # test_suite='tests',
)