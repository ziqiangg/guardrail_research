"""Registry of guardrail products shown in the workbook. Order = column order in sheet 3 and sheet order after sheet 3.

HOW TO ADD A PRODUCT
  1. Add one dict to PRODUCTS below (slug, name, header_prefix, two_level_md, inventory_sheet, inventory_builder_module).
     header_prefix is the text before the colon in the "## Column ...: <Prefix>: <name>" headings of the draft.
  2. Write the drafts: drafts/<slug>_two_level.md (the Table 3 columns) and the inventory draft the builder reads.
  3. Write benchtest/build_<slug>_inventory.py exposing CFG (see build_lg_inventory.py / build_sentinel_inventory.py)
     plus build(wb)/verify(wb, xlsx) as those modules do; build_two_level.main() imports and calls it.
  HDR_RE (fill_nemo_columns), MDS (build_two_level) and the expected sheet ORDER are derived from this registry.
  NeMo's inventory builder (build_inventory) is the original, hand-written one; later products use inventory_sheet.
"""
import re

from paths import DRAFTS

PRODUCTS = [
    dict(slug="nemo", name="NeMo Guardrails", header_prefix="NeMo Guardrails:",
         two_level_md=DRAFTS / "two_level_v2.md", inventory_sheet="3b. NeMo Rail Inventory",
         inventory_builder_module="build_inventory", notes="original product; 3b built by build_inventory"),
    dict(slug="llamaguard", name="Llama Guard", header_prefix="Llama Guard:",
         two_level_md=DRAFTS / "lg_two_level.md", inventory_sheet="3d. Llama Guard Inventory",
         inventory_builder_module="build_lg_inventory", notes="inventory via inventory_sheet"),
    dict(slug="sentinel", name="GovTech Sentinel", header_prefix="GovTech Sentinel:",
         two_level_md=DRAFTS / "sentinel_two_level.md", inventory_sheet="3e. GovTech Sentinel Inventory",
         inventory_builder_module="build_sentinel_inventory", notes="inventory via inventory_sheet"),
    dict(slug="presidio", name="Presidio", header_prefix="Presidio:",
         two_level_md=DRAFTS / "presidio_two_level.md", inventory_sheet="3f. Presidio Inventory",
         inventory_builder_module="build_presidio_inventory", notes="inventory via inventory_sheet; PD1-PD6"),
    dict(slug="sdp", name="Sensitive Data Protection", header_prefix="Sensitive Data Protection:",
         two_level_md=DRAFTS / "sdp_two_level.md", inventory_sheet="3g. SDP Inventory",
         inventory_builder_module="build_sdp_inventory", notes="inventory via inventory_sheet; SD1-SD6"),
]

SHEET3 = "3. Guardrail Research Table"
# sheets that are not per-product inventories; "after" is the sheet they are inserted after (None = last)
EXTRA_SHEETS = [dict(key="3c", sheet="3c. NeMo Evaluation Tooling", builder_module="build_eval_sheet",
                     after="3b. NeMo Rail Inventory")]
SHEET4 = dict(sheet="4. Candidate Comparison Groups", builder_module="build_groups_sheet", after=None)


def _sheet_order():
    order = [SHEET3]
    for p in PRODUCTS:
        order.append(p["inventory_sheet"])
        for e in EXTRA_SHEETS:
            if e["after"] == p["inventory_sheet"]:
                order.append(e["sheet"])
    order.append(SHEET4["sheet"])
    return order


ORDER = _sheet_order()
MDS = [p["two_level_md"] for p in PRODUCTS]
HDR_RE = re.compile(r"^## Column[^:]*:\s*((?:%s):.*)$"
                    % "|".join(re.escape(p["header_prefix"].rstrip(":")) for p in PRODUCTS))
