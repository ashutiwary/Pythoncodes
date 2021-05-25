#check letter is vowel or consonant

l = str(input("Enter any letter to check vowel or consonant: "))
vowel = "aeiouAEIOU"

if l in vowel:
    print("vowel")
else:
    print("consonant")