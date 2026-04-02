from setuptools import setup, find_packages


setup(
    name='ndfl-puslore',
    version='0.0.2',
    description='Simple NDFL calculator. The part of FOSS course.',
    author='Puslore',
    url='https://github.com/Puslore/fossdev',
    package_dir={'': 'src'},
    packages=find_packages(where='src')
)
