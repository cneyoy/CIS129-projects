
#Carlos Neyoy
#05-07-2024
#c129 programing and problem solving
#this python script will write student names and grades to a text file 
from os import write
from typing import Counter
import csv

def main():
    sentinel = 0
    runs = 0
    gradebook ={"Names":"Grades"}
    names = ""
    grades = ""
    
    sentinel = sentinelVal()
    while runs <= sentinel - 1 :
        runs += 1
        names = str(input("input name of student: "))
        grades = int(input("input the grade the student recieved: "))
        gradebook.update({names:grades})
    writeTo(gradebook)
    readFrom()
    writetoCsv()
    
def writetoCsv():
  sentinel = 0
  runs = 0
  firstlastn = []
  examgrades = []
  fields = ["Name","Last Name","Exam1grade","Exam2grade","Exam3grade"]
  csvgradebook = {}
   
  while runs <= sentinel - 1 :
        runs += 1
        firstlastn[0] = str(input("Input students first name: "))
        firstlastn[1] = str(input("Input students last name: "))
        examgrades[0] = int(input("Input students first exam score: "))
        examgrades[1] = int(input("Input students second exam score: "))
        examgrades[2] = int(input("Input students third exam score: "))
        
        csvgradebook.update({firstlastn:examgrades})
   


  with open("grades.csv", "w") as csvfile:
       writer = csv.DictWriter(csvfile,fieldnames=fields)
       writer.writeheader()
       writer.writerows(csvgradebook)

def writeTo(gradebook):
   f = open("grades.txt","w")
   for names, grades in gradebook.items() :
       f.write(f"{names:<10}{grades:>10} \n")

def readFrom():
  r = open("grades.txt","r")
  stringgrades = ""
  grades = []
  counter = 0
  for line in r :
      for i in line :
          if i.isdigit() == True :
              grades.append(i)
  stringgrades = "".join(grades)
  finalgrades = [stringgrades[i:i + 2] for i in range(0,len(stringgrades),2)]
  finalgrades = [int(x) for x in finalgrades]     
  print("this is the list of grades ",finalgrades)
  lines = len(finalgrades)
  print(f"total number of grades: {lines}")
  print(f"grade average for students in this class: {sum(finalgrades)/len(finalgrades)}")
    
def sentinelVal(): 
    
    while True:
        value= int(input("how many grades will you be inputing today "))
        if value <= 0 :
            print("sentinal value must be greater than 0 ")
        else:
            break
    return value
main()