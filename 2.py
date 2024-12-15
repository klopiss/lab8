import math
def u(x, y):
    return x - y
def v(x, y):
    return x**2 + math.sin(y)
def F(u, v):
    if abs(u * v) > 700:
        raise ValueError("Произведение слишком велико для вычисления экспоненты.")
    return math.exp(u * v) + v
def R_R(x,y):
    u_u = u(x,y)
    v_v = v(x,y)
    F_F = F(u_u, v_v)
    if F_F == 0:
        raise ValueError("Значение F не может быть равно нулю для вычисления логарифма")
    if u_u * v_v <0:
        raise ValueError("Произведение не может быть отрицательным")
    if  abs(u_u*v_v) < 1e-10:
        raise ValueError("Слишком маленькие значения")
    R = math.log(abs(F_F)) + math.sqrt(abs(u_u*v_v))
    return R
try:
    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    result = R_R(x, y)
    print(f"Значение R: {result}")
except ValueError as e:
    print(f"Ошибка: {e}")