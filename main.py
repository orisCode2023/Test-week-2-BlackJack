from core.game_logic import *



if __name__ == "__main__":
    deck = build_standard_deck()
    shuffeld = shuffle_by_suit(deck)
    player = {"hand": [ ] } 
    dealer = {"hand": [ ] }
    run_full_game(shuffeld, player, dealer)
