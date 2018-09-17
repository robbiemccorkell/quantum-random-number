# Quantum Random Number Generator

Generates a random integer between 0 and a given maximum using a simulated quantum computer.

Requirements:
- Python 3.5 or later

## Setup

```bash
pip install -r requirements.txt
```

With VirtualEnv:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python ./main.py [max]
```

Where `[max]` is the maximum integer for the generated random number. E.g:

```bash
$ python ./main.py 15
9
```

For help:
```bash
python ./main.py -h
```