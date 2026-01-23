"""
Geminiへの入力プロンプトとレスポンスモデルの定義

このモジュールは、Geminiモデルに送信するプロンプトと、
期待されるレスポンスの構造を定義します。
"""

from pydantic import BaseModel


class Output(BaseModel):
    """
    Geminiからのレスポンスモデル

    Attributes:
        descriptions: 画像内容の説明文のリスト
    """

    description: str


# 画像のみを入力とする場合のプロンプト
INPUT_PROMPT = (
    "## 提供するもの：\n"
    "- 画像を1枚与える。\n"
    "## 質問 \n"
    "- 画像には手書き文字が書かれています。\n"
    "- 読み取り、descriptionに入れてください。\n"
)


def print_output(output: Output):
    """
    Geminiからのレスポンスを整形して表示

    Args:
        output: Geminiからのレスポンスモデル
    """
    print("=== Gemini Response ===")
    print(f"description: {output.description}")
    print("=======================")


def save_to_file(output: Output, output_path: str):
    """
    Geminiからのレスポンスをファイルに保存

    Args:
        output: Geminiからのレスポンスモデル
        output_path: 出力テキストファイルのパス
    """
    with open(output_path, "w") as f:
        f.write(f"description: {output.description}\n")
