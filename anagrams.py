'''anagrams.py

@author aayush
@version 10/04/21
'''

import load_word_list, sys

# Constants

USAGE = f'Usage: {sys.argv[0]} [word]' # Usage of script

# Functions

def main():
    '''
    Runs a script that inputs the user for words or names and prints their
    anagrams.
    '''
    # Main loop for program
    while True:
        # Ask user to enter word or name
        word = input('Enter a word or name: ')
        # If no input enter, end program
        if not word:
            print('Terminating program.')
            return 0
        # Find all anagrams and print them
        print_anagrams(word)


def print_anagrams(word):
    '''Finds all anagrams of a given word and print them out.

    Argument: word - a word or name
    '''
    # Convert value to lowercase
    word_lower = word.lower()
    # Generate list of anagrams
    anagrams = find(word_lower, word_list)
    # Print all anagrams
    if anagrams:
        print(f'Anagrams of: {word}', *anagrams, sep='\n')
    else:
        print('No anagrams found for:', word)


def find(a_word, word_list):
    '''
    Finds all anagrams of a word.

    Arguments:
      - a_word: word to find anagrams for
      - word_list to search for anagrams

    Returns: list containing all anagrams of a_word    
    '''
    # Create list to store anagrams
    anagrams = list()
    # Sorting anagrams returns equal lists
    word_sorted = sorted(a_word) # sort word for future comparison
    # For each word in word list
    for word in word_list:
        # A word is not its own anagram
        if word == a_word:
            continue
        # If word is an anagram of given word
        if sorted(word) == word_sorted:
            # Add it to list of anagrams
            anagrams.append(word)
    # Return list of anagrams
    return anagrams


# If run as a script, execute the following
if __name__ == '__main__':
    # Load list of words
    word_list = load_word_list.load(load_word_list.WORD_FILE)
    
    # Program run without command-line arguments:
    # run the main loop
    if len(sys.argv) == 1:
        main()
    # Program run with one command-line argument:
    # find anagrams of argument
    elif len(sys.argv) == 2:
        # argument is word to find anagrams for
        word = sys.argv[1]
        print_anagrams(word)
    # Incorrect usage
    else:
        print(USAGE)
    
