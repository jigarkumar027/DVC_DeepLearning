import os
from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd

def get_data(config_path):
    config = read_yaml(config_path)

    source_donwload_dirs = config['source_download_dirs']


if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(parsed_args.config)