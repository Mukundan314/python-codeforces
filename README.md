
<h1 align="center"> python-codeforces</h1>

<div align="center">
  <strong>Codeforces API wrapper for python</strong>
</div>

<br />

<div align="center">
  <a href="https://python-codeforces.readthedocs.io/en/latest/?badge=latest">
    <img alt="Documentation Status" src="https://readthedocs.org/projects/python-codeforces/badge/?version=latest" />
  </a>
  <a href="https://travis-ci.com/Mukundan314/python-codeforces">
    <img alt="Build Status" src="https://travis-ci.com/Mukundan314/python-codeforces.svg?branch=master" />
  </a>
  <a href="https://pypi.org/project/python-codeforces/">
    <img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/python-codeforces.svg" />
  </a>
</div>

---

### Installation

#### Using `pip`

```shell
pip install python-codeforces
```

#### From source

```shell
git clone https://github.com/Mukundan314/python-codeforces.git
cd python-codeforces
pip install .
```

#### For Development

```shell
git clone https://github.com/Mukundan314/python-codeforces.git
cd python-codeforces
pip install -e .
```

### Commandline tools

#### `cf-run`

Run a program against sample testcases.

```shell
usage: cf-run [-h] [-t TIMEOUT] [-g] contestId index program

positional arguments:
  contestId             Id of the contest. It is not the round number. It can
                        be seen in contest URL.
  index                 A letter or a letter followed by a digit, that
                        represent a problem index in a contest.
  program               Path to executable that needs to be tested

optional arguments:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Timeout for program in seconds, -1 for no time limit
                        (default: 10)
  -g, --gym             If true open gym contest instead of regular contest.
                        (default: false)
```

### Documentation

Documentation can be found at https://python-codeforces.readthedocs.io/en/latest/

### License

See [LICENSE](LICENSE).
