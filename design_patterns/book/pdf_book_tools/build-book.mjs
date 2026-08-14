import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "marked";
import puppeteer from "puppeteer";
import { PDFDocument } from "pdf-lib";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "../.."); // design_patterns/
const OUT_DIR = path.join(__dirname, "out");
const PDF_DIR = path.resolve(__dirname, "../pdf");
const CSS_PATH = path.join(__dirname, "styles", "book.css");

const BOOK = {
  title: "Design Pattern: The Art of Composing Solutions",
  titleLead: "Design Pattern",
  titleRestLines: ["The Art of Composing", "Solutions"],
  shortTitle: "Design Pattern",
  subtitle:
    "When, Why, and Which One: The Developer's Guide to Choosing the Right Pattern",
  version: "1.0.0",
  author: "Arun Mangatt",
  role: "Software Architect",
};

/** Reading order with humorous chapter openers */
const CHAPTERS = [
  {
    file: "README.md",
    base: ROOT,
    part: "Introduction",
    label: "Intro",
    quote: "If cars, factories, and class diagrams keep showing up in one book—relax. You’re in the right garage.",
  },
  {
    file: "docs/index.md",
    base: ROOT,
    part: "Overview",
    label: "Contents map",
    quote: "A map is not the journey—but without one, you’ll still refactor in circles.",
  },
  {
    file: "docs/1000_singleton.md",
    base: ROOT,
    part: "Creational POV",
    label: "Singleton",
    quote: "There can be only one. Please stop calling new in a loop.",
  },
  {
    file: "docs/1100_prototype.md",
    base: ROOT,
    part: "Creational POV",
    label: "Prototype",
    quote: "Why reinvent the wheel when you can clone the whole car and change the paint?",
  },
  {
    file: "docs/1200_factory_method.md",
    base: ROOT,
    part: "Creational POV",
    label: "Factory Method",
    quote: "Don’t ask what you get—ask which factory is on shift today.",
  },
  {
    file: "docs/1210_simple_factory.md",
    base: ROOT,
    part: "Creational POV",
    label: "Simple Factory",
    quote: "One counter, many products. Like a cafeteria—except the food compiles.",
  },
  {
    file: "docs/1220_factory_method_gof.md",
    base: ROOT,
    part: "Creational POV",
    label: "Factory Method (GoF)",
    quote: "When your parent class doesn’t know the child’s type, but still insists on raising it.",
  },
  {
    file: "docs/1300_abstract_factory.md",
    base: ROOT,
    part: "Creational POV",
    label: "Abstract Factory",
    quote: "Matching sets only. No sedan doors on an SUV chassis—your future self says thanks.",
  },
  {
    file: "docs/1400_builder.md",
    base: ROOT,
    part: "Creational POV",
    label: "Builder",
    quote: "Rome wasn’t built in one constructor call. Neither was this object.",
  },
  {
    file: "docs/1500_adapter.md",
    base: ROOT,
    part: "Structural POV",
    label: "Adapter",
    quote: "The universal travel plug of software—ugly, useful, and somehow always in your bag.",
  },
  {
    file: "docs/1510_python_decorator.md",
    base: ROOT,
    part: "Structural POV",
    label: "Python @decorator vs Patterns",
    quote: "Same word, different universe. Python’s @ is not GoF’s tuxedo.",
  },
  {
    file: "docs/1600_composite.md",
    base: ROOT,
    part: "Structural POV",
    label: "Composite",
    quote: "Treat one leaf like a forest—then wonder why your recursion needs coffee.",
  },
  {
    file: "docs/1610_composite_gof.md",
    base: ROOT,
    part: "Structural POV",
    label: "GoF Composite",
    quote: "Folders containing folders containing ‘final_final_v3’. Nature is healing.",
  },
  {
    file: "docs/1700_proxy.md",
    base: ROOT,
    part: "Structural POV",
    label: "Proxy",
    quote: "I’ll take the meeting for the real object. It’s busy—or shy—or expensive.",
  },
  {
    file: "docs/1800_facade.md",
    base: ROOT,
    part: "Structural POV",
    label: "Facade",
    quote: "One friendly button. Behind it: twelve subsystems arguing in the parking lot.",
  },
  {
    file: "docs/1900_bridge.md",
    base: ROOT,
    part: "Structural POV",
    label: "Bridge",
    quote: "Decouple so thoroughly that even your abstractions start dating other implementations.",
  },
  {
    file: "docs/1910_bridge_vs_abstract_factory.md",
    base: ROOT,
    part: "Structural POV",
    label: "Bridge vs Abstract Factory",
    quote: "Two patterns walk into a bar. One makes families; the other refuses to settle.",
  },
  {
    file: "docs/2000_decorator.md",
    base: ROOT,
    part: "Structural POV",
    label: "Decorator",
    quote: "Wrap it. Wrap the wrap. Ship it. Call it ‘layered architecture’ on the résumé.",
  },
  {
    file: "docs/2100_template_method.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Template Method",
    quote: "The skeleton stays. You only get to customize the elbows.",
  },
  {
    file: "docs/2200_observer.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Observer",
    quote: "When something changes, tell everyone. Then wonder why your inbox is on fire.",
  },
  {
    file: "docs/2300_strategy.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Strategy",
    quote: "Eco, Sport, or Comfort—same steering wheel, different personality disorders.",
  },
  {
    file: "docs/2310_strategy_vs_bridge.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Strategy vs Bridge",
    quote: "They look alike at a glance. Like twins—until one starts swapping algorithms mid-drive.",
  },
  {
    file: "docs/2400_command.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Command",
    quote: "Press button. Receive bacon—or start the engine. Intent packaged as an object.",
  },
  {
    file: "docs/2500_state.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "State",
    quote: "The object woke up as Idle and went to bed as Driving. Mood swings, but documented.",
  },
  {
    file: "docs/2600_iterator.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Iterator",
    quote: "Next, next, next—until is_done. The playlist of data structures.",
  },
  {
    file: "docs/2700_interpreter.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Interpreter",
    quote: "Rain OR fog? The car understands. Your regex still doesn’t.",
  },
  {
    file: "docs/2800_chain_of_responsibility.md",
    base: ROOT,
    part: "Behavioral POV",
    label: "Chain of Responsibility",
    quote: "Not my ticket—pass it along. Corporate workflow, now with pointers.",
  },
  {
    file: "docs/9000_summary_design_patterns.md",
    base: ROOT,
    part: "Summary",
    label: "Design Patterns Summary",
    quote: "If you skipped ahead for the pictures: welcome. The spoilers are educational.",
  },
];

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".webp": "image/webp",
  ".md": "text/markdown; charset=utf-8",
};

function toWebPath(absPath) {
  const rel = path.relative(ROOT, absPath).split(path.sep).join("/");
  return "/" + rel;
}

function preprocessMarkdown(raw, chapterDir, mermaidBlocks) {
  let md = raw;

  md = md.replace(/<p\s+align=["']right["']>[\s\S]*?<\/p>/gim, "");
  md = md.replace(
    />\s*\[!NOTE\]\s*\n((?:>.*(?:\n|$))+)/gim,
    (_, body) => {
      const text = body
        .split("\n")
        .map((line) => line.replace(/^>\s?/, ""))
        .join("\n")
        .trim();
      return `<blockquote class="note">\n\n${text}\n\n</blockquote>\n`;
    }
  );

  md = md.replace(
    /<p align="center">\s*([\s\S]*?)\s*<\/p>/gim,
    (_, inner) => `<div class="img-row">${inner}</div>`
  );

  // Drop fixed HTML width/height so CSS can fit images on the page
  md = md.replace(/\s(width|height)\s*=\s*["'][^"']*["']/gim, "");
  md = md.replace(/\s(width|height)\s*=\s*[^\s>]+/gim, "");

  md = md.replace(
    /(<img\b[^>]*\bsrc=["'])([^"']+)(["'][^>]*>)/gim,
    (full, pre, src, post) => {
      if (/^(https?:|data:)/i.test(src)) return full;
      const abs = path.resolve(chapterDir, src);
      return `${pre}${toWebPath(abs)}${post}`;
    }
  );

  md = md.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (full, alt, src) => {
    const cleaned = src.trim().replace(/^<|>$/g, "");
    if (/^(https?:|data:)/i.test(cleaned)) return full;
    const abs = path.resolve(chapterDir, cleaned);
    return `![${alt}](${toWebPath(abs)})`;
  });

  // Extract mermaid BEFORE marked.parse — marked breaks HTML <pre> on blank lines
  md = md.replace(/```mermaid\s*([\s\S]*?)```/gim, (_, code) => {
    const kind = /sequenceDiagram/i.test(code)
      ? "sequence"
      : /classDiagram/i.test(code)
        ? "class"
        : "diagram";
    const id = mermaidBlocks.length;
    mermaidBlocks.push({ code: code.trim(), kind });
    return `\n\n<div class="mermaid-slot" data-mermaid-id="${id}"></div>\n\n`;
  });

  return md;
}

function mermaidFigureHtml(code, kind) {
  const escaped = code
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
  return `<figure class="book-figure" data-fig-kind="${kind}"><pre class="mermaid">${escaped}</pre></figure>`;
}

function restoreMermaidPlaceholders(html, mermaidBlocks) {
  return html.replace(
    /<div class="mermaid-slot" data-mermaid-id="(\d+)"\s*><\/div>/g,
    (_, id) => {
      const block = mermaidBlocks[Number(id)];
      if (!block) return "";
      return mermaidFigureHtml(block.code, block.kind);
    }
  );
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function buildChapterHrefMap() {
  const map = new Map();
  CHAPTERS.forEach((ch, i) => {
    map.set(path.basename(ch.file), `#ch-${i + 1}`);
  });
  return map;
}

function hrefForDoc(file, hrefMap) {
  const base = path.basename(String(file).split("#")[0]);
  return hrefMap.get(base) || "#";
}

/** Overview page: all three POVs with internal chapter links (PDF-safe). */
function renderOverviewBody(hrefMap) {
  const sections = [
    {
      title: "1. Creational POV",
      tagline: "How the car is built",
      blurb:
        "These patterns deal with object creation mechanisms, aiming to make the process more flexible and reusable.",
      rows: [
        ["Singleton", "1000_singleton.md", "Only one engine control unit (ECU) exists—shared across the system."],
        ["Prototype", "1100_prototype.md", "Clone and update an existing car design to make a new car design."],
        ["Factory Method", "1200_factory_method.md", "A car factory decides which model to produce based on order type."],
        ["Simple Factory", "1210_simple_factory.md", "A single factory creates products from a parameter or type."],
        ["Factory Method (GoF)", "1220_factory_method_gof.md", "Classic Creator/Product factorization from the GoF catalog."],
        ["Abstract Factory", "1300_abstract_factory.md", "A manufacturer picks sedan or SUV factory line and gets matching parts."],
        ["Builder", "1400_builder.md", "Build a car step-by-step: chassis, engine, electrics, paint."],
      ],
    },
    {
      title: "2. Structural POV",
      tagline: "How the spare parts are organized",
      blurb:
        "These patterns focus on how classes and objects are composed to form larger structures.",
      rows: [
        ["Adapter", "1500_adapter.md", "Like an adapter between an Indian plug and a European socket."],
        ["Python @decorator vs Patterns", "1510_python_decorator.md", "How Python decorators relate to Adapter and Decorator—and why they differ."],
        ["Composite", "1600_composite.md", "Comment threads—one node class; empty children means leaf."],
        ["GoF Composite", "1610_composite_gof.md", "Classic Leaf + Composite split—folder and file tree."],
        ["Proxy", "1700_proxy.md", "A stand-in that controls access to a real subject."],
        ["Facade", "1800_facade.md", "One friendly interface over several subsystems."],
        ["Bridge", "1900_bridge.md", "Decouples abstraction from implementation so both can vary."],
        ["Bridge vs Abstract Factory", "1910_bridge_vs_abstract_factory.md", "When you need matched families versus two independent hierarchies."],
        ["Decorator", "2000_decorator.md", "Wraps an object to extend behavior without changing its class."],
      ],
    },
    {
      title: "3. Behavioral POV",
      tagline: "How the car behaves while driving",
      blurb:
        "These patterns manage algorithms, relationships, and responsibilities between objects.",
      rows: [
        ["Template Method", "2100_template_method.md", "A fixed skeleton of steps with customizable hooks."],
        ["Observer", "2200_observer.md", "Sensors notify listeners when something changes."],
        ["Strategy", "2300_strategy.md", "Swap eco, sport, or comfort behavior at runtime."],
        ["Strategy vs Bridge", "2310_strategy_vs_bridge.md", "Behavior swap versus two growing hierarchies."],
        ["Command", "2400_command.md", "Package an action as an object the invoker can run."],
        ["State", "2500_state.md", "Behavior changes with the object’s current state."],
        ["Iterator", "2600_iterator.md", "Walk a collection without exposing its structure."],
        ["Interpreter", "2700_interpreter.md", "Evaluate simple language rules (for example rain OR fog)."],
        ["Chain of Responsibility", "2800_chain_of_responsibility.md", "Pass a request along handlers until one handles it."],
      ],
    },
    {
      title: "4. Summary",
      tagline: "All patterns at a glance",
      blurb: "Class and sequence diagram summary for the patterns above.",
      rows: [
        ["Design Patterns Summary", "9000_summary_design_patterns.md", "PNG class and sequence diagrams for every pattern in this book."],
      ],
    },
  ];

  const povImg = "/static/images/index/pov1.png";
  const [creational, structural, behavioral, summary] = sections;

  function sectionHtml(section, extraClass = "") {
    let rows = "";
    for (const [name, file, analogy] of section.rows) {
      const href = hrefForDoc(file, hrefMap);
      rows += `<tr>
  <td><a href="${href}"><strong>${escapeHtml(name)}</strong></a></td>
  <td>${escapeHtml(analogy)}</td>
</tr>`;
    }
    return `
<section class="pov-section ${extraClass}">
  <h2>${escapeHtml(section.title)}</h2>
  <p class="pov-tagline"><em>“${escapeHtml(section.tagline)}”</em></p>
  <p>${escapeHtml(section.blurb)}</p>
  <div class="table-wrap">
    <table class="pov-table">
      <thead>
        <tr><th>Pattern</th><th>Car analogy</th></tr>
      </thead>
      <tbody>
${rows}
      </tbody>
    </table>
  </div>
</section>`;
  }

  return `
<div class="pov-intro-page">
  <h1>Different types of Design Patterns</h1>
  <p>Here onwards we call this <code>Design Patterns From Different Points Of View</code> (or POV), rather than only “different types of design patterns.”</p>
  <figure class="book-figure pov-hero-figure">
    <img class="pov-hero-img" src="${povImg}" alt="Points of view on design patterns">
    <figcaption>Fig: Points of view on design patterns</figcaption>
  </figure>
</div>
${sectionHtml(creational, "pov-page-start")}
${sectionHtml(structural, "pov-page-start")}
${sectionHtml(behavioral, "pov-page-start")}
${sectionHtml(summary, "pov-summary-continue")}
`;
}

function renderChapterHtml(chapter, index, hrefMap) {
  const abs = path.join(chapter.base, chapter.file);
  if (!fs.existsSync(abs)) {
    console.warn(`Missing chapter: ${chapter.file}`);
    return "";
  }

  let body;
  if (chapter.file.replace(/\\/g, "/") === "docs/index.md") {
    body = renderOverviewBody(hrefMap);
  } else {
    const dir = path.dirname(abs);
    const raw = fs.readFileSync(abs, "utf8");
    const mermaidBlocks = [];
    const md = preprocessMarkdown(raw, dir, mermaidBlocks);
    body = marked.parse(md, { async: false });
    body = restoreMermaidPlaceholders(body, mermaidBlocks);
    body = body
      .replace(/<table>/g, '<div class="table-wrap"><table>')
      .replace(/<\/table>/g, "</table></div>");
    // Rewrite relative .md links to in-book chapter anchors when possible
    body = body.replace(
      /href="([^"]+\.md)(#[^"]*)?"/g,
      (full, file) => {
        const href = hrefForDoc(file, hrefMap);
        return href === "#" ? full : `href="${href}"`;
      }
    );
  }

  const opener = chapter.quote
    ? `<section class="chapter-opener-page" id="opener-${index}">
  <blockquote class="chapter-quote">
    <span class="quote-mark">Chapter opener</span>
    ${escapeHtml(chapter.quote)}
  </blockquote>
</section>`
    : "";
  return `
${opener}
<section class="chapter" id="ch-${index}">
  <div class="chapter-label">${escapeHtml(chapter.part)} · ${String(index).padStart(2, "0")}</div>
  ${body}
</section>`;
}

function buildTocHtml(chapters) {
  const parts = [];
  let currentPart = null;
  let n = 0;
  for (const ch of chapters) {
    n += 1;
    if (ch.part !== currentPart) {
      if (currentPart !== null) parts.push("</ol>");
      currentPart = ch.part;
      parts.push(`<div class="toc-section">${escapeHtml(currentPart)}</div><ol>`);
    }
    parts.push(
      `<li><a class="toc-link" href="#ch-${n}"><span class="num">${String(n).padStart(2, "0")}</span> ${escapeHtml(ch.label)}</a></li>`
    );
  }
  if (currentPart !== null) parts.push("</ol>");
  return parts.join("\n");
}

const ABOUT_LOGOS = [
  { file: "ibm", alt: "IBM" },
  { file: "lexisnexis", alt: "LexisNexis" },
  { file: "google", alt: "Google" },
  { file: "amd", alt: "AMD" },
  { file: "globalfoundries", alt: "GlobalFoundries" },
  { file: "airbus", alt: "Airbus" },
  { file: "volkswagen", alt: "Volkswagen" },
];

function logoDataUri(fileBase) {
  const logoDir = path.join(__dirname, "assets", "logos");
  const pngPath = path.join(logoDir, `${fileBase}.png`);
  const svgPath = path.join(logoDir, `${fileBase}.svg`);
  if (fs.existsSync(pngPath)) {
    const b64 = fs.readFileSync(pngPath).toString("base64");
    return `data:image/png;base64,${b64}`;
  }
  if (fs.existsSync(svgPath)) {
    let svg = fs.readFileSync(svgPath, "utf8");
    if (!/\sfill=/.test(svg)) {
      svg = svg.replace(/<path\b/g, '<path fill="#1a1a1a"');
      svg = svg.replace(/<svg\b/, '<svg fill="#1a1a1a"');
    }
    return `data:image/svg+xml;charset=utf-8,${encodeURIComponent(svg)}`;
  }
  throw new Error(`Missing logo asset: ${fileBase}`);
}

function buildAboutLogoStrip() {
  return ABOUT_LOGOS.map(
    ({ file, alt }) =>
      `        <li><img src="${logoDataUri(file)}" alt="${escapeHtml(alt)}" height="32" /></li>`
  ).join("\n");
}

function buildHtml(chapterHtml, tocHtml, cssText) {
  const year = new Date().getFullYear();
  const coverSrc = "/book/pdf_book_tools/assets/cover_design_patterns.png";
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>${escapeHtml(BOOK.title)} — ${escapeHtml(BOOK.author)}</title>
  <style>${cssText}</style>
  <script src="/book/pdf_book_tools/node_modules/mermaid/dist/mermaid.min.js"></script>
</head>
<body>
  <section class="cover">
    <div class="cover-top">
      <p class="cover-series">Software Architecture</p>
      <h1 class="cover-title">
        <span class="cover-title-lead">${escapeHtml(BOOK.titleLead)}</span>
        <span class="cover-title-rest">${BOOK.titleRestLines.map((line) => `<span class="cover-title-line">${escapeHtml(line)}</span>`).join("")}</span>
      </h1>
      <p class="version">Version ${escapeHtml(BOOK.version)}</p>
      <p class="subtitle">${escapeHtml(BOOK.subtitle)}</p>
    </div>
    <div class="cover-photo-wrap">
      <img class="cover-photo" src="${coverSrc}" alt="Vehicle parts composing a complete vehicle — the art of composing solutions" />
    </div>
    <div class="cover-bottom">
      <div class="cover-author-only">
        <p class="by-line">Author</p>
        <p class="name">${escapeHtml(BOOK.author)}</p>
      </div>
      <p class="cover-year">${year}</p>
    </div>
  </section>

  <section class="front-matter about-author">
    <h2>About the Author</h2>
    <p class="about-author-body">
      <span class="about-author-name">${escapeHtml(BOOK.author)}</span> is a Software Architect who has spent more than twenty years
      designing and building software with care—for the systems, for the teams, and for the
      people who live with the code afterward.
    </p>
    <div class="about-orgs">
      <p class="about-orgs-label">Worked with</p>
      <ul class="about-logo-grid" aria-label="Organizations">
${buildAboutLogoStrip()}
      </ul>
    </div>
  </section>

  <section class="front-matter preface">
    <h2>Preface</h2>

    <p>
      Software is written for people. Machines only run it.
    </p>
    <p>
      Early in a career, most of us are happy when the code works.
      Later, we notice something else: a change in one place breaks another,
      simple requests take too long, and the next person—or our future selves—
      struggles to understand what we meant.
    </p>
    <p>
      That is usually when design patterns begin to matter.
      Not as fashion. Not as a list to memorize.
      They matter when we need a clear way to shape code so it can grow
      without becoming fragile.
    </p>
    <p>
      This book is a quiet guide for that moment.
      It walks through the classic patterns with plain language,
      everyday pictures, simple diagrams, and small Python examples.
      For each one, it asks the questions that matter in real work:
      when to use it, why it helps, and how to tell it apart from patterns
      that look similar.
    </p>
    <p>
      You do not need to read every chapter in order.
      Start with the overview if you want the map.
      Open a pattern when a problem is already on your desk.
      Return to the comparisons when two choices feel too close.
    </p>
    <p>
      If this book helps you choose with a little more care—
      and write code that is kinder to the next reader—
      it has done its work.
    </p>
    <p class="preface-signoff">— ${escapeHtml(BOOK.author)}</p>
  </section>

  <section class="front-matter toc" id="contents">
    <h2>Contents</h2>
    ${tocHtml}
  </section>

  ${chapterHtml}

  <script>
    (async function () {
      try {
        mermaid.initialize({
          startOnLoad: false,
          theme: "neutral",
          securityLevel: "loose",
          fontFamily: "Segoe UI, Helvetica Neue, Arial, sans-serif",
          themeVariables: {
            fontSize: "14px",
          },
          flowchart: { useMaxWidth: true, htmlLabels: true },
          sequence: { useMaxWidth: true, mirrorActors: false },
        });
        const nodes = Array.from(document.querySelectorAll("pre.mermaid"));
        for (let i = 0; i < nodes.length; i++) {
          try {
            await mermaid.run({ nodes: [nodes[i]] });
          } catch (err) {
            nodes[i].insertAdjacentHTML(
              "afterend",
              '<p style="color:#b45309;font-size:9pt;">Diagram could not be rendered.</p>'
            );
            console.warn("mermaid failed", i, err);
          }
          if (i % 5 === 0) await new Promise((r) => setTimeout(r, 0));
        }
      } finally {
        document.documentElement.setAttribute("data-mermaid-ready", "true");
      }
    })();
  </script>
</body>
</html>`;
}

function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      try {
        const urlPath = decodeURIComponent((req.url || "/").split("?")[0]);
        const safe = path.normalize(urlPath).replace(/^(\.\.[/\\])+/, "");
        const abs = path.join(ROOT, safe);
        if (!abs.startsWith(ROOT) || !fs.existsSync(abs) || fs.statSync(abs).isDirectory()) {
          res.writeHead(404);
          res.end("Not found");
          return;
        }
        const ext = path.extname(abs).toLowerCase();
        res.writeHead(200, { "Content-Type": MIME[ext] || "application/octet-stream" });
        fs.createReadStream(abs).pipe(res);
      } catch {
        res.writeHead(500);
        res.end("Error");
      }
    });
    server.listen(0, "127.0.0.1", () => {
      const { port } = server.address();
      resolve({ server, port });
    });
  });
}

async function fitFigures(page) {
  await page.evaluate(() => {
    const maxH = "72mm";
    const seqMaxH = "144mm";
    const rowMaxH = "32mm";

    function captionFromSrc(src) {
      const file = (src || "").split("/").pop() || "";
      const name = file.replace(/\.[^.]+$/, "").replace(/[_-]+/g, " ");
      if (/bus\.png|car\.png|truck\.png/i.test(src)) {
        return "Familiar vehicles that share a common underlying design pattern.";
      }
      if (/pov1/i.test(src)) {
        return "Points of view on design patterns.";
      }
      if (/structure\.png/i.test(src) && /bridge_vs_abstract/i.test(src)) {
        return "Side-by-side structure: Abstract Factory builds matched families; Bridge keeps abstraction and implementation separate.";
      }
      if (/when_to_choose/i.test(src)) {
        return "A quick guide for choosing Abstract Factory or Bridge when both seem plausible.";
      }
      if (/strategy_shape/i.test(src)) {
        return "Strategy shape: a context holds a strategy and swaps behavior at runtime.";
      }
      if (/bridge_shape/i.test(src)) {
        return "Bridge shape: two hierarchies evolve independently through an implementer reference.";
      }
      if (/invoker_commands_engine/i.test(src)) {
        return "Command flow: the invoker stores a command, then runs it against the receiver.";
      }
      if (/_class(\.png)?$/i.test(file) || /\bclass\b/i.test(name)) {
        return `${name.replace(/\bclass\b/i, "").trim() || "Pattern"} class diagram—roles and relationships at a glance.`;
      }
      if (/_sequence(\.png)?$/i.test(file) || /\bsequence\b/i.test(name)) {
        return `${name.replace(/\bsequence\b/i, "").trim() || "Pattern"} sequence diagram—how objects collaborate over time.`;
      }
      return name
        ? `${name.charAt(0).toUpperCase()}${name.slice(1)} illustrated for this chapter.`
        : "Supporting illustration for this chapter.";
    }

    function mermaidCaption(kind) {
      if (kind === "class") {
        return "Class diagram — key types and how they connect.";
      }
      if (kind === "sequence") {
        return "Sequence diagram — the typical call flow between participants.";
      }
      return "Diagram summarizing the idea in this section.";
    }

    function ensureCaption(figure, text) {
      let cap = figure.querySelector("figcaption");
      if (!cap) {
        cap = document.createElement("figcaption");
        figure.appendChild(cap);
      }
      cap.textContent = `Fig: ${text}`;
    }

    function wrapAsFigure(node, text) {
      if (node.closest("figure.book-figure")) {
        ensureCaption(node.closest("figure.book-figure"), text);
        return;
      }
      const figure = document.createElement("figure");
      figure.className = "book-figure";
      node.parentNode.insertBefore(figure, node);
      figure.appendChild(node);
      ensureCaption(figure, text);
    }

    // Multi-image rows → one figure + one caption
    document.querySelectorAll(".img-row").forEach((row) => {
      const imgs = [...row.querySelectorAll("img")];
      imgs.forEach((img) => {
        img.removeAttribute("width");
        img.removeAttribute("height");
        img.style.maxWidth = "28%";
        img.style.maxHeight = rowMaxH;
        img.style.height = "auto";
        img.style.objectFit = "contain";
      });
      const alt = imgs.map((i) => i.getAttribute("alt") || "").find((a) => a.trim());
      const src = imgs[0] ? imgs[0].getAttribute("src") || "" : "";
      wrapAsFigure(row, alt || captionFromSrc(src));
    });

    document.querySelectorAll(".pov-hero-img, .pov-hero-figure img").forEach((img) => {
      img.removeAttribute("width");
      img.removeAttribute("height");
      img.style.maxWidth = "95%";
      img.style.width = "auto";
      img.style.maxHeight = "175mm";
      img.style.height = "auto";
      img.style.objectFit = "contain";
    });

    // Standalone images (not cover, not already in a row figure)
    document.querySelectorAll("img:not(.cover-photo):not(.pov-hero-img)").forEach((img) => {
      if (
        img.closest(".img-row") ||
        img.closest(".cover") ||
        img.closest(".pov-hero-figure") ||
        img.closest(".about-logo-grid")
      ) {
        return;
      }
      img.removeAttribute("width");
      img.removeAttribute("height");
      const alt = (img.getAttribute("alt") || "").trim();
      const src = img.getAttribute("src") || "";
      const isSequence =
        /sequence/i.test(alt) || /_sequence(\.png)?$/i.test(src.split("/").pop() || "");
      const isClass =
        /class/i.test(alt) || /_class(\.png)?$/i.test(src.split("/").pop() || "");
      img.style.maxWidth = isSequence ? "92%" : "78%";
      img.style.width = "auto";
      img.style.maxHeight = isSequence ? seqMaxH : maxH;
      img.style.height = "auto";
      img.style.objectFit = "contain";
      wrapAsFigure(img, alt || captionFromSrc(src));
      const fig = img.closest("figure.book-figure");
      if (fig) {
        fig.classList.add(isSequence ? "fig-sequence" : isClass ? "fig-class" : "fig-other");
        fig.style.pageBreakInside = "avoid";
        fig.style.breakInside = "avoid-page";
      }
    });

    // Mermaid figures
    document.querySelectorAll("figure.book-figure[data-fig-kind]").forEach((figure) => {
      const kind = figure.getAttribute("data-fig-kind") || "diagram";
      ensureCaption(figure, mermaidCaption(kind));
      figure.style.pageBreakInside = "avoid";
      figure.style.breakInside = "avoid-page";
    });
    document.querySelectorAll("pre.mermaid, .mermaid").forEach((el) => {
      if (el.closest("figure.book-figure")) return;
      // leftover unwrapped mermaid
      const figure = document.createElement("figure");
      figure.className = "book-figure";
      el.parentNode.insertBefore(figure, el);
      figure.appendChild(el);
      ensureCaption(figure, mermaidCaption("diagram"));
      figure.style.pageBreakInside = "avoid";
      figure.style.breakInside = "avoid-page";
    });

    document.querySelectorAll(".cover-photo").forEach((img) => {
      img.style.maxWidth = "92%";
      img.style.maxHeight = "3.9in";
      img.style.width = "auto";
      img.style.objectFit = "contain";
      img.style.border = "none";
    });

    document.querySelectorAll("figure.book-figure svg").forEach((svg) => {
      const figure = svg.closest("figure.book-figure");
      const kind = figure ? figure.getAttribute("data-fig-kind") : "";
      const h = kind === "sequence" ? seqMaxH : maxH;
      // Keep viewBox scaling — do NOT strip width/height to auto (Chrome print collapses to 0)
      svg.style.maxWidth = "100%";
      svg.style.width = "100%";
      svg.style.maxHeight = h;
      svg.style.height = "auto";
      svg.setAttribute("preserveAspectRatio", "xMidYMid meet");
    });

    document.querySelectorAll(".img-row, .book-figure, img:not(.cover-photo)").forEach((el) => {
      el.style.pageBreakInside = "avoid";
      el.style.breakInside = "avoid-page";
    });

    // Large figures: start on a new page so diagram + caption stay together (no clipping)
    const mm = (n) => (n * 96) / 25.4;
    const tallPx = mm(170);
    document.querySelectorAll("figure.book-figure").forEach((fig) => {
      if (fig.classList.contains("pov-hero-figure")) return;
      const h = fig.getBoundingClientRect().height;
      if (h > tallPx) {
        fig.style.pageBreakBefore = "always";
        fig.style.breakBefore = "page";
      }
      fig.style.pageBreakInside = "avoid";
      fig.style.breakInside = "avoid-page";
      const cap = fig.querySelector("figcaption");
      if (cap) {
        cap.style.pageBreakBefore = "avoid";
        cap.style.breakBefore = "avoid";
      }
    });
  });
}

/** Ensure figure+caption remain visible and on one page when possible. */
async function ensureFiguresFitPages(page) {
  await page.evaluate(() => {
    const mm = (n) => (n * 96) / 25.4;
    const pageBudget = mm(235);
    document.querySelectorAll("figure.book-figure").forEach((fig) => {
      if (fig.classList.contains("pov-hero-figure")) return;
      const kind = fig.getAttribute("data-fig-kind") || "";
      let h = fig.getBoundingClientRect().height;
      if (h > pageBudget) {
        fig.style.pageBreakBefore = "always";
        fig.style.breakBefore = "page";
        const target = kind === "sequence" ? "130mm" : "68mm";
        fig.querySelectorAll("svg").forEach((svg) => {
          svg.style.maxHeight = target;
          svg.style.width = "100%";
          svg.style.height = "auto";
        });
        fig.querySelectorAll("img").forEach((img) => {
          img.style.maxHeight = target;
        });
      }
      fig.style.pageBreakInside = "avoid";
      fig.style.breakInside = "avoid-page";
      // Guard against zero-size SVGs after print CSS
      fig.querySelectorAll("svg").forEach((svg) => {
        const box = svg.getBoundingClientRect();
        if (box.height < 8) {
          svg.style.width = "100%";
          svg.style.maxWidth = "100%";
          svg.style.height = "auto";
          svg.style.maxHeight = kind === "sequence" ? "144mm" : "72mm";
          if (!svg.getAttribute("viewBox") && svg.getAttribute("width") && svg.getAttribute("height")) {
            // leave attributes as-is
          }
        }
      });
    });
  });
}

async function main() {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  fs.mkdirSync(PDF_DIR, { recursive: true });
  const cssText = fs.readFileSync(CSS_PATH, "utf8");

  console.log(`Assembling ${CHAPTERS.length} chapters…`);
  const hrefMap = buildChapterHrefMap();
  const chapterHtml = CHAPTERS.map((ch, i) =>
    renderChapterHtml(ch, i + 1, hrefMap)
  ).join("\n");
  const tocHtml = buildTocHtml(CHAPTERS);
  const html = buildHtml(chapterHtml, tocHtml, cssText);

  const htmlPath = path.join(OUT_DIR, "design-patterns-book.html");
  const pdfPath = path.join(PDF_DIR, "design_patterns_1_0_0.pdf");
  fs.writeFileSync(htmlPath, html, "utf8");
  console.log(`Wrote HTML: ${htmlPath}`);

  const { server, port } = await startServer();
  const bookUrl = `http://127.0.0.1:${port}/book/pdf_book_tools/out/design-patterns-book.html`;
  console.log(`Serving at ${bookUrl}`);

  const chromeCandidates = [
    process.env.PUPPETEER_EXECUTABLE_PATH,
    "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
  ].filter(Boolean);
  const executablePath = chromeCandidates.find((p) => fs.existsSync(p));
  if (!executablePath) {
    server.close();
    throw new Error("No Chrome/Edge found. Set PUPPETEER_EXECUTABLE_PATH or install Chrome.");
  }
  console.log(`Using browser: ${executablePath}`);

  const browser = await puppeteer.launch({
    headless: true,
    executablePath,
    protocolTimeout: 600000,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });

  try {
    const page = await browser.newPage();
    page.setDefaultTimeout(600000);
    page.on("console", (msg) => {
      if (msg.type() === "warning" || msg.type() === "error") {
        console.log(`[browser ${msg.type()}] ${msg.text()}`);
      }
    });

    console.log("Loading book + rendering diagrams…");
    await page.goto(bookUrl, { waitUntil: "domcontentloaded", timeout: 120000 });
    await page.waitForFunction(
      () => document.documentElement.getAttribute("data-mermaid-ready") === "true",
      { timeout: 600000, polling: 1000 }
    );
    await fitFigures(page);
    await ensureFiguresFitPages(page);
    await new Promise((r) => setTimeout(r, 800));

    const diagramStats = await page.$$eval("figure.book-figure svg", (els) =>
      els.slice(0, 5).map((svg) => {
        const r = svg.getBoundingClientRect();
        return { w: Math.round(r.width), h: Math.round(r.height) };
      })
    );
    console.log("Sample SVG sizes:", JSON.stringify(diagramStats));

    const diagramCount = await page.$$eval(".mermaid svg, figure.book-figure svg", (els) => els.length);
    console.log(`Rendered Mermaid SVG count: ${diagramCount}`);

    console.log("Writing PDF…");
    const pdfOptionsBase = {
      format: "A4",
      printBackground: true,
      preferCSSPageSize: false,
      margin: { top: "16mm", bottom: "16mm", left: "14mm", right: "14mm" },
    };

    const coverPdfPath = path.join(OUT_DIR, "_cover.pdf");
    const bodyPdfPath = path.join(OUT_DIR, "_body.pdf");

    // Cover only — no header/footer
    await page.pdf({
      ...pdfOptionsBase,
      path: coverPdfPath,
      pageRanges: "1",
      displayHeaderFooter: false,
      margin: { top: "10mm", bottom: "10mm", left: "10mm", right: "10mm" },
    });

    // Remaining pages — with header/footer
    await page.pdf({
      ...pdfOptionsBase,
      path: bodyPdfPath,
      pageRanges: "2-",
      displayHeaderFooter: true,
      headerTemplate: `
        <div style="width:100%;box-sizing:border-box;padding:0 16mm;font-family:Segoe UI,Helvetica Neue,Arial,sans-serif;">
          <div style="display:flex;justify-content:space-between;align-items:baseline;padding-bottom:4px;border-bottom:0.6px solid #e8eaee;">
            <span style="font-size:7.5pt;letter-spacing:0.14em;text-transform:uppercase;color:#9aa3b2;">Design Pattern</span>
            <span style="font-size:7.5pt;color:#b0b7c3;font-style:italic;letter-spacing:0.02em;">The Art of Composing Solutions</span>
          </div>
        </div>`,
      footerTemplate: `
        <div style="width:100%;box-sizing:border-box;padding:0 16mm;font-family:Georgia,'Times New Roman',serif;text-align:center;">
          <div style="padding-top:5px;border-top:0.6px solid #e8eaee;color:#9aa3b2;font-size:9pt;letter-spacing:0.08em;">
            <span class="pageNumber"></span>
          </div>
        </div>`,
      margin: { top: "17mm", bottom: "16mm", left: "14mm", right: "14mm" },
    });

    const coverBytes = fs.readFileSync(coverPdfPath);
    const bodyBytes = fs.readFileSync(bodyPdfPath);
    const merged = await PDFDocument.create();
    const coverDoc = await PDFDocument.load(coverBytes);
    const bodyDoc = await PDFDocument.load(bodyBytes);
    const coverPages = await merged.copyPages(coverDoc, coverDoc.getPageIndices());
    coverPages.forEach((p) => merged.addPage(p));
    const bodyPages = await merged.copyPages(bodyDoc, bodyDoc.getPageIndices());
    bodyPages.forEach((p) => merged.addPage(p));
    const mergedBytes = await merged.save();
    fs.writeFileSync(pdfPath, mergedBytes);
    for (const tmp of [coverPdfPath, bodyPdfPath]) {
      try {
        fs.unlinkSync(tmp);
      } catch {
        /* ignore */
      }
    }
    console.log(`Wrote PDF: ${pdfPath}`);
  } finally {
    await browser.close();
    server.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
