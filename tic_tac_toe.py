import random


def toss():
    print(
        "----------->Welcome  to Tic Tac Toe<---------------\n\n\n Figthing over WHO is gonna GO first? Let the "
        "computer decide then (@-@)\n\n\n")
    print(
        '>>>>>>>>Enter Y to Let computer decide  '
        '(If You have already Decided who is gonna go first then Enter N to '
        'start the game immediately):\t')
    toss_decision = input()
    if toss_decision.lower() == "y":
        player_selection = random.randint(1, 2)
        print("\n\n>>>>>>>>Pick a number 1 or 2?\t")
        player_picked = int(input())
        if player_picked > 2:
            print("wrong input,Enter a number between 1 and 2")
            player_picked = int(input())
        if player_picked <= 2:
            pass
            if player_picked == player_selection:
                print(">>>>The MORON who entered " + str(player_picked) + " will be >>>PLAYER-1  (AND WILL GO FIRST)")
                return
            elif player_picked != player_selection:
                print(
                    ">>>>The MORON who entered " + str(player_picked) + " will be >>>PLAYER-2    (AND WILL GO SECOND)")
                return

    else:
        return


def asking():
    print("Player 1 -----> what you wana choose (X or O) : ", end="")
    player1_1 = input()
    if player1_1.lower() == 'x':
        player1_1 = "X"
        player2_1 = "O"
    else:
        player1_1 = "O"
        player2_1 = "X"
    print("SO Player 1 will be ------>" + player1_1)
    print("SO Player 2 will be ------>" + player2_1)

    return player1_1, player2_1


def printing_board(positons):
    line1 = "\t\t{0}\t|\t{1}\t|\t{2}\t".format(str(positons[6]), str(positons[7]), str(positons[8]))
    line3 = "\t\t{0}\t|\t{1}\t|\t{2}\t".format(str(positons[3]), str(positons[4]), str(positons[5]))
    line5 = "\t\t{0}\t|\t{1}\t|\t{2}\t".format(str(positons[0]), str(positons[1]), str(positons[2]))
    line2 = "\t------------------------"

    def print_board():
        print(line1)
        print(line2)
        print(line3)
        print(line2)
        print(line5)

    a = "\n"
    print(a * 20)
    print_board()


def taking_input(player1_2, player2_2):
    position = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    printing_board(position)
    num_of_attempt = 1
    player_marker = "Player 1"
    for _ in range(1, 20):
        print(player_marker + "  Enter a number between 1 to 9:")
        num: int = int(input())
        if 1 <= num <= 9:
            if num_of_attempt % 2 != 0:
                player_marker = "Player 2 "
                position[num - 1] = player1_2
                # check_winner()
                num_of_attempt += 1
                printing_board(position)
                if position[0] == position[3] == position[6] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
                elif position[8] == position[7] == position[6] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
                elif position[8] == position[5] == position[2] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
                elif position[0] == position[1] == position[2] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
                elif position[3] == position[4] == position[5] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
                elif position[1] == position[7] == position[4] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
                elif position[8] == position[4] == position[0] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
                elif position[2] == position[4] == position[6] == player1_2:
                    print("----->>> And the winner is Player 1 !!!!!!!!!  ")
                    break
            else:
                player_marker = "Player 1 "
                position[num - 1] = player2_2
                num_of_attempt += 1
                printing_board(position)
                if position[0] == position[3] == position[6] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
                elif position[8] == position[7] == position[6] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
                elif position[8] == position[5] == position[2] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
                elif position[0] == position[1] == position[2] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
                elif position[3] == position[4] == position[5] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
                elif position[1] == position[7] == position[4] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
                elif position[8] == position[4] == position[0] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
                elif position[2] == position[4] == position[6] == player2_2:
                    print("----->>> And the winner is Player 2 !!!!!!!!!  ")
                    break
            if num_of_attempt == 10:
                print("------>The match is null (!_!)(!_!)(!_!)")
                break
        else:
            print("invalid input,plz enter again")

    return position


while True:
    toss()
    player1, player2 = asking()
    taking_input(player1, player2)
    print("------->Want to play again??????<-----------\n------>Type Y to play again\n------>Type N to exit \t")
    decision = input()
    if decision == "y":
        continue
    else:
        break
