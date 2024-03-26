import os
from box.exceptions import BoxValueError

#The YAML module in Python is used to work with YAML (YAML Ain't Markup Language) data. 
# YAML is a human-readable data serialization format commonly used for configuration files, 
# data exchange, and other purposes. The yaml module provides functions to parse YAML data into Python data structures 
# (e.g., dictionaries, lists), and to serialize Python data structures into YAML format.
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations

def read_yaml(path_to_yaml:path) -> ConfigBox:
    """reads yaml files and return

    Args:
        path_to_yaml (path): path like input

    Raises:
        ValueError: if ymal file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    """create a list of directories

    Args:
        path_to_directories (list): list of path directories
        verbose (bool, optional): ignore if multiple directories to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")
            
@ensure_annotations
def get_size(path:path) -> str:
    """Get size in KB

    Args:
        path (path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb =round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"