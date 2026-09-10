def tabla_secante(f, a, h_values):
    for h in h_values:
        secant_slope = (f(a + h) - f(a)) / h
        print(f"h: {h}, Secant slope: {secant_slope}")

def f(x):
    return x**2

tabla_secante(f, 3, [0.1, 0.01, 0.001, 0.0001, -0.001, -0.01, 0.00000000001])