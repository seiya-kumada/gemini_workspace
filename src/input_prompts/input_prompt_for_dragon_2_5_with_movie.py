"""
Geminiへの入力プロンプトとレスポンスモデルの定義

このモジュールは、Geminiモデルに送信するプロンプトと、
期待されるレスポンスの構造を定義します。
"""

from pydantic import BaseModel, Field


class Output(BaseModel):
    """
    Geminiからのレスポンスモデル

    """

    structured_description: str = Field(description="物体の形状や構造についての詳細な説明。色や材質には言及しない。")


# 動画を入力とする場合のプロンプト
INPUT_PROMPT = (
    "## 提供するもの：\n"
    "- 動画を1本与える。\n"
    "## 動画内容 \n"
    "- この動画はある物体を3D表示し、x,y,z軸周りに回転した様子を撮影したものです。\n"
    "- 座標系は左手系です。\n"
    "- 最初にx軸周りに回転し、その後y軸、z軸の順に回転します。\n"
    "- 画面奥から手前の方向がz軸です。\n"
    "## 質問 \n"
    "- この動画を理解したあと、各フィールドの説明に従い回答しなさい。\n"
)


def print_output(output: Output):
    """
    Geminiからのレスポンスを整形して表示

    Args:
        output: Geminiからのレスポンスモデル
    """
    print("=== Gemini Response ===")
    print(f"【構造の説明】{output.structured_description}")
    print("=======================")


def save_to_file(output: Output, output_path: str):
    """
    GeminiからのレスポンスをJSONファイルに保存

    Args:
        output: Geminiからのレスポンスモデル
        output_path: 出力テキストファイルのパス
    """
    with open(output_path, "w") as f:
        f.write(f"【構造の説明】{output.structured_description}\n")
        f.write(f"【構造の説明】{output.structured_description}\n")
