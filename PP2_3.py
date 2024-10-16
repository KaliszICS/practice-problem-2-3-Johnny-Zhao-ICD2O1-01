'''
    Practice Questions: Else If
    Author: Johnny Zhao
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024
'''

def q1(): 
  wordQ1 = (str(input("Input a word: ")))
  if wordQ1[-2:] == "ey":
    print("-eys")
  elif wordQ1[-1] == "y":
    print("-ies")
  elif wordQ1[-3:] == "ife":
    print("-ives")
  else:
    print("-s")

def q2(): 
  #Write Assignment code here



#Do not alter the following code
#Comment out the following code when running your tests

  q1()
q2()
