#!/bin/bash

#uv run python -m src.main

_/_/_/ 画像一枚をGPT4oに投げる。
ROOT_DIR_PATH="/home/kumada/data/yachiyo_red_text_detection/"
IMAGE_SUB_DIR_PATH="images/手書き赤黄チェック_1/dpi_200"
FILE_NAME="手書き赤黄チェック_1_4"
OUTPUT_SUB_DIR_PATH="gemini_outputs"
MAX_TOKENS=8192
TOP_P=1.0
TEMPERATURE=0.0
uv run python -m src.invoke_gemini \
    --input_path ${ROOT_DIR_PATH}/${IMAGE_SUB_DIR_PATH}/${FILE_NAME}.jpg \
    --output_path ${ROOT_DIR_PATH}/${OUTPUT_SUB_DIR_PATH}/${FILE_NAME}.txt \
    --max_tokens ${MAX_TOKENS} \
    --top_p ${TOP_P} \
    --temperature ${TEMPERATURE}
