"""Single source of truth for file locations. Everything is relative to this file, so the repo can live anywhere
(Windows or Linux). Other scripts keep their old constant names (DIR, XLSX, BAK3 ...) as aliases of these."""
from pathlib import Path

ROOT = DIR = Path(__file__).resolve().parent
DRAFTS = ROOT / "drafts"
DIAGRAMS = ROOT / "diagrams"
BASELINES = ROOT / "baselines"
XLSX = ROOT / "AI Guardrails Research and Comparison.xlsx"
DOCX = ROOT / "AI Guardrails Research and Comparison.docx"


def bak(n):
    """Frozen baseline workbook vN (benchtest/baselines/...v{n}.xlsx)."""
    return BASELINES / f"AI Guardrails Research and Comparison.v{n}.xlsx"
