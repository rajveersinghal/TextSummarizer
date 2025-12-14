import os
import yaml
from box.exceptions import BoxValueError
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
import logging



def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty or malformed.")
    except Exception as e:
        logging.error(f"Error reading YAML file {path_to_yaml}: {e}")
        raise e



def create_directories(path_to_directories: list, verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Directory created at: {path}")



def get_size(path: Path) -> str:
    """
    Returns the size of the file at the given path in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024, 2)
    return f"{size_in_kb} KB"