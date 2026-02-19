#!/bin/bash

#uv run python -m src.main

#_/_/_/ 画像1枚をGeminiに投げる。
#ROOT_DIR_PATH="/home/kumada/data/depth_image_aligner/"
#IMAGE_SUB_DIR_PATH="images"
#FILE_NAME="C_Sample3"
#OUTPUT_SUB_DIR_PATH="gemini_outputs"
#MAX_TOKENS=8192
#TOP_P=1.0
#TEMPERATURE=0.0
#uv run python -m src.invoke_gemini \
#    --input_path "${ROOT_DIR_PATH}/${IMAGE_SUB_DIR_PATH}/${FILE_NAME}.jpg" \
#    --output_path "${ROOT_DIR_PATH}/${OUTPUT_SUB_DIR_PATH}/${FILE_NAME}.txt" \
#    --max_tokens ${MAX_TOKENS} \
#    --top_p ${TOP_P} \
#    --temperature ${TEMPERATURE}

#_/_/_/ 動画一本をGeminiに投げる。
#ROOT_DIR_PATH="/home/kumada/data/gemini_workspace/"
#IMAGE_SUB_DIR_PATH="movies"
#FILE_NAME="C_Sample3"
#OUTPUT_SUB_DIR_PATH="outputs"
#MAX_TOKENS=8192
#TOP_P=1.0
#TEMPERATURE=0.0
#uv run python -m src.invoke_gemini_with_movie \
#    --input_path "${ROOT_DIR_PATH}/${IMAGE_SUB_DIR_PATH}/${FILE_NAME}.mp4" \
#    --output_path "${ROOT_DIR_PATH}/${OUTPUT_SUB_DIR_PATH}/${FILE_NAME}.txt" \
#    --max_tokens ${MAX_TOKENS} \
#    --top_p ${TOP_P} \
#    --temperature ${TEMPERATURE}

#_/_/_/ 画像2枚をGeminiに投げる。
#ROOT_DIR_PATH="/home/kumada/data/gemini_workspace/"
#IMAGE_SUB_DIR_PATH="images"
#FILE_NAME_1="C_Sample3"
#FILE_NAME_2="zumen"
#OUTPUT_SUB_DIR_PATH="outputs"
#MAX_TOKENS=8192
#TOP_P=1.0
#TEMPERATURE=0.0
#uv run python -m src.invoke_gemini_with_two_images \
#    --input_path_1 "${ROOT_DIR_PATH}/${IMAGE_SUB_DIR_PATH}/${FILE_NAME_1}.jpg" \
#    --input_path_2 "${ROOT_DIR_PATH}/${IMAGE_SUB_DIR_PATH}/${FILE_NAME_2}.png" \
#    --output_path "${ROOT_DIR_PATH}/${OUTPUT_SUB_DIR_PATH}/${FILE_NAME_1}_${FILE_NAME_2}.txt" \
#    --max_tokens ${MAX_TOKENS} \
#    --top_p ${TOP_P} \
#    --temperature ${TEMPERATURE}

#_/_/_/ 動画1本と画像1枚をGeminiに投げる。
ROOT_DIR_PATH="/home/kumada/data/gemini_workspace/"
MOVIE_SUB_DIR_PATH="movies"
IMAGE_SUB_DIR_PATH="images"
MOVIE_FILE_NAME="C_Sample3"
IMAGE_FILE_NAME="zumen"
OUTPUT_SUB_DIR_PATH="outputs"
MAX_TOKENS=8192
TOP_P=1.0
TEMPERATURE=0.0
uv run python -m src.invoke_gemini_with_image_and_movie \
    --image_path "${ROOT_DIR_PATH}/${IMAGE_SUB_DIR_PATH}/${IMAGE_FILE_NAME}.png" \
    --movie_path "${ROOT_DIR_PATH}/${MOVIE_SUB_DIR_PATH}/${MOVIE_FILE_NAME}.mp4" \
    --output_path "${ROOT_DIR_PATH}/${OUTPUT_SUB_DIR_PATH}/${MOVIE_FILE_NAME}_${IMAGE_FILE_NAME}.txt" \
    --max_tokens ${MAX_TOKENS} \
    --top_p ${TOP_P} \
    --temperature ${TEMPERATURE}
