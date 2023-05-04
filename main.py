ticketssold = 0
maxtickets = 6
profit = 0
money = 0
charged = 0


def yesnofunc():
  yesno = input("do you wish to see program instructions? ")
  if yesno =="yes" or yesno == "y":
    print("instructions go here")
  elif yesno == "no" or yesno == "n":
    pass
  else:
    print("yes or no")
    yesnofunc()
yesnofunc()

while ticketssold < maxtickets:
  name = input("please enter your name: ")
  if name == "":
    print("error, name cannot be left blank, try again")
    continue
  elif name =="xxx":
    break
  age = input("age: ")
  try: 
    int(age)
  except ValueError:
    print("please enter an integer")
    continue
  age = int(age)
  if 12 <= age <= 120:
    pass
  elif age <12:
    print("error, you are too young")
    continue
  else: 
    print("that looks like a typo, please try again")
    continue
  payment = input("cash or credit?: ")
  if payment == "cash":
    if age <16:
      profit +=2.50
      charged += 7.50
      money += 7.50
    elif age <65:
      profit +=5.50
      charged+=10.50
      money +=10.50
    else: 
      profit += 1.50
      charged += 6.50
      money += 6.50
  elif payment == "credit":
    if age <16:
      profit +=2.50
      charged += 7.88
      money += 7.50
    elif age <65:
      profit +=5.50
      charged+=11.03
      money +=10.50
    else: 
      profit += 1.50
      charged += 6.83
      money += 6.50
  else:     
    print("error, only aceptable inputs are \"cash\" or \"credit\" ")
    continue
  ticketssold +=1
print("congrats you have sold",ticketssold,"tickets, all values are in $")
print("profits:")
print(profit)
print("money attained:")
print(money)
print("people have been charged:")
print(charged)
print("average ticket profit")
print(profit/ticketssold)
print("average ticket cost for user:")
print(charged/ticketssold)
print("average money gotten per ticket:")
print(money/ticketssold)