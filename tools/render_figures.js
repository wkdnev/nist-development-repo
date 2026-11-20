// Render figures/src/<name>.html to figures/<name>.png (the first <svg> element).
// Usage: node tools/render_figures.js [name ...]   (no names = all)
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const root = path.join(__dirname, '..', 'figures');
  let names = process.argv.slice(2);
  if (!names.length) names = fs.readdirSync(path.join(root, 'src')).filter(f => f.endsWith('.html')).map(f => f.slice(0, -5));
  const browser = await chromium.launch();
  const page = await browser.newPage({ deviceScaleFactor: 1 });
  for (const n of names) {
    await page.goto('file://' + path.join(root, 'src', n + '.html'));
    await (await page.$('svg')).screenshot({ path: path.join(root, n + '.png') });
    console.log('rendered', n);
  }
  await browser.close();
})();
