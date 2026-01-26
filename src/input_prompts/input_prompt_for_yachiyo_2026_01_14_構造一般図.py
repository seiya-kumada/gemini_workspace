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
    "- あなたは橋梁・PC構造物の基本設計を担当する構造設計エンジニアです。\n"
    "## 質問 \n"
    "- 画像は、「構造一般図」です。\n"
    "- この図面から「構造物の全体像・構造形式・設計条件を最も特徴づける情報」のみを、簡潔なキーワードとして抽出し、itemsに入れてください。\n"
    "## 抽出対象 \n"
    "- 構造物の種類・用途（橋梁、桁橋、歩道橋、高架構造 等）\n"
    "- 構造形式（PC単純桁、PC連続箱桁、RCラーメン 等）\n"
    "- 支間構成（単径間／多径間、支間長、連続条件）\n"
    "- 主構造寸法（桁高、橋長、幅員）\n"
    "- 支承条件（固定・可動、支承形式）\n"
    "- 設計条件・設計区分（活荷重区分、設計基準、耐震区分）\n"
    "## 注意点\n"
    "- 表記ゆれを正規化する。（例：「プレストレストコンクリート橋」→「PC橋」）\n"
    "- 数値は意味を持つもののみ記載（例：支間長 40m）\n"
    "- 同一内容は1回のみ抽出する。\n"
    "- 不明確な情報は推定せず抽出しない。\n"
    "## 抽出例\n"
    "- PC橋\n"
    "- PC連続箱桁\n"
    "- 3径間連続\n"
    "- 支間長 45m + 60m + 45m\n"
    "- 桁高 2.5m\n"
    "- 固定支承＋可動支承\n"
    "- 道路橋示方書\n"
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
