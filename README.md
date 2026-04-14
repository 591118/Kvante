# Kvante

Lokalt læringsprosjekt for kvanteprogrammering med **Qiskit** og **Docker**. Koden i `app/` følger en bevisst progresjon: først én qubit, deretter to med entanglement.

## Krav

- [Docker](https://docs.docker.com/get-docker/) (bygger og kjører alt i container)

## Bygg og kjør

Bygg imaget én gang (eller etter endringer i `Dockerfile` / avhengigheter):

```bash
docker build -t kvante .
```

Standardkommandoen i imaget kjører **alle** skriptene i `app/` i fast rekkefølge:

1. `hello_quantum.py` — én qubit, superposisjon (Hadamard) og måling  
2. `hello_quantum_with_two_bits.py` — to qubits, Bell-lignende oppsett (H + CNOT)

```bash
docker run --rm kvante
```

Merk: riktig flagg er `--rm` (to bindestreker), ikke `-rm`.

### Kjør ett skript om gangen

```bash
docker run --rm kvante python app/hello_quantum.py
docker run --rm kvante python app/hello_quantum_with_two_bits.py
```

## Prosjektstruktur

| Sti | Innhold |
|-----|---------|
| `app/` | Kjørbare Qiskit-eksempler |
| `docs/` | Konsepter, strategi, eksperimentlogg og veikart |
| `requirements.txt` | Python-avhengigheter |
| `Dockerfile` | Miljø og standard `CMD` for hele `app/`-løpet |

## Videre lesing

- [docs/learningStrategy.md](docs/learningStrategy.md) — steg-for-steg: hvordan du lærer med repoet  
- [docs/concepts.md](docs/concepts.md) — korte definisjoner du bruker i koden  
- [docs/experiments.md](docs/experiments.md) — hva du har kjørt og observert  
- [docs/roadmap.md](docs/roadmap.md) — neste steg i læringen  
