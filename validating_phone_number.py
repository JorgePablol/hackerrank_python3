#VALIDATING PHONE NUMBER

#    Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.
#    A valid mobile number is a ten digit number starting with a 7, 8 or 9.




import re   

if __name__ == '__main__':
    for i in range(int(input())):
        n = input()
        check = bool(re.search(r"^[789]\d{9}$", n))
        if check:
            print('YES')
        else:
            print('NO')
