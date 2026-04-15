"""
Lagrer IBM Quantum-innlogging lokalt (valgfritt — ibm.py kan også bruke kun .env).

Kjør fra prosjektrot: python -m app.ibm_connection
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService

_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_ROOT / ".env")


def main() -> None:
    token = os.environ.get("IQP_API_TOKEN", "").strip()
    if not token:
        print(
            "Mangler IQP_API_TOKEN.\n"
            "Windows (PowerShell): $env:IQP_API_TOKEN = 'din-nøkkel'\n"
            f"Eller {_ROOT / '.env'} med IQP_API_TOKEN=... (committes ikke).",
            file=sys.stderr,
        )
        sys.exit(1)

    instance = os.environ.get("IQP_INSTANCE", "").strip() or None
    kwargs = {"token": token}
    if instance:
        kwargs["instance"] = instance

    QiskitRuntimeService.save_account(**kwargs)
    print("IBM Quantum-konto lagret. Du kan nå bruke QiskitRuntimeService() uten token i kode.")


if __name__ == "__main__":
    main()
