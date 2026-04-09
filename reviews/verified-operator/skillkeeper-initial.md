# 初次準入審查

## 來源摘要

- source root: `tmp/foreign_skills/soxakore-codex-engineering-skills-verified-operator-1`
- source type: single skill folder
- requested canonical skill name: `verified-operator`
- source 已以 `verified-operator` 作為 skill name，差異只在來源資料夾 slug
- 顯式支援檔案：
  - `examples/` 5 個實例
  - `templates/templates.md`
  - `agents/openai.yaml`

## 為什麼值得納管

這個 skill 對「需要真的操作系統並驗證結果」的任務有明確定位，能力邊界與風險分級也寫得完整。它不是泛泛的 execution prompt，而是把 world model、risk grading、receipts、rollback、drift recovery、phase orchestration 與 temporal reasoning 都定義成可重複流程，對 public skill 層有明顯實用性。

## 風險摘要

- 內容鼓勵對外部系統採取實際操作，若 canonical draft 把 approval gate 或 secret redaction 弄丟，風險會立即升高
- 內容長且覆蓋面廣，改寫時容易遺失 invocation cues、reference hooks 或 advanced mode 條件
- examples 含有外部服務、DNS、Vercel、ADB 等情境，若只保留 instruction 不保留 examples，使用時機會明顯退化

## 維護成本

- 中高
- 主要成本來自長 instruction 的保真維護與 examples/templates 的同步
- 但 source 結構單純，沒有 scripts 或 assets，治理成本仍可接受

## Canonicalization Constraints

- `source-inventory.md` 必須視為 binding contract
- 必須保留 L0/L1/L2/L3 風險分級與 L2+ 先確認的規則
- 必須保留 receipts、rollback、checkpoint、drift recovery、completion bar
- 必須保留 advanced sections (§16-§21) 的使用條件與能力線索
- 必須保留對 `examples/` 與 `templates/templates.md` 的顯式引用，以及何時查看它們
- target-specific wording 應移到 frontmatter，不可在 instruction 內混入 agent-specific 句型

## Must-Preserve List

- verified execution 而非 narration 的核心目標
- 五步 quick start 與 complex mode extension
- ledger / audit trail / checkpoint / final summary / metrics templates 的引用
- approval and safety rules
- drift recovery、conflicting signals、ambiguous success、concurrent human changes
- dependency graph、confidence scoring、invariant monitoring、failure taxonomy、multi-phase orchestration、temporal reasoning
- trigger examples 與 when-not-to-use boundaries

## Removable-Only-If-Justified List

- `agents/openai.yaml` 的 wording 可 remap 到 canonical frontmatter
- source frontmatter 可轉換成 `package.json` 與 target frontmatter
- 章節編號或少量排版可為 canonical packaging 做最小調整

## Verdict

`allow`
