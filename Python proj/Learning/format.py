print(" yes ".strip())
print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeasdasdasd".count("e"))
print("yadndadado do".endswith("do"))
print("123".isnumeric())
print("hu3llo".isnumeric())
wordlist=["random", "words", "so", "annoytuibg", "to", "write", "all", "the"]
print("____".join(wordlist))
print("___".join(["words", "are", "annoying", "and", "hard",]))
print("goodbye cruel world""....".split("......"))

name = input("Enter Name Here: ")
luckynum = len(name * 3)
print("This is practice for the .format string..... Hello {}, your lucky number is {}! congrats!".format(name, luckynum))
print("this is another .format string practice...Hello {name}, your lucky number is {luckynum}!".format(name=name, luckynum=len(name) * 3))
price = 7.5
wtax=price*1.02
print("this is practice for more .format practice...base price: ${:.2f}!. With tax: ${:.2f}".format(price, wtax))
#the 2f represents 2 float
#can use <> to align to the right or left
#{:>3} alignes to wthe left 3 spacess