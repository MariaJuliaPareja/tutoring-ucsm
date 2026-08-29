# Ejercicio 1.1: Conjuntos por comprension
# Ejercicio a
A = {x for x in range(2,31) if x % 3 == 0}
# Ejercicio b
print(9 in A, 10 in A, 27 in A)
# Ejercicio c
print(len(A)) # ¿Qué múltiplos de 3 estan entre 2 y 30? 
# Ejercicio d
B = { x for x in A if x > 15}
print(B.issubset(A))