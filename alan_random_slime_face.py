import random
import re

def generate_random_string(multiple_three=1):
    return ["".join([random.choice("ATCG") for __ in range(3)]) for _ in range(multiple_three)]

def import_text(path_to_text=None):

    # Check if input is provided
    if not path_to_text:
        path_to_text = input("Path to file here: ")

    path_to_text = re.sub("'", "", path_to_text)
    path_to_text = re.sub('"', "", path_to_text)
    path_to_text = path_to_text.strip()

    # Load text file
    _tmp_text = ""
    with open(path_to_text, "r") as _tmp_file:
        _tmp_text = _tmp_file.read()

    if not len(_tmp_text) % 3 == 0:
        raise Exception("Not multiple of 3")

    return _tmp_text
