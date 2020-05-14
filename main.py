1.
org_password = "87654321"
login = input("Input your login: ")
password = input("Input your password: ")
if password == org_password:
    print("You are welcome!")
else:
    print("Error!")

2.
sec = int(input("Enter seconds: "))
h = (sec // 3600) % 24
m = sec % 3600 // 60
s = sec % 60
print("{:02}:{:02}:{:02}".format(h, m, s))

3.
n = input("Enternumber: ")
nn = int(n + n)
nnn = int(n + n + n)
sum = int(n) + (nn) + (nnn)
print(sum)

4.
number = int(input("Введите целое положительное число: "))
max_num = -1
while number > 10:
    d = number % 10
    number //= 10
    if d > max_num:
        max_num = d
print(max_num)

5.
rev = int(input("Введите значение выручки: "))
cos = int(input("Введите значение издержек: "))
profit = rev - cos
if profit > 0:
    print(f"Фирма работает с прибылью {profit} руб.")
elif profit < 0:
    print(f"Фирма работает с убытком {profit} руб.")

else:
    print("Фирма работает нулевой рентабельностью")
man = int(input("Введите количество работников: "))
one_man_p = profit / man
print(f"Прибыль фирмы на одного сотрудника составляет {one_man_p:.2f} руб.")

6.
a = 2
b = 3
n = 0
while True:
    a = a * 1.1
    n += 1
    if a > b:
        break
    if a % 2 == 10:
        continue
    print(f"{n}-й день: {a:.2f} км.")
print(f"Ответ: на {n}-й день спортсмен достиг результата - не менее {b} км.")
