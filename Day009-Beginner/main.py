import art


def showLogo():
    print(art.logo)


def getUserInfo():
    name = str(input("What is your name? "))
    bid = int(input("What is your bid? $"))

    print("Are there any other bidders ? Type 'yes' or 'no'")
    others = True if str(input()).lower() == 'yes' else False
    print(f"{name} has {bid} bid. You have {others} others.")


def main():
    showLogo()
    getUserInfo()


if __name__ == "__main__":
    main()
