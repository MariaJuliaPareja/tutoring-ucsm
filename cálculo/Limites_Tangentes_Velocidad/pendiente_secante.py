def f(x):
    return x**2

a = 1
for h in [0.1, 0.01, 0.001, 0.0001, -0.001, -0.01, 0.00000000001]:
    secant_slope = (f(a + h) - f(a)) / h
    print(f"h: {h}, Secant slope: {secant_slope}")