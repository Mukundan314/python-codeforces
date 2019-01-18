
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

### Using `cf-run`

```shell
cf-run [contestId] [index] [program]
```

Example:

```
$ gcc a.c -o ./out
$ cf-run 1100 A ./out
A. Roman and Browser
time limit per test: 1 second
memory limit per test: 256 megabytes

--------------------------------------------------------------------------------

Time: 16 ms

Input
4 2
1 1 -1 1

Participant's output
2

Jury's answer
2

--------------------------------------------------------------------------------

Time: 19 ms

Input
14 3
-1 1 -1 -1 1 -1 -1 1 -1 -1 1 -1 -1 1

Participant's output
9

Jury's answer
9
```

### Documentation

Documentation can be found at https://python-codeforces.readthedocs.io/en/latest/

### License

See [LICENSE](LICENSE).
