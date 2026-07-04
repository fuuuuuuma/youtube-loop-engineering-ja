# youtube-loop-engineering-ja — YouTube運用ループ（投稿以外）Claude Codeキット

> **これは何**：YouTube運用のうち「リサーチ→台本→（声/アバターは任意）→サムネイル→QC」を、
> Claude Codeの**ゴール型ループ**（成功条件＋評価役で、合格するまで自動反復する）で仕組み化するための配布キットです。
> **投稿（アップロード・公開）はこのキットの対象外**——常に人間が手動で行います（BAN対策の意図的な設計）。

このキットは、YouTube「ClaudeCodeチャンネル」の解説回
**「YouTube自動運用ループ徹底解説」** の配布物です。

---

## 3行でわかる

- **合格基準は数値で決める。** 文字数・秒数・音量など、機械的に判定できる形にする。
- **不合格の項目だけをやり直す。** 全部作り直さない。ピンポイント修正で1周を軽くする。
- **投稿だけは、あえて自動化しない。** BAN対策として、最終確認と公開は必ず人間が行う。

---

## 使い方（3ステップ）

1. **配置する**: `CLAUDE.md` と `.claude/` をプロジェクト直下に置き、Claude Codeでそのフォルダを開く
2. **回す**: リサーチ・台本・サムネイルまでを `.claude/skills/youtube-loop/SKILL.md` の手順で進める
3. **QCする**: `prompts/goal-loop-qc.md` の雛形を自分の動画の合格基準に書き換えて `/goal` に渡し、100点まで自動反復させる

> QCが完了したら、**人間が最終確認してから手動でYouTubeに投稿**してください。

---

## 収録物

| パス | 中身 |
|---|---|
| `CLAUDE.md` | Claude Codeが自動で読む背骨（ゴール型ループの方針・最重要ルール） |
| `.claude/skills/youtube-loop/SKILL.md` | リサーチ→台本→サムネイル→QCの簡略版スキル |
| `scripts/gen_thumbnail.py` | サムネイル生成（OpenAI API・`gpt-image-2`・要 `OPENAI_API_KEY`） |
| `prompts/goal-loop-qc.md` | ゴール型ループの雛形プロンプト（Objective/Evidence/Validation/Done/Block形式） |
| `reference/video-loop-blueprint.md` | ツール非依存の汎用ブループリント（チェックリスト形式） |
| `CREDITS.md` / `LICENSE` | 由来・謝辞 ／ MIT |

---

## 由来・ライセンス

ゴール型ループの考え方は Anthropic の [Getting Started with Loops](https://claude.com/blog/getting-started-with-loops)
（2026-06-30）由来。くわしくは [CREDITS.md](CREDITS.md)。本キットは **MIT**（[LICENSE](LICENSE)）—— 自由に使い・改変し・配ってOKです。
