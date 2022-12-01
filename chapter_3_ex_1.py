wining_number = 27
user_input = int(input("guess a number between 1 and 100 "))
if user_input == wining_number:
    print("YOU WIN!!!")
else:
    if user_input < wining_number:
        print("too low")
    else:
        print("too high")



