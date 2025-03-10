import webbrowser
import sys


RICKROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


def open_video():
    webbrowser.open(RICKROLL_URL)


def input_math():
    while True:
        user_input = input("1 times 1 = ? ")

        if user_input == "exit":
            sys.exit()

        try:
            answer = int(user_input)
            if answer == 1:
                print("Correct!")
                break
            else:
                print("Wrong! Try again.")
                open_video()
        except ValueError:
            open_video()


if __name__ == "__main__":
    input_math()
