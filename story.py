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
    print("You step forward to pull it from its pedestal, and the air rings with the sound of steel.")
    print("Suddenly, a roaring dragon streaks past overhead, and glides around to land in a clearing before you.")
    print("You advance, blade in hand, slaying the fell beast and saving the kingdom.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You walk forward and discover the crumbing entrance to a dark, foreboding dungeon.")

if __name__ == "__main__":
    intro()
