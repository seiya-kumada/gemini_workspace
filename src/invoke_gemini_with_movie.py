"""
動画をGeminiで分析するモジュール

このモジュールは、動画ファイルをGeminiに送信し、
動画の内容を分析・説明してもらいます。
"""

import argparse
import json
import os

from google import genai
from google.genai import types

import src.input_prompts.input_prompt_for_dragon_2_5_with_movie as ip
import src.utils as utils


def extract_args() -> argparse.Namespace:
    """
    コマンドライン引数を解析する

    Returns:
        argparse.Namespace: 解析された引数
            - input_path: 入力動画ファイルのパス
            - output_path: 出力テキストファイルのパス
            - max_tokens: 最大出力トークン数
            - temperature: 生成の温度パラメータ（0.0-2.0、低いほど確定的）
            - top_p: 生成のtop_pパラメータ（0.0-1.0、核サンプリング）
    """
    parser = argparse.ArgumentParser(description="動画をGeminiで分析する")
    parser.add_argument("--input_path", required=True, help="入力動画ファイルのパス")
    parser.add_argument("--output_path", required=True, help="出力テキストファイルのパス")
    parser.add_argument("--max_tokens", type=int, default=8192, help="最大出力トークン数")
    parser.add_argument("--temperature", type=float, default=None, help="温度パラメータ")
    parser.add_argument("--top_p", type=float, default=None, help="top_pパラメータ")
    return parser.parse_args()


def load_video(filename: str) -> types.Part:
    """
    動画ファイルを読み込んでGemini API用のPartオブジェクトを生成

    Args:
        filename: 動画ファイルのパス

    Returns:
        types.Part: Gemini APIリクエスト用の動画データ
    """
    with open(filename, "rb") as video_file:
        video_data = video_file.read()

    # ファイル拡張子からMIMEタイプを判定
    ext = os.path.splitext(filename)[1].lower()
    mime_types = {
        ".mp4": "video/mp4",
        ".mpeg": "video/mpeg",
        ".mpg": "video/mpeg",
        ".mov": "video/quicktime",
        ".avi": "video/x-msvideo",
        ".flv": "video/x-flv",
        ".mkv": "video/x-matroska",
        ".webm": "video/webm",
        ".wmv": "video/x-ms-wmv",
        ".3gp": "video/3gpp",
    }
    mime_type = mime_types.get(ext, "video/mp4")

    return types.Part.from_bytes(data=video_data, mime_type=mime_type)


if __name__ == "__main__":
    # コマンドライン引数を取得
    args = extract_args()
    assert os.path.exists(args.input_path), f"入力ファイルが存在しません: {args.input_path}"

    # Geminiクライアントを初期化
    client = genai.Client(api_key=utils.gemini_api_key)

    # 動画を読み込み
    video = load_video(args.input_path)
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
        contents=[prompt, video],
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
