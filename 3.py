def sqrt_a(a, e=1e-6):
    if a<0:
        raise ValueError("Квадратный корень из отрицательного числа не считается")
    x0 = (1+a)/2
    def y(x_x):
        x_next = 0.5*(x_x + a / x_x)
        if abs(x_next - x_x) < e:
            return x_next
        return y(x_next)
    return y(x0)
while True:
    try:
        a = float(input("Введите неотрицательное число: "))
        if a < 0:
            print("Ошибка: введите неотрицательное число ")
            continue
        break
    except ValueError:
        print("Это не число, попробуйте ещё раз")
e = 1e-6
result = sqrt_a(a, e)
print(f"Приближённое значение x: {result:6f}")
