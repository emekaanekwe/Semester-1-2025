from setuptools import setup, find_packages

setup(
    name='tabular_q_learning',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
