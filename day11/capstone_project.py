import random

def draw_card():
    # Aces are 11 by default; J, Q, K mapped to 10
    game_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(game_list)

def calculate_score(cards):
    """
    Returns 0 if blackjack (two-card 21).
    Adjusts Ace (11 -> 1) if score goes over 21.
    """
    # Blackjack check
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Convert Ace 11 -> 1 as needed (handle multiple aces safely)
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(u_score, d_score):
    if u_score == d_score:
        return "Draw."
    elif d_score == 0:
        return "You lose — dealer has Blackjack!"
    elif u_score == 0:
        return "You win with a Blackjack!"
    elif u_score > 21:
        return "You lose — you busted."
    elif d_score > 21:
        return "You win — dealer busted."
    

def play_game():
    user_cards, dealer_cards = [], []
    is_game_over = False

    for _ in range(2):
        user_cards.append(draw_card())
        dealer_cards.append(draw_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        # If user or dealer has blackjack, or user busted, stop
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").strip().lower()
            if user_should_deal == 'y':
                user_cards.append(draw_card())
            else:
                is_game_over = True

    # Dealer draws until score >= 17 (unless dealer has blackjack)
    dealer_score = calculate_score(dealer_cards)
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(draw_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {calculate_score(dealer_cards)}")
    print(compare_score(calculate_score(user_cards), calculate_score(dealer_cards)))

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break