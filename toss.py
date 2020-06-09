import random

def toss():
    print("----------->Welcome  to Tic Tac Toe<---------------\n\n\n Figthing over WHO is gonna GO first? Let the computer decide then (@-@)\n\n\n")
    print(">>>>>>>>Enter Y to Let computer decide  (If You have already Decided who is gonna go first then Enter N to start the game immediately):\t")
    toss_decision=input()
    if toss_decision.lower()=="y":
        player_selection=random.randint(1,2)
        print("\n\n>>>>>>>>Pick a number 1 or 2?\t")
        player_picked=int(input())
        if player_picked>2:
            print("wrong input,Enter a number between 1 and 2")
            player_picked = int(input())
        if player_picked<=2:
            pass
            if player_picked==player_selection:
                print(">>>>The MORON who entered "+str(player_picked)+" will be >>>PLAYER-1  (AND WILL GO FIRST)")
                return
            elif player_picked!=player_selection:
                print(">>>>The MORON who entered "+str(player_picked)+" will be >>>PLAYER-2    (AND WILL GO SECOND)")
                return

    else:
        return

toss()