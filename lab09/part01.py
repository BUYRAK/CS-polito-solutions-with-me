import random


def main():
    # Part 1.1/1
    """
    list_int = [1, 4, 9, 16, 25]
    # first value
    list_int[0] = 3
    # last value
    list_int[-1] = 5
    """
    # Part 1.1/2
    """
    list_int = [1, 4, 9, 16, 25]
    list_last = list_int[-1]
    list_int.remove(list_last)
    list_int.insert(0, list_last)
    print(list_int)
    """
    # Part 1.1/3
    """
    for i in list_int:
        if i % 2 == 0:
            list_int.remove(i)
            list_int.insert(i + 2, 0)
    """
    # Part 1.1/4
    """
    array = [2, 3, 4, 5, 6, 7, 1, 24, 6, 21]
    for i in array:
        if i == array[-1] or i == array[0]:
            print("This is first or last index")
        else:
            if array[array.index(i) + 1] > array[array.index(i) + 2]:
                print(f"First Value: {i}")
                i = array[array.index(i) + 2]
                print(f"After Value: {i}")
            else:
                print(f"First Value: {i}")
                i = array[array.index(i) + 2]
                print(f"After Value: {i}")
    """
    # Part 1.1/5
    """
    array_1_5 = [2, 3, 4, 5, 6, 7, 1, 24, 6]
    leng_of_list = len(array_1_5)
    print(leng_of_list)
    if leng_of_list % 2 == 0:
        # Full list
        print(array_1_5)
        remove_value = (leng_of_list + 2)
        # Delete the middle element
        array_1_5.pop(int(remove_value / 3))
        print(array_1_5)
        # Delete the 2.middle element
        array_1_5.pop(int(remove_value / 3))
        print(array_1_5)
    else:
        array_1_5.append(5)
        remove_value = (leng_of_list / 2)
        array_1_5.pop(-1)
        array_1_5.pop(int(remove_value))
        print(array_1_5)
    """
    # Part 1.1/6
    # same of 1.1/5

    # Part 1.1/7
    """
    array_1_7 = [2, 3, 7, 4, 7, 8, 3, 2, 5, 324, 76, 8, 435, 123]
    array_1_7.sort()
    print(array_1_7[-2])
    """
    # Part 1.1/8
    """
    array_1_8 = [2, 3, 7, 4, 7, 8, 3, 2, 5, 324, 76, 8, 435, 123]
    # if I want to sort the array, I use be array_1_8.sort()
    if array_1_8.sort():
        print(True)
    else:
        print(False)
    """
    # Part 1.1/9
    """
    array_1_9 = [2, 3, 7, 4, 4, 7, 8, 3, 2, 5, 324, 76, 8, 435, 123]
    i = 0
    for x in array_1_9:
        if i != 13:
            if array_1_9[i] == array_1_9[i+1]:
                print(array_1_9.pop(i))
        i += 1
    """
    # Part 1.2/1
    """
    l = []
    for i in range(1, 11):
        l.append(i) 
    print(l)
    """
    # Part 1.2/2
    """
    l = []
    x = 0
    for i in range(0, 11):
        l.append(x)
        x += 2
    print(l)
    """
    # Part 1.2/3
    """
    l = []
    for i in range(0, 11):
        n = i ** 2
        l.append(n)
    print(l)
    """
    # Part 1.2/4
    """
    l = []
    for i in range(10):
        l.append(0)
    """
    # Part 1.2/6
    """
    l = []

    for i in range(1, 11):
        l.append(i ** 2)

    l = [0]
    for i in range(1, 10):
        if l[-1] == 0:
            l.append(1)
        else:
            l.append(0)

    print(l)
    """
    # Part 1.2/7
    """
    l = []
    x = 0
    for i in range(1, 11):
        if x > 4:
            x = 0

        l.append(x)
        x += 1

    print(l)
    """
    # Part 1.3
    """
    for i in range(5):
        number = random.randint(10, 50)
        star = "*"
        print(number * star)
    """
    # Part 1.4
    """
    l = [-1, -20, -3, -7, -19]
    x = 0
    for i in l:
        star = "*"
        print(abs(l[x]) * star)
        x += 1
    """
    # Part 1.5
    """
    countries = []
    country_stars = []
    for i in range(5):
        country = input("Please enter a Country: ")
        countries.append(country)
        country_star = input("Please enter star of the country: ")
        country_stars.append(int(country_star))
    x = 0
    for i in countries:
        star = "*"
        print(f"{countries[x]}: {country_stars[x] * star}")
        x += 1
    """
    # Part 1.6


if __name__ == "__main__":
    main()
