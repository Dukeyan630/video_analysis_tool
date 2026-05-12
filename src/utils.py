import argparse
from pathlib import Path

def parse_args():
    paser = argparse.ArgumentParser(description="短视频数据解析工具")

    paser.add_argument(
        "--input",
        type=str,
        default = "data/test_project.xlsx",
        help="上传文件路径，支持解析xlsx和csv文件"
    )

    return parse_args()
