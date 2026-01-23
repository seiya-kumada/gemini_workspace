#!/bin/bash

#uv run python -m src.main

_/_/_/ 画像一枚をGPT4oに投げる。
ROOT_DIR_PATH="/home/kumada/data/cct_blog_handwriting_ocr/"
IMAGE_SUB_DIR_PATH="inputs"
FILE_NAME="hand_writing_sample_05"
OUTPUT_SUB_DIR_PATH="gemini_outputs"
MAX_TOKENS=8192
TOP_P=1.0
TEMPERATURE=0.0
uv run python -m src.invoke_gemini \
    --input_path ${ROOT_DIR_PATH}/${IMAGE_SUB_DIR_PATH}/${FILE_NAME}.png \
    --output_path ${ROOT_DIR_PATH}/${OUTPUT_SUB_DIR_PATH}/${FILE_NAME}.txt \
    --max_tokens ${MAX_TOKENS} \
    --top_p ${TOP_P} \
    --temperature ${TEMPERATURE}
