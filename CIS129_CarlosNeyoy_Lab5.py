#carlos neyoy
#c129 prog & problem solving
#03-13-2024
# this is two programs the first is commented as it only asked me to fill in the blanks in the paper i tried using functions because we learned a little about them in class 
# the second program calculates how many bottles one would have accumilated in a week and the total they would get for all the battles



#setting local variables

# monthlySales = 0
# storeAmount = 0
# empAmount = 0
# salesIncrease = 0
# keepGoing = "y"

# #defines a function that determines the store bonus amount
# def detstoreAmount():
#    if monthlySales >= 110000 :
#         storeAmount = 6000
#    elif monthlySales >= 100000:
#         storeAmount = 5000
#    elif monthlySales >= 90000:
#         storeAmount = 4000 
#    elif monthlySales >= 80000:
#         storeAmount = 3000
#    else :
#         storeAmount = 0

# #defines a function that determines employee bonus amount
# def detEmpAmount():
#     if salesIncrease >= 0.05:  
#      empAmount = 75 
#     elif salesIncrease >= 0.04 :
#      empAmount = 50
#     elif salesIncrease >= 0.03:
#      empAmount = 40
#     else:
#      empAmount = 0
# #defines function that will output the calculated information to the user 
# def Oput():
#    if storeAmount == 6000 and empAmount == 75:
#     print("the store bonus is ", "$",storeAmount)
#     print("the employee bonus amount is", "$",empAmount)
#     print("Congrats! You have reached the highest bonus amounts possible!")
#    else :
#      print("the store bonus is ", "$",storeAmount)
#      print("the employee bonus amount is", "$",empAmount)

# #here our program is run by calling the functions defined above inside a while loop for repetition 
# while keepGoing == "y":
#    monthlySales = int(input("please input the monthly sales."))
#    detstoreAmount()
#    salesIncrease = float(input("please enter the sales increase"))
#    salesIncrease = salesIncrease/100
#    detEmpAmount()
#    Oput()
#    keepGoing = input("would you like to run the program again")

#part 2 of the lab starts here 

#this variable will store the accumulated bottle values



totalBottles = 0
#this variable will control the loop
counter = 1
#this variable will store the number of bottles returned on a day
todayBottles = 0
#This variable will store the calculated value of totalBottles times .10
totalPayout = 0
#This variable will be used to run the program again
keepGoing = "y"

# while loop that runs the program for repeated entries
while keepGoing =='y':
   
    #first input for bottles 
    todayBottles = int(input(f"Enter number of bottles returned for day #{counter}: "))
   #calculates and stores the bottles and there value
   totalBottles += todayBottles
   totalPayout += todayBottles * 0.10
   
   
   
   #executes when the loop has run 7 times displays the total bottles collected and there value and then promts the user if he wants to run the program again 
   if counter == 7:
      print(f'\n The total number of bottles collected is {totalBottles}')
      print(f'total payout for the week $ {round(totalPayout,3)}')
    
      todayBottles = 0
      totalPayout = 0
      totalBottles = 0
      counter =0

      keepGoing = input("\n Do you want to enter another week's worth of data enter 'y' or 'n': ")
      print("\n")
   #increases the counter to determine how many times the loop has run
   counter += 1
   
    
   

   
   