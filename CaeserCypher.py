# Isaac Hong, 350645248
# Create a function that takes two arguments (a word and an integer (for shifting)) and encrypts the given word.
def shift(word, key): 
    '''shifts the characters of a given word down or up the alphabet based on the key shifted

    arguments
        word : string | represents the word needed to be shifted
        key : integer | represents the value in which each character can be shifted


    return
        string : the shifted string
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    value = 0 
    shifted = ''
    for c in word:
        value = alphabet.index(c)
        value += key 
        value = value % 26
        shifted += alphabet[value]
    return shifted

word = input()
key = int(input())
print (shift(word, key))
