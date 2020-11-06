def game(starting_game=True):
    command = ""
    game_started = False
    while starting_game:
        command = input("Write a command: ").lower()
        if command == "start":
            if game_started:
                print("Game already started")
            else:
                game_started = True
                print("Game started")
        elif command == "stop":
            if not game_started:
                print("Game is not started")
            else:
                game_started = False
                print("Game stopped")
        elif command == "quit":
            break
        else:
            print(
                """
Sorry, this command doesn't exist. 
Enter something that exists
    """
            )


game()
