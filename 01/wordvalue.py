from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = open(DICTIONARY,'r')
    wordList = []
    for i in words.read().splitlines():
        wordList.append(i)

    words.close()
    return wordList

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for i in word.upper():
        score = score + LETTER_SCORES.get(i, 0)
    return score

def max_word_value(wordList=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if wordList is None:
        wordList = load_words()
        
    maxScore = 0
    maxScoreWord = ''
    for word in wordList:
        s = calc_word_value(word)
        if s > maxScore:
            maxScore = s
            maxScoreWord = word
            
    return maxScoreWord
            
if __name__ == "__main__":
    pass # run unittests to validate
