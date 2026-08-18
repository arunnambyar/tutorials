import puppeteer from "puppeteer";
import path from "path";
import fs from "fs";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dir = path.resolve(
  __dirname,
  "../../../cloud/aws/static/1010_accounts_organizations"
);
const names = [
  "01_root_ou",
  "02_management_account",
  "03_multiple_ous",
  "04_multiple_accounts",
  "05_full_picture",
];

const browser = await puppeteer.launch({
  headless: true,
  executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
});

for (const name of names) {
  const svgPath = path.join(dir, `${name}.svg`);
  const pngPath = path.join(dir, `${name}.png`);
  const svg = fs.readFileSync(svgPath, "utf8");
  const match = svg.match(/width="(\d+)"\s+height="(\d+)"/);
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
  await (await page.$("svg")).screenshot({ path: pngPath, omitBackground: false });
  await page.close();
  console.log("Wrote", pngPath, fs.statSync(pngPath).size);
}

await browser.close();
