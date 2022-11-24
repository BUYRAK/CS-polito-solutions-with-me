import unicodedata

# 02.2.1 Characters.
"""
textOne = "Snake"
textTwo = "Bird"
textThree = "Lion"

print(f"{textOne[:3]}...{textOne[3:]}\n"
      f"{textTwo[:3]}...{textTwo[3:]}\n"
      f"{textThree[:3]}...{textThree[3:]}")
"""
# 02.2.2 Telephone Number.
"""
phoneNumber = input("Please enter your phone number:")

if len(str(phoneNumber)) > 10:
    print("Your phone number is invalid please try again later")
else:
    areaCode = phoneNumber[:3]
    separate = phoneNumber[3:6]
    print(f"Your phone number is ({areaCode}) {separate}-{phoneNumber[6:10]}")
"""
# 02.2.4 Emoji.
"""
emojiOne = "😀"
emojiTwo = "🌷"
emojiThree = "🌼"

print(f"U+{ord(emojiOne):4X} - {unicodedata.name(emojiOne):40} - {emojiOne} - RANK 50")
print(f"U+{ord(emojiTwo):4X} - {unicodedata.name(emojiTwo):40} - {emojiTwo} - RANK 133")
print(f"U+{ord(emojiThree):4X} - {unicodedata.name(emojiThree):40} - {emojiThree} - RANK 154")
"""
# 02.2.5 Registrations.
"""
studentOne = "423A"
studentTwo = "132B"

if int(studentOne[:1]) > int(studentTwo[:1]):
    print(f"Student a more than big b {studentOne} - {studentTwo}")
else:
    print(f"Student b more than big a {studentTwo} - {studentOne}")
"""