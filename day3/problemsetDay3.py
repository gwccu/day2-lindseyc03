#even or odd

userNum = int(input("Enter a number: "))
if (userNum % 2) == 0:
    print("Your number is even")
else:
    print("Your number is odd")

userNum1 = int(input("Enter a number: "))
userNum2 = int(input("Enter a second number: "))
userNum3 = int(input("Enter a third number: "))

rem1 = userNum1 % 2
rem2 = userNum2 % 2
rem3 = userNum3 % 2

if (rem1 != 0) and (rem2 != 0) and (rem3 != 0):
    print("All three numbers are odd")
elif not(rem1 !=0) and not(rem2 != 0) and (rem3 != 0 ):
    print(userNum3, "is odd")
elif (rem1 !=0) and not(rem2 != 0) and (rem3 != 0):
    print(userNum1, "is odd and", userNum3, "is also odd")
elif (rem1 !=0) and (rem2 !=0) and not(rem3 !=0):
    print(userNum1, "is odd and so is", userNum2,)
elif (rem1 != 0) and not(rem2 != 0)
