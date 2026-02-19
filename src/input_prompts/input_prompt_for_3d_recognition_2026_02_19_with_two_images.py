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
    application_description: str = Field(description="構造説明から想定される物体の用途。")
    process_prediction: str = Field(description="物体を製造するためのプロセスの予測。")
    risk_description: str = Field(description="物体の構造的リスクの説明。")
    material_description: str = Field(description="構造や構造的リスクから予測される最適な材質・材料の説明。")


# 画像とOCR結果を入力とする場合のプロンプト
INPUT_PROMPT = (
    "## 提供するもの：\n"
    "- 画像を2枚与える。\n"
    "## 質問 \n"
    "- 1枚目の画像には、ある物体を20個の視点から見た時のデプス画像がまとめられています。近いほど暗く、遠いほど白くなります。\n"
    "- 2枚目の画像は、この物体の2D図面です。さまざまな記号と寸法が含まれています。\n"
    "- これら2枚の画像を理解したあと、各フィールドの説明に従い回答しなさい。\n"
)


def print_output(output: Output):
    """
    Geminiからのレスポンスを整形して表示

    Args:
        output: Geminiからのレスポンスモデル
    """
    print("=== Gemini Response ===")
    print(f"【構造の説明】{output.structured_description}")
    print(f"【用途の説明】{output.application_description}")
    print(f"【製造プロセスの予測】{output.process_prediction}")
    print(f"【構造的リスクの説明】{output.risk_description}")
    print(f"【材質・材料の説明】{output.material_description}")
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
        f.write(f"【用途の説明】{output.application_description}\n")
        f.write(f"【製造プロセスの予測】{output.process_prediction}\n")
        f.write(f"【構造的リスクの説明】{output.risk_description}\n")
        f.write(f"【材質・材料の説明】{output.material_description}")
