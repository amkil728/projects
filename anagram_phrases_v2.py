# anagram_phrases_v2.py

''' anagram_phrases.py

@author aayush
@version 12/04/21

Allows the user to interactively construct a phrase that is an anagram of a
name or word. On entering the name, the program produces a list of all words
(from a given list of words) that only use letters occurring in the name. The
user can then select a word, after which the program produce a list of words
that with letters that only occur in the name, after removing the letters from
the word chosen by the user. This continues until an anagram phrase has been
formed, or there are no more remaining letters. The interface allows the user
to restart the process at any point.
'''

import load_word_list
from collections import Counter

# Load word list
WORDS = load_word_list.load(load_word_list.WORD_FILE)

def find_anagrams(letters, word_list):
    '''Returns all words from the given list of words that can be formed only
    using letters that occur in letters.

    Arguments:
        - letters: represents all letters that can be used.
        - word_list: iterable containing all valid words

    Returns: list of words that can be formed from letters in s
    '''

    # Create list to hold all anagrams
    anagrams = list()

    # Create counter for letters in word
    letter_count = Counter(letters)
    
    # For each word in word list
    for word in word_list:
        # Create counter of letters in word
        word_counter = Counter(word)

        # If counter for word is contained in letter_count
        if contains(letter_count, word_counter):
            # Add word to list of anagrams
            anagrams.append(word)

    # Return list of anagrams
    return anagrams


def contains(counter1, counter2):
    ''' Checks if counter1 contains counter2, i.e, if the value for each
    key in counter1 is less than the value for the corresponding key in counter2.

    Arguments:
        - counter1, counter2: Counters with keys of same type
    Returns:
        True, if counter1 contains counter2
        False, otherwise
    '''

    # For each key in counter2
    for key in counter2:
        # If value in counter2 is greater than value in counter1
        if counter2[key] > counter1[key]:
            # counter2 is not contained in counter1
            return False

    # Otherwise, all values in counter2 are less than values in counter1
    # So, counter1 contains counter2
    return True


def build_anagram_phrase(letters):
    '''Given a string of letters, allows the user to interactively build a phrase
    which is anagram of the letters, by successively choosing words that are formed
    only using the given letters. The user can restart at any time by not entering
    anything when prompted to choose a word.
    '''
    # Create counter of letters
    letter_count = Counter(letters)

    # Create list to hold all words chosen by user
    words = list()

    # While there are letters with non-zero key in counter
    while any(letter_count.values()):
        # Find all anagrams that can be formed from letters in counter
        anagrams = find_anagrams(letter_count, WORDS)

        # If no words can be found, exit loop
        if not anagrams:
            print('No words can be formed with the remaining letters.')
            break

        # Print these words
        print('Words that can be formed:')
        while True:
            display_words(anagrams)
            choice = input('Press any key to see more words: ')
            if not choice:
                break

        # Allow user to select a word, or choose to start over
        word = input('Select a word, or press enter to start over: ')

        # If user did not enter a word
        if not word:
            # Start over
            print('Starting over.')
            build_anagram_phrase(letters)

        # Add word to list of words
        words.append(word)

        # Subtract letters of word from counter
        word_counter = Counter(word)
        letter_count.subtract(word_counter)

        # Display remaining letters in alphabetical order
        print('Letters remaining from word (in alphabetical order):', end=' ')
        print(''.join(sorted(letter_count.elements())))

    # Print phrase comprised of chosen words
    print('You have constructed the phrase:')
    print(' '.join(words).title())


def display_words(word_list):

    start, index = '', 0

    while True:
        if len(word_list) <= 50:
            print(*word_list, sep='\n')
            break

        print('More than 50 words found.')

        letters = set(wd[index] for wd in word_list if len(wd) > index)
        prefixes = [start + letter for letter in letters]

        print('Words starting with:\n', *sorted(prefixes))

        choice = input('Enter letters to see words starting with them: ')

        while choice not in prefixes:
            print('Please enter valid starting letters.')
            choice = input('Enter letters: ')
            
        start = choice
        index += 1
        word_list = [wd for wd in word_list if wd.startswith(start)]


# Main loop
def main():
    # Get name or word from user
    name = input('Enter a word or a name:\n')

    # Get lowercase string containing all letters in name
    letters = name.replace(' ', '').lower()

    # Let the user interactively build an anagram phrase
    build_anagram_phrase(letters)

    # Ask user if they want to start over
    restart = input('Would you like to start over (y/n): ')
    if restart not in ['no', 'n']:
            build_anagram_phrase(letters)

if __name__ == '__main__':
    main()
