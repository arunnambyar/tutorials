import puppeteer from "puppeteer";
import path from "path";
import fs from "fs";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dir = path.resolve(
  __dirname,
  "../../../cloud/static/1010_accounts_subscriptions_projects"
);
const name = "cloud_structure_tree";
const svg = fs.readFileSync(path.join(dir, `${name}.svg`), "utf8");
const match = svg.match(/width="(\d+)"\s+height="(\d+)"/);
const browser = await puppeteer.launch({
  headless: true,
  executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
});
const page = await browser.newPage();
await page.setViewport({
  width: Number(match[1]),
  height: Number(match[2]),
  deviceScaleFactor: 2,
});
await page.setContent(
  `<!DOCTYPE html><html><head><style>html,body{margin:0;padding:0;background:#fff}</style></head><body>${svg}</body></html>`,
  { waitUntil: "networkidle0" }
);
const pngPath = path.join(dir, `${name}.png`);
await (await page.$("svg")).screenshot({ path: pngPath, omitBackground: false });
await browser.close();
console.log("Wrote", pngPath, fs.statSync(pngPath).size);
