ticketssold = 0
maxtickets = 4
if input("do you wish to see program instructions? ").lower() == "yes":
  print("instructions go here")
while ticketssold < maxtickets:
  name = input("please enter your name: ")
  if name == "":
    print("error, name cannot be left blank, try again")
    continue
  age = int(input("age: "))
  if 12 <= age:
    pass
  elif age <12:
    print("error, you are too young")
    continue
  payment = input("cash or card?: ")
  if payment == "cash":
    pass
  elif payment == "card":
    pass
  else: pass
  ticketssold +=1
print("congrats you have sold all tickets")