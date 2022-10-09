# მომხმარებელს ტერმინალიდნ შემოატანინეთ სამი რიხვი და დამიჯამეთ კენტები
num1=int(input("enter num 1: "))
num2=int(input("enter num 2: "))
num3=int(input("enter num 3: "))

sum_of_odd_num = 0


if num1 % 2 == 1:
   sum_of_odd_num += num1
if num2 % 2 == 1:
   sum_of_odd_num += num2
if num3 % 2 == 1:
   sum_of_odd_num += num3

print("the sum of odd numbers is {}". fomrat(sum_of_odd_num))
# print(sum_of_odd_num)