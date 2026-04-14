# Veikart

Stegvis læring som speiler det som ligger i repoet i dag. Juster rekkefølgen når du legger til nye moduler.

**Hvordan du bruker dette:** følg [learningStrategy.md](learningStrategy.md) for øktstruktur, mini-oppgaver og sjekkliste før du går videre.

## Nå (i repoet)

1. **Én qubit** — `app/hello_quantum.py`  
   Forstå krets, H-gate, måling og counts i simulatoren.

2. **To qubits** — `app/hello_quantum_with_two_bits.py`  
   Bygg videre med CNOT og se korrelerte utfall (`00` / `11`).

## Neste naturlige steg (forslag)

- Variér **shots** og noter hvordan statistikken endrer seg.  
- Tegn krets som bilde (Qiskit + matplotlib) og arkiver i `docs/` eller notater.  
- Eget skript for **Bell-tilstand** med tydelig kommentar om kontroll/mål.  
- Intro til **rotasjonsporter** (f.eks. `ry`) på én qubit.  
- Senere: enkel **kvantealgoritme** (f.eks. Deutsch–Jozsa eller Grover i minimalt omfang) når grunnmuren sitter.

## Kobling til «resten»

Når du jobber med app/optimizer parallelt: noter hvilke problemer som er *kvante-egnet* (struktur, størrelse, noise) versus hva som fortsatt bør løses klassisk. Det holder å ha noen linjer her per idé — ikke alt må implementeres med én gang.
