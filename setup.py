from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

setup(
    name='python-codeforces',
    version='0.1.0',
    author='Mukundan',
    author_email='mukundan314@gmail.com',
    description='Codeforces API wrapper for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='codeforces',
    url='https://github.com/Mukundan314/python-codeforces',
    packages=find_packages()
)
