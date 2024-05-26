import random

def print_instructions():
    print("                           ACEY DUCEY CARD GAME")
    print("                 CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print()
    print()
    print("ACEY-DUCEY IS PLAYED IN THE FOLLOWING MANNER")
    print("THE DEALER (COMPUTER) DEALS TWO CARDS FACE UP")
    print("YOU HAVE AN OPTION TO BET OR NOT BET DEPENDING")
    print("ON WHETHER OR NOT YOU FEEL THE CARD WILL HAVE")
    print("A VALUE BETWEEN THE FIRST TWO.")
    print("IF YOU DO NOT WANT TO BET, INPUT A 0")
    print()

def deal_card():
    card = random.randint(2, 14)
    if card == 11:
        return "JACK"
    elif card == 12:
        return "QUEEN"
    elif card == 13:
        return "KING"
    elif card == 14:
        return "ACE"
    else:
        return str(card)

def card_value(card):
    if card == "JACK":
        return 11
    elif card == "QUEEN":
        return 12
    elif card == "KING":
        return 13
    elif card == "ACE":
        return 14
    else:
        return int(card)

def main():
    print_instructions()
    
    Q = 100  # Player's initial money
    
    while True:
        print(f"\nYOU NOW HAVE {Q} DOLLARS.")
        print("\nHERE ARE YOUR NEXT TWO CARDS:")
        
        while True:
            card1 = deal_card()
            card2 = deal_card()
            if card_value(card1) < card_value(card2):
                break
        
        print(card1)
        print(card2)
        
        bet = int(input("WHAT IS YOUR BET: "))
        
        if bet == 0:
            print("CHICKEN!!")
            continue
        
        if bet > Q:
            print(f"SORRY, MY FRIEND, BUT YOU BET TOO MUCH. YOU HAVE ONLY {Q} DOLLARS TO BET.")
            continue
        
        card3 = deal_card()
        print(f"\nThe third card is: {card3}\n")
        
        if card_value(card1) < card_value(card3) < card_value(card2):
            print("YOU WIN!!!")
            Q += bet
        else:
            print("SORRY, YOU LOSE")
            Q -= bet
        
        if Q <= 0:
            print("\nSORRY, FRIEND, BUT YOU BLEW YOUR WAD.")
            replay = input("TRY AGAIN (YES OR NO): ").strip().upper()
            if replay == "YES":
                Q = 100
            else:
                print("O.K., HOPE YOU HAD FUN!")
                break

if __name__ == "__main__":
    main()
