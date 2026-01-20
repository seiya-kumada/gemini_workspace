import os

from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv(override=True)

# Gemini設定
gemini_api_key = os.environ["GEMINI_API_KEY"]
gemini_model_name = os.environ.get("GEMINI_MODEL_NAME", "gemini-3-flash-preview")
