"""
Bell-lignende krets (H + CNOT + måling) på IBM Quantum via Runtime Sampler.

Krever IQP_API_TOKEN (og valgfritt IQP_INSTANCE) i miljø eller .env i prosjektrot.
Uten token: skriver melding og returnerer (for Docker/CI uten hemmeligheter).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler

_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")


def _service_from_env() -> QiskitRuntimeService | None:
    token = os.environ.get("IQP_API_TOKEN", "").strip()
    if not token:
        return None
    instance = os.environ.get("IQP_INSTANCE", "").strip() or None
    kwargs: dict = {"token": token}
    if instance:
        kwargs["instance"] = instance
    try:
        return QiskitRuntimeService(**kwargs)
    except Exception as e:
        print(f"Kunne ikke koble til IBM Quantum: {e}", file=sys.stderr)
        return None


def main() -> None:
    service = _service_from_env()
    if service is None:
        print(
            "Hopper over IBM Quantum (mangler IQP_API_TOKEN). "
            "Legg nøkkel i .env eller kjør med --env-file ved Docker."
        )
        return

    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    print("Krets (tekst):")
    print(qc.draw(output="text"))

    backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)
    print(f"Backend: {backend.name}")

    pm = generate_preset_pass_manager(optimization_level=1, target=backend.target)
    isa = pm.run(qc)

    sampler = Sampler(mode=backend)
    job = sampler.run([(isa,)])
    print(f"Jobb-id: {job.job_id()}")
    result = job.result()
    pub = result[0]
    counts = pub.data.c.get_counts()
    print("\nMålinger (IBM):")
    print(counts)


if __name__ == "__main__":
    main()
