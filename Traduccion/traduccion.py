#Elavorar un programa que tenga un archivo de texto llamado EN-ES.txt el cual contiene 
#Las traducciones de palabras de ingles al español

'''
Gat = Gato
Hello = Hola
Laptop = computadora portatil
'''

'''
El programa debe tener la capacidad de:
1. Agregar nuevas traducciones
2.Traducir al idioma de la siguiente forma codigo de origen, codigo destino, y palabra
EN-ES Gat --> Gato
ES-EN Gato = Gat
'''
def Ingresar_traduccion(archivo, codigo_origen, codigo_destino, palabra):
    with open( archivo,  "a") as file:
        file.write(f"{codigo_origen} = {codigo_destino} = {palabra}\n")

#proceso de traduccion
def traducir(archivo, codigo_origen, codigo_destino, palabra):
        with open(archivo, "r") as file:
             
           lineas = file.readlines()
           for linea in lineas:
               partes = linea.strip().split(" = ")
               if len(partes) ==3:
                   codigo_origen, codigo_destino, traduccion = partes
                   if codigo_origen == codigo_origen and codigo_destino == codigo_destino and traduccion == palabra:
                      return f"{codigo_origen} {codigo_destino} {palabra} --> {traduccion}"
        return "Traduccion No Encontrada"
            


Ingresar_traduccion("EN-ES.txt", "EN", "ES", "Gat")
Ingresar_traduccion("EN-ES.txt", "EN", "ES", "Hello")
Ingresar_traduccion("EN-ES.txt", "EN", "ES", "laptop")
Ingresar_traduccion("ES-EN.txt", "ES", "EN", "Gato")
Ingresar_traduccion("ES-EN.txt", "ES", "EN", "Hola")
Ingresar_traduccion("ES-EN.txt", "ES", "EN", "Computadora portatil")



resultado1 = traducir("EN-ES.txt", "EN", "ES", "Gat")
resultado2 = traducir("ES-EN.txt", "ES", "EN", "Gato")

print(resultado1)
print(resultado2)


            