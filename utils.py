import random
import re
import constants


def generate_random_string(multiple_three=1):
    """
    Generate list of 3 characters

    Arguments
    ---------
    multiple_three (int)
        The length in which list should be

    Returns
    -------
    list
        List containing string with length 3
    """

    rand_list = []

    for count in range(multiple_three):
        rand_string = "".join([random.choice("ATCG") for _ in range(3)])
        rand_list.append(rand_string)

    return rand_list


def import_sequence(path_to_text, ignore_length=False):
    """
    Load the sequence from path

    Also verify the sequence length to be multiple of 3s
    and ignore if specified

    Arguments
    ---------
    path_to_text (str)
        Path to the sequence
    ignore_length (bool:False)
        Ignore the length of the sequence

    Returns
    -------
    str
        The sequence of DNA
    """

    # Remove quotes if there is any
    path_to_text = re.sub("'", "", path_to_text)
    path_to_text = re.sub('"', "", path_to_text)
    path_to_text = path_to_text.strip()

    # Load text file
    _tmp_text = ""
    with open(path_to_text, "r") as _tmp_file:
        _tmp_text = _tmp_file.read()

    # Verify that the sequence is multiple of 3
    if not len(_tmp_text) % 3 == 0:
        raise NotMultipleOf3("Not multiple of 3")

    return _tmp_text


def splice_sequence(string_sequence):
    """
    Splice the sequence of text to set of 3s

    This assumes that the string sequence multiple of 3

    Arguments
    ---------
    string_sequence (str)
        The string sequence of multiple of 3

    Returns
    -------
    List
        The list of 3 character strings
    """

    seq_list = []
    n_sets = (int)(len(string_sequence) / 3)

    for set_count in range(n_sets):
        seq_list.append(string_sequence[set_count: set_count+3])

    return seq_list


def translate_sequence(list_of_char_sequence):
    """
    Translate a sequence into genetic code

    Arguments
    ---------
    list_of_char_sequence ([str])
        The list of genetic code

    Returns
    -------
    list of string
        ["genetic code here", ...]
    """

    translated = []

    for dna_set in list_of_char_sequence:
        translated.append(constants.GENETEIC_CODE_DICTIONARY.get(dna_set))

    return translated


class NotMultipleOf3(Exception):

    pass
