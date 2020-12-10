import bitarray as bit
from io import open
import sys
#algoritmo de ordenamiento usado para ordenar frecuencias
def insertionSort(alist):
        for index in range(1,len(alist)):
                position = index
                while position>0 and alist[position-1][1]>alist[position][1]:
                        (alist[position],alist[position-1]) = (alist[position-1],alist[position])
                        position = position-1
        return alist
#saca las frecuencias de cada uno de los caracteres
def frecuencias(string):
	resp = []
	i = 0
	j = 0
	while(i<len(string)):
                
		encontrado = False
		while(j<len(resp)):
			if string[i]==resp[j][0]:
				resp[j][1]+=1
				encontrado = True
			j += 1
		if not encontrado:
			resp.append([string[i],1])
		i+=1
		j = 0
	return insertionSort(resp)

#crea el arbol a partir de las frecuencias
def crea_arbol(frecuencia):
        arb = []
        sum = suma_frecuencias(frecuencia)
        while(len(frecuencia)!=0):
                if len(arb)==0:
                        rama = []
                        valor = frecuencia[0][1]+frecuencia[1][1]
                        rama.append(valor)
                        rama.append([frecuencia[0][0],[],[]])
                        rama.append([frecuencia[1][0],[],[]])
                        arb.append(rama)
                        frecuencia.pop(0)
                        frecuencia.pop(0)
                elif arb[0][0] > frecuencia[0][1]:
                        rama = []
                        valor = frecuencia[0][1]+frecuencia[1][1]
                        rama.append(valor)
                        rama.append([frecuencia[0][0],[],[]])
                        rama.append([frecuencia[1][0],[],[]])
                        arb.append(rama)
                        frecuencia.pop(0)
                        frecuencia.pop(0)
                else:
                        rama = []
                        hoja2 = []
                        valor = arb[0][0]+frecuencia[0][1]
                        hoja = arb[0]
                        hoja2.append(frecuencia[0][0])
                        hoja2.append([])
                        hoja2.append([])
                        rama.append(valor)
                        rama.append(hoja)
                        rama.append(hoja2)
                        arb.append(rama)
                        frecuencia.pop(0)
                        arb.pop(0)
        while arb[0][0]!=sum:
                rama = []
                valor = arb[0][0] + arb[1][0]
                hoja = arb[0]
                hoja2= arb[1]
                rama.append(valor)
                rama.append(hoja)
                rama.append(hoja2)
                arb.append(rama)
                arb.pop(0)
                arb.pop(0)
                        
        return arb[0]

#saca los codigos de cada caracter por separado
def caminos(subarbol,actual,diccionario):
        if type(subarbol[0]) == str:
                diccionario[subarbol[0]] = actual
        else:
                caminos(subarbol[1],actual + "0",diccionario)
                caminos(subarbol[2],actual + "1",diccionario)
                
#saca el codigo de todo el string
def codigoPalabra(palabra,diccionario):
        codigo = ""
        for i in palabra:
                codigo = codigo + diccionario[i]
        return codigo
                

#es utilizada para la funcion crea_arbol suma todas las frecuencias
def suma_frecuencias(frecuencia):
        i = 0
        suma = 0
        while(i<len(frecuencia)):
                suma+=frecuencia[i][1]
                i+=1
        return suma

#saca la altura de un arbol
def altura(arb):
	if (arb==[]):
		return 0
	return 1 + max(altura(arb[1]),altura(arb[2]))

#saca la cantidad de numero de nodos por nivel
def n_nodos_level(arb,n):
	if(arb == []):
		return 0
	elif(n == 0):
		return 1
	else:
		return n_nodos_level(arb[1], n-1)+n_nodos_level(arb[2], n-1)


#saca los nodos de todos los niveles
def nodos_nivel(arb):
        i = altura(arb)-1
        lista = []
        while(i>=0):
                lista.append(["Nivel: "+ str(i),"Nodos: "+str(n_nodos_level(arb,i))])
                i-=1
        return lista

def print_frecuencias(string):
	resp = []
	i = 0
	j = 0
	while(i<len(string)):
                
		encontrado = False
		while(j<len(resp)):
			if string[i]==resp[j][0]:
				resp[j][1]+=1
				encontrado = True
			j += 1
		if not encontrado:
			resp.append([string[i],1])
		i+=1
		j = 0
	return insertionSort(resp)


#saca la anchura del arbol
def anchura_arbol(arb):
        return ancho_arbol_aux(arb,0,[])

def ancho_arbol_aux(arb,n,acum):
        if (arb==[]):
                return 0
        elif(n>altura(arb)):
                return max(acum+[1])
        return ancho_arbol_aux(arb,n+1,acum+[n_nodos_level(arb,n+1)])

if len(sys.argv) < 2:
        print("El programa no tiene argumentos, se requiere el nombre del archivo a comprimir")
        sys.exit()

archivo = open(sys.argv[1],"r",encoding="latin1")
s = archivo.read()
archivo.close()
x = frecuencias(s)
a = crea_arbol(x)
tablaf = print_frecuencias(s)
nodosnivel = nodos_nivel(a)
anchura1 = anchura_arbol(a)
altura1 = altura(a)


diccionario = {}
caminos(a,"",diccionario)

def print_stats(frecuencia,nodos,altura,anchura):
        return str("Las frecuencias de cada caracter son: ")+str(frecuencia)+"\n"+str("La cantidad de nodos por nivel son: ")+"\n"+str(nodos)+"\n"+str("La altura del arbol es: ")+"\n"+str(altura)+"\n"+str("La anchura del arbol es: ")+"\n"+str(anchura)
b = codigoPalabra(s,diccionario)
bits = bit.bitarray(b)
j = print_stats(tablaf,nodosnivel,altura1,anchura1)
with open(sys.argv[1]+".huff",'wb') as huff:
        bits.tofile(huff)
with open(sys.argv[1]+".stats","w")as stats:
        stats.write(j)
with open(sys.argv[1]+".table","w")as table:
        table.write(str(diccionario))
print(sys.argv[1]+".huff ",sys.argv[1]+".stats ",sys.argv[1]+".table")







