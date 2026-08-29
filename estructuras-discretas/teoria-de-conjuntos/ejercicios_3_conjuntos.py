# Ejercicio 3
from itertools import combinations
# Funcion powerset, Ejercicio a
def powerset(A):
	A = list (A)
	resultado = []
	for k in range (len (A) + 1):
		for combo in combinations (A, k):
			resultado.append (set(combo))
	return resultado
# Recursión, Ejercicio d
def powerset_recursivo(A):
	A_list=list(A)
	if not A_list:
		return [set()]
	# Tomar 1er elemento del resto
	head = A_list[0]
	tail = A_list[1:]
	# Llamada recursiva
	sub_p = powerset_recursivo(tail)
	return sub_p + [s | {head} for s in sub_p]

A = {1, 2, 3}
P = powerset(A)
# Ejercicio b
print (len (P) == 2 ** len (A))
# Ejercicio c
for s in P:
	print (s)
P_rec = powerset_recursivo(A)
for s in P_rec:
	print(s)