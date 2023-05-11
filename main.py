import random
ticketssold = 0
maxtickets = 4
profit = 0
namelist = [""]
costlist = [""]
surchargelist = [""]
winner = ""
printnumber = 1
def yesnofunc():
  yesno = input("do you wish to see program instructions? ")
  if yesno =="yes" or yesno == "y":
    print("instructions go here")
  elif yesno == "no" or yesno == "n":
    pass
  else:
    print("invalid responce please try either yes or no")
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
    if ticketssold >0:
      break
    else:
      print("you need to have sold at least one ticket first")
      continue
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
  payment = input("cash or credit?: ").lower()
  if payment == "cash" or payment == "ca":
    if age <16:
      profit +=2.50
      surcharge += 0
      ticketcost += 7.50
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
if ticketssold == maxtickets: print("\ncongrats on selling all tickets")
else: print("\ncongrats, you have sold",ticketssold,"ticket(s)")
print("\n                  ---ticket data---\n")

while printnumber < (ticketssold+1):
  print("ticket #"+str(printnumber)+", name:",str(namelist[printnumber])+", ticket cost:",str(costlist[printnumber])+", surcharge:",str(surchargelist[printnumber]),"\n")
  printnumber += 1


winner = random.randint(1,ticketssold)
print("the winner is",namelist[winner]+",",namelist[winner],"has won $"+str(costlist[winner]),"A.K.A",namelist[winner],"has won a free ticket")
print("total profits: $"+str(profit))
quit()