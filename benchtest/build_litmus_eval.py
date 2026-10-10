"""Sheet '3n. Litmus Eval Tooling' from drafts/litmus_eval_tooling_final.md. Called by build_two_level.main().

Thin config over build_eval_sheet.py (the generic eval-sheet builder, shared with 3c and 3k).
Placed right after the Litmus inventory sheet (3m), R003.
Public API: add_sheet(wb, ws3=None) -> ws ; verify(wb, xlsx=None)
"""
import paths as P
import build_eval_sheet as ES

MD = str(P.DRAFTS / "litmus_eval_tooling_final.md")
S3N = "3n. Litmus Eval Tooling"  # 23 characters
TITLE = "3n. GovTech Litmus Evaluation Tooling (hosted service, no release; playbook@45908b48)"
NOTE = ("Evaluation-tool facts, the test list, published results and reuse assessment for the test bench (possible "
        "sources and suggestions, not decisions). Labels as in sheet 3.")
CFG = dict(md=MD, sheet=S3N, after="3m. Litmus Inventory", title=TITLE, note=NOTE)
assert len(S3N) <= 31


def add_sheet(wb, ws3=None):
    return ES.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return ES.verify(wb, None, xlsx, CFG)
