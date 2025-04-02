voted = {}

def check_voter(name):
    if name in voted:
        print("Выгнать его!")
    else:
        voted[name] = True
        print("Допустить к голосованию")

if __name__ == "__main__":
    check_voter("Ed")
    check_voter("John")
    check_voter("Ed")