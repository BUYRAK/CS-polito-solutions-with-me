import linecache

# Part 1 / [1.1]
def main():
    with open("input.txt") as input:
        leng = len(input.readlines())
        lines = []
        for i in range(1, leng + 1):
            line = linecache.getline("input.txt", i)
            lines.append(f"/*{i}*/{line}")

    with open("output.txt", "w") as output:
        output.writelines(lines)


if __name__ == '__main__':
    main()
