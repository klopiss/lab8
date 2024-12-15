def sum_del(n):
    divisors = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors += i
            if i != n // i:
                divisors += n // i
    return divisors
def friendly(a, b):
    return a != b and sum_del(a) == b and sum_del(b) == a
def find_friendly(limit):
    checked = set()
    for a in range(2, limit + 1):
        if a in checked:
            continue
        b = sum_del(a)
        if b <= limit and friendly(a, b):
            print(f"Дружественная пара: {a} и {b}")
            checked.add(a)
            checked.add(b)
try:
    limit = int(input("Введите целое натуральное число: "))
    if limit < 2:
        print("Число должно быть больше или равно 2")
    else:
        find_friendly(limit)
except ValueError:
    print("Ошибка: введите целое натуральное число")

