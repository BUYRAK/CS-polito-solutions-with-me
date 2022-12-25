def main():
    # 1.1
    """
    cardPin = "1234"
    enterPin = input("Please enter your Pin: ")
    pin_attempts = 1

    while pin_attempts < 3:
        if enterPin == cardPin:
            print("Success your pin is correct!")
            break
        else:
            pin_attempts += 1
            enterPin = input(f"Please enter again your Pin (Your Attempts: {pin_attempts}): ")
        if pin_attempts == 3:
            print("Your card is blocked.")
    """
    # 1.2
    """
    vowelChars = ['a', 'e', 'i', 'o', 'u']
    countryName = input("Please enter a country name: ")
    str_total = countryName.split()
    if len(str_total) >= 2:
        print(f"les {countryName}")
        exit()

    for vowel in vowelChars:
        if vowel == countryName[0] or vowel.upper() == countryName[0]:
            print(f"l'{countryName}")
            exit()

    if countryName[-1] == 'e':
        print(f"la {countryName}")
    else:
        print(f"le {countryName}")
    """
    # 1.3
    """
    number = int(input("Please enter a integer number: "))
    numberList = []

    for i in range(2, int(number/2)+1):
        if number % i == 0:
            numberList.append(i)
            number = number / i

    if number > 1:
        numberList.append(int(number))

    print(numberList)
    """
    # 1.4
    """
    ticketCount = 100
    while ticketCount != 0:
        enter = input("Welcome to Ticket App \n"
                      "1-Learn Tickets Stock \n"
                      "2-Buy Ticket \n"
                      "3-Close The App \n")

        if enter == '1':
            print(f"We have {ticketCount} pcs \n")
        elif enter == '2':
            buy_ticket = int(input("How many do you want to buy? (max: 4): "))
            if buy_ticket > 4:
                print("Error! You can't buy more than 4")
            else:
                print("Success You Bought It")
                ticketCount -= buy_ticket
                print(f"We have {ticketCount} pcs \n")
        else:
            exit()
    """


if __name__ == '__main__':
    main()
