numbers=[]
first_num = int(input("Введите количество элементов списка:"))

for c in range(first_num):
    new_number=int(input("Введите значения списка через enter : "))
    numbers.append(new_number)
print(numbers)
s=int(input("Введите искомое число : "))
max=0
count = 0
for v in numbers:
    if v == s:
        count = v
    elif v!=s:
        if v>=s+1:
            count = v

print(f"Максимально приближенное из чисел :{count}")