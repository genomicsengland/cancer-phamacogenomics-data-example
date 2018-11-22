from distutils.core import setup
from setuptools import find_packages

test_deps = ['mock']

setup(
    name='datemodelling',
    version=1,
    packages=find_packages(),
    scripts=[],
    url='',
    license='',
    author='priesgo',
    author_email='pablo.ferreiro@genomicsengland.co.uk',
    description='',
    install_requires=[
        'gelreportmodels==7.1.12',
        'mock',
        'pytest'
    ],
    tests_require=test_deps,
    extras_require={'test': test_deps},
)
