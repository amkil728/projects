''' load_word_list.py

@author aayush
@version 08/04/21

Load a file as a list of words. The file should be formatted with each line
being a single word. If the file is a dictionary (list of words) for a language,
allows checking for valid words (and phrases) in that language.
'''

import sys
from pathlib import Path

# Constants

# Default file to use
WORD_FILE = Path.home() / 'words.txt'

# Functions

def load(f_name):
    '''Opens the file with given name, if it exists, and returns a list of
    strings representing the words in the file.

    Arguments: f_name - name (and path, if needed) of file to load words from

    Returns: list of all words in file, in lower case
    '''

    try:
        with open(f_name) as file:
            lines = file.read().strip().split('\n')
            words = [line.lower() for line in lines]
        return words
    except IOError:
        print(f'Error opening file {f_name}. Terminating program.',
              file=sys.stderr)
        sys.exit(1)
