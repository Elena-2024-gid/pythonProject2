n = int (input ("Введите число от 3 до 20: "))
result = ''

for a in range (1, n//2+1):
    for b in range (a+1,n):
        if n % (a+b) == 0:
            result += str (a)+str (b)
print(result)
