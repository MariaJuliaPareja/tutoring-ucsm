# Ejercicio 2.1
# Ejercicio a
def union_manual(A,B):
	resultado = set()
	for elem in A:
		resultado.add(elem)
	for elem in B:
		resultado.add(elem)
	return resultado
# Ejercicio b
def intereseccion_manual(A,B):
	resultado = set()
	for elem in A:
		for elem in B:
			resultado.add(elem)
	return resultado
# Ejercicio c
def diferencia_manual(A,B):
	resultado = set()
	for elem in A:
		if elem not in B:
			resultado.add(elem)
	return resultado

# Ejercicio d
A = {1,2,3,4}
B = {3,4,5,6}

assert union_manual(A,B) == A | B
assert interseccion_manual(A,B) == A & B
assert diferencia_manual(A,B) == A - B
print('Todo oki')
