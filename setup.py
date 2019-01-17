from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()

setup(
    name='python-codeforces',
    version='0.2.2',
    description='Codeforces API wrapper for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='codeforces',
    url='https://github.com/Mukundan314/python-codeforces',
    author='Mukundan',
    author_email='mukundan314@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['docs']),
    install_requires=['bs4', 'colorama'],
    extras_requires={ 'docs': ['sphinx', 'sphinx_rtd_theme'] },
    scripts=['bin/cf-run'],
    python_requires='>=3.6,<4',
    project_urls={
        "Bug Tracker": "https://github.com/Mukundan314/python-codeforces/issues/",
        "Documentation": "https://python-codeforces.readthedocs.io/en/stable/",
        "Source": "https://github.com/Mukundan314/python-codeforces"
    }
)
