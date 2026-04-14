from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def main() -> None:
    # 1 qubit, 1 classical bit
    qc = QuantumCircuit(1, 1)

    # Sett qubiten i superposisjon
    qc.h(0)

    # Mål qubiten
    qc.measure(0, 0)

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