def car_helper(helper=True):
    # speak = ""
    while helper:
        speak = input("Speak: ").lower()
        if "hello" in speak or "hi" in speak or "hey" in speak:
            print("Hello, how may I help you?")
        elif (
            "thank you" in speak
            or "end" in speak
            or "okay" in speak
            or "stop talking" in speak
        ):
            print("Okay, goodbye")
            break
        elif (
            "how to start" in speak
            or "starting the car" in speak
            or "starting" in speak
        ):
            print(
                "Press the red button beside the steering wheel for three seconds to start the car"
            )
        elif (
            "how to stop" in speak or "stopping the car" in speak or "stopping" in speak
        ):
            print(
                "Press the red button beside the steering wheel for two seconds to stop the car"
            )
        elif "drive" in speak:
            print("Let's drive")
        elif "talk" in speak or "speak" in speak:
            print("Hi, what seems to be the problem?")
        else:
            print("I'm sorry but I can't help you with that")


car_helper()
