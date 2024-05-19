import random

user_score=0
computer_score=0
num=0
options=["head","tail"]

playing=input("Do you want to play Head and Tail? ").lower()
if playing != "yes":
    quit()

while(True):
    user_input1=input("Head or Tail or press q to quit :\n").lower()
    if user_input1 == 'q':
       quit()

    if user_input1 not in options:
        print("wrong selection chose again")
        continue

    while(True):
       user_input2=input("choose a number from 1 to 5\n")
       if user_input2.isdigit():
          user_input2=int(user_input2)
          if user_input2 < 1 and user_input2 > 5:
             continue 
       else:
         print("wrong selection chose a number 1 to 5")
         continue
       break
    computer_input=random.randint(1,5)
    
    if user_input1 == "head":
       num=user_input2+computer_input
       if num % 2 != 0:
          print("computer's number: "+str(computer_input))
          print("sum: "+ str(num))
          print("Its head you win ")
       else:
          print("computer's number: "+str(computer_input))
          print("sum: "+ str(num))
          print("you lose")
    
    if user_input1 == "tail":
       num=user_input2+computer_input
       if num % 2 == 0:
          print("computer's number: "+str(computer_input))
          print("sum: "+ str(num))
          print("Its tail you win ")
       else:
          print("computer's number: "+str(computer_input))
          print("sum: "+ str(num))
          print("you lose")
       