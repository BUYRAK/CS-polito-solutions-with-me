def main():
    # Part 1.8
    """
    players_count = int(input("Enter players count: "))
    players = []
    word_list = []
    guess = ""
    player = 0
    for i in range(players_count):
        players.append(player)
        if len(word_list) == 0:
            word = str(input("Enter a word: "))
            word_list.append(word)
        guess = input(f"Player {player} \"{word[0:3]}\" Guess the word: ")
        player += 1
        if guess == word:
            word_list[-1] = guess

    if guess == word_list[-1]:
        print(f"Success User {player}")
    """

if __name__ == "__main__":
    main()
