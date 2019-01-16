from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

setup(
    name='python-codeforces',
    version='0.2.1',
    author='Mukundan',
    author_email='mukundan314@gmail.com',
    description='Codeforces API wrapper for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='codeforces',
    url='https://github.com/Mukundan314/python-codeforces',
    python_requires='>=3.6,<4',
    install_requires=['bs4'],
    extras_requires={ 'docs': ['sphinx', 'sphinx_rtd_theme'] },
    packages=find_packages(exclude=['docs']),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
