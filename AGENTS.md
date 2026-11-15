# Instrukser for KI-agenter

Den felles instruksen for alle KI-agenter ligger i plattformen:
**[Realfagsambassaden/Plattform/AGENTS.md](https://github.com/Realfagsambassaden/Plattform/blob/main/AGENTS.md)**. Les den før du gjør noe. Notasjonen følger [Plattform/NOTASJON.md](https://github.com/Realfagsambassaden/Plattform/blob/main/NOTASJON.md).

Det viktigste, kort:

- Endringer går via gren og pull request mot `main`. Alt på `main` publiseres automatisk.
- Hver side har `title`, `tema` og `undertema` øverst (se `tema.yml` i plattformen). Si «tema», ikke «emne» («emne» betyr institusjonens emne, f.eks. IFYA1000). Nivået settes for hele læreboka i plattformens `fag.yml`.
- **Begreper** (se `Plattform/AGENTS.md` §0): dette repoet er en **lærebok** (i koden «fag»). En **løype** er en lesevei for et emne, og et **kurs** er en undervisers semesteropplegg i studieappen. Ordet «fag» brukes bare i vanlig betydning.
- **Skriv kursnøytralt:** aldri «i dette faget», «i denne læreboka», «i kurset», «i pensum», «i kompendiet» eller «i forrige kapittel» på en innholdsside. Vis heller til nivå («På forkursnivå …», «På ingeniørnivå …»).
- Bare lærerens egne videoer (DrNormann). Mangler video: plassholder `<!-- video: kommer (videoer/<side-id>) -->`.
- KI-skrevet stoff merkes `<!-- tillegg: Claude -->`.
