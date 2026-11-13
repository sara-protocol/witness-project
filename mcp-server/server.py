"""
Witness Project MCP Server — READ-ONLY. Compatible with mcp 2.x.
"""
import os, csv, pathlib, json, sys

from mcp.server.fastmcp import FastMCP

REGISTRY_DIR = pathlib.Path(os.environ.get(
    "WITNESS_REGISTRY_DIR",
    pathlib.Path(__file__).parent.parent / "registry"
))
STATUS = "v0.2 backfilled, NOT frozen. E-M-T-L-I formal ratings pending Method Manual v1.0. Do not cite as peer-reviewed conclusion."

mcp = FastMCP("witness-project")

FILE_MAP = {
    "claims": "claims.csv",
    "concepts": "concepts.csv",
    "references": "references.csv",
    "evidence": "evidence.csv",
    "bridging": "bridging.csv",
    "revision": "revision.csv",
    "sprint": "sprint.csv",
}

def _read(kind: str):
    path = REGISTRY_DIR / FILE_MAP[kind]
    if not path.exists():
        return []
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def _wrap(kind: str, rows):
    return {"status": STATUS, "ai_label": "ai-assisted", "source": f"registry/{FILE_MAP[kind]}", "count": len(rows), "rows": rows}

def _find(kind: str, key_field: str, key: str):
    rows = _read(kind)
    for r in rows:
        if (r.get(key_field) or "").strip().upper() == key.strip().upper():
            return {"status": STATUS, "ai_label": "ai-assisted", "row": r}
    return {"status": STATUS, "error": f"{key} not found in {kind}"}

@mcp.tool()
def list_claims() -> dict:
    """List all claims P01-P27."""
    return _wrap("claims", _read("claims"))

@mcp.tool()
def get_claim(claim_id: str) -> dict:
    """Get one claim by ID, e.g. P17, P03, P06a."""
    return _find("claims", "Claim ID", claim_id)

@mcp.tool()
def list_concepts() -> dict:
    """List all concepts C-001..."""
    return _wrap("concepts", _read("concepts"))

@mcp.tool()
def get_concept(concept_id: str) -> dict:
    """Get one concept by ID, e.g. C-005a."""
    return _find("concepts", "Concept ID", concept_id)

@mcp.tool()
def list_references() -> dict:
    """List all references REF-001..."""
    return _wrap("references", _read("references"))

@mcp.tool()
def get_reference(ref_id: str) -> dict:
    """Get one reference by ID, e.g. REF-009."""
    return _find("references", "REF ID", ref_id)

@mcp.tool()
def list_evidence() -> dict:
    """List all evidence EVD-001..."""
    return _wrap("evidence", _read("evidence"))

@mcp.tool()
def list_bridging() -> dict:
    """List all bridging BR-001..."""
    return _wrap("bridging", _read("bridging"))

@mcp.tool()
def list_revision() -> dict:
    """List all revision REV-001..."""
    return _wrap("revision", _read("revision"))

@mcp.tool()
def search_registry(query: str) -> dict:
    """Full-text search across claims, concepts, references, evidence, bridging."""
    q = query.lower()
    hits = []
    for kind in ["claims", "concepts", "references", "evidence", "bridging"]:
        for row in _read(kind):
            blob = " ".join(str(v) for v in row.values()).lower()
            if q in blob:
                hits.append({"kind": kind, "row": row})
    return {"status": STATUS, "ai_label": "ai-assisted", "query": query, "count": len(hits), "hits": hits[:30]}

if __name__ == "__main__":
    # Print to stderr only, stdout must stay clean for MCP stdio protocol
    print(f"[witness-project] registry={REGISTRY_DIR} exists={REGISTRY_DIR.exists()}", file=sys.stderr, flush=True)
    mcp.run()
