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
    part_description: str = Field(
        description="いくつの部品から構成された物体かの説明。部品ごとに、形状や構造についての詳細な説明を行う。色や材質には言及しない。"
    )
    application_description: str = Field(description="構造説明から想定される物体の用途。")
    process_prediction: str = Field(description="物体を製造するためのプロセスの予測。")
    risk_description: str = Field(description="物体の構造的リスクの説明。")
    material_description: str = Field(description="構造や構造的リスクから予測される最適な材質・材料の説明。")


# 画像とOCR結果を入力とする場合のプロンプト
INPUT_PROMPT = (
    "## 提供するもの：\n"
    "- 画像を1枚与える。\n"
    "## 画像の説明 \n"
    "- この画像には、20枚の画像がまとめられています。\n"
    "- それぞれがデプス画像です。近いほど暗く、遠いほど白くなります。\n"
    "- 仮想的な球の中心に物体を置き、その物体を様々な視点から撮影したものです。\n"
    "- 視点は北極点（画像左上）からスタートし、赤道を通って南極点（画像左下）まで、等間隔で配置されています。\n"
    "- 北極点と南極点以外では、緯線に沿ってぐるっと一周しています。\n"
    "## 質問 \n"
    "- この画像を理解したあと、各フィールドの説明に従い回答しなさい。\n"
)


def print_output(output: Output):
    """
    Geminiからのレスポンスを整形して表示

    Args:
        output: Geminiからのレスポンスモデル
    """
    print("=== Gemini Response ===")
    print(f"【構造の説明】{output.structured_description}")
    print(f"【部品の説明】{output.part_description}")
    print(f"【用途の説明】{output.application_description}")
    print(f"【製造プロセスの予測】{output.process_prediction}")
    print(f"【構造的リスクの説明】{output.risk_description}")
    print(f"【材質・材料の予測】{output.material_description}")
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
        f.write(f"【部品の説明】{output.part_description}\n")
        f.write(f"【用途の説明】{output.application_description}\n")
        f.write(f"【製造プロセスの予測】{output.process_prediction}\n")
        f.write(f"【構造的リスクの説明】{output.risk_description}\n")
        f.write(f"【材質・材料の予測】{output.material_description}\n")
