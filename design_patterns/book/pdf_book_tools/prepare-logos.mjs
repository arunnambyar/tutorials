import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import puppeteer from "puppeteer";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const logoDir = path.join(__dirname, "assets", "logos");

const SIMPLE_ICONS = {
  ibm: "ibm",
  google: "google",
  amd: "amd",
  airbus: "airbus",
  volkswagen: "volkswagen",
};

async function fetchSimpleIcon(slug) {
  const url = `https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/${slug}.svg`;
  const res = await fetch(url);
  if (!res.ok) throw new Error(`Failed ${slug}: ${res.status}`);
  let svg = await res.text();
  svg = svg.replace(/<path\b/g, '<path fill="#1a1a1a"');
  return svg;
}

const wordmarks = {
  lexisnexis: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 36" width="220" height="36" role="img" aria-label="LexisNexis">
  <text x="0" y="28" font-family="Georgia, 'Times New Roman', serif" font-size="26" font-weight="700" fill="#1a1a1a">LexisNexis</text>
</svg>`,
  globalfoundries: `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 36" width="260" height="36" role="img" aria-label="GlobalFoundries">
  <text x="0" y="27" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="#1a1a1a">GlobalFoundries</text>
</svg>`,
};

fs.mkdirSync(logoDir, { recursive: true });

for (const [name, slug] of Object.entries(SIMPLE_ICONS)) {
  const svg = await fetchSimpleIcon(slug);
  fs.writeFileSync(path.join(logoDir, `${name}.svg`), svg);
  console.log("fetched", name);
}
for (const [name, svg] of Object.entries(wordmarks)) {
  fs.writeFileSync(path.join(logoDir, `${name}.svg`), svg);
  console.log("wrote", name);
}

const chromeCandidates = [
  process.env.PUPPETEER_EXECUTABLE_PATH,
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
].filter(Boolean);
const executablePath = chromeCandidates.find((p) => fs.existsSync(p));
if (!executablePath) throw new Error("Chrome/Edge not found");

const browser = await puppeteer.launch({
  headless: true,
  executablePath,
  args: ["--no-sandbox", "--disable-setuid-sandbox"],
});
const page = await browser.newPage();
await page.setViewport({ width: 900, height: 300, deviceScaleFactor: 3 });

const names = [
  "ibm",
  "lexisnexis",
  "google",
  "amd",
  "globalfoundries",
  "airbus",
  "volkswagen",
];

for (const name of names) {
  const svg = fs.readFileSync(path.join(logoDir, `${name}.svg`), "utf8");
  const dataUrl = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
  const html = `<!doctype html><html><head><style>
    html,body{margin:0;background:transparent;height:100%;}
    body{display:flex;align-items:center;justify-content:center;}
    #l{height:72px;width:auto;max-width:560px;}
  </style></head><body><img id="l" src="${dataUrl}" /></body></html>`;
  await page.setContent(html, { waitUntil: "load", timeout: 60000 });
  await page.waitForFunction(() => {
    const img = document.getElementById("l");
    return img && img.complete && img.naturalWidth > 0;
  });
  await new Promise((r) => setTimeout(r, 150));
  const box = await page.$eval("#l", (el) => {
    const r = el.getBoundingClientRect();
    return { x: r.x, y: r.y, width: r.width, height: r.height };
  });
  const pad = 2;
  await page.screenshot({
    path: path.join(logoDir, `${name}.png`),
    omitBackground: true,
    clip: {
      x: Math.max(0, box.x - pad),
      y: Math.max(0, box.y - pad),
      width: Math.ceil(box.width + pad * 2),
      height: Math.ceil(box.height + pad * 2),
    },
  });
  console.log(`${name} png ${Math.round(box.width)}x${Math.round(box.height)}`);
}

await browser.close();
