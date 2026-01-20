"""
Gemini APIの動作確認用シンプルチャット
"""

import os

from dotenv import load_dotenv
from google import genai

# .envファイルから環境変数を読み込む
result = load_dotenv()
print(f".env loaded: {result}")
# APIキーを環境変数から取得
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# クライアントを初期化
client = genai.Client(api_key=api_key)

# シンプルなチャットリクエスト
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="こんにちは！自己紹介をしてください。",
)

print(response.text)
