from datetime import datetime

print("=" * 50)
print("🤖 Welcome to CodSoft AI Chatbot")
print("=" * 50)

name = input("Enter Your Name: ")

print(f"\nHello {name}! Type 'help' to see commands.")
print("Type 'exit' to quit.\n")

while True:

    user = input(f"{name}: ").lower().strip()

    # Chat History Save
    with open("chat_history.txt", "a") as file:
        file.write(f"{name}: {user}\n")

    # Greetings
    if user in ["hello", "hi", "hey"]:
        reply = f"Hello {name}! How can I help you today?"

    elif user == "good morning":
        reply = "Good Morning! Have a productive day."

    elif user == "good night":
        reply = "Good Night! Sleep well."

    # About
    elif user == "your name":
        reply = "I am CodSoft AI Chatbot."

    elif user == "about":
        reply = "I am a Rule-Based Chatbot developed using Python."

    # Date
    elif user == "date":
        reply = datetime.now().strftime("Today's Date: %d-%m-%Y")

    # Time
    elif user == "time":
        reply = datetime.now().strftime("Current Time: %H:%M:%S")

    # Joke
    elif user == "joke":
        reply = "Why do programmers hate nature? It has too many bugs."

    # Thank You
    elif user in ["thanks", "thank you"]:
        reply = "You're Welcome!"

    # Calculator
    elif user == "calculator":

        try:
            num1 = float(input("Enter First Number: "))
            op = input("Enter Operator (+,-,*,/): ")
            num2 = float(input("Enter Second Number: "))

            if op == "+":
                result = num1 + num2

            elif op == "-":
                result = num1 - num2

            elif op == "*":
                result = num1 * num2

            elif op == "/":
                result = num1 / num2

            else:
                result = "Invalid Operator"

            reply = f"Result = {result}"

        except:
            reply = "Invalid Input"

    # Help Menu
    elif user == "help":
        reply = """
Available Commands:

hello
hi
hey
good morning
good night
your name
about
date
time
joke
calculator
thanks
exit
"""

    # Exit
    elif user == "exit":
        print("Bot: Goodbye! Have a Great Day.")
        break

    else:
        reply = "Sorry, I don't understand that command."

    print("Bot:", reply)

    with open("chat_history.txt", "a") as file:
        file.write(f"Bot: {reply}\n")