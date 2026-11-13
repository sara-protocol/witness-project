"""Quick local test without an MCP client. Reads CSVs directly."""
import pathlib, csv, os
reg = pathlib.Path(os.environ.get("WITNESS_REGISTRY_DIR", pathlib.Path(__file__).parent.parent / "registry"))
for name in ["claims.csv","concepts.csv","references.csv"]:
    p = reg / name
    print(name, "exists:", p.exists())
    if p.exists():
        with open(p, encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
            print("  rows:", len(rows), "first keys:", list(rows[0].keys())[:4] if rows else [])
