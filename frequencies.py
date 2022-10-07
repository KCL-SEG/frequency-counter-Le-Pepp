"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    i = 0
    while i < len(items):
        items[i] = str(items[i])
        i += 1
    
    frequencies = {}
    i = 0
    while i < len(items):
        x = items[i]
        j = 0
        repeats = 0
        while j < len(items):
            if x == items[j]:
                repeats += 1
            j += 1
        frequencies[items[i]] = repeats
        i += 1
    return frequencies

