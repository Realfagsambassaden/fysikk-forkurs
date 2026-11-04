# Videoer

Hver emneside får en video på 2–3 minutter (maks 5). Assistenten lager en **videopakke**:

- `manus.md`: manus til innlesing (ca. 140 ord i minuttet) med tidskoder for hva som skjer på skjermen.
- `anim.html`: animasjonen, i tavlestilen fra fysikkhjelp.no.
- en ferdig `.mp4` uten lyd. Den sendes til læreren og lagres ikke i git.

Læreren leser inn manuset og står selv i bildet **nede i høyre hjørne**. Sonen fra x = 1300 og y = 420 i et 1920×1080-bilde (ca. nederste høyre tredjedel) er alltid tom i animasjonen. Den ferdige videoen lastes opp til YouTube og legges inn på siden med `{{< video https://www.youtube.com/watch?v=… >}}`.

## Mapper

```
video/
  _verktoy/        felles: lag.js, fonter, tavlebakgrunn, logo
  01-hva-er-fysikk/  én mappe per side: anim.html, manus.md, bilder til animasjonen
```

Mappenavnet er `<kapittelnr>-<sidenavn>`, f.eks. `07-02-konstant-akselerasjon` for side 02 i kapittel 07. Første kapittel bruker bare kapittelnummeret fordi det er en innledning.

## Lage videoen

Krever Node med Playwright (Chromium) og ffmpeg.

```
node video/_verktoy/lag.js video/01-hva-er-fysikk preview "0:8,3:38"   # stillbilder med sonen markert, i sjekk/
node video/_verktoy/lag.js video/01-hva-er-fysikk render               # hele videoen
```

## Regler for animasjonen

- 1920×1080, 30 bilder/s. Én scene per avsnitt i manuset, med myk inn- og uttoning (0,4 s).
- Ingenting i presentatørsonen, heller ikke bevegelige ting som passerer gjennom den.
- Farger og skrift som på nettstedet: tavle `#0d1110`, kritt `#ecefe6`, grønn `#6ef04a`, oransje `#f19c2c`, gul `#eee462`, turkis `#56d7b8`. Overskrifter i Montserrat, resten i Comic Neue. Logoen øverst til høyre.
- Formler tegnes som bilder med matplotlib (mathtext, `cm`) med norsk notasjon: desimalkomma, enheter oppreist.
- Tidspunktene i `render()` skal følge tidskodene i manuset.
- Se stillbilder av de travleste øyeblikkene før hele videoen lages.
