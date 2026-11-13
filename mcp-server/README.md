# Witness Project MCP Server

Model Context Protocol server for the Witness Project.

让任何支持 MCP 的 AI 客户端，直接读取本仓库的登记册，而不是靠复制粘贴旧版 Excel。

## What it exposes

| Tool | What it does |
|---|---|
| `list_claims` | 列出 P01-P27 全部命题 |
| `get_claim` | 查一条命题原文 + 层面 + 状态 |
| `list_concepts` | 列出全部概念 C-001... |
| `get_concept` | 查一条概念定义 |
| `list_references` | 列出 REF-001... |
| `get_reference` | 查一条文献 |
| `list_evidence` | 列出 EVD-001... |
| `list_bridging` | 列出 BR-001... 跨层桥接 |
| `list_revision` | 列出 REV-001... 版本历史 |
| `search_registry` | 全文搜索登记册（命题 / 概念 / 文献 / 证据） |

## Rules (hard-coded in server)

- 只读，不写。MCP 永远不能改 registry、不能开 PR、不能改评级。
- 所有返回都带 `status: v0.2 backfilled, NOT frozen` 和 `ai_label: ai-assisted` 提醒。
- 不返回任何“已发表结论”的表述。未冻结的评级必须标注未冻结。

## Run

```bash
cd mcp-server
pip install -r requirements.txt
python server.py
```

## Configure in your AI client

### Claude Desktop / Cursor / VS Code (MCP config)

```json
{
  "mcpServers": {
    "witness-project": {
      "command": "python",
      "args": ["/absolute/path/to/witness-project/mcp-server/server.py"],
      "env": {
        "WITNESS_REGISTRY_DIR": "/absolute/path/to/witness-project/registry"
      }
    }
  }
}
```

Replace `/absolute/path/to/` with your real path. Example on Windows:
`C:/Users/gog98/witness-project-github-v1/mcp-server/server.py`

### Test

In your AI client, ask:
- `用 witness-project MCP 查 P17 的原文`
- `用 witness-project MCP 搜 W-phen`
- `用 witness-project MCP 列出所有桥接 BR-`

If it returns CSV content with `v0.2 NOT frozen`, it works.

## Deploy (optional, later)

- Local: run `server.py` on your machine, point `WITNESS_REGISTRY_DIR` to your local clone.
- Remote / hosted: deploy as SSE / HTTP MCP server on a small VPS, point it to the GitHub repo. Do NOT expose write access.
- GitHub Action: on every push to `main`, validate CSVs still parse. See `../.github/workflows/mcp-validate.yml` (planned).
