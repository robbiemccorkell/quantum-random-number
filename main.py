# Import the Qiskit SDK
import math, argparse, warnings
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

warnings.filterwarnings("ignore")

MAX_QUBITS = 5

def parse_input():
  parser=argparse.ArgumentParser()
  parser.add_argument('max', metavar='n', type=int, nargs='?', default=16, help='a maximum integer to generate')
  parser.add_argument('--remote', action='store_true', default=False, help='run command on reale remote quantum processor')
  args = parser.parse_args()

  next_power = next_power_of_2(args.max)
  if (next_power > args.max):
    print(f"Rounding input {args.max} to next power of 2: {next_power}")
    args.max = next_power

  return args

def next_power_of_2(n):
  return int(math.pow(2, math.ceil(math.log(n, 2))))

def bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]

def num_bits(n):
  return math.floor(math.log(n, 2)) + 1

def get_register_sizes(n, max_qubits):
  register_sizes = [max_qubits for i in range(int(n / max_qubits))]
  remainder = n % max_qubits
  return register_sizes if remainder == 0 else register_sizes + [remainder]

def random_int(max):
  bits = ''
  n_bits = num_bits(max - 1)
  register_sizes = get_register_sizes(n_bits, MAX_QUBITS)
  for x in register_sizes:
    q = QuantumRegister(x)
    c = ClassicalRegister(x)
    qc = QuantumCircuit(q, c)

    qc.h(q)
    qc.measure(q, c)

    job_sim = execute(qc, "local_qasm_simulator", shots=1)
    sim_result = job_sim.result()
    counts = sim_result.get_counts(qc)

    bits += bit_from_counts(counts)
  return int(bits, 2)

input = parse_input()
result = random_int(input.max)

print(result)