def isAnagram(s1, s2):
    # it sorts the string by letters order.
    if sorted(s1) == sorted(s2):
        print("Is an anagram")
    else:
        print("Is not an anagram")


s1 = input("Please enter the first string>")
s2 = input("Please enter the second string>") 
isAnagram(s1, s2)