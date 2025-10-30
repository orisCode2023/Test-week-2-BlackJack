def check_valid_request(choose):
    if choose.islower():
        return False
    
    if type(choose) != str:
        return False
    
    if "S" != choose != "H":
        return False
    return True


def ask_player_action():
    print("Pleas enter your choice in caps letter")
    choose = input("To hit enter: 'H', To stand enter: 'S' ")
    while True:
        if check_valid_request(choose):
            break
        else:
            print("Pleas enter your choice in caps letter")
            choose = input("To hit enter: 'H', To stand enter: 'S' ")
    return choose


