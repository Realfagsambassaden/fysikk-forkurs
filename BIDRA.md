# Slik bidrar du – Realfagsambassaden

Takk for at du vil være med! Her er alt du trenger for å skrive et fag.

## 1. Tre måter å redigere på

| Du vil … | Gjør slik |
|---|---|
| Rette en skrivefeil raskt | Åpne fila på github.com og klikk blyanten ✏️. Skriv, og klikk **Commit changes**. |
| Skrive mye i nettleseren | Trykk **punktum (.)** på tastaturet når du er inne i repoet. Da åpnes en full editor (VS Code) i nettleseren. |
| Jobbe på egen maskin | Installer [VS Code](https://code.visualstudio.com) og [Quarto](https://quarto.org/docs/get-started/). Klon repoet (Source Control → Clone Repository). |

## 2. Mappene

```
fag.yml                  – navn, nettsted og status for faget
kapitler/
  01-forste-kapittel/
    index.qmd            – kapittelets forside
    01-eksempelside.qmd  – én side; sorteres etter filnavn
  02-neste-kapittel/ …
bilder/                  – tegninger og figurer
```

## 3. Temaer – viktig!

Alt stoff på nettstedene er ordnet **etter tema**, ikke etter kurs eller universitet. Hver side må derfor si hvilket tema og **undertema** den hører til, øverst i fila:

```yaml
---
title: "Arbeid gjort av en kraft"
tema: arbeid-og-energi
undertema: arbeid
---
```

Hvert tema er delt i noen få undertemaer (se `undertemaer` under temaet i tema.yml). Ekstraoppgaver får `undertema: oppgaver`. Sider om samme undertema på ulike nivåer kobles automatisk sammen, og studentene får en knapp for å bytte nivå.

**Nivå** (`forkurs`, `ingenior` eller `fordypning`) settes for hele faget i `fag.yml` i plattformen. En enkelt side kan overstyre med `niva: fordypning` øverst i fila.

Gyldige temaer står i [tema.yml i plattformen](https://github.com/Realfagsambassaden/Plattform/blob/main/tema.yml), for eksempel `kinematikk`, `newtons-lover`, `arbeid-og-energi`, `hydrostatikk`, `elektrisk-felt`, `kvantefysikk`. Mangler temaet ditt? Si fra, så legger vi det til.

Siden dukker da opp under riktig tema på nettstedet, sammen med alt annet stoff om samme tema. Kurs (som TFY4106 på NTNU) lages som **løyper** på toppen: en rekkefølge av sider fra ulike temaer.

Vi sier «tema», ikke «emne», fordi «emne» også betyr et kurs (emnekode, emnebeskrivelse). De gamle feltnavnene `emne:` og `delemne:` virker fortsatt, men bruk `tema:` og `undertema:`.

## 4. Byggeklosser

Alle eksemplene står i `kapitler/01-forste-kapittel/01-eksempelside.qmd`. Kort oppsummert:

- **Formler:** `$F = ma$` i teksten, `$$ … $$` på egen linje.
- **Video:** `{{< video https://www.youtube.com/watch?v=… >}}`
- **Bokser:** `::: {.callout-note title="Definisjon: …"}` … `:::` (også `callout-tip`, `callout-warning`) og `::: {.eksempel}`.
- **Oppgave med løsning:** `::: {.oppgave tittel="…"}` med en `::: {.losning}` inni. Studentene får «Vis løsning» og «Få et hint» (KI-hint som bruker løsningen din, så skriv gode løsninger).
- **Kjørbar Python:** en kodeblokk som starter med ` ```{.python .kjor}`.

## 5. Stil

- Én idé om gangen. Korte avsnitt, mange figurer.
- Skriv til noen som ikke kan faget fra før. Forklar *hvorfor*, ikke bare *hvordan*.
- Fysikkonstanter og enheter skrives ikke i kursiv.
- Tegninger: Dashman-stil og håndskrift fra iPad passer godt. Lagre som PNG eller WebP.

## 6. Status

Sett `status` i `fag.yml`:

- `skjult` – vises ikke på nettsiden (start her)
- `arbeid` – vises med «Under arbeid»
- `klar` – vises som ferdig

## 7. Rettigheter

Innholdet publiseres av Realfagsambassaden. Avklar lisens og eierskap med plattformansvarlig før du publiserer innhold du har laget i en annen jobb.

Spørsmål? Ta kontakt med plattformansvarlig.
