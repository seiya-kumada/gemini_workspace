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
    "- あなたはプレストレストコンクリート（PC）構造に精通した構造設計・施工管理エンジニアです。\n"
    "## 質問 \n"
    "- 画像は、「PC鋼材定着部詳細図」です。\n"
    "- この図面から「PC鋼材の定着方式・定着具構成・耐久性に直接関係する要素」のみを、簡潔なキーワードとして抽出し、itemsに入れてください。\n"
    "## 抽出対象 \n"
    "- 定着方式（例：くさび定着、ねじ定着、固定端／緊張端）\n"
    "- 定着具構成要素（例：アンカーヘッド、アンカープレート、グラウトキャップ、アンカーキャップ）\n"
    "- PC鋼材情報（例：PC鋼より線、1S15.2、1S21.8、本数、束ね方）\n"
    "- グラウト・防錆・充填に関する要素（例：セメントグラウト、グリース、充填確認孔、排気孔）\n"
    "- 定着部補強に関する要素（例：定着補強筋、割裂防止筋、局部補強）\n"
    "## 注意点\n"
    "- 表記ゆれは正規化する（例：「PC鋼より線」「PCストランド」→「PC鋼より線」）\n"
    "- 数値は意味を持つもののみ記載\n"
    "- 同一内容は1回のみ抽出する。\n"
    "- 不明確な情報は推定せず抽出しない。\n"
    "## 抽出例\n"
    "- くさび定着方式\n"
    "- 緊張端\n"
    "- アンカープレート\n"
    "- ウェッジ\n"
    "- PC鋼より線 1S21.8 × 4本\n"
    "- グラウトキャップ\n"
    "- 定着部補強筋\n"
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
