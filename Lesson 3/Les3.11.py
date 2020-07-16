number = input()
x = 0
for i in number:
    x += int(i)
print(x)

number2 = int(input())
num1 = number2//100
x = number2 - (num1*100)
num2 = x//10
num3 = x - (num2*10)
print(num1 + num2 + num3)
