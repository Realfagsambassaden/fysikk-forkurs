// Lager video fra en animasjonsside (anim.html) i en videomappe.
//   node video/_verktoy/lag.js <videomappe> preview "0:6,1:25"   → bilder i <videomappe>/sjekk/ med presentatørsonen markert
//   node video/_verktoy/lag.js <videomappe> render [0,1,...]      → <videomappe>/scener/sN.mp4 og <videomappe>/<mappenavn>.mp4
//
// anim.html må definere window.S = [[scene-id, sekunder], ...] og window.render(sceneIndeks, t),
// og ha et element #sone (skjult) som viser presentatørsonen: x ≥ 1300, y ≥ 420 i et 1920×1080-bilde.
// Ingenting skal tegnes i sonen – der står læreren når videoen spilles inn.
// Ferdige .mp4-filer legges ikke i git (se .gitignore); de sendes til læreren.
const { chromium } = require('playwright');
const { spawn, execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  const [mappeArg, mode, arg] = process.argv.slice(2);
  const DIR = path.resolve(mappeArg);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(DIR, 'anim.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const S = await page.evaluate(() => window.S);

  if (mode === 'preview') {
    fs.mkdirSync(path.join(DIR, 'sjekk'), { recursive: true });
    await page.evaluate(() => (document.getElementById('sone').style.display = 'block'));
    for (const spec of arg.split(',')) {
      const [n, t] = spec.split(':').map(Number);
      await page.evaluate(([n, t]) => window.render(n, t), [n, t]);
      await page.screenshot({ path: path.join(DIR, 'sjekk', `s${n + 1}_${t}.png`) });
    }
  } else {
    const which = arg ? arg.split(',').map(Number) : S.map((_, i) => i);
    const SC = path.join(DIR, 'scener');
    fs.mkdirSync(SC, { recursive: true });
    for (const n of which) {
      const out = path.join(SC, `s${n + 1}.mp4`), tmp = out.replace('.mp4', '.tmp.mp4');
      const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', '30', '-c:v', 'mjpeg', '-i', '-',
        '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '30', tmp]);
      const done = new Promise((res, rej) => ff.on('close', c => (c === 0 ? res() : rej(new Error('ffmpeg ' + c)))));
      const frames = Math.round(S[n][1] * 30);
      for (let f = 0; f < frames; f++) {
        await page.evaluate(([n, t]) => window.render(n, t), [n, f / 30]);
        const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
        if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      }
      ff.stdin.end(); await done; fs.renameSync(tmp, out);
      console.log('ferdig', out, frames, 'bilder');
    }
    const liste = S.map((_, i) => `file '${path.join(SC, `s${i + 1}.mp4`)}'`).join('\n');
    fs.writeFileSync(path.join(SC, 'liste.txt'), liste);
    const ut = path.join(DIR, path.basename(DIR) + '.mp4');
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', path.join(SC, 'liste.txt'), '-c', 'copy', ut]);
    console.log('video:', ut);
  }
  await browser.close();
})();
