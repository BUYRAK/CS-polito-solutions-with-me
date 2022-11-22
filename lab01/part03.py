import cowsay

# 01.3.1
"""
print('Hello Computer Science Lab')
"""
# 01.3.2
"""
print(1+2+3+4+5+6+7+8+9+10)
print()
"""
# Another Solution
"""
number = 0
total = 0
while number < 10:
    number += 1
    total += number
    print('1+' + str(number) + '=' + str(total))

print(total)
"""
# 01.3.3
"""
print(1*2*3*4*5*6*7*8*9*10)
print()
"""
# 01.3.4
""""
options = {
    'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
    'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
    'R': ['**** ', '*   *', '**** ', '*  * ', '*   *'],
    'A': [' *** ', '*   *', '*****', '*   *', '*   *'],
    'K': ['*   *', '*  * ', '**   ', '*  * ', '*   *'],
    }

def print_big(newList):
   for i in range(5):
       for j,_ in enumerate(newList):
           print(options[newList[j]][i]+"   ",end = " ")
       print()

name = "BURAK"
print_big(list(name))
"""

# 01.3.6
""""
interestAmount = 1000*5/100
accountWallet = 1000
firstYearWallet = accountWallet
secondYearWallet=firstYearWallet+firstYearWallet*5/100
thirdYearWallet=secondYearWallet+secondYearWallet*5/100
print('Your First Year Wallet Amount='+str(firstYearWallet))
print('Your Second Year Wallet Amount='+str(secondYearWallet))
print('Your Third Year Wallet Amount='+str(thirdYearWallet))
"""
# 01.3.7
"""
print('+-------+'+'\n'+'| Burak |'+'\n'+'+-------+')
"""
# 01.3.8
""""
cowsay.cow('Hello PolitoLab')
"""
# 01.3.10
""""
number = 0
numberOne = 1
while number < 5:
    if numberOne == 1:
        print('1 '+'0 '+'1 '+'0 '+'1 ')
        numberOne = 2
    else:
        print('0 '+'1 '+'0 '+'1 '+'0 ')
        numberOne = 1
    number+=1
"""
# 01.3.11
""""
print(100*'-')
"""
# 01.3.11
"""
print(100*'0')
"""
# 01.3.14
""""
numberFirst = 0
numberTwo = 1
numberFibonacci = numberFirst+numberTwo
i = 0
while i <= 4:
    i += 1
    numberFibonacci += numberFibonacci
    print(numberFibonacci)
"""
# 01.3.15
"""
totalExcersize = 11
solutionPoint = totalExcersize*100/100
mySuccess = 10*100/solutionPoint
print('%' + str(int(mySuccess)))
"""
