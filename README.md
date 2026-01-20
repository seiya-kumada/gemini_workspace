# Gemini Workspace

Google Gemini API を使用した画像分析プロジェクト。

## セットアップ

### 1. 依存関係のインストール

```bash
uv sync
```

### 2. 環境変数の設定

`.env` ファイルを作成し、以下を設定：

```
GEMINI_API_KEY=your-api-key-here
GEMINI_MODEL_NAME=gemini-3-flash-preview  # オプション（デフォルト: gemini-3-flash-preview）
```

APIキーは [Google AI Studio](https://aistudio.google.com/) から取得できます。

## 使用方法

### シンプルなチャット（動作確認用）

```bash
uv run python -m src.main
```

### 画像分析

```bash
uv run python -m src.invoke_gemini \
    --input_path /path/to/image.jpg \
    --output_path /path/to/output.txt \
    --max_tokens 8192
```

オプション引数：
- `--input_path`: 入力画像ファイルのパス（必須）
- `--output_path`: 出力テキストファイルのパス（必須）
- `--max_tokens`: 最大出力トークン数（デフォルト: 8192）
- `--temperature`: 生成の温度パラメータ（0.0-2.0）
- `--top_p`: 核サンプリングパラメータ（0.0-1.0）

## プロジェクト構成

```
gemini_workspace/
├── src/
│   ├── main.py                 # 動作確認用シンプルチャット
│   ├── invoke_gemini.py        # 画像分析メイン処理
│   ├── utils.py                # 設定・ユーティリティ
│   └── input_prompts/          # プロンプト定義
│       └── input_prompt_for_yachiyo_2026_01_20.py
├── .env                        # 環境変数（git管理外）
├── pyproject.toml              # プロジェクト設定
└── README.md
```

## 利用可能なモデル

| モデル | 特徴 |
|--------|------|
| `gemini-3-flash-preview` | 最新・高精度（プレビュー） |
| `gemini-3-pro-preview` | 最新・最高精度（プレビュー） |
| `gemini-2.5-flash` | 本番向け・バランス型 |
| `gemini-2.0-flash` | 高速・低コスト |

## 料金

- 無料枠あり（レート制限付き）
- 有料枠: gemini-2.0-flash は $0.10/100万入力トークン、$0.40/100万出力トークン

詳細: https://ai.google.dev/gemini-api/docs/pricing
