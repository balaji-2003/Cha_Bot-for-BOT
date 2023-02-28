import re

# function to add two numbers
def add(num1, num2):
    return num1 + num2

# function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Can't divide by zero. Please enter a valid operand."
    else:
        return num1 / num2

# function to handle small talk
def small_talk(sentence):
    greetings = ['hi', 'hello', 'hey']
    if sentence.lower() in greetings:
        return "Hello! I am your bot. How can I assist you today?"
    else:
        return "I'm sorry, I didn't understand what you meant. Can you please try again?"

# main function to handle user input
def main():
    print("Welcome to the basic math operations bot!")
    while True:
        operation = input("What mathematical operation do you want to perform? (add/subtract/multiply/divide): ")
        num1 = float(input("Enter the first operand: "))
        num2 = float(input("Enter the second operand: "))
        
        # check for valid operation input
        if not re.match("^[aA|sS|mM|dD]+$", operation):
            print("Invalid input. Please enter a valid operation.")
            continue
        
        # perform selected operation
        if operation.lower() == 'add' or operation.lower() == 'a':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif operation.lower() == 'subtract' or operation.lower() == 's':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif operation.lower() == 'multiply' or operation.lower() == 'm':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif operation.lower() == 'divide' or operation.lower() == 'd':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        
        # ask user if they want to perform another operation
        repeat = input("Do you want to perform another operation? (yes/no): ")
        if repeat.lower() == 'yes' or repeat.lower() == 'y':
            continue
        else:
            break

# initialize the chatbot
def chatbot():
    print("Hello! I am a basic math operations bot. How can I assist you today?")
    while True:
        sentence = input("You: ")
        if sentence.lower() in ['bye', 'goodbye']:
            print("Bot: Goodbye! Have a nice day.")
            break
        elif any(word in sentence.lower() for word in ['hi', 'hello', 'hey']):
            print("Bot: Hello! How can I assist you today?")
        elif any(word in sentence.lower() for word in ['add', 'subtract', 'multiply', 'divide']):
            main()
        else:
            print("Bot: I'm sorry, I didn't understand what you meant. Can you please try again?")

# start the chatbot
chatbot()
