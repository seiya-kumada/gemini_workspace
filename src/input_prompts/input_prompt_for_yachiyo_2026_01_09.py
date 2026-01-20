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

    descriptions: list[str]


# 画像のみを入力とする場合のプロンプト
INPUT_PROMPT = (
    "# 提供するもの：\n"
    "- 画像を1枚与える。\n"
    "## 質問 \n"
    "- 画像には図面が描かれています。縮尺率がSとして記載されています。\n"
    "- Sを読み取ってください。\n"
    "- 読み取った文字をdescriptionに格納してください。\n"
)


def print_output(output: Output):
    """
    Geminiからのレスポンスを整形して表示

    Args:
        output: Geminiからのレスポンスモデル
    """
    for desc in output.descriptions:
        print(f"- {desc}")


def save_to_file(output: Output, output_path: str):
    """
    Geminiからのレスポンスをファイルに保存

    Args:
        output: Geminiからのレスポンスモデル
        output_path: 出力テキストファイルのパス
    """
    with open(output_path, "w") as f:
        for desc in output.descriptions:
            f.write(f"- {desc}\n")
