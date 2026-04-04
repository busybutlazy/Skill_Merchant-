---
name: create-skill
description: "Use this skill when the user wants to create a new public skill in this repository's canonical-skills, scaffold its package, or draft the first version of its package and instructions."
---

# Create Public Skill

用來在這個 repo 的 `canonical-skills/` 中建立新的公開 skill。

## Use This For

- 新增一個可分發的公開 skill
- 草擬 `package.json`、`manifest.json`、`instruction.md` 與 target overrides
- 建立 skill 所需的基本資料夾結構

## Do Not Use This For

- 修改 repo 維護者專用的 `.agents/skills/`
- 安裝 skill 到其他專案
- 只做小幅文字修正或版本調整

## Workflow

### 1. Gather the definition

先確認：

- skill 名稱
- 使用情境
- 不該觸發的情境
- 分類
- 主要 workflow
- 是否需要 `scripts/`、`references/`、`examples/`、`assets/`

### 2. Check repository conventions

讀取：

- `AGENTS.md`
- `README.md`
- 至少一個 `canonical-skills/` 既有 skill 作為結構參考

### 3. Create the public skill

在 `canonical-skills/<skill-name>/` 建立：

- `package.json`
- `manifest.json`
- `instruction.md`
- `targets/codex.frontmatter.json`
- `targets/claude.frontmatter.json`
- 視需要建立輔助目錄

`instruction.md` 應包含：

- 觸發時機
- 不適用情境
- 執行流程
- 必要限制與輸出要求

`package.json` 應包含：

- `name`
- `version`
- `description`
- `updated_at`
- `tags`

### 4. Validate consistency

確認：

- 目錄名稱、identity `name`、target override `name` 一致
- `description` 足以讓 Codex 判斷是否該觸發
- `package.json` 的版本與日期合理
- 內容屬於公開可分發 skill，而不是 repo 管理技能

### 5. Prepare for manager install flow

提醒自己或使用者：

- 這個 skill 之後會由 Python CLI render 並安裝到其他專案
- 因此內容不應依賴這個 repo 自己的特殊維護流程
