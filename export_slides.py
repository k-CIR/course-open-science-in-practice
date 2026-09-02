"""
export_slides.py
----------------
Convert all .pptx and .pdf files in the presentations directory into
PNG-based slide galleries and place them under docs/slides/ so MkDocs can
serve them.

Pipeline per file:
  1. .pptx  -> LibreOffice (soffice) converts .pptx → .pdf
     .pdf   -> used as-is (step skipped)
  2. Ghostscript (gs) rasterises each PDF page → slide_NNN.png
  3. A self-contained index.html gallery is written with prev/next navigation

Each presentation gets its own subdirectory:
    docs/slides/<stem>/
        index.html
        slide_001.png
        slide_002.png
        ...

Link to the gallery from a lecture/resource page with a normal markdown
link, e.g. from docs/lectures/lecture-1-why-git.md:
    [:material-image-multiple: View slide gallery](../slides/lecture-1-why-git/index.html){ .md-button }

Usage (from the documentation/ repo root):
    .venv/bin/python export_slides.py

Optional arguments:
    --presentations   Path to the directory containing .pptx/.pdf files
                      (default: ../main/presentations)
    --output          Path to the slides output directory
                      (default: docs/slides)
    --dpi             Resolution for PNG rasterisation (default: 150)
    --force           Re-export even if the output directory already exists

Examples:
    .venv/bin/python export_slides.py
    .venv/bin/python export_slides.py --dpi 200
    .venv/bin/python export_slides.py --force
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


GALLERY_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background: #1a1a2e;
      color: #eee;
      font-family: "Inter", "Segoe UI", Roboto, sans-serif;
      height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    #viewer {{
      flex: 1;
      min-height: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem 1rem 0;
    }}

    #viewer img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      border-radius: 6px;
      box-shadow: 0 8px 32px rgba(0,0,0,0.6);
      display: block;
    }}

    #controls {{
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 1.5rem;
      padding: 0.6rem 1.5rem;
      margin: 0.6rem auto 0.5rem;
      background: rgba(255,255,255,0.07);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 999px;
      backdrop-filter: blur(6px);
    }}

    button {{
      background: #e75480;
      color: #fff;
      border: none;
      border-radius: 999px;
      padding: 0.5rem 1.25rem;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s, transform 0.1s;
    }}

    button:hover  {{ background: #ff8fbf; transform: translateY(-1px); }}
    button:active {{ transform: translateY(0); }}
    button:disabled {{ background: rgba(255,255,255,0.2); cursor: not-allowed; transform: none; }}

    #counter {{
      font-size: 1rem;
      color: rgba(255,255,255,0.7);
      min-width: 70px;
      text-align: center;
    }}

    #progress {{
      position: fixed;
      bottom: 0; left: 0;
      height: 3px;
      width: 100%;
      background: rgba(255,255,255,0.1);
    }}

    #progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, #e75480, #ffb3d1);
      transition: width 0.3s ease;
    }}
  </style>
</head>
<body>

  <div id="viewer">
    <img id="slide" src="slide_001.png" alt="Slide 1">
  </div>

  <div id="controls">
    <button id="prev" onclick="go(-1)">&#8592; Previous</button>
    <span id="counter">1 / {total}</span>
    <button id="next" onclick="go(1)">Next &#8594;</button>
  </div>

  <div id="progress"><div id="progress-fill"></div></div>

  <script>
    const total = {total};
    let current = 1;

    function pad(n) {{ return String(n).padStart(3, '0'); }}

    function go(dir) {{
      const next = current + dir;
      if (next < 1 || next > total) return;
      current = next;
      document.getElementById('slide').src = 'slide_' + pad(current) + '.png';
      document.getElementById('slide').alt = 'Slide ' + current;
      document.getElementById('counter').textContent = current + ' / ' + total;
      document.getElementById('prev').disabled = current === 1;
      document.getElementById('next').disabled = current === total;
      document.getElementById('progress-fill').style.width = (current / total * 100) + '%';
    }}

    document.addEventListener('keydown', function(e) {{
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown')  go(1);
      if (e.key === 'ArrowLeft'  || e.key === 'ArrowUp')    go(-1);
    }});

    // Init state
    document.getElementById('prev').disabled = true;
    document.getElementById('progress-fill').style.width = (1 / total * 100) + '%';
  </script>
</body>
</html>
"""


def find_tool(name: str, alternatives: list[str] | None = None) -> Path:
    """Look up `name` on PATH, falling back to `alternatives` if not found.

    Needed because the official Windows Ghostscript installer names its
    executable gswin64c.exe / gswin32c.exe rather than gs (conda-forge's
    ghostscript package does provide a plain gs, so this only kicks in for
    non-conda installs).
    """
    for candidate in [name, *(alternatives or [])]:
        path = shutil.which(candidate)
        if path:
            return Path(path)
    tried = ", ".join([name, *(alternatives or [])])
    print(f"ERROR: none of ({tried}) found on PATH. Install it and retry.", file=sys.stderr)
    sys.exit(1)


def pptx_to_pdf(pptx: Path, out_dir: Path, soffice: Path) -> Path:
    """Convert a .pptx to PDF using LibreOffice in headless mode."""
    subprocess.run(
        [str(soffice), "--headless", "--convert-to", "pdf",
         str(pptx), "--outdir", str(out_dir)],
        check=True,
        capture_output=True,
    )
    pdf = out_dir / (pptx.stem + ".pdf")
    if not pdf.exists():
        raise FileNotFoundError(f"LibreOffice did not produce {pdf}")
    return pdf


def pdf_to_pngs(pdf: Path, out_dir: Path, dpi: int, gs: Path) -> list[Path]:
    """Rasterise every page of a PDF to PNG using Ghostscript."""
    out_dir.mkdir(parents=True, exist_ok=True)
    pattern = str(out_dir / "slide_%03d.png")
    subprocess.run(
        [str(gs), "-dBATCH", "-dNOPAUSE", "-dSAFER",
         "-sDEVICE=png16m", f"-r{dpi}",
         f"-sOutputFile={pattern}", str(pdf)],
        check=True,
        capture_output=True,
    )
    return sorted(out_dir.glob("slide_*.png"))


def write_gallery(slide_dir: Path, title: str, total: int) -> None:
    # Remove any stale files from previous export methods
    for stale in ("styles.css", "script.js"):
        (slide_dir / stale).unlink(missing_ok=True)
    html = GALLERY_HTML.format(title=title, total=total)
    (slide_dir / "index.html").write_text(html, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).parent

    parser = argparse.ArgumentParser(
        description="Export all .pptx files to PNG slide galleries for MkDocs.",
    )
    parser.add_argument(
        "--presentations",
        type=Path,
        default=repo_root / ".." / "main" / "presentations",
        help="Directory containing .pptx source files (default: ../main/presentations)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo_root / "docs" / "slides",
        help="Directory to write gallery output into (default: docs/slides)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=150,
        help="PNG resolution in DPI (default: 150; use 200 for sharper output)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-export even if the output subdirectory already exists",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    gs = find_tool("gs", ["gswin64c", "gswin32c"])

    presentations_dir: Path = args.presentations.resolve()
    output_dir: Path        = args.output.resolve()

    if not presentations_dir.is_dir():
        print(f"ERROR: presentations directory not found: {presentations_dir}", file=sys.stderr)
        sys.exit(1)

    # Exclude Office lock files (~$*.pptx) created while a file is open
    pptx_files = sorted(
        p for p in presentations_dir.glob("*.pptx")
        if not p.name.startswith("~$")
    )
    pdf_files = sorted(presentations_dir.glob("*.pdf"))
    source_files = sorted(pptx_files + pdf_files)

    if not source_files:
        print(f"No .pptx or .pdf files found in {presentations_dir}")
        sys.exit(0)

    # LibreOffice is only needed to convert .pptx -> .pdf; skip the lookup
    # (and the dependency) when only raw .pdf sources are being exported.
    soffice = find_tool("soffice") if pptx_files else None

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Source : {presentations_dir}")
    print(f"Output : {output_dir}")
    print(f"DPI    : {args.dpi}")
    print(f"Found  : {len(source_files)} file(s)\n")

    ok = skipped = failed = 0

    for source in source_files:
        slide_out = output_dir / source.stem

        if slide_out.exists() and not args.force:
            print(f"  SKIP  {source.name}  (already exported — use --force to overwrite)")
            skipped += 1
            continue

        print(f"  ...   {source.name}", end="", flush=True)
        try:
            with tempfile.TemporaryDirectory() as tmp:
                tmp_path = Path(tmp)
                if source.suffix.lower() == ".pptx":
                    pdf = pptx_to_pdf(source, tmp_path, soffice)
                else:
                    pdf = source
                pngs = pdf_to_pngs(pdf, slide_out, args.dpi, gs)

            write_gallery(slide_out, source.stem.replace("_", " ").title(), len(pngs))
            print(f"  ->  {slide_out.relative_to(output_dir.parent.parent)}  ({len(pngs)} slides)")
            ok += 1
        except Exception as exc:
            print(f"\n  FAIL  {source.name}: {exc}", file=sys.stderr)
            failed += 1

    print(f"\nDone: {ok} exported, {skipped} skipped, {failed} failed.")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
