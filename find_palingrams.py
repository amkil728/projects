# find_palingrams.py

def find_palingram(wd, word_list):
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
        palingrams = list()
        for word in word_list:
                phrase = find_palingram(word, word_list)
                if phrase:
                        palingrams.append(phrase)
