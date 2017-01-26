import random
import re
import alan_random_slime_face as arsf

def dnaString():
    usersay = int(input("How many acids? >>> "))
    init = ""
    for _ in range(usersay):
        init += random.choice("ATCG")
    return init



def test_runs(num=1):
    for test_num in range(num):
        print("--- Running test {} ---".format(test_num))

        x = {"TTT": "Phe",
            "TTC": "Phe",
            "TTA": "Leu",
            "TTG": "Leu",

            "CTT": "Leu",
            "CTC": "Leu",
            "CTA": "Leu",
            "CTG": "Leu",

            "ATT": "Ile",
            "ATC": "Ile",
            "ATA": "Ile",
            "ATG": "Met",

            "GTT": "Val",
            "GTC": "Val",
            "GTA": "Val",
            "GTG": "Val",

            "TCT": "Ser",
            "TCC": "Ser",
            "TCA": "Ser",
            "TCG": "Ser",

            "CCT": "Pro",
            "CCC": "Pro",
            "CCA": "Pro",
            "CCG": "Pro",

            "ACT": "Thr",
            "ACC": "Thr",
            "ACA": "Thr",
            "ACG": "Thr",

            "GCT": "Ala",
            "GCC": "Ala",
            "GCA": "Ala",
            "GCG": "Ala",

            "TAT": "Tyr",
            "TAC": "Tyr",
            "TAA": "Stop",
            "TAG": "Stop",

            "CAT": "His",
            "CAC": "His",
            "CAA": "Gln",
            "CAG": "Gln",

            "AAT": "Asn",
            "AAC": "Asn",
            "AAA": "Lys",
            "AAG": "Lys",

            "GAT": "Asp",
            "GAC": "Asp",
            "GAA": "Glu",
            "GAG": "Glu",

            "TGT": "Cys",
            "TGC": "Cys",
            "TGA": "Stop",
            "TGG": "Trp",

            "CGT": "Arg",
            "CGC": "Arg",
            "CGA": "Arg",
            "CGG": "Arg",

            "AGT": "Ser",
            "AGC": "Ser",
            "AGA": "Arg",
            "AGG": "Arg",

            "GGT": "Gly",
            "GGC": "Gly",
            "GGA": "Gly",
            "GGG": "Gly",}

        xxx = arsf.generate_random_string(100)

        print("--- RAW Generated Sequence ---")
        print(xxx)
        print("--- End Block ---\n")

        translated = []
        for dna in xxx:
            translated.append(x.get(dna, None))

        print("--- translated block ---")
        print(translated)
        print("--- End Block ---\n")

test_runs(1)
