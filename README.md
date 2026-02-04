# Gemini Workspace

Google Gemini API を使用した画像・動画分析プロジェクト。

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

### 動画分析

```bash
uv run python -m src.invoke_gemini_with_movie \
    --input_path /path/to/video.mp4 \
    --output_path /path/to/output.txt \
    --max_tokens 8192
```

### 共通オプション引数

| 引数 | 説明 | デフォルト |
|------|------|----------|
| `--input_path` | 入力ファイルのパス（必須） | - |
| `--output_path` | 出力テキストファイルのパス（必須） | - |
| `--max_tokens` | 最大出力トークン数 | 8192 |
| `--temperature` | 温度パラメータ（0.0-2.0、低いほど確定的） | None |
| `--top_p` | 核サンプリングパラメータ（0.0-1.0） | None |

## プロジェクト構成

```
gemini_workspace/
├── src/
│   ├── main.py                      # 動作確認用シンプルチャット
│   ├── invoke_gemini.py             # 画像分析メイン処理
│   ├── invoke_gemini_with_movie.py  # 動画分析メイン処理
│   ├── utils.py                     # 設定・ユーティリティ
│   └── input_prompts/               # プロンプト定義
│       ├── input_prompt_for_xxx.py  # 各タスク用プロンプト
│       └── ...
├── .env                             # 環境変数（git管理外）
├── pyproject.toml                   # プロジェクト設定
└── README.md
```

## 対応ファイル形式

### 画像
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)

### 動画
- MP4 (.mp4)
- MPEG (.mpeg, .mpg)
- MOV (.mov)
- AVI (.avi)
- MKV (.mkv)
- WebM (.webm)
- その他（最大10MB程度）

## 利用可能なモデル

| モデル | 特徴 |
|--------|------|
| `gemini-3-pro-preview` | 最高精度。マルチモーダル理解に最強 |
| `gemini-3-pro-image-preview` | 画像生成+理解の両方に対応（Nano Banana Pro） |
| `gemini-3-flash-preview` | 速度・コスト・性能のバランス型 |
| `gemini-2.5-pro` | 安定版。コード・数学・STEM推論に強い |
| `gemini-2.5-flash` | 安定版。コスパが良い |
| `gemini-2.0-flash` | 旧世代。高速・低コスト |

## 料金

- 無料枠あり（レート制限付き）
- 有料枠（100万トークンあたり）:
  - gemini-3-flash-preview: 入力 $0.50 / 出力 $3.00
  - gemini-2.0-flash: 入力 $0.10 / 出力 $0.40

詳細: https://ai.google.dev/gemini-api/docs/pricing
