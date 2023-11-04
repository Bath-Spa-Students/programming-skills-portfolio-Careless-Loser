#A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
#each word-meaning pair in your output.
#Glossary_5_Words is a dictionary that stores programming terms and their definitions.
Glossary_5_Words = {
    'Variable': 'A variable is used to temporarily store a piece of data.',
    'Comment': 'A note in a program that the Python interpreter ignores it and it is used by using #hashtag.',
    'String': 'A series of characters which is in the "".',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
#The code selects the term 'Variable' from the dictionary and prints its definition.
word = 'Variable'
print(f"\n{word.title()}: {Glossary_5_Words[word]}")
#The code then selects the term 'Comment' from the dictionary and prints its definition.
word = 'Comment'
print(f"\n{word.title()}: {Glossary_5_Words[word]}")
#The code selects the term 'String' from the dictionary and prints its definition.
word = 'String'
print(f"\n{word.title()}: {Glossary_5_Words[word]}")
#The code selects the term 'loop' from the dictionary and prints its definition.
word = 'loop'
print(f"\n{word.title()}: {Glossary_5_Words[word]}")
#Finally, the code selects the term 'dictionary' from the dictionary and prints its definition.
word = 'dictionary'
#The code essentially provides a glossary of programming terms and displays their definitions one by one.
print(f"\n{word.title()}: {Glossary_5_Words[word]}")