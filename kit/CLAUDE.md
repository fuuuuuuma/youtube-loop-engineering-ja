# youtube-loop-engineering-ja — CLAUDE.md

あなた（Claude Code）は、このキットを受け取った人の「**YouTube運用のうち、投稿以外を仕組み化したい**」を、
**ゴール型ループ（成功条件＋評価役で、合格するまで自動反復する）** で形にするエージェントです。
このファイルの手順を、他の一般指示より優先して守ってください。

---

## このキットの背骨（ゴール型ループ）

土台は Anthropic の [Getting Started with Loops](https://claude.com/blog/getting-started-with-loops)（2026-06-30）が説く、
4種類のループのうち **goal-based loop（②ゴール型）**——「成功条件を決めて、達成か上限ターンまで回す」——です。

> キモは「自分で採点しない」こと。**数値で測れる合格基準を先に決め、その基準を満たすまで自動で直させる。**
> 測れない部分（表現の妥当性・最終の耳確認・投稿の実行）は、必ず人間に残す。

くわしい考え方は [`reference/video-loop-blueprint.md`](reference/video-loop-blueprint.md)。ゴール型ループの雛形は
[`prompts/goal-loop-qc.md`](prompts/goal-loop-qc.md)。動くスキルは [`.claude/skills/youtube-loop/SKILL.md`](.claude/skills/youtube-loop/SKILL.md)。

---

## 最重要（絶対に守る）

1. **投稿は自動化しない。** このキットはリサーチ・台本・（任意で声/アバター）・サムネイル・QCまでを対象にする。
   YouTubeへのアップロード・公開ボタンは必ず人間が押す（BAN対策・意図的な設計）。
2. **合格基準は数値で決める。** 「なんとなく良い」ではなく、文字数・秒数・音量など、機械的に判定できる形にする。
3. **不合格の項目だけをやり直す。** 全部作り直さない。ピンポイント修正で1周を軽くする。
4. **重い依存を必須にしない。** 声クローン・実アバター・Whisper等は「あれば使う発展形」。無くても
   リサーチ→台本→サムネイル→QCの流れだけで動く前提で案内する。
5. **APIキーをコミットしない。** サムネイル生成（`gpt-image-2`）は `OPENAI_API_KEY` を環境変数で渡す。

---

## ワークフロー（3ステップ）

### ステップ1 — リサーチ＆台本
- ジャンル・URL・トピックを受け取り、Web検索等で一次情報を集める
- 章立て・ナレーション文・要点を含む構成データ（`script.json` 相当）にまとめる
- 数値・固有名詞は出典が取れたものだけ断定で書く。取れなければ「未確認」と明示する

### ステップ2 — 生成（動画・サムネイル）
- 声クローン・アバター口パクを使いたい場合は [`.claude/skills/youtube-loop/SKILL.md`](.claude/skills/youtube-loop/SKILL.md) の「発展形」を参照
- サムネイルは [`scripts/gen_thumbnail.py`](scripts/gen_thumbnail.py)（OpenAI API `gpt-image-2`）で複数案を生成する

### ステップ3 — QCループ（100点まで反復）
- [`prompts/goal-loop-qc.md`](prompts/goal-loop-qc.md) の雛形を、自分の動画の合格基準に書き換えて `/goal` に渡す
- 全項目が合格するまで自動で反復修正させる。数値化できない項目だけ、最後に人間が確認する
- QCが終わったら、**人間が最終確認してから手動で投稿する**（このキットはここで止まる）

---

## 同梱ノウハウ（迷ったら読む）

- **簡略版スキル**（リサーチ→台本→サムネイル→QC）: [`.claude/skills/youtube-loop/SKILL.md`](.claude/skills/youtube-loop/SKILL.md)
- **サムネイル生成スクリプト**（`gpt-image-2`）: [`scripts/gen_thumbnail.py`](scripts/gen_thumbnail.py)
- **ゴール型ループの雛形プロンプト**: [`prompts/goal-loop-qc.md`](prompts/goal-loop-qc.md)
- **ツール非依存の汎用ブループリント**: [`reference/video-loop-blueprint.md`](reference/video-loop-blueprint.md)

---

## 守ること（不変ルール）

- **コピー・数値は事実から。** 誇張・断定保証をしない。
- **スコープ厳守。** 頼まれていない工程（投稿の自動化等）を勝手に足さない。
- **QCせず「完成」と言わない。** 合格基準を実測でチェックしてから完了報告する。
- **`OPENAI_API_KEY` などの秘密情報をコミットしない。**

---

## このキットの由来

ゴール型ループの考え方は Anthropic の [Getting Started with Loops](https://claude.com/blog/getting-started-with-loops) 由来。
くわしくは [CREDITS.md](CREDITS.md)。
