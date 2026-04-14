# Konsepter

Korte notater som matcher rekkefølgen i `app/`. Utvid etter hvert som du legger til nye filer.

## Qubit

Den grunnleggende enheten i kvanteinformasjon. Til forskjell fra en klassisk bit (0 eller 1) kan en qubit være i en **superposisjon** av 0 og 1 inntil den måles.

## Superposisjon

En tilstand der utfallet av en måling ikke er fastlåst på forhånd. I `hello_quantum.py` brukes **Hadamard-porten** `H` på én qubit slik at måling gir omtrent like mange `0` og `1` over mange kjøringer (her: 1024 *shots*).

## Måling (measurement)

Når du måler en qubit, kollapser tilstanden til et konkret resultat (`0` eller `1`) i den klassiske registerbiten. Resultatet samles i **tellinger** (*counts*), f.eks. `{'0': 512, '1': 512}`.

## Kvantekrets (`QuantumCircuit`)

En sekvens av operasjoner (porter) på qubits, avsluttet med måling der det er relevant. Qiskit kan tegne kretsen som tekst eller figur.

## Simulator (`AerSimulator`)

Et klassisk program som **simulerer** kvantemekanikken. Nyttig for læring og debugging uten tilgang til ekte kvantehardware. Kretsen **transpileres** til simulatorinstruksjoner før kjøring.

## Flere qubits og CNOT

Med to qubits har du tilstander i et større rom. **CNOT** (her: `cx(0, 1)`) er en to-qubit-port som kan **entanglere** qubits når den kombineres med f.eks. `H` på kontroll-qubit. Se `hello_quantum_with_two_bits.py`: etter H på qubit 0 og CNOT mot qubit 1 forventer du typisk hovedsakelig `00` og `11` i tellingene (Bell-tilstand).

## Shots

Antall ganger simulatoren kjører kretsen og samler statistikk. Flere shots gir jevnere fordeling; få shots gir mer «støy» i enkeltkjøringer.
