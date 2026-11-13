# MCP Guide — 给 AI 用的接口

## 为什么需要 MCP

GitHub 是给人看的。MCP 是给 AI 读的。

没有 MCP：每次你要把 Excel / CSV 复制给 AI，AI 读到的是你上次发的旧版本。
有 MCP：AI 直接连仓库，读到的是 `main` 分支的最新登记册。

## 架构

```
AI Client (Claude / Cursor / VS Code)
    |  MCP (stdio, 本地)
    v
mcp-server/server.py (只读)
    |
    v
registry/*.csv (唯一事实来源)
```

## 安全规则（写死在 server.py 里）

1. 只读，不写。MCP 不能改 registry、不能开 Issue / PR、不能改评级。
2. 所有返回都带 `NOT frozen` 状态，防止 AI 把回填版当成结论。
3. 不暴露 Token、不暴露私人信息。本地运行，不需要把仓库公开给 MCP 服务商。

## 本地接入（推荐，先做这个）

1. 把 `mcp-server/` 放进仓库（已在包里）
2. `pip install -r mcp-server/requirements.txt`
3. 在你的 AI 客户端 MCP 配置里加 witness-project，指向 `mcp-server/server.py`
4. 在 AI 里问：`用 witness-project MCP 查 P17`

## 远程部署（以后再做，不要现在做）

远程 MCP 需要一台服务器 + 鉴权，现在不要做。先用本地 MCP 验证流程，等 Sprint 1 复核有结论了，再考虑是否要部署一个公开只读的 MCP 端点。

## 常见问题

- **AI 说找不到工具？** 检查 MCP 配置里的绝对路径是否正确，Windows 要用 `C:/...` 不是 `C:\...`
- **AI 返回旧数据？** 检查 `WITNESS_REGISTRY_DIR` 是否指向你最新的 clone，不是旧的下载文件夹
- **AI 想通过 MCP 改评级？** 拒绝。改评级必须走 GitHub Issue / PR，这是治理规则，不是技术限制
