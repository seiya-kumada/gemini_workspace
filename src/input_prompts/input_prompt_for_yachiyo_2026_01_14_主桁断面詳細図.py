"""
GPT-4oへの入力プロンプトとレスポンスモデルの定義

このモジュールは、Azure OpenAI GPT-4oモデルに送信するプロンプトと、
期待されるレスポンスの構造を定義します。
"""

from pydantic import BaseModel


class Output(BaseModel):
    """
    GPT-4oからのレスポンスモデル

    Attributes:
        description: 画像内容の説明文
    """

    items: list[str]


# 画像とOCR結果を入力とする場合のプロンプト
INPUT_PROMPT = (
    "## 提供するもの：\n"
    "- 画像一枚を与える。\n"
    "## 前提 \n"
    "- あなたは橋梁・PC構造物の詳細設計を担当する構造設計エンジニアです。\n"
    "## 質問 \n"
    "- 画像は、「主桁断面詳細図」です。\n"
    "- この図面から「主桁断面の形状特性・構造成立条件・局部補強を最も特徴づける情報」のみを、簡潔なキーワードとして抽出し、itemsに入れてください。\n"
    "## 抽出対象 \n"
    "- 断面形式（箱桁、T桁、I桁、多室箱桁 等）\n"
    "- 断面主要寸法（桁高、床版厚、ウェブ厚、フランジ厚）\n"
    "- 断面内構成（ウェブ数、リブ、横桁、隔壁）\n"
    "- 局部補強・増厚部（支点部増厚、定着部増厚、補強リブ）\n"
    "- せん断・ねじり抵抗要素（閉断面、スターラップ密、ねじり補強）\n"
    "- 断面内配置条件（PC鋼材通過空間、点検孔、作業空間）\n"
    "## 注意点\n"
    "- 表記ゆれは正規化する（例：「PC鋼より線」「PCストランド」→「PC鋼より線」\n"
    "- 寸法は断面を特徴づけるもののみ記載。\n"
    "- 類似寸法は代表値にまとめる。\n"
    "- 不明な情報は推定せず記載しない。\n"
    "## 抽出例\n"
    "- 単室箱桁\n"
    "- 桁高 2.5m\n"
    "- 床版厚 250mm\n"
    "- ウェブ厚 300mm\n"
    "- 支点部増厚\n"
    "- 閉断面\n"
    "- PC鋼材通過空間確保\n"
)


def print_output(output: Output):
    """
    GPT-4oからのレスポンスを整形して表示

    Args:
        output: GPT-4oからのレスポンスモデル
    """
    print("- 抽出された特徴名称:")
    for item in output.items:
        print(f"    > {item}")


def save_to_file(output: Output, output_path: str):
    """
    GPT-4oからのレスポンスをJSONファイルに保存

    Args:
        output: GPT-4oからのレスポンスモデル
        output_path: 出力テキストファイルのパス
    """
    with open(output_path, "w") as f:
        f.write("- 抽出された特徴名称:\n")
        for item in output.items:
            f.write(f"    > {item}\n")
