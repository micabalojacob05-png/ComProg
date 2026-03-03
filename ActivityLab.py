players = []

while True:
    
    print("\n1. Show Players")
    print("2. Add Player")
    print("3. Update Player")
    print("4. Delete Player")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        if len(players) == 0:
            print("No players found.")
        else:
            print("\nPlayer List:")
            for i in range(len(players)):
                print(f"{i + 1}. {players[i]}")

    elif choice == "2":
        new_player = input("Enter new player name: ")
        players.append(new_player)
        print("Player added successfully!")

    elif choice == "3":
        if len(players) == 0:
            print("No players to update.")
        else:
            for i in range(len(players)):
                print(f"{i + 1}. {players[i]}")

            index = int(input("Enter player number to update: ")) - 1

            if 0 <= index < len(players):
                new_name = input("Enter new name: ")
                players[index] = new_name
                print("Player updated successfully!")
            else:
                print("Invalid player number.")

    elif choice == "4":
        if len(players) == 0:
            print("No players to delete.")
        else:
            for i in range(len(players)):
                print(f"{i + 1}. {players[i]}")

            index = int(input("Enter player number to delete: ")) - 1

            if 0 <= index < len(players):
                player_to_remove = players[index]
                players.remove(player_to_remove)
                print("Player deleted successfully!")
            else:
                print("Invalid player number.")

    elif choice == "5":
        print("Exiting")
        break

    else:
        print("Invalid choice. Please try again.")