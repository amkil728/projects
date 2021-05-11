'''
find_palingrams.py

Find all two word palingrams that can be formed from a list of words. A palingram
is a palindromic phrase, i.e., a phrase that reads the same when read backwards as forwards.
E.g., pull up, stir grits, etc.
Notice that each such phrase has a core word which consists of two parts, a palindromic
part, and the other part, which, when reversed forms a word.
E.g., in 'pull up', the core word is 'pull', which can be divided into 'll', which is
palindromic, and 'pu', which when reversed gives 'up', which is a word. And in 'stir grits',
the core word is 'grits', which can be divided into 'g', which is a single letter, and hence
palindromic, and 'rits', when when reversed gives 'stir'.

@author amkil728
@version 10/04/21
'''

def find_palingram(wd, word_list):
	'''Finds all palingrams that can be formed from the given list of words, using the
	given word as the core word.
	
	Arguments:
	  - wd: word to use as core word
	  - word_list: list of words
	
	Returns:
		A list of pairs which contain the given word, and other word forming a
		palingram, if any can be formed;
		False, otherwise
	'''
	wd_len = len(wd)
	rev_wd = wd[::-1]
	for i in range(1, wd_len+1):
		# First check if palingram can be formed from end of word
		# last i letters of wd should form a word when reversed
		# and first len(wd) - i letters should be palindromic
		end_rev = rev_wd[:i]
		if end_rev in word_list and wd[:-i] == rev_wd[i:]:
			return (end_rev, wd)
		# Then check if palingram can be formed from front of word
		# first i letters of wd should form a word when reversed
		# and last len(wd) - i letters should be palindromic
		front_rev = rev_wd[-i:]
		if front_rev in word_list and wd[i:] == rev_wd[:-i]:
			return (wd, front_rev)
	return False


def find_all_palingrams(word_list):
	'''Finds all palingrams that can be formed from the list of words.
	
	Returns: list of pairs representing palingrams'''
        palingrams = list()
        for word in word_list:
                phrase = find_palingram(word, word_list)
                if phrase:
                        palingrams.append(phrase)
	return palingrams
