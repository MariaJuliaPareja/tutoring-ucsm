# Ejercicio 4
# Ejercicio 4.1
A = {1, 2, 3, 4, 5, 6}
# Ejercicio a
R = {(a,b) for a in A for b in A if a % b == 0}
# Ejercicio b
def es_reflexiva (R, A):
	return all ((a, a) in R for a in A)
def es_simetrica (R):
	return all ((b, a) in R for (a, b) in R)
def es_antisimetrica (R):
	return all(a == b for (a, b) in R if (b, a) in R)
def es_transitiva (R):
	return all ((a, c) in R for (a, b1) in R for (b2 , c) in R if b1 == b2)~
# Ejercicio c
print (" Reflexiva :", es_reflexiva (R, A))
print (" Simetrica :", es_simetrica (R))
print (" Antisimetrica :", es_antisimetrica (R))
print (" Transitiva :", es_transitiva (R))
# Ejercicio 4.2
# Ejercicio a
def es_orden_parcial(R,A):
	return es_reflexiva(R,A) and es_antimetrica(R) and es_transitiva(R)
print ("Orden parcial", es_orden_parcial(R,A))
# Ejercicio b
def relacion_inversa(R):
	return {(b,a) for (a,b) in R}
R_inv = relacion_inversa(R)
# Representa es divisor de. Si R cada par (a,b)
# signfica a es multipo b, al invertir significa que b es divisor de a
