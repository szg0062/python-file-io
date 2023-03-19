#! /usr/bin/env python3

import re

"""
The goal of this script is to search for terms in the Origin of Species by Charles Darwin that are related to heritability.
        Heritable, inherit, inheritance, and other word related to heritability.
"""

def origin_terms():
    """
    This function is going to open the text file, read it, and sort the words to find any that are associated with heritability.

    It will then take those words and write them into a new file named "Heritable_words.txt".

    For this script to run, you must import the "re" package to use regular expressions.

    -----------------------------------------------------------------------------------------

    Parameters:
    in_stream = Must have the file 'origin.txt' which contains the text from The Origin of Species by Charles Darwin. 

    -----------------------------------------------------------------------------------------

    Returns:
    out_stream = This function will return the file 'Heritable_words.txt' which contains the word associated with heritability and the line number of the text that it was found on.

    """

    count_words = 0
    with open('origin.txt', 'r') as in_stream:
        with open('Heritable_words.txt', 'w') as out_stream:
            for num, line in enumerate(in_stream):
                line = line.strip()
                word_list = line.split()
                targets = re.compile(r'(\w*herit\w*)', re.IGNORECASE)
                matches = targets.findall(line)
                for word in matches:
                    count_words += 1
                    out_stream.write(str(num) + '\t{0}\n'.format(word))
    
    print("Done!!")
    print('origin.txt is closed?', in_stream.closed)
    print('Heritable_words.txt is closed?', out_stream.closed)
    print("Inheritance was mentioned " + str(count_words) + " times")

if __name__ == "__main__":
    origin_terms()

