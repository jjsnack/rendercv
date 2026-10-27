# Resume pipeline

Helpers for building one-page resumes with this fork. Nothing personal lives here; the resumes themselves are kept elsewhere (see below).

- `fit.py CV.yaml [--min 0.5] [--max 0.85] [--out DIR]`: renders the CV at the loosest `design.typography.line_spacing` (in em) that still gives one page, by bisection, and leaves the result in `--out` (default `build/` next to the YAML). Run it with the fork's environment, e.g. `uv run --project <fork> --python 3.13 --extra full python tools/resume/fit.py CV.yaml`. It needs the fonts the CV names (the sample uses Geist, Geist Mono and Geist Pixel).
- `examples/Geist_Sample_CV.yaml`: a placeholder CV with the Geist design, every fork option and every Typst helper, commented.
- `scripts/rendercv_skill/generate.py --output DIR/SKILL.md`: writes the RenderCV agent skill, including the fork's options and helpers, to a path of your choice (the default run also rewrites `docs/llms.txt` and the zip).

## How the owner uses it
A workspace project folder keeps `people/<name>/<CV>.yaml` (git-ignored) and a `Makefile` that calls `fit.py`, copies monthly snapshots to `~/Documents/resume/<name>/YYYY-MM/`, and installs the generated skill in its own `.claude/skills/rendercv/`.

## Limits
`fit.py` assumes the page count never drops as spacing grows, and only changes line spacing; entry and section gaps are fixed values in the YAML. RenderCV's text parser keeps only flat Typst commands (see the skill's "Fork additions" section).
