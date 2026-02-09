"""
GPT-4oへの入力プロンプトとレスポンスモデルの定義

このモジュールは、Azure OpenAI GPT-4oモデルに送信するプロンプトと、
期待されるレスポンスの構造を定義します。
"""

from pydantic import BaseModel


class Output(BaseModel):
    """
    GPT-4oからのレスポンスモデル

    """

    structured_description: str
    application_description: str
    process_prediction: str
    risk_description: str
    material_description: str


# 画像とOCR結果を入力とする場合のプロンプト
INPUT_PROMPT = (
    "## 提供するもの：\n"
    "- 画像を1枚与える。\n"
    "## 質問 \n"
    "- この画像には、ある物体を20個の視点から見た時のデプス画像がまとめられています。近いほど暗く、遠いほど白くなります。\n"
    "- その物体について構造の観点から詳細に説明し、structured_descriptionに格納しなさい。デプス画像なので色や材質については言及せず、形状や構造について詳しく説明してください。\n"
    "- 上の構造説明から、その物体の用途をきめ細かく想定し、application_descriptionに格納しなさい。\n"
    "- その物体を製造するためのプロセスを予測し、process_predictionに格納しなさい。\n"
    "- その物体の構造的リスクについて説明し、risk_descriptionに格納しなさい。\n"
    "- 上の構造説明や構造的リスクから適した材質・材料を予測し、material_descriptionに格納しなさい。\n"
)


def print_output(output: Output):
    """
    GPT-4oからのレスポンスを整形して表示

    Args:
        output: GPT-4oからのレスポンスモデル
    """
    print("=== GPT-4o Response ===")
    print(f"【構造の説明】{output.structured_description}")
    print(f"【用途の説明】{output.application_description}")
    print(f"【製造プロセスの予測】{output.process_prediction}")
    print(f"【構造的リスクの説明】{output.risk_description}")
    print(f"【材質・材料の説明】{output.material_description}")
    print("=======================")


def save_to_file(output: Output, output_path: str):
    """
    GPT-4oからのレスポンスをJSONファイルに保存

    Args:
        output: GPT-4oからのレスポンスモデル
        output_path: 出力テキストファイルのパス
    """
    with open(output_path, "w") as f:
        f.write(f"【構造の説明】{output.structured_description}\n")
        f.write(f"【用途の説明】{output.application_description}\n")
        f.write(f"【製造プロセスの予測】{output.process_prediction}\n")
        f.write(f"【構造的リスクの説明】{output.risk_description}\n")
        f.write(f"【材質・材料の説明】{output.material_description}")
