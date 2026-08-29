# Ejercicio 1
a = ['Carlo','Jose','Luis']
n = len(a)
I = {i for i in range(n)} # I = {0,1,2}
# a[-1] -> a[n-1]

# Ejercicio 2
R = {(x,y) for x in a for y in a if len(x) <= len(y)}
# Resultado: 7 de 10 posibles pares

# Reflexiva : True (menor igual)
# Transitiva : True x<=y<=z
# Antisimetrica : False (Jose != Luis, misma long)
# No orden parsial : False