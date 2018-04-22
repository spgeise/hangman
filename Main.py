
def hangman(word):
    wrong = 0
    stages = ["",
              "______      ",
              "|     |     ",
              "|     O     ",
              "|    /|\    ",
              "|    /\     ",
              "|___________"]
    rletters = list(word)
    win = False
    board = ["__"] * len(word)
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Player 2 guess a letter: "
        char = input(msg)
        if char in rletters:
            print("\n")
            print("Correct!")
            print("\n")
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("\nWinner!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n")
        print("You lose! It was {}.".format(word))


print("Welcome to Hangman!\n")
start = "Player 1 enter a word: "
word = input(start)
hangman(word)
