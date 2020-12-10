import sys
import ast
import bitarray as bit

def remove_char(a):
    return a[1:]

def descomprimir(diccionario,bits):
    lista = ''
    res = ''
    letras = list(diccionario.keys())
    valores = list(diccionario.values())
    i = 0
    j = 0
    while(i<len(bits)):
        lista+=bits[i]
        while(j<len(valores) and lista != ''):
            if lista==valores[j]:
                res+=letras[j]
                lista=''
            j+=1
        j = 0
        i +=1
        
        
    return res

if len(sys.argv) < 4:
        print("El programa no tiene la cantidad de argumentos necesarios")
        sys.exit()
bits = bit.bitarray()
with open(sys.argv[1],"rb") as huff:
    bits.fromfile(huff)
h = ''
for i in bits:
    if i:
        h = h + '1'
    else:
        h = h + '0'
table = open(sys.argv[2],"r",encoding="latin1")
t = table.read()
table.close()

diccionario1 = ast.literal_eval(t)

with open(sys.argv[3],"w")as nuevo_archivo:
        nuevo_archivo.write(descomprimir(diccionario1,h))
print(sys.argv[3])


