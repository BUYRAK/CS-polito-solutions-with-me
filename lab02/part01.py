# 02.1.1 Two numbers.
"""
numberOne: int = 5
numberTwo: int = 10

print('Sum of two integers variable: ' + str(numberOne+numberTwo))
print('Diffrence of two integers variable: ' + str(numberTwo-numberOne))
print('Average of two integers variable: ' + str(numberTwo+numberOne/2))
print('Value of the difference two integers variable: ' + str(abs(numberTwo+numberOne)))
print('Most max veriable: ' + str(max(numberTwo, numberOne)))
print(f"Most min veriable: {str(min(numberTwo, numberOne))}")
"""
# 02.1.2 Resistances.
"""
r1Value = input("Enter R1 in Ω:")
r1 = float(r1Value)

r2Value = input("Enter R2 in Ω:")
r2 = float(r2Value)

r3Value = input("Enter R3 in Ω:")
r3 = float(r3Value)

R2_R3_Total = (r3 * r2) / (r3 + r2)

R_Total = r1 + R2_R3_Total

print(f"Total Resistance of the Circuit is {R_Total} Ω")
"""
# 02.1.3 Digits.
"""
print(f"Please enter 5 digits number:")
positiveNumber = input()
stringExpression = str(positiveNumber)

print(f"First number:{stringExpression[:1]} \n"
      f"Second number:{stringExpression[1:2]} \n"
      f"Third number:{stringExpression[2:3]} \n"
      f"Fourth number:{stringExpression[3:4]} \n"
      f"Fifth number:{stringExpression[4:5]} \n")
"""

# 02.1.4 Hybrid car.
"""
def new_car(newCarCost, newCarEstimateKm, newCarEstimateFuelPrice):

    newCarTotalFuel = newCarEstimateKm / newCarEstimateFuelPrice

    newCarTotalFuel *= 1.80

    if newCarEstimateKm*5 >= 100000:
        totalCost = newCarTotalFuel + newCarCost + 3000
    else:
        totalCost = newCarTotalFuel + newCarCost

    print(f"Total cost after 5 years: {totalCost}")

new_car(12000,13500,7.5)
"""
# 02.1.5 Electric force.
"""
EPSILON = 8.854 * (10 ** (-12))
PI = 3.14

Q1 = float(input("Q1 in Coulomb:"))
Q2 = float(input("Q2 in Coulomb:"))
r = float(input("r in Meters:"))


F = (Q1 * Q2) / (4 * PI * EPSILON * (r**2))

print(f"The electric force is {F} N.")
"""
