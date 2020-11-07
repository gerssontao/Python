bloques = int(input("Ingrese el número de bloques: "))
altura = 0 
#
# Escribe tu código aquí.
#
i=1
while i <= bloques:
    altura = i 
    bloques = bloques - i 
    i+=1
print("La altura de la pirámide:", altura)
