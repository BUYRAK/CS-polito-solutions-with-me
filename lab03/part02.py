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
from math import sqrt

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
"""
isMarried = input("Are you Married Y/N: ")
income = int(input("Please enter your income per/month: "))

if isMarried == "Y":
    if income <= 16000:
        tax = income * 10 / 100
        print(f"Your tax is: {int(tax)}")
    elif 16000 < income <= 64000:
        tax = income * 15 / 100
        tax += 1600
        print(f"Your tax is: {int(tax)}")
    elif income > 64000:
        tax = income * 25 / 100
        tax += 8800
        print(f"Your tax is: {int(tax)}")
else:
    if income <= 8000:
        tax = income * 10 / 100
        print(f"Your tax is: {int(tax)}")
    elif 8000 < income <= 32000:
        tax = income * 15 / 100
        tax += 800
        print(f"Your tax is {int(tax)}")
    elif income > 32000:
        tax = income * 25 / 100
        tax += 4400
        print(f"Your tax is {int(tax)}")
"""
# 03.2.7 Conversions.
""" 
this is a long process and always is manual so i didn't write it.

print("You can conversion ml, l, g, kg, mm, cm, m, km, fl, oz, gal, oz, lb, in, ft, mi")
measurement = input("Please enter measurement: ")
toMeasurement = input("select the unit of measure you want to convert: ")

# Volume units.
if measurement == "ml" and toMeasurement == "fl. oz":
    factor = 0.03381406
elif measurement == "l" and toMeasurement == "fl. oz":
    factor = 33.81405650
elif measurement == "ml" and toMeasurement == "gal":
    factor = 0.00026417
elif measurement == "l" and toMeasurement == "gal":
    factor = 0.26417218

# Weight / mass units.
elif measurement == "g" and toMeasurement == "oz":
    factor = 0.03527399
elif measurement == "kg" and toMeasurement == "oz":
    factor = 35.27399072
elif measurement == "g" and toMeasurement == "lb":
    factor = 0.00220462
elif measurement == "kg" and toMeasurement == "lb":
    factor = 2.20462442

# Distance units.
elif measurement == "mm" and toMeasurement == "in":
    factor = 0.03937008
elif measurement == "cm" and toMeasurement == "in":
    factor = 0.39370079
elif measurement == "m" and toMeasurement == "in":
    factor = 39.37007874
elif measurement == "km" and toMeasurement == "in":
    factor = 39370.07874016
elif measurement == "mm" and toMeasurement == "ft":
    factor = 0.00328084
elif measurement == "cm" and toMeasurement == "ft":
    factor = 0.03280840
elif measurement == "m" and toMeasurement == "ft":
    factor = 3.28083990
elif measurement == "km" and toMeasurement == "ft":
    factor = 3280.83989501
elif measurement == "mm" and toMeasurement == "mi":
    factor = 0.00000062
elif measurement == "cm" and toMeasurement == "mi":
    factor = 0.00000621
elif measurement == "m" and toMeasurement == "mi":
    factor = 0.00062137
elif measurement == "km" and toMeasurement == "mi":
    factor = 0.62137119
# Incompatible units.
else:
    exit("Those units are not compatible.")

# Read the value to convert from the user.
value = float(input("Value? "))

# Compute the result.
result = value * factor

# Display the result.
print(value, measurement, "=", result, toMeasurement)
"""
# 03.2.8 Shopping vouchers.
"""
print("you will win %8-10-12-14 for purchases of $10 or more")
moneySpent = int(input("Please enter your spending for shopping: "))

if 10 > moneySpent <= 60:
    yourCoupon = moneySpent * 8 / 100
    print(f"Congrats! you won a coupon worth ${yourCoupon}")
elif 60 > moneySpent <= 150:
    yourCoupon = moneySpent * 10 / 100
    print(f"Congrats! you won a coupon worth ${yourCoupon}")
elif 150 > moneySpent <= 210:
    yourCoupon = moneySpent * 12 / 100
    print(f"Congrats! you won a coupon worth ${yourCoupon}")
elif moneySpent > 210:
    yourCoupon = moneySpent * 14 / 100
    print(f"Congrats! you won a coupon worth ${yourCoupon}")
"""
# 03.2.9 waveLengths.
"""
waveLength = float(input("Enter the wavelength: "))

if waveLength > 1e-1:
    print("Radio Waves")
elif waveLength > 1e-3:
    print("Microwaves")
elif waveLength > 7e-7:
    print("Infrared")
elif waveLength > 4e-7:
    print("Visible Light")
elif waveLength > 1e-8:
    print("Ultraviolet")
elif waveLength > 1e-11:
    print("X-rays")
else:
    print("Gamma rays")
"""
# 03.2.10 Back to the comet.
"""

"""
