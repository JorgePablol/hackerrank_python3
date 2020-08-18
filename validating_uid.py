#VALIDATING UID
  #The company decides to create a unique identification number (UID) for each of its employees.
  #The company has assigned you the task of validating all the randomly generated UIDs.
  #LINK = https://www.hackerrank.com/challenges/validating-uid/problem
  
  
import re
for i in range(int(input())):
    string = input().strip()
    string = "".join(sorted(string))
    if len(string) == 10:
    
        if (re.search(r"[A-Z]{2}", string) and re.search(r"\d{3}", string) and not re.search(r"[^A-Za-z0-9]", string) and not re.search(r"(\w)\1", string)):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
