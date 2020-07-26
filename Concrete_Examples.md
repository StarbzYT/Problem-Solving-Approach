Explore Examples

Once you have understood the problem, explore examples or sample inputs to realize what your program should do.

Tips:
    1. Start with simple examples (basic inputs that give a standard output).

    2.  Progress to more complex examples (may be different types of input which are valid or edge cases).

    3. Explore examples with empty inputs (what happens if the input is inherently falsy?).

    4. Explore examples with invalid inputs (how do you deal with errors? Companies must always what to do if the user types in invalid text.)

Ex.
    Write a function which takes in a string and returns the count of each character in the string.

    Start with simple examples (basic inputs that give a standard output)
        print(charcount("aaaa"))  # 4
        print(charcount("hello"))  # 5
        
        * Remember to clarify any questions!
    
    Progress to more complex examples (may be different types of input which are valid or edge cases).
        print(charcount("my number is 3522345))  # Do we count the spaces? Numbers?
        print(charcount("Hello hi"))  # Is 'H' counted the same as 'h' or seperately?

        * Clarify!
    
    Explore examples with empty inputs (what happens if the input is inherently falsy?). Explore examples with invalid inputs (how do you deal with errors? Companies must always what to do if the user types in invalid text.)
        print(charcount(""))
        print(charcount())
        print(charcount(None))  # bools technically still has characters
        Do you want to return an error, None, or 0?




