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
    "- あなたは橋梁・PC構造物に精通した構造設計・施工管理エンジニアです。\n"
    "## 質問 \n"
    "- 画像は、「主桁配筋図」です。\n"
    "- この図面から「主桁の構造性能・施工・加工に直接影響する配筋情報」のみを、簡潔なキーワードとして抽出し、itemsに入れてください。\n"
    "## 抽出対象 \n"
    "- 主鉄筋・配力筋・せん断補強筋の情報（鉄筋径、ピッチ、段配筋、2段・3段配筋）\n"
    "- 鉄筋の配置条件（上縁・下縁、腹部、ウェブ、フランジ）\n"
    "- 継手・定着に関する情報（重ね継手、機械式継手、定着長、フック）\n"
    "- 部位別補強情報（支点部補強、開口補強、端部補強）\n"
    "- 施工・加工に影響する指定（曲げ加工、組立順序、干渉注意、現場調整）\n"
    "## 注意点\n"
    "- 表記ゆれを正規化する。\n"
    "- 同一内容は1回のみ抽出する。\n"
    "- 不明確な場合は抽出しない。\n"
    "## 抽出例\n"
    "- 下縁主鉄筋 D32@150\n"
    "- 上縁配力筋 D19@200\n"
    "- せん断補強筋 D13@100（支点部）\n"
    "- 重ね継手\n"
    "- 定着長確保\n"
    "- 端部補強筋\n"
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
