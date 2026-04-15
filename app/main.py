"""
Kjører i rekkefølge:
1) hello_quantum.py — lokal simulator (Aer)
2) hello_quantum_with_two_bits.py — lokal simulator
3) ibm.py — ekte IBM Quantum (hvis IQP_API_TOKEN er satt; ellers hoppes over)

Docker: python -m app.main
Lokalt fra Kvante/: python -m app.main
"""

from __future__ import annotations

import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (OSError, ValueError):
        pass

from app import hello_quantum
from app import hello_quantum_with_two_bits
from app import ibm as ibm_run


def main() -> None:
    print("========== 1/3 Lokalt: én qubit ==========\n")
    hello_quantum.main()
    print("\n========== 2/3 Lokalt: to qubits ==========\n")
    hello_quantum_with_two_bits.main()
    print("\n========== 3/3 IBM Quantum ==========\n")
    ibm_run.main()


if __name__ == "__main__":
    main()
