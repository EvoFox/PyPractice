import re

#6. My personal attempt at a word stutterer, overly complex and doesn't need regex
def wordStutter (word):
    #Define pattern from incoming string
    pattern = '('
    for char in range(0, 2): #builds 'in'
        pattern += word[char]

    pattern += ')(.*)' #Pattern is finished building

    #Build replacement string that utilises the capture groups in the pattern
    replace = r'\1... \1... \1\2?'

    #Use the pattern and replacement string in order to process the incoming word and return the stuttered version
    stutter = re.sub(pattern, replace, word)
    return stutter 

#6. The simpler, and likely intended solution
def simpleWordStutter(word):
    #string[:x] returns the first x characters from a string
    #string[x:] returns all characters except the first two from a string
    stutter = word[:2] + '... ' + word[:2] + '... ' + word +'?'
    return stutter
