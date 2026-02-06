# Gemini Workspace

## プロジェクト概要
Google Gemini API を使用した画像・動画分析プロジェクト

## 開発コマンド
- 実行: `uv run python -m src.モジュール名`
- 依存関係追加: `uv add パッケージ名`
- 依存関係同期: `uv sync`

## コード規約

### プロンプト定義
- 配置場所: `src/input_prompts/input_prompt_for_xxx.py`
- 各ファイルに必須の要素:
  - `Output` クラス（Pydanticモデル）
  - `INPUT_PROMPT` 定数
  - `print_output(output: Output)` 関数
  - `save_to_file(output: Output, output_path: str)` 関数

### メインモジュール
- 画像分析: `src/invoke_gemini.py`
- 動画分析: `src/invoke_gemini_with_movie.py`
- プロンプトモジュールは `import src.input_prompts.xxx as ip` でインポート

### 環境変数
- `.env` ファイルに設定
- `GEMINI_API_KEY`: APIキー（必須）
- `GEMINI_MODEL_NAME`: モデル名（オプション、デフォルト: gemini-3-flash-preview）

## ファイル構成
```
src/
├── main.py                      # 動作確認用
├── invoke_gemini.py             # 画像分析
├── invoke_gemini_with_movie.py  # 動画分析
├── utils.py                     # 共通設定
└── input_prompts/               # プロンプト定義
```

## 構造化出力
- `response_mime_type="application/json"` と `response_schema=ip.Output` で構造化出力を使用
- レスポンスは `json.loads(response.text)` でパースし、`ip.Output(**result_dict)` で変換
