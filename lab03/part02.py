# 03.2.1 Trends.
"""
input("Warning!!! \n"
      "Your numbers must increase sequentially or they are must decrease sequentially")
firstValue = int(input("Enter the first value: "))
secondValue = int(input("Enter the second value: "))
thirdValue = int(input("Enter the third value: "))

if firstValue < secondValue < thirdValue:
    print("Correctly!! your numbers are increase sequentially.")
elif firstValue > secondValue > thirdValue:
    print("Correctly!! your numbers are decrease sequentially.")
else:
    print("Error!! your numbers line is not correct")
"""
# 03.2.2 Grades.
"""
enterGrade = input("Please enter student grade: ")

if enterGrade == "A":
    print("Your grade is 4.0")
elif enterGrade == "A+":
    print("Your grade is 4.3")
elif enterGrade == "A-":
    print("Your grade is 3.7")
elif enterGrade == "B":
    print("Your grade is 3.0")
elif enterGrade == "B+":
    print("Your grade is 3.3")
elif enterGrade == "B-":
    print("Your grade is 2.7")
elif enterGrade == "C":
    print("Your grade is 2.0")
elif enterGrade == "C+":
    print("Your grade is 2.3")
elif enterGrade == "C-":
    print("Your grade is 1.7")
elif enterGrade == "D":
    print("Your grade is 1.0")
elif enterGrade == "D+":
    print("Your grade is 1.3")
elif enterGrade == "D-":
    print("Your grade is 0.7")
else:
    print("Your grade is 0.0")
"""
# 03.2.3 Seasonal cycles.
"""
month = int(input("Please enter a month: "))
day = int(input("Please enter a day: "))


if 1 <= month <= 3:
    season = "Winter"
elif 4 <= month <= 6:
    season = "Spring"
elif 7 <= month <= 9:
    season = "Summer"
elif 10 <= month <= 12:
    season = "Fall"

if month % 3 == 0 and day >= 21:
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Fall"
    else:
        season = "Winter"

print("The day is in:", season)
"""
# 03.2.4 Leap years.
"""
x = int(input("Enter a year: "))

if (x > 1582 and x % 100 == 0 and x % 400 != 0) or x % 4 != 0:
    print("This year is not leapyear.")
else:
    print("This year is leapyear.")
"""
# 03.2.5 Grades again.
"""
grade = float(input("Enter your grade: "))
lastGrade = round(grade, 1)

print(lastGrade)

if lastGrade > 4.1 and lastGrade <= 4.3:
    print("Your grade is A+")
elif lastGrade >= 4.0 and lastGrade < 4.3:
    print("Your grade is A")
elif lastGrade >= 3.7 and lastGrade < 4.0:
    print("Your grade is A-")
elif lastGrade > 3.1 and lastGrade <= 3.3:
    print("Your grade is B+")
elif lastGrade >= 3.0 and lastGrade < 3.3:
    print("Your grade is B")
elif lastGrade >= 2.7 and lastGrade < 3.0:
    print("Your grade is B-")
elif lastGrade > 2.1 and lastGrade <= 2.3:
    print("Your grade is C+")
elif lastGrade >= 2.0 and lastGrade < 2.3:
    print("Your grade is C")
elif lastGrade >= 1.7 and lastGrade < 2.0:
    print("Your grade is C-")
elif lastGrade > 1.1 and lastGrade <= 1.3:
    print("Your grade is D+")
elif lastGrade >= 1.0 and lastGrade < 1.3:
    print("Your grade is D")
elif lastGrade >= 0.7 and lastGrade < 1.0:
    print("Your grade is D-")
elif lastGrade < 0.7:
    print("Your grade is F")
"""
# 03.2.6 Taxes.
