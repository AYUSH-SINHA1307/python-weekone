#if elif else statement
age = int(input("PLEASE INPUT YOUR AGE : "))
if 0<age<=3:
    print("Ticket price : FREE")
elif 3<age<=10:
    print("Ticket price : 150 ")
elif 10<age<=60:
    print("Ticket price : 250 ")
else:
    print("Tickket price : 200")
