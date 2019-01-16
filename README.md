# python-codeforces

[![Documentation Status](https://readthedocs.org/projects/python-codeforces/badge/?version=latest)](https://python-codeforces.readthedocs.io/en/latest/?badge=latest)

Codeforces API wrapper for python

## Installation

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

## Using `cf-run`

```shell
cf-run [contestId] [index] [program]
```

Example:

```shell
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

## Documentation

Documentation can be found at https://python-codeforces.readthedocs.io/en/latest/

## License

See [LICENSE](LICENSE).
