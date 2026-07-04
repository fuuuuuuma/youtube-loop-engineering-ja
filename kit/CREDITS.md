# CREDITS / クレジット

**youtube-loop-engineering-ja** は、YouTube運用のうち投稿以外の工程（リサーチ・台本・サムネイル・QC）を
Claude Codeの「ゴール型ループ」で仕組み化するための独自実装のキットです。中核の考え方について、
以下の原典に感謝します。

| 本キット | 由来・参考 | 作者 | 種別 |
|---|---|---|---|
| `CLAUDE.md`・`prompts/goal-loop-qc.md`（ゴール型ループの考え方） | [Getting Started with Loops](https://claude.com/blog/getting-started-with-loops)（Anthropic・2026-06-30） | Delba de Oliveira, Michael Segner | 記事（引用・参照） |
| `.claude/skills/youtube-loop/SKILL.md`（スキル構成） | Claude Code公式のSKILL.md形式 | Anthropic | 仕様（参照） |
| `scripts/gen_thumbnail.py`（画像生成呼び出し） | OpenAI Images API（`gpt-image-2`） | OpenAI | API（参照） |

`scripts/gen_thumbnail.py` の実装形（標準ライブラリのみでOpenAI Images APIを叩く最小スクリプト）は、
姉妹企画 `claude-code-lp-builder-ja` の `scripts/gen_image.py` と同じ考え方を踏襲しています。

---

## Getting Started with Loops（ゴール型ループの土台）

- 記事: https://claude.com/blog/getting-started-with-loops
- 著者: Delba de Oliveira, Michael Segner（Anthropic）
- 公開日: 2026-06-30

「エージェントが、止まる条件に達するまで作業のサイクルを繰り返すこと」というループの定義、
「ゴール型（`/goal`）＝成功条件と評価役を決めて、達成か上限ターンまで回す」という分類、
「定量的なチェックほど自己検証しやすい」「まず一番簡単な解から」という原則を、
本キットのQCループ設計の土台としています。

---

本キットは **MIT License** です（[LICENSE](LICENSE)参照）。自由に使い・改変し・配ってOKです。
