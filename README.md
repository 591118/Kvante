# Kvante

Lokalt læringsprosjekt for kvanteprogrammering med **Qiskit** og **Docker**. Koden i `app/` følger en bevisst progresjon: først én qubit, deretter to med entanglement.

## Krav

- [Docker](https://docs.docker.com/get-docker/) (bygger og kjører alt i container)

## Bygg og kjør

Bygg imaget én gang (eller etter endringer i `Dockerfile` / avhengigheter):

```bash
docker build -t kvante .
```

Standardkommandoen kjører **`app/main.py`**, som i rekkefølge kjører:

1. `hello_quantum.py` — lokal simulator (én qubit)  
2. `hello_quantum_with_two_bits.py` — lokal simulator (to qubits)  
3. `ibm.py` — ekte **IBM Quantum** (kun hvis `IQP_API_TOKEN` finnes; ellers hoppes steget over)

```bash
docker run --rm kvante
```

Med IBM-nøkkel (`.env` i prosjektroten):

```bash
docker run --rm --env-file .env kvante
```

Merk: riktig flagg er `--rm` (to bindestreker), ikke `-rm`.

### Lokalt (fra prosjektrot `Kvante/`)

```bash
python -m app.main
```

Lagre IBM-innlogging én gang (valgfritt): `python -m app.ibm_connection`. Filen `.env` bruker `IQP_API_TOKEN` og valgfritt `IQP_INSTANCE` — se `.env.example`.

### Kjør ett skript om gangen

```bash
docker run --rm kvante python -m app.hello_quantum
docker run --rm kvante python -m app.hello_quantum_with_two_bits
docker run --rm --env-file .env kvante python -m app.ibm
```

## Prosjektstruktur

| Sti | Innhold |
|-----|---------|
| `app/` | Kjørbare Qiskit-eksempler |
| `docs/` | Konsepter, strategi, eksperimentlogg og veikart |
| `youtubeLearning/` | Video-notater, AI-oppsummeringer (se under) |
| `requirements.txt` | Python-avhengigheter |
| `Dockerfile` | Miljø og standard `CMD` for hele `app/`-løpet |

## youtubeLearning — notater og oppsummeringer

| Hva | Fil(er) | Merknad |
|-----|---------|---------|
| **Dine notater (intro 1–5)** | [`Intro1.md`](youtubeLearning/Intro1.md), [`intro2.md`](youtubeLearning/intro2.md), [`intro3.md`](youtubeLearning/intro3.md), [`intro4.md`](youtubeLearning/intro4.md), [`intro5.md`](youtubeLearning/intro5.md) | Rå notater fra YouTube-kilder, i rekkefølge. |
| **AI-oppsummering (Cursor)** | [`youtubeLearning/AIoppsummering.md`](youtubeLearning/AIoppsummering.md) | Samkjørt sammendrag av intro 1–5 + tverrgående tema for research. |
| **Chat-oppsummering (ChatGPT)** | [`youtubeLearning/chatOppsummering.md`](youtubeLearning/chatOppsummering.md) | Sammendrag fra ChatGPT-samtale (supplement til Cursor-filen). |

Bruk gjerne **dine notater** som sannhetskilde for hva du faktisk så; bruk **AIoppsummering** og **chatOppsummering** som strukturerte repetisjons- og søkeinnganger.

## Videre lesing

- [docs/learningStrategy.md](docs/learningStrategy.md) — steg-for-steg: hvordan du lærer med repoet  
- [docs/concepts.md](docs/concepts.md) — korte definisjoner du bruker i koden  
- [docs/experiments.md](docs/experiments.md) — hva du har kjørt og observert  
- [docs/roadmap.md](docs/roadmap.md) — neste steg i læringen  
