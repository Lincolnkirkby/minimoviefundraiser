import random #random number required for raffle
#variables
ticketssold = 0
maxtickets = 5
profit = 0
totalticketsales = 0
namelist = [""]
costlist = [""]
surchargelist = [""]
printnumber = 1
winner = ""

#yes/no checker
def yesnofunc():
  yesno = input("do you wish to see program instructions? ")
  if yesno =="yes" or yesno == "y":
    print("instructions go here")#placeholder
  elif yesno == "no" or yesno == "n":
    pass
  else:
    print("invalid responce please try either yes or no")
    yesnofunc()
yesnofunc()

#while loop
while ticketssold < maxtickets:
  ticketcost = 0
  surcharge = 0
  name = input("please enter your name: ")
  if name == "":
    print("error, name cannot be left blank, try again")
    continue #resets the loop
  elif name =="xxx":#cancels the loop if input = xxx, but only if more than one ticket is sold to stop the code from breaking later on
    if ticketssold >0:
      break
    else:
      print("you need to have sold at least one ticket first")
      continue
  #age verification
  age = input("age: ")
    #age is integer verification
  try: 
    int(age)
  except ValueError:
    print("please enter an integer")
    continue
  age = int(age)
  if 12 <= age <= 120: #age is appropriate verification
    pass
  elif age <12:
    print("error, you are too young")
    continue
  else: 
    print("that looks like a typo, please try again")
    continue
  if age <16: #pricing brackets
    ticketcost = 7.50
  elif age <65:
    ticketcost =10.50
  else: 
    ticketcost = 6.50
    
  payment = input("cash or credit?: ").lower() #asking payment method
  if payment == "cash" or payment == "ca":
    pass
  elif payment == "credit" or payment == "cr":
    surcharge = round(ticketcost*0.05, 2) #surcharge calculation, surcharge is 5%
  else:     
    print("error, only aceptable inputs are \"cash\" or \"credit\", \"ca\" or \"cr\"")
    continue
  #saving all information gained in loop into global variables
  profit += (ticketcost-5)
  totalticketsales += ticketcost + surcharge
  namelist.append(name)
  costlist.append(ticketcost)
  surchargelist.append(surcharge)
  ticketssold +=1


if ticketssold == maxtickets: print("\ncongrats on selling all tickets")#/n creates a new line in print messages
else: print("\ncongrats, you have sold",ticketssold,"ticket(s)")
#printing of the attendee details
print("\n-------Ticket Data-------\n")
while printnumber < (ticketssold+1):#this code only runs the ammount of times equal to the amount of tickets sold
  print("ticket #"+str(printnumber)+", name:",str(namelist[printnumber])+", ticket cost: $"+str(costlist[printnumber])+", surcharge: $"+str(surchargelist[printnumber]),"\n") #this should output somthing like this: ticket #1, name: Lincoln, ticket cost: $10.5, surcharge: $0 
  printnumber += 1
#profit calculation
print("-------Ticket Cost / Profit-------\n")
print("total profits: $"+str(profit))
print("total ticket sales: $"+str(totalticketsales))

#raffle code
print("\n-------Raffle Winner-------\n")
winner = random.randint(1,ticketssold)
print("the winner is",namelist[winner]+",",namelist[winner],"has won $"+str(costlist[winner]),"A.K.A",namelist[winner],"has won a free ticket") # should print somthing like: the winner is Lincoln, Lincoln has won $10.5 A.K.A Lincoln has won a free ticket
quit()