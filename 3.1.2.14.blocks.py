bloques = int(input("Ingrese el número de bloques: "))
altura= 1
capaCompleta = 1
capaInferior = 0
capaSuperior = 0
#
# Escribe tu código aquí.
#
i=1
while i < bloques:
    print(capaInferior, capaSuperior)
    capaInferior = capaInferior + 1
    i += 1
    print(i)
    print(capaInferior, capaSuperior)
print("La altura de la pirámide:", altura)
