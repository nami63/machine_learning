str='asdfghjk'
str=str.casefold()
rev=reversed(str)
if list(str)==list(rev):
    print("palindrome")