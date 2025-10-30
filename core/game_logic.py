from core.deck import *
from core.player_io import *


def calculate_hand_value(hand: list[dict]):
    total = 0
    for val in hand:
        total += val["value"] 
    return total


def deal_two_each(deck: list[dict], player: dict, dealer: dict):
    deal_to_start = 2
    while deal_to_start > 0:
        player["hand"].append(deck.pop(len(deck) - 1))
        dealer["hand"].append(deck.pop(len(deck) - 1))
        deal_to_start -= 1
    print(f"The begginig value of the player is: {calculate_hand_value(player["hand"])}")
    print(f"The begginig value of the dealer is: {calculate_hand_value(dealer["hand"])}")


def pull_card(deck: list[dict]):
    return deck.pop(len(deck) - 1)


def dealer_play(deck: list[dict], dealer: dict):

    while calculate_hand_value(dealer["hand"]) <= 17:
        dealer["hand"].append(pull_card(deck))

        if calculate_hand_value(dealer["hand"]) > 21:
            print("the dealer lost you win ")
            return False

    return True


def compare_cards(p1_card: dict, p2_card: dict):
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    if p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        return "WAR"


def run_full_game(deck: list[dict], player: dict, dealer: dict):
    deal_two_each(deck, player, dealer)
    while True:
        if ask_player_action() == "H":
            player["hand"].append(pull_card(deck))
            if calculate_hand_value(player["hand"]) > 21:
                print("Sorry, Maybe next time")
                break
            else:
                continue
        else:
            if dealer_play(deck, dealer):
                print(compare_cards(player["hand"], dealer["hand"]))
            else:
                break
               



