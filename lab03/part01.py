from math import sqrt

# 03.1.1 True or False.
"""
valueOne = 1
valueTwo = 1.0
valueThree = 2.0
valueFour = '1'
valueFive = 'hello'

if valueOne == 1:
    print('First Variable is True')
else:
    print('First Variable is False')

if valueTwo == 1:
    print('Second Variable is True')
else:
    print('Second Variable is False')

if valueThree == sqrt(4):
    print('Third Variable is False')
else:
    print('Third Variable is True')

if valueFour == 1:
    print('Fourth Variable is True')
else:
    print('Fourth Variable is False')

if valueFive == 'Hello':
    print('Fifth Variable is True')
else:
    print('Fifth Variable is False')
"""
# 03.1.2 Identikit of the string.
"""
message = input("Enter Your Message:")

if message.isalpha():
    print("The string contains only letters.")
elif message.isupper():
    print("The string contains upper letters.")

if message.islower():
    print("The string contains lower letters.")
elif message.isdigit() & message.isalpha():
    print("The string contains alpha and digit letters.")

if not message.endswith("."):
    print(f" I added dot for your message {message}.")

if not message[0].isupper():
    print(f" I edited your message {message.capitalize()}")
"""
# 03.1.3 Strings and substrings.
"""
longDna = input("Insert a long dna sequence")
longDna = longDna.upper()

shortDna = input("Please insert short dna sequence(just 3 letter)")
shortDna = shortDna.upper()

if len(shortDna) != 3:
    print("Error! Please enter just 3 letter")
    exit()

found = longDna.find(shortDna)

if found == -1:
    print("Short sequence is not contains long sequence.")
else:
    print("Short sequence is contains long sequence", found)


numberOfRepeat = longDna.count(shortDna)
print(f"Short sequence contains {numberOfRepeat} times.")
"""
# 03.1.4 It’s equal.
"""
x = 3.0
s = "seven point five"
if x == 3.0:
    s = 'three point zero'
print(s)
"""
# 03.1.5 Matter of logic.
"""
valueNumber = int(input("Please enter a value: "))

if valueNumber >= 0:
    print("Entered value is big than 0 or the value is same")
elif valueNumber <= 0:
    print("Entered value is small than 0 or the value is same")
elif 0 < valueNumber <= 100:
    print("The value is big than 0 and small than 100")
elif valueNumber == 0 or valueNumber >= 200 and len(valueNumber) == 3:
    print("Entered value is big than 200 or the value is 0")
"""
# 03.1.6 De Morgan.
"""
x = int(input("Insert an integer number: "))

ruleOne = not (0 < x < 100)
ruleTwo = x <= 0 or x >= 100
print('not (0 < x < 100', ruleOne)
print('x <= 0 or x >= 100', ruleTwo)

ruleThree = not (x > 0 or x < 100)
ruleFour = 0 >= x >= 100
print('not (x > 0 or x < 100)', ruleThree)
print('x >= 0 and x >= 100', ruleFour)

ruleFive = not (x > 0 or 100 < x)
ruleSix = 0 > x > 100
print('not (x > 0 or 100 < x)', ruleFive)
print('0 > x > 100', ruleSix)

ruleSeven = not (0 < x < 100 or x == -1)
ruleEight = 0 < x < 100 or x != -1
print('not (x > 0 or 100 < x)', ruleSeven)
print('x <= 0 and x >= 100 or x != -1', ruleEight)
"""


