#! /usr/bin/env python3
import os
import argparse
from PIL import Image
import numpy as np


# python creatDummyImage.py -b [画像生成位置] -s [画像サイズ（MB）] -n [生成数]
# 使用例：python creatDummyImage.py -b ./ -s 10 -n 5
def create_large_image(file_path, target_size_mb):
    target_size_bytes = target_size_mb * 1048576  # 1048576バイトは10メガバイト（PC上は10.5MBくらいとなる）
    num_pixels = target_size_bytes // 3
    dimension = int(np.sqrt(num_pixels))
    image = Image.fromarray(
        np.random.randint(0, 256, (dimension, dimension, 3), dtype=np.uint8)
    )
    image.save(file_path)
    return file_path


def create_multiple_large_images(base_path, target_size_mb, num_images):
    created_image_paths = []
    for i in range(num_images):
        # Generate an image
        file_path = f"{base_path}{i}.png"
        create_large_image(file_path, target_size_mb)
        created_image_paths.append(file_path)
    return created_image_paths


parser = argparse.ArgumentParser(description="Generate large random images.")
parser.add_argument(
    "-b", "--base_path", type=str, required=True, help="Base path for image generation"
)
parser.add_argument(
    "-s", "--size", type=int, required=True, help="Target size of the images in MB"
)
parser.add_argument(
    "-n", "--num", type=int, required=True, help="Number of images to generate"
)
args = parser.parse_args()

base_path = args.base_path
target_size_mb = args.size
num_images = args.num

created_image_paths = create_multiple_large_images(
    base_path, target_size_mb, num_images
)
