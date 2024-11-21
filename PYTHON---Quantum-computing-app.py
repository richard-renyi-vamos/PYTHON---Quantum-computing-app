from qiskit import QuantumCircuit, transpile, Aer, IBMQ, execute
from qiskit.providers.ibmq import least_busy
import os

# Load your IBMQ account
IBMQ.save_account('YOUR_API_TOKEN', overwrite=True)  # Replace with your API token
IBMQ.load_account()

# Get the least busy backend
provider = IBMQ.get_provider(hub='ibm-q')
backend = least_busy(provider.backends(filters=lambda x: x.configuration().n_qubits >= 2 and
                                       not x.configuration().simulator and x.status().operational))
print(f"Using backend: {backend}")

# Create a Quantum Circuit
qc = QuantumCircuit(2, 2)
qc.h(0)  # Apply Hadamard gate to qubit 0
qc.cx(0, 1)  # Apply CNOT gate between qubit 0 and qubit 1
qc.measure([0, 1], [0, 1])  # Measure both qubits

print("Quantum Circuit:")
print(qc)

# Execute the circuit
job = execute(qc, backend=backend, shots=1024)

# Get the results
result = job.result()
counts = result.get_counts(qc)
print(f"Measurement results: {counts}")
