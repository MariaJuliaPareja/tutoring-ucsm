def s(t):
    return 4.9 * t ** 2

a = 5
for h in [0.1, 0.01, 0.001, 0.0001, -0.001, -0.01, 0.00000000001]:
    average_velocity = (s(a + h) - s(a)) / h
    print(f"h: {h}, Average velocity: {average_velocity}")