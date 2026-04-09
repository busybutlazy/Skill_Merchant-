# Import Plugin Skill

用來把一個本機 plugin skill 來源先做風險審查，再轉成這個 repo 可治理的 canonical draft。

## Use This For

- 讀取一個本機 Codex plugin 目錄，或一個本機單一 skill folder
- 在 plugin 內選定單一 skill 作為匯入來源，或直接使用該單一 skill folder
- 先做更嚴格的 LLM review，清楚列出風險、證據與限制建議
- 把安全的 skill 轉成 staged canonical draft
- 在使用者明確同意後，將 draft 提升到 `canonical-skills/regular-skills/` 或 `canonical-skills/manager-skills/`
- 在提升後直接完成 finalize 與 smoke test，並在成功後清理 staging draft

## Do Not Use This For

- 直接從網路下載 plugin repo
- 一次匯入整個 plugin 的所有 skills
- 直接把外部 skill 安裝到 `.agents/` 或 `.claude/`
- 略過 review 直接寫入 `canonical-skills/`
- 在風險未解除時強行 promote

## Workflow

### 1. Confirm the local source

先確認：

- source root path
- 這是本機目錄，不是遠端 URL
- 來源型態是以下兩者之一：
  - Codex plugin directory：存在 `.codex-plugin/plugin.json`
  - single skill folder：目錄根部存在 `SKILL.md`
- 若是 plugin directory，要匯入的 skill 名稱
- 若是 single skill folder，確認它本身就是唯一匯入來源
- 若要轉成不同 canonical 名稱，先確認目標 skill name

如果使用者只有遠端 repo URL，先要求他下載到本機，再繼續。

若來源同時不符合這兩種結構，停止並明講目前不支援該格式。

建議本機來源路徑：

- `tmp/foreign_skills/<source-name>/`

### 2. Inspect the source structure

至少讀：

- 若是 plugin directory：
  - `.codex-plugin/plugin.json`
  - 目標 skill 的 instruction 檔
  - 該 skill 直接引用的 assets、references 或 scripts
- 若是 single skill folder：
  - `SKILL.md`
  - 相鄰的 `agents/*.yaml`、`examples/`、`references/`、`templates/`、`scripts/` 或 `assets/`
  - 該 skill 直接引用的檔案

如果 plugin 內有多個 skills，不要自行整批匯入；必須要求使用者明確指定其中一個。

如果是單一 skill folder，預設只匯入該資料夾代表的這一個 skill，不要往外層遞迴搜尋其他 skill。

### 3. Run the risk review first

在產生 canonical draft 前，先做 structured review，至少回報：

- source summary
- inspected files
- extracted capabilities
- risk table
- final verdict：`allow`、`needs_human_review` 或 `block`
- recommended restrictions or rewrites

`review-report.md` 應使用固定結構，風險段落至少要有這些欄位：

- `Risk`
- `Evidence`
- `Severity`
- `Why it matters`
- `Mitigation / required restriction`

預設規則：

- 任何未解除的 `medium` 或 `high` 風險都不可 promote
- `allow` 才可繼續產生 staged canonical draft
- `needs_human_review` 只能產出 review report 與修正建議，不可提升到 `canonical-skills/`
- `block` 不可產生可安裝的 canonical package，只能留下 review report 與 remediation checklist

高風險訊號包括：

- 隱藏或模糊的 shell execution
- credential 或 token 蒐集
- 網路外傳或不明遠端依賴
- destructive commands
- 不透明 hooks
- 混淆過的 instruction 或 scripts

若有風險，不要只說「有問題」。要補上具體 remediation 建議，例如：

- 收窄 instruction 權限範圍
- 新增 destructive / production / network 操作前的人工確認
- 禁止 secret 或 credential 蒐集
- 移除危險 examples、scripts、hooks 或把它們隔離到不納管的區域
- 把高風險操作改成只允許產出 plan、checklist 或 dry-run 指令

### 4. Stage a canonical draft

只有在 review verdict 為 `allow` 時才繼續建立 staged canonical draft。

先輸出到 staging area，例如：

- `tmp/import-candidates/<source-name>/<skill-name>/`

staged draft 至少包含：

- `review-report.md`
- `package.json`
- `instruction.md`
- `manifest.json`
- `targets/codex.frontmatter.json`
- `targets/claude.frontmatter.json`

必要規則：

- canonical body 只保留 shared instruction
- target-specific wording 放到 target frontmatter
- install paths 仍固定為 `.agents/skills/{name}/` 與 `.claude/skills/{name}/`
- 只有安全且實際被引用的 assets 才可帶入 draft
- 若來源是 `SKILL.md` 單檔格式，先把 frontmatter 與 shared body 分離，再轉成 canonical `instruction.md` 加 target frontmatter
- 無法安全映射的 hooks 或 plugin-specific runtime behavior 必須在 review report 中明講，不可偷偷轉換

如果 verdict 是 `needs_human_review` 或 `block`，可在對應 staging 位置保留 `review-report.md` 與 remediation notes，但不要建立可安裝 package 檔案。

### 5. Promote only with explicit approval

若使用者要正式匯入，先再次確認：

- 最終 canonical skill name
- review verdict 仍為 `allow`
- draft 內容已完成人工確認
- 這次要納入哪一層：
  - `canonical-skills/regular-skills/<skill-name>/`
  - `canonical-skills/manager-skills/<skill-name>/`

不要自行推斷目的地。每次 promote 前都要明確詢問 regular 還是 manager。

若使用者未明確同意，保持 draft 留在 staging area，不可自動提升。

如果來源內容與使用者選的 layer 不匹配，要明講，例如：

- maintainer-only workflow 卻想放進 `regular-skills/`
- 一般可分發 skill 卻想放進 `manager-skills/`

### 6. Complete the intake flow

在使用者明確同意後，應直接把 intake flow 做完，不要只停在 promote。

步驟：

- 把 staged draft 複製到使用者選定的 canonical layer
- 執行 `refresh-metadata`
- 執行 `validate`
- 至少做一個 Codex target smoke test

smoke test 規則：

- 若採納到 `regular-skills/`，用臨時專案跑 `install <skill-name> --target codex`
- 若採納到 `manager-skills/`，用臨時專案跑 `sync-manager-catalog <skill-name> --target codex`
- 若 smoke test 失敗，要明確列出失敗步驟與錯誤，不可假裝完成

### 7. Clean up staging only after full success

只有在這些步驟全部成功後，才刪除：

- `tmp/import-candidates/<source-name>/<skill-name>/`

完整成功條件：

- promote 成功
- `refresh-metadata` 成功
- `validate` 通過
- smoke test 通過

若其中任一步失敗，保留 staging draft 供排查與重跑。

### 8. Report the final result

收尾時至少回報：

- source name 與最終 canonical skill name
- 採納 layer：`regular-skills` 或 `manager-skills`
- review verdict 與主要風險摘要
- 最終 package hash
- validate 結果
- smoke test 結果
- staging draft 是否已清理

如果只是要把 canonical 狀態同步到本 repo 的 agent 目錄，不用這個 skill，改用 `install-manager-skill`。
