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
    "- あなたはPC橋梁の設計・施工計画に精通した構造設計・施工管理エンジニアです。\n"
    "## 質問\n"
    "- 画像は、「PC鋼材配置図」です。\n"
    "- この図面から「PC鋼材の配置計画・系統構成・構造的意図を最も特徴づける情報」のみを、簡潔なキーワードとして抽出し、itemsに入れてください。\n"
    "## 抽出対象 \n"
    "- PC鋼材の種類・仕様（PC鋼より線、1S15.2、1S21.8、本数、束ね本数）\n"
    "- ケーブル（テンドン）系統情報（ケーブル番号：C102 等、系統数）\n"
    "- 配置位置・配置条件（上縁／下縁、ウェブ内、偏心量、配置高さ）\n"
    "- 配置形状・経路（直線配置、曲線配置、ドレープ形状、放物線）\n"
    "- 区間別配置条件（支点部／中央部、配置変更区間）\n"
    "- 緊張条件の区別（緊張端／固定端、片引き／両引き）\n"
    "## 注意点\n"
    "- 表記ゆれを正規化する。（例：「1S-15.2」「15.2mm」→「1S15.2」）\n"
    "- 数値は意味を持つもののみ記載\n"
    "- 同一内容は1回のみ抽出する。\n"
    "- ケーブル番号と仕様は可能な限りセットで記載\n"
    "- 不明確な情報は推定せず抽出しない。\n"
    "## 抽出例\n"
    "- PC鋼より線 1S15.2\n"
    "- ケーブル C102\n"
    "- 1系統4本束\n"
    "- 下縁配置\n"
    "- ドレープ配置\n"
    "- 支点部偏心大\n"
    "- 両引き緊張\n"
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
