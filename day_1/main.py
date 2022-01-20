firstNum = int(input())
secondNum = int(input())

print("1 is for add")
print("2 is for subtract")
print("3 is for multiply")
print("4 is for divide")
print("5 is for modulus")

option = int(input())

answer = 0
if (option == 1):
    answer = firstNum + secondNum
elif (option == 2):
    answer = firstNum - secondNum
elif (option == 3):
    answer = firstNum * secondNum
elif (option == 4):
    answer = firstNum / secondNum
else:
    answer = firstNum % secondNum

print("The answer is {}".format(answer))
