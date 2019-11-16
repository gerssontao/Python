mLista=["Maria", "Pepe", "Martha", "Antonio"]

print(mLista[2]) #Martha
print(mLista[-1]) #Antonio
print(mLista[-4]) #Maria
print(mLista[2:]) #del 2 en adelante
print(mLista[3:]) #Dos ultimos elementos
print(mLista[1:]) #Dos ultimos elementos

mLista.append("Sandra") #agregar al ultimo indice

mLista.insert(2, "Andres") #agregar en el indice elegido

mLista.extend(["Tito", "Timoteo"]) #agregar varios elementos

print(mLista)

print(mLista.index("Antonio")) #imprimir  

