"""
画像をGeminiで分析するモジュール

このモジュールは、単一の画像ファイルをGeminiに送信し、
画像の内容を分析・説明してもらいます。
"""

import argparse
import json
import os

from google import genai
from google.genai import types

import src.input_prompts.input_prompt_for_yachiyo_2026_01_20 as ip
import src.utils as utils


def extract_args() -> argparse.Namespace:
    """
    コマンドライン引数を解析する

    Returns:
        argparse.Namespace: 解析された引数
            - input_path: 入力画像ファイルのパス
            - output_path: 出力テキストファイルのパス
            - max_tokens: 最大出力トークン数
            - temperature: 生成の温度パラメータ（0.0-2.0、低いほど確定的）
            - top_p: 生成のtop_pパラメータ（0.0-1.0、核サンプリング）
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path")
    parser.add_argument("--output_path")
    parser.add_argument("--max_tokens", type=int, default=8192)
    parser.add_argument("--temperature", type=float, default=None)
    parser.add_argument("--top_p", type=float, default=None)
    return parser.parse_args()


def load_image(filename: str) -> types.Part:
    """
    画像ファイルを読み込んでGemini API用のPartオブジェクトを生成

    Args:
        filename: 画像ファイルのパス

    Returns:
        types.Part: Gemini APIリクエスト用の画像データ
    """
    with open(filename, "rb") as image_file:
        image_data = image_file.read()

    # ファイル拡張子からMIMEタイプを判定
    ext = os.path.splitext(filename)[1].lower()
    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    mime_type = mime_types.get(ext, "image/jpeg")

    return types.Part.from_bytes(data=image_data, mime_type=mime_type)


if __name__ == "__main__":
    # コマンドライン引数を取得
    args = extract_args()
    assert os.path.exists(args.input_path)

    # Geminiクライアントを初期化
    client = genai.Client(api_key=utils.gemini_api_key)

    # 画像を読み込み
    image = load_image(args.input_path)
    prompt = ip.INPUT_PROMPT

    print(prompt)

    # 生成設定を構築
    generation_config = types.GenerateContentConfig(
        max_output_tokens=args.max_tokens,
        response_mime_type="application/json",
        response_schema=ip.Output,
    )

    if args.temperature is not None:
        generation_config.temperature = args.temperature
    if args.top_p is not None:
        generation_config.top_p = args.top_p

    # Geminiにリクエストを送信
    response = client.models.generate_content(
        model=utils.gemini_model_name,
        contents=[prompt, image],
        config=generation_config,
    )

    if response.text is None:
        raise ValueError("Gemini returned empty response")

    result_dict = json.loads(response.text)
    result = ip.Output(**result_dict)

    ip.print_output(result)

    # 結果をファイルに保存
    output_path = os.path.join(args.output_path)
    ip.save_to_file(result, output_path)
