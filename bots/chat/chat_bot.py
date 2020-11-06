def chatting(talking=True):
    while talking:
        say_something = input("say something: ")

        if say_something.lower() == "hey":
            print("What's up?")
        elif say_something.lower() == "good morning":
            print("Good morning, how was your night?")
        elif say_something.lower() == "great and yours":
            print("Same as well")
        elif say_something.lower() == "how are you":
            print("I'm good thank you. And you?")
        elif say_something.lower() == "i'm good as well thank you":
            print("That's great")
        elif say_something.lower() == "end":
            break
        else:
            print("I'm sorry but I don't understand that")


chatting()