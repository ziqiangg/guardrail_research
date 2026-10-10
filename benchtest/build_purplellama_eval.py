"""Sheet '3k. CyberSecEval Eval Tooling' from drafts/purplellama_eval_tooling_final.md. Called by build_two_level.main().

Thin config over build_eval_sheet.py (the generic eval-sheet builder, shared with 3c NeMo Evaluation Tooling).
Placed right after the Purple Llama inventory sheet (3j), R003.
Public API: add_sheet(wb, ws3=None) -> ws ; verify(wb, xlsx=None)
"""
import paths as P
import build_eval_sheet as ES

MD = str(P.DRAFTS / "purplellama_eval_tooling_final.md")
S3K = "3k. CyberSecEval Eval Tooling"  # 29 characters
TITLE = "3k. Meta CyberSecEval 4 Evaluation Tooling (PurpleLlama@172c1074)"
NOTE = ("Evaluation tools, datasets, published results and reuse assessment for the test bench (possible sources and "
        "suggestions, not decisions). Labels as in sheet 3.")
CFG = dict(md=MD, sheet=S3K, after="3j. Purple Llama Inventory", title=TITLE, note=NOTE)
assert len(S3K) <= 31


def add_sheet(wb, ws3=None):
    return ES.add_sheet(wb, CFG)


def verify(wb, xlsx=None):
    return ES.verify(wb, None, xlsx, CFG)
