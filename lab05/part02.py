import random


def main():
    # 2.1
    """
    a = 32310901
    b = 1729
    m = 224
    for i in range(0, 100):
        random_int = random.randint(0, 100)
        result = (a * random_int + b) % m
        print(f"Your random number: {random_int} \n"
              f"Your result with formula {result}")
    """
    # 2.2
    """
    x = 0
    y = 0
    for i in range(0, 100):
        x += random.randint(0, 4)
        y += random.randint(0, 4)
        drunkard_location = (x, y)

    print(drunkard_location)
    """
    # 2.3







if __name__ == '__main__':
    main()
