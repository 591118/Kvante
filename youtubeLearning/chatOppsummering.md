# ChatGPT Oppsummering – Quantum Learning

Samlet oppsummering av læring fra **Intro 1–5** + egne refleksjoner.
Denne filen fokuserer på **kjernebegreper, forståelse og praktisk retning**.

---

# 🧠 Kvantemaskin (Quantum Computer)

En kvantemaskin er en datamaskin som bruker **kvantemekanikk** til å utføre beregninger.

* Klassiske maskiner bruker bits (0 eller 1)
* Kvantemaskiner bruker **qubits**
* Kan beskrive og utnytte naturens fundamentale oppførsel

💡 Viktig:

> Kvantemaskiner er ikke bare “raskere PC-er” – det er en helt annen måte å regne på

Inspirert av Richard Feynman:

> Hvis naturen er kvantemekanisk, bør en maskin som simulerer naturen også være det

---

# 🔢 Qubits vs Bits

## Klassisk bit

* 0 eller 1
* Som en bryter (av/på)

## Qubit

* 0, 1 eller en kombinasjon
* Representeres som en **vektor i et tilstandsrom**

Metafor:

* Bit = Nordpol eller Sørpol
* Qubit = Kan være hvor som helst på kloden

---

# 🌊 Superposisjon

Superposisjon betyr at en qubit kan være i flere tilstander samtidig.

Eksempel:

* Klassisk: 0 eller 1
* Kvante: 0 og 1 samtidig (med sannsynlighet)

Metafor:

* Mynt på bordet = klassisk
* Mynt i lufta = superposisjon

💡 Viktig:

* Før måling → flere muligheter
* Etter måling → én verdi

---

# 🔗 Entanglement (Sammenfiltring)

To qubits kan bli koblet slik at:

* Tilstanden til én påvirker den andre
* Selv over store avstander

Eksempel:

* Måler du én → vet du den andre

💡 Dette er en av de viktigste fordelene i quantum computing

---

# ⚡ Eksponentiell vekst

* 1 qubit → 2 tilstander
* 2 qubits → 4 tilstander
* 3 qubits → 8 tilstander

👉 Generelt:

* n qubits → 2ⁿ tilstander

Dette gir:

* enorm kompleksitet
* potensielt ekstrem ytelse

---

# 🧪 Sycamore processor

* Utviklet av Google
* Brukt i demonstrasjon av **quantum supremacy**

💡 Viste at en kvantemaskin kunne løse et spesifikt problem raskere enn klassisk supercomputer

---

# 🏆 Quantum Supremacy

Betyr:

> Når en kvantemaskin løser et problem som klassiske maskiner ikke klarer effektivt

⚠️ Viktig:

* Gjelder spesifikke problemer
* Ikke generelt “bedre på alt”

---

# 🤖 AI / ML / DL + Quantum

Mulige bruksområder:

* Optimalisering (porteføljer, logistikk)
* Quantum Machine Learning (QML)
* Kernel-metoder (QSVM)
* Feature mapping i høy dimensjon

Fra Intro 5:

* Quantum kernel → kan forbedre klassifikasjon
* brukes med SVM

💡 For deg:

> Dette er mest relevante området å koble til appen din

---

# 🔐 Kryptering (Cryptography)

Kvante påvirker sikkerhet på to måter:

## Trussel

* Shor's Algorithm kan bryte RSA

## Mulighet

* Kvantesikker kryptografi (Post-Quantum Crypto)
* Quantum Key Distribution (QKD)

💡 Viktig:

> Ikke bruk quantum direkte i auth – bruk post-quantum kryptografi

---

# 🔍 Grover's Algorithm

Brukes til:

* søk i usorterte datasett

Fordel:

* Klassisk: O(n)
* Kvante: O(√n)

👉 Kvadratisk speedup

---

# 🔓 Shor's Algorithm

Brukes til:

* faktorisering av tall

Konsekvens:

* Kan bryte klassisk kryptering (RSA)

---

# 🧊 Qubit Stability (Stabilitet)

Stort problem i dag:

* Qubits mister tilstand (decoherence)
* Krever ekstrem kulde (~ -270°C)
* Feilrate er høy

Dette fører til:

* behov for error correction
* begrenset skala

---

# ⚠️ Nåværende begrensninger

* Få qubits (50–100+ i praksis)
* høy feilrate
* vanskelig å skalere
* fortsatt tidlig teknologi

---

# 🚀 Praktisk retning (for dette prosjektet)

Du bygger nå:

## 1. Fundament

* Qiskit
* circuits
* Docker

## 2. Neste steg

* entanglement (2 qubits)
* flere algoritmer

## 3. Videre

* backend (FastAPI)
* koble til app

## 4. Avansert

* portfolio optimizer (quantum + ML)
* hybrid system

---

# 💡 Viktigste takeaway

* Quantum ≠ erstatning for klassisk
* Quantum = supplement for spesifikke problemer

👉 Størst verdi:

* optimalisering
* ML
* simulering

---

# 📚 Videre research

Søk på:

* quantum circuits
* qiskit tutorials
* quantum kernel methods
* QSVM
* hybrid quantum classical systems

---

# 🧠 Din posisjon nå

Du har:

* ML/DL bakgrunn
* matematikk
* programmering
* første quantum kode

👉 Dette er en ekstremt sterk kombinasjon