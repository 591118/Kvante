from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def main() -> None:
    # 2 qubits, 2 classical bits
    qc = QuantumCircuit(2, 2)

    # Sett første qubit i superposisjon
    qc.h(0)

    # Koble qubit 0 til qubit 1 med entanglement
    qc.cx(0, 1)

    # Mål begge qubits
    qc.measure([0, 1], [0, 1])

    print("Quantum circuit:")
    print(qc.draw(output="text"))

    simulator = AerSimulator()
    compiled_circuit = transpile(qc, simulator)

    job = simulator.run(compiled_circuit, shots=1024)
    result = job.result()
    counts = result.get_counts()

    print("\nMeasurement counts:")
    print(counts)


if __name__ == "__main__":
    main()