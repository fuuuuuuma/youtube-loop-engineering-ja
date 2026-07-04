#!/usr/bin/env python3
"""GPT Image 2.0（gpt-image-2）でYouTubeサムネイル画像を1枚生成する最小スクリプト。

Claude Code から呼ぶ前提。OpenAI Images API を直接叩く（標準ライブラリのみ・依存なし）。

前提:
  export OPENAI_API_KEY=sk-...        # 必須（OpenAI Developers のキー）

使い方:
  python3 scripts/gen_thumbnail.py --title "YouTube自動運用ループ徹底解説" \
      --description "投稿以外を全部自動化する、という考え方の解説動画" \
      --out thumbnail.png

サイズ:
  YouTubeサムネイルの推奨比率は16:9。gpt-image-2 は 1536x1024（横長）が近い比率になる。

注意:
  - パラメータは OpenAI Images API に準拠。仕様変更時は body を調整する。
  - 画像内の日本語テキストは高精度だが、生成後に誤字・崩れを必ず目視で確認すること。
  - 複数案を生成して比較したい場合は --n を増やす（1枚ずつ連番で保存される）。
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-2"


def build_prompt(title: str, description: str) -> str:
    return (
        f"YouTubeサムネイル画像。タイトル「{title}」の内容が一目でわかる構図。"
        f"補足: {description}。"
        "文字は大きく読みやすいフォントで、背景とのコントラストを高くする。"
        "被写体は画面中央〜やや左寄りに配置し、右側にタイトル文字のスペースを空ける。"
        "誇張した表現・煽り立てる装飾は避け、清潔感のあるデザインにする。"
    )


def generate(prompt: str, size: str, out: str, quality: str, n: int) -> None:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        sys.exit("OPENAI_API_KEY が未設定です。`export OPENAI_API_KEY=...` を実行してください。")

    payload = {"model": MODEL, "prompt": prompt, "size": size, "n": n}
    if quality and quality != "auto":
        payload["quality"] = quality
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"API エラー {e.code}: {e.read().decode('utf-8', 'ignore')[:600]}")
    except urllib.error.URLError as e:
        sys.exit(f"接続エラー: {e}")

    items = data.get("data") or []
    if not items:
        sys.exit(f"画像データを取得できませんでした: {json.dumps(data)[:400]}")

    base, ext = os.path.splitext(out)
    ext = ext or ".png"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)

    for i, item in enumerate(items):
        if item.get("b64_json"):
            img = base64.b64decode(item["b64_json"])
        elif item.get("url"):
            with urllib.request.urlopen(item["url"], timeout=300) as r:
                img = r.read()
        else:
            print(f"警告: {i}番目の画像データが取得できませんでした", file=sys.stderr)
            continue

        path = out if len(items) == 1 else f"{base}-{i+1}{ext}"
        with open(path, "wb") as f:
            f.write(img)
        print(path)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate YouTube thumbnail(s) with GPT Image 2.0")
    ap.add_argument("--title", required=True, help="動画タイトル")
    ap.add_argument("--description", default="", help="動画の要点（1〜2文）")
    ap.add_argument("--size", default="1536x1024", help="例 1536x1024（16:9に近い横長）")
    ap.add_argument("--out", required=True, help="保存先パス（例 thumbnail.png）。--n>1なら連番で保存")
    ap.add_argument("--quality", default="high", choices=["low", "medium", "high", "auto"])
    ap.add_argument("--n", type=int, default=1, help="生成する案の数（複数案を比較したいとき）")
    args = ap.parse_args()
    prompt = build_prompt(args.title, args.description)
    generate(prompt, args.size, args.out, args.quality, args.n)
