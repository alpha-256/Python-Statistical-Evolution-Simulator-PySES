# Built-in Library
import random
import utils

# Custom Stuff
import constants
import functools

# --- --- ---


def dnaString():

    usersay = int(input("How many acids? >>> "))
    init = ""

    for _ in range(usersay):
        init += random.choice(constants.GENETIC_ACID)

    return init


def test_runs(num=1):
    for test_num in range(num):
        print("--- Running test {} ---".format(test_num))

        xxx = utils.generate_random_string(100)

        print("--- RAW Generated Sequence ---")
        print(xxx)
        print("--- End Block ---\n")

        translated = []
        for dna in xxx:
            translated.append(constants.GENETEIC_CODE_DICTIONARY.get(dna, None))

        print("--- translated block ---")
        print(translated)
        print("--- End Block ---\n")


def test_run_decorator(run_count=0):
    """
    Run the function N times

    Arguments
    ---------
    run_count (int)
        Run the function number of times
    """

    @functools.wraps
    def real_decorator(fx):

        @functools.wraps
        def wrapper(*args, **kwargs):

            for count in range(run_count):
                print("--- Running Test: {}/{} ---".format(count + 1, run_count))
                fx(*args, **kwargs)

        return wrapper

    return real_decorator


@test_run_decorator(2)
def test_run2():

    raw_seq = utils.generate_random_string(6)

    gen_code = utils.translate_sequence(raw_seq)

    for idx, character_set in enumerate(raw_seq):
        print(character_set[0], "|")
        print(character_set[1], "|")
        print(character_set[2], "| ->", gen_code[idx])
        print()
    print('=== Complete ===')

    return


if "__main__" == __name__:

    test_run2()
