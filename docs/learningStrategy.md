# Strategi for steg-for-steg-læring

Denne filen er «hvordan du lærer»; [roadmap.md](roadmap.md) er «hva du gjør når». Bruk dem sammen.

## Prinsipp

Én ting om gangen: **kjør → observer → forklar med egne ord → noter → først deretter neste steg**. Hopp ikke over notatene — de er det som gjør læringen din gjenfinnbar om en måned.

## Før du starter en økt (5 minutter)

1. Åpne [experiments.md](experiments.md) og forbered en ny rad (dato + hvilket steg du er på).
2. Bestem **ett** fokus for økta: enten «forstå koden som finnes» eller «gjør én liten endring».

## Steg 0 — Miljø (én gang)

- Bygg imaget: `docker build -t kvante .`
- Kjør hele løpet: `docker run --rm kvante`
- Bekreft at du ser to kretsutskrifter og **counts** uten feil.

## Steg 1 — Én qubit (`hello_quantum.py`)

| Del | Hva du gjør |
|-----|-------------|
| **Les** | Les koden linje for linje. Slå opp ukjente ord i [concepts.md](concepts.md). |
| **Kjør** | `docker run --rm kvante python app/hello_quantum.py` flere ganger. |
| **Observer** | Tallene varierer litt mellom kjøringer — det er forventet (stokastikk). |
| **Forklar** | Skriv én setning: *Hvorfor* kan `0` og `1` begge dukke opp etter `H`? |
| **Noter** | Lim inn eksempel på counts i [experiments.md](experiments.md). |

**Mini-oppgaver** (velg én per økt, ikke alle på én gang):

- Endre **shots** (f.eks. 100 vs 10 000) og beskriv forskjellen i spredning.
- Kommenter ut `H` og kjør igjen — hva skjer, og hvorfor?

## Steg 2 — To qubits (`hello_quantum_with_two_bits.py`)

| Del | Hva du gjør |
|-----|-------------|
| **Les** | Forstå rekkefølgen: `H` på qubit 0, deretter `cx(0, 1)`. |
| **Kjør** | Samme mønster som steg 1. |
| **Observer** | Du forventer mest `00` og `11`, lite `01` og `10`. |
| **Forklar** | Skriv: *Hva gjør CNOT når kontrollen er i superposisjon?* (kort, i egne ord). |
| **Noter** | Oppdater [experiments.md](experiments.md). |

**Mini-oppgaver:**

- Bytt rekkefølge eller fjern `H` — forutsig resultatet *før* du kjører.
- Tegn kretsen på papir før du ser på Qiskit-teksttegningen.

## Steg 3 — Koble sammen og utvide

Når steg 1–2 føles «kjente»:

1. Les [roadmap.md](roadmap.md) og velg **ett** neste tema (f.eks. Bell dedikert fil, rotasjon, eller algoritme-intro).
2. Implementer i **ny fil** under `app/` og legg den inn i Dockerfile-rekkefølgen når den skal med i standardkjøring.
3. Oppdater [concepts.md](concepts.md) med nye begreper du faktisk bruker.

## Anbefalt ukerytme (tilpass etter livet ditt)

| Dag | Aktivitet |
|-----|-----------|
| **1× / uke** | Nytt konsept eller ny mini-oppgave (30–60 min). |
| **1× / uke** | Repetisjon: kjør forrige steg uten å lese koden først — klarer du å forutsi counts? |

Hvis du bare har **15 min**: kjør én fil, noter counts, én setning i [experiments.md](experiments.md).

## Sjekkliste før du går videre til neste kapittel

Du er klar for neste steg når du uten juks kan svare på:

- [ ] Hva gjør `H` og hva ser du i målingene på én qubit?
- [ ] Hva er forskjellen på kvantetilstand *før* og *etter* måling?
- [ ] Hvorfor gir `H` + `cx` på to qubits hovedsakelig `00` og `11`?

## Dokumentene dine — kort rollefordeling

| Fil | Bruk |
|-----|------|
| [learningStrategy.md](learningStrategy.md) | Slik øver du (denne filen). |
| [roadmap.md](roadmap.md) | Hva som kommer i hvilken rekkefølge. |
| [concepts.md](concepts.md) | Ordbok / definisjoner. |
| [experiments.md](experiments.md) | Logg over kjøringer og tall. |

Ikke vær redd for uklare spørsmål i loggen — det du skriver ned i dag er gull verdt neste uke.
