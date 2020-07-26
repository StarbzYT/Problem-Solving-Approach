# solution for question: write a func which returns the count of chars in a string
# can simplify to include periods, symbols, etc.


def charcount(string):  # O(n)
    count = {}  # count of letters
    # take away spaces and lowercase everything
    new_string = string.replace(" ", "").lower()
    # loop through new_string
    for char in new_string:
        if char.isalnum() is True:  # check if char is a num or letter (can use regex instead)
            if char not in count:  # is char in count already?
                count[char] = 1  # set equal to one
            else:
                count[char] += 1  # or add one if already in count
    return count


print(charcount("Hi or hello, I am Adarsh"))
print(charcount("Hi or hello, I am Adarsh!*%###"))
print(charcount(""))
print(charcount(" "))
print(charcount("1,!23,56"))
# refactor or change to different ways. Experiment!
