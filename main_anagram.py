# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    if (len(word)==len(anagram)):
        w = word.lower()
        a = anagram.lower()
        if sorted(w)== sorted(a):
            return True
        else:
            return False
    else:
        return False

word = input("Enter first word: ")
anagram = input("Enter next word: ")
print(find_anagram(word, anagram))
