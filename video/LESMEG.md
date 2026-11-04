# Videoer

Hver emneside får en video på 2–3 minutter (maks 5). Videoene lages i en **egen videochat** (ferdigheten `fysikkhjelp-video`), ikke av nattjobben.

## Arbeidsflyt

1. **Nattjobben** lager siden og legger inn en plassholder der videoen skal stå:
   ```
   <!-- video: kommer (manus i video/<mappe>/manus.md) -->
   ![Video kommer](../../bilder/video-kommer.png){fig-alt="Video kommer"}
   ```
2. **Videochatten** lager videopakken sammen med læreren:
   - `manus.md`: manus til innlesing (ca. 140 ord i minuttet) med tidskoder for hva som skjer på skjermen.
   - `anim.html`: animasjonen, i tavlestilen fra fysikkhjelp.no.
   - en ferdig `.mp4` uten lyd. Den sendes til læreren og lagres ikke i git.
3. **Læreren** leser inn manuset og står selv i bildet **nede i høyre hjørne**, og laster opp til YouTube. Sonen fra x = 1300 og y = 420 i et 1920×1080-bilde (ca. nederste høyre tredjedel) er alltid tom i animasjonen.
4. **Videochatten** legger YouTube-lenken inn i `video/ferdige.yml` (`<mappe>: <lenke>`).
5. **Nattjobben** bytter plassholderen (begge linjene) ut med `{{< video <lenke> >}}` på siden. Først da vises videoen.

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
- Formler tegnes som bilder med matplotlib (mathtext, `cm`). Manus og formler følger [notasjonsreglene](https://github.com/Realfagsambassaden/Plattform/blob/main/NOTASJON.md): naturkonstanter oppreist (`\mathrm{g}`), g = 9,81 m/s², desimalkomma og gjeldende siffer.
- Tidspunktene i `render()` skal følge tidskodene i manuset.
- Se stillbilder av de travleste øyeblikkene før hele videoen lages.
