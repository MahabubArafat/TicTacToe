
def asking():
    print("Player 1 -----> what you wana choose (X or O) : ",end="")
    player1=input()
    if player1.lower() == 'x':
        player1="X"
        player2="O"
    else:
        player1="O"
        player2="X"
    print("SO Player 1 will be ------>"+player1)
    print("SO Player 2 will be ------>"+player2)

asking()