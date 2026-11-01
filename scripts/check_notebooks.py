"""Offline structural, syntax and self-contained notebook smoke checks."""
import ast
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted(ROOT.glob("**/*.ipynb"))
assert len(NOTEBOOKS) == 34, f"Expected 34 notebooks, found {len(NOTEBOOKS)}"
errors = []
for path in NOTEBOOKS:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
        assert doc.get("nbformat") == 4
        assert isinstance(doc.get("cells"), list)
        code = [c for c in doc["cells"] if c.get("cell_type") == "code"]
        assert code, "No executable cells"
        for index, cell in enumerate(code):
            source = "".join(cell.get("source", []))
            assert cell.get("execution_count") is None
            assert not cell.get("outputs", [])
            # IPython magics and shell escapes are not standard Python syntax.
            lines = source.splitlines()
            if any(line.lstrip().startswith(("%", "!", "?")) for line in lines):
                continue
            try:
                ast.parse(source, filename=str(path))
            except SyntaxError as exc:
                errors.append(f"{path.relative_to(ROOT)} cell {index}: {exc}")
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
for name in ("04-mcp-and-the-tool-ecosystem.ipynb", "05-skills-and-progressive-disclosure.ipynb", "01-designing-an-inference-service.ipynb"):
    path = next(p for p in NOTEBOOKS if p.name == name)
    cell = [c for c in json.loads(path.read_text())["cells"] if c["cell_type"] == "code"][-1]
    with tempfile.TemporaryDirectory() as directory:
        script = Path(directory) / "example.py"
        script.write_text("".join(cell["source"]))
        result = subprocess.run([sys.executable, str(script)], capture_output=True, text=True, timeout=15)
        if result.returncode:
            errors.append(f"{name}: local example failed: {result.stderr}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(NOTEBOOKS)} notebook structures; three offline smoke examples")
