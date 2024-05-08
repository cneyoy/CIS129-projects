#carlos neyoy
#4-30-2024
#c129 lab 10
# this code grabs a monetary input in the form of a float and returns in computer check form 



def main():
    #declare variables we will use throughout the programs
    comCheck = ["*","*","*","*","*","*","*","*","*","*",]
    invalidInput = ["A","B","C","D","E","F","G","H","I","J","K","L","M",'N',"O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m",'n',"o","p","q","r","s","t","u","v","w","x","y","z","!","@","#","$","%","^","&","*","(",")","-","=","+",";",":",",","<",">","?","/","'","[","]","{","}","|"]
    userAmount = ""
    savedValue = ""
    savedcomCheck = ""
    savedValue = inputval(userAmount,invalidInput)
    savedcomCheck = processCheck(savedValue,comCheck)
    printCheck(savedcomCheck)
#manages the data inputed to make it easier to manipulate at the end    
def inputval(userAmount,invalidInput):
       userAmount = input("input a monetary value")
       userAmount = ''.join(x for x in userAmount if not x in invalidInput)
       if userAmount == None :
           print("there was an error make sure you input a monetary value with a decimal. only 10 characters are allowed") 
       elif len(userAmount) > 10:
           print("there was an error make sure you input a monetary value with a decimal. only 10 characters are allowed")
       else :
        return userAmount
        
#processes the string data to print the check in a formated way with * instead of white spaces         
def processCheck(savedValue,comCheck):
     counter = 0 
     for i in savedValue:
         counter -= 1
         comCheck[counter] = savedValue[counter]
     return comCheck
#prints the check out like specified with a little more details to make it more realistic on my part 
def printCheck(savedcomCheck):
     savedcomCheck = ''.join(savedcomCheck) 
     print(f"{'Name' : <10}{'______________':>45}")
     print(f"{'Date' : <10}{'_____________':>45}")
     print(f"{'Pay to' :<10}____________{'Amount':^15}{savedcomCheck :>18} $")
     print(f"{'----------' :>55}")
     print(f"{'12345678910':>55}")
main()