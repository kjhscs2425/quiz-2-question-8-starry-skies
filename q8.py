"""
8. Use for-loops to print out every 3-letter word that:
starts with one of these letters: c, t,, b
has one of these letters in the middle: a, o
ends with one of these letters: p, t, n

(This should print out 18 words in total)
"""

# YOUR CODE HERE


def call_number():
    first_words = ["c", "t", "b"]
    second_words = ["a", "o"]
    third_words = ["p", "t", "m"]
    combo = [first_words, second_words, third_words]
    for i in first_words[3]:
        print(first_words)
    for i in second_words[3]:
        print(second_words)
    for letter in third_words:
        print(third_words)
  
    # for i in len(first_words):
    #     return first_words[i]
    # for i in len(second_words):
    #     return second_words[i]
    # for i in len(third_words):
    #     return third_words[i]
    # for i in (len(combo)):
    #     print(f"{first_words[i]} + {second_words[i]} + {third_words[i]}")

    # for i in range(18):
    #     (first_words)
    #      if i == "c" or i == "t" or i == "b":
    #       word += i
    #       return word == 2
    #     for i in "abcdefghijklmnopqrstuvwxyz":
    #        if i == "a" and word == 2 or i == "o" and word == 2:
    #           word += i
    #           return word == 3
    #     for i in "abcdefghijklmnopqrstuvwxyz":
    #        if i == "p" and word == 3 or i == "t" and word == 3 or i == "n" and word == 3:
    #           word += i
    #           return word
    #     print(word)
call_number()
        
