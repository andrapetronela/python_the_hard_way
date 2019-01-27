#def break_words(stuff):
#    words = stuff.split(' ')
#    return words
##print(break_words('string'))
## string to array
#
##Sorts the words
#def sort_words(words):
#    return sorted(words)
#print(sort_words('meat'))

## prints ['a', 'e', 'm', 't']

##Prints the first word after popping it off.
#def print_first_word(words):
#    word = words.pop(0)
#    return word
#print(print_first_word(['car', 'apple'], words))

#arr.pop() - removes the last item
#arr.pop(1) - removes second element from list

##Prints the last word after popping it off
#def print_last_word(words):
#    word = words.pop(-1)
#    print(word)
#    
#def sort_sentence(sentence):
#    words = break_words(sentence)
#    return sort_words(words)
#
#print(sort_sentence('Finally, she arrived at the restaurant, after 2 hours of delay.'))
# order: number, capital letter, a, b ...
# ['2', 'Finally,', 'after', 'arrived', 'at', 'delay.', 'hours', 'of', 'restaurant,', 'she', 'the']

#def print_first_and_last(sentence):
#    words = break_words(sentence)
#    print_first_word(words)
#    print_last_word(words)
#    
#def print_first_and_last_sorted(sentence):
#    words = sort_sentence(sentence)
#    print_first_word(words)
#    print_last_word(words)