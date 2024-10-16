'''
    Practice Questions: Else If
    Author: Johnny Zhao
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024
'''

def q1(): 
  wordQ1 = (str(input("In: "))) #asking the user to input a word, turning it into a string datatype
  if wordQ1[-2:] == "ey": #if the word ends in "ey", then
    print("-eys") #output "-eys"
  elif wordQ1[-1] == "y": #if the previous doesn't match, then if the word ends in "y", then
    print("-ies") #output "-ies"
  elif wordQ1[-3:] == "ife": #if the previous doesn't match, then if the word ends in "ife", then
    print("-ives") #output "-ives"
  else: #if none of the above, then
    print("-s") #output "-s"

def q2(): 
  numQ2 = int(input("In: ")) #asking the user to input a integer, turning their number into an integer datatype
  if numQ2 > 0: #if the number is greater than 0, then
    print(f"{numQ2} is positive") #output "_their number_ is positive"
  elif numQ2 < 0: #if the number is not greater than 0, then if the number is less than 0, then
    print(f"{numQ2} is negative") #output "_their number_ is negative"
  
def q3():
  numQ31 = float(input("Input a number: ")) #asking the user to input a number, turning their number into a float datatype
  numQ32 = float(input("Input a number: ")) #asking the user to input a number, turning their number into a float datatype x2
  numQ33 = float(input("Input a number: ")) #asking the user to input a number, turning their number into a float datatype x3
  if numQ31 + numQ32 < numQ33 or numQ31 + numQ33 < numQ32 or numQ32 + numQ33 < numQ31: #checking if two number added together is less than the other number, if in that case, then
    print("No Triangle") #output "No Triangle"
  elif numQ31 == numQ32 == numQ33: #if the previous doesn't match, then if all number are equal, then
    print("Equilateral") #output "Equilateral"
  elif numQ31 == numQ32 or numQ32 == numQ33 or numQ31 == numQ33: #if the previous doesn't match, then if two number are equal, then
    print("Isosceles") #output "Isosceles"
  else: #if none of the above, then
    print("Scalene") #output "Scalene"
    
#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()