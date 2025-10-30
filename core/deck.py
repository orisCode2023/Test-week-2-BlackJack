import random


def check_value(value: str):
    new_value = 0
    match value:
        case "2":
            return int(value)
        case "3":
            return int(value)
        case "4":
            return int(value)
        case "5":
            return int(value)
        case "6":
            return int(value)
        case "7":
            return int(value)
        case "8":
            return int(value)
        case "9":
            return int(value)
        case "10":
            return int(value)
        case "J":
            value = 10
        case "Q":
            value = 10
        case "K":
            value = 10
        case "A":
            value = 1
    return value


def create_card(rank: str, suite: str):
    card_template_dic = {"rank": rank, "suite": suite, "value": check_value(rank)}
    card_template_dic.update(card_template_dic)
    return card_template_dic


def build_standard_deck():
    deck = []
    card = {}
    suite = ["H", "C", "S", "D"]
    for s in suite:
        for rank in range(1, 14):
            if 2 <= rank <= 10:
                card = create_card(str(rank), s)
            match rank:
                case 1:
                    card = create_card("A", s)
                case 11:
                    card = create_card("J", s)
                case 12:
                    card = create_card("Q", s)
                case 13:
                    card = create_card("K", s)
            if card is not None:
                deck.append(card)
    return deck


def get_random_numbers(deck: list[dict]):
    index_i = random.randint(0, len(deck) -1)
    index_j = random.randint(0, len(deck) -1)
    return index_i, index_j


def check_validation_j(deck: list[dict], index1: int, index2: int ):
    if index1 == index2:
        return False
    
    if deck[index1]["suite"] == "H":
        if index2 % 5 != 0:
            return False 
    
    if deck[index1]["suite"] == "C":
        if index2 % 3 != 0:
            return False 
        
    if deck[index1]["suite"] == "D":
        if index2 % 2 != 0:
            return False 
        
    if deck[index1]["suite"] == "S":
        if index2 % 7 != 0:
            return False

    return True


def shuffle_by_suit(deck: list[dict], swaps: int = 5000):
    while swaps > 0:
        index_i, index_j = get_random_numbers(deck)
        if check_validation_j(deck, index_i, index_j):
            deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
            swaps -= 1
        else:
            continue
    return deck


    






    



