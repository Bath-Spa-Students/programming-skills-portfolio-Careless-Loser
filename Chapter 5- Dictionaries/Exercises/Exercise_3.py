#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.
# Define a dictionary of programming terms and their simplified definitions.
glossary = {
    'Boolean Expression': 'In programming, a statement that can be either "true" or "false" is called a boolean expression. It functions similarly to a yes-or-no question in code, with the program using the response to guide its decisions.',
    'Comment': 'In programming, a "Comment" is essentially a note intended for human readers rather than the computer. It provides programmers with explanations.',
    'Float': 'A number like 3.14 that has a decimal point is referred to as a "float" in programming.',
    'Loop': 'Iterating through a collection of items one by one.',
    'Key': 'In programming, a "key" is similar to a label in a dictionary that is used to locate and retrieve related data.',
    'Dictionary': 'In computer programming, a dictionary is a set of labeled objects with a corresponding piece of information on each label.',
    'Value': 'In coding, "value" refers to the actual data that is connected to a dictionary label.',
    'Conditional Test': 'Comparing two values to check a condition.',
    'List': 'A collection of items in a specific order.',
    'String': 'in programming is like a sequence of characters, which can be letters, numbers, or symbols.'
}
# Iterate through the dictionary and print each term with its simplified definition.
for term, definition in glossary.items():
    print(f"\n{term}: {definition}")
