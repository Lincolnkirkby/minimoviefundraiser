import random
ticketssold = 0
maxtickets = 6
profit = 0
namelist = [""]
costlist = [""]
surchargelist = [""]

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
  ticketcost = 0
  surcharge = 0
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
  if payment == "cash" or payment == "ca":
    if age <16:
      profit +=2.50
      surcharge += 0
      ticketcost += 0
    elif age <65:
      profit +=5.50
      surcharge+=0
      ticketcost +=10.50
    else: 
      profit += 1.50
      surcharge += 0
      ticketcost += 6.50
  elif payment == "credit" or payment == "cr":
    if age <16:
      profit +=2.50
      surcharge += 0.38
      ticketcost += 7.50
    elif age <65:
      profit +=5.50
      surcharge+=1.03
      ticketcost +=10.50
    else: 
      profit += 1.50
      surcharge += 0.33
      ticketcost += 6.50
  else:     
    print("error, only aceptable inputs are \"cash\" or \"credit\" ")
    continue
  namelist.append(name)
  costlist.append(ticketcost)
  surchargelist.append(surcharge)
  ticketssold +=1
if ticketssold == maxtickets: print("congrats on selling all tickets")
else: print("congrats, you have sold",ticketssold,"ticket(s)")
print("profits:")
print(profit)