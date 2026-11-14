# Mal for ny lærebok – Realfagsambassaden

Dette er utgangspunktet for nytt stoff på fysikkhjelp.no, matematikkhjelp.no, kjemihjelp.no eller biologihjelp.no.

**Slik starter du en ny lærebok:**

1. Klikk den grønne knappen **Use this template → Create a new repository** øverst på denne siden.
   Velg eier **Realfagsambassaden** og gi repoet et navn som `fysikk-mekanikk` eller `matte-kalkulus1`.
2. Fyll ut `fag.yml` (navn, nettsted, kortnavn, status).
3. Skriv sidene i `kapitler/`, og merk hver side med hvilket **tema** og **undertema** den hører til (`tema:` og `undertema:` øverst i fila). Se `kapitler/01-forste-kapittel/01-eksempelside.qmd` for alt du kan bruke.
4. Be plattformansvarlig legge læreboka inn i `fag.yml` i plattform-repoet (én linje), og sett `status: arbeid` eller `klar` når du vil at det skal vises.

Hver gang du lagrer (commit + push) på `main`, oppdateres nettsiden av seg selv etter noen minutter.

Les **[BIDRA.md](BIDRA.md)** for en fullstendig guide.
