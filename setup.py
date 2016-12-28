from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kata',
    version='0.0.1',
    description='Kata Practice',
    long_description=readme,
    author='Todd Benson',
    author_email='todd@grayknightsecurity.com',
    url='https://github.com/ToddBenson/kata',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
