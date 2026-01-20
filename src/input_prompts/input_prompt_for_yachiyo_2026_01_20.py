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

    ken_name: str
    zu_name: str


# 画像のみを入力とする場合のプロンプト
INPUT_PROMPT = (
    "# 提供するもの：\n"
    "- 画像を1枚与える。\n"
    "## 質問 \n"
    "- 画像には図面が描かれています。\n"
    "- 図面内の表から「件名」を読み取りken_nameに入れてください。\n"
    "- 図面内の表から「図名」を読み取りzu_nameに入れてください。\n"
)


def print_output(output: Output):
    """
    Geminiからのレスポンスを整形して表示

    Args:
        output: Geminiからのレスポンスモデル
    """
    print("=== Gemini Response ===")
    print(f"件名 (ken_name): {output.ken_name}")
    print(f"図名 (zu_name): {output.zu_name}")
    print("=======================")


def save_to_file(output: Output, output_path: str):
    """
    Geminiからのレスポンスをファイルに保存

    Args:
        output: Geminiからのレスポンスモデル
        output_path: 出力テキストファイルのパス
    """
    with open(output_path, "w") as f:
        f.write(f"件名 (ken_name): {output.ken_name}\n")
        f.write(f"図名 (zu_name): {output.zu_name}\n")
