# common string methods
# lower() and casefold() -- convert uppercase to lowercase
text = "MY NAME IS MUSTAFA".lower()
text_8 = "MY NAME IS FATIMA".casefold()
print(text)
print(text_8)

# upper() -- convert lowercase to uppercase
text_1 = "my name is mustafa".upper()
print(text_1)

# capitalize() -- convert the first char of a sentence to uppercase and other chars to lowercase
text_2 = "my NAME IS MUSTAFA".capitalize()
text_3 = "my name is mustafa".capitalize()
print(text_2)
print(text_3)

# title() -- convert first chars of words in a sentence into uppercase and other chars or words into lowercase
text_4 = "my name is mustafa".title()
text_5 = "MY NAME IS MUSTAFA".title()
print(text_4)
print(text_5)

# strip() remove spaces from start and end of a text string
text_6 = "       my name is mustafa       ".strip()
print(text_6)

# split() convert a text string into list based a char that we want by default it uses space to split the text
text_7 = "my name is mustafa".split(" ")
print(text_7)

# islower() checks if all chars in a text string is lowercase or not, return True or False
text_9 = "my name is mustafa".islower()
text_10 = "MY NAME IS MUSTAFA".islower()
text_11 = "MY NAME is mustafa".islower()
print(text_9, text_10, text_11)

# isupper() checks if all chars in a text string is uppercase or not, return True or False
text_12 = "my name is mustafa".isupper()
text_13 = "MY NAME IS MUSTAFA".isupper()
text_14 = "my name IS MUSTAFA".isupper()
print(text_12, text_13, text_14)

# len() will return the length of a sequence
text_15 = "my name is mustafa"
text_16 = "hello this is python string methods"
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_dict = {"name": "mustafa", "job": "programmer"}
my_tuple = ("mustafa", "ali", "masoud", "ehsan", "maisam")
my_set = {10, 20, 30, 40, 50}
print(len(text_15))
print(len(text_16))
print(len(my_list))
print(len(my_dict))
print(len(my_tuple))
print(len(my_set))

# count() will count a specific char or element from a sequence
text_17 = "my name is mustafa".count("m")
text_18 = "my name is mustafa".count(" ")
my_second_list = [1, 2, 3, 3, 3, 3, 4, 5, 6].count(3)
print(text_17)
print(text_18)
print(my_second_list)

# endswith() checks if a string ends with a specific value
text_19 = "my name is mustafa".split()
if text_19[3].endswith("a"):
    text_19[3] = "ali"
    a, b, c, d = text_19
    print(a, b, c, d)

# startswith() checks if a string starts with a specific value
text_20 = "my name is Fatima".split()
if text_20[3].startswith("m"):
    print(True)
else:
    print(False)

# isnumerci() returns true if all chars in a string are numeric(0-9)
text_21 = "this is number 4".isnumeric()
text_22 = "1234567890".isnumeric()
text_23 = "this is python".isnumeric()
print(text_21, text_22, text_23)

# replace() well replace a word or char to another word or char in a string
text_24 = "this is java methods".replace("java", "python")
text_25 = "I'm not a programmer".replace("not", "")
print(text_24)
print(text_25)

# find(), index() return the index of a specific value

text_26 = "try to work hard".find("a")
text_27 = "try to be honest with everyone".index("r")
print(text_26)
print(text_27)

