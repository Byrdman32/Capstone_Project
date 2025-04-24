# Authors: Duncan Truitt
# File: functions.py
# Description: Contains misc functions used throughout the backend

import os
import re
import warnings
from pathlib import Path

def read_env_file(path):
    """
    Opens and reads a .env file, returns variable as key-value pairs.
    
    Parameters:
    path: Path to the .env file.
    
    Returns:
    Dictionary of environment variables.
    """

    reg_expression = r'^\w+=\w+$'
    # Check if the file exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")

    # Open the file and get contents
    else:
        with open(path, 'r') as file:
            lines = file.readlines()
            file.close()
        
        # Read in lines and parse them into a dictionary
        return_dict = dict()
        for line in lines:
            line = line.strip()
            if re.match(reg_expression, line):
                key, value = line.split('=')
                return_dict[key] = value
            else:

                # throw a warning if theres a line that doesnt expect matching format
                warnings.warn(f"Line '{line}' does not match the expected format 'KEY=VALUE'. Check the .env file")


    return return_dict