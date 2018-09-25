# Quantum Random Number Generator

Generates a random integer between 0 and a given maximum using a quantum computer.

Requirements:
- Python 3.5 or later

For use on a real remote quantum computer:
- Create an account with [IBM Q Experience](https://quantumexperience.ng.bluemix.net/qx)
- Generate an API token at [My Account -> Advanced](https://quantumexperience.ng.bluemix.net/qx/account/advanced)

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
$ python ./main.py 12
Rounding input 12 to next power of 2: 16
9
```

For help:
```bash
python ./main.py -h
```

### Real quantum backend

For use on a real quantum computer, generate an API key with [IBM Q Experience](https://quantumexperience.ng.bluemix.net/qx) using the instructions above.

Then run the script with:

```bash
python ./main.py -remote --qx-token <your-token> 15
```

Your instructions will be put in a queue to be run on the [IBM Q 5 Tenerife](https://github.com/Qiskit/qiskit-backend-information/tree/master/backends/tenerife/V1) quantum computer. This can take some time (approx 10 - 20 minutes) to complete.

IBM Q provides 15 credits per run for free users, and the IBMq5 backend has 5 available qubits. The script will loop until the necessary number of bits have been generated to create a random number up to the desired maximum, and will consume 3 credits each loop. This means that the script is capable of generating numbers up to a maximum of 33554431 (25 bits) in a single run before credits run out.

Free units are reset every time a result is viewed, so if the script completes sucessfully you should get your 15 credits back. If the script errors, or is cancelled, credits will be refreshed on the next successful run or on the next calendar day.