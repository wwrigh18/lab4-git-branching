def intro():
    print("You wake up in a dark forest. You can go left, right, or center.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice == "center":
        center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")
    print("You don't hesitate, striding forward and kicking the rodent into the brush.")
    print("In the light of the sun, a goddess appears, rage splayed over her face.")
    print("This was a test, and you have failed. The goddess curses you for your cruelty.")

def center_path():
    print("You walk forward and discover the crumbing entrance to a dark, foreboding dungeon.")

if __name__ == "__main__":
    intro()
