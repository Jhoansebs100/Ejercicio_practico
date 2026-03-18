"""El programa debe permitir:

1️⃣ Registrar estudiantes
2️⃣ Calcular el promedio de tres notas
3️⃣ Determinar el estado del estudiante
4️⃣ Permitir registrar varios estudiantes usando un menú
5️⃣ Mostrar un resumen final"""
N1= 0
N2 = 0
N3 = 0
sumprom=0
estudiantes=0

def registrar_estudiante():
    name = input("Ingresar tu nombre, porfavor: ")
    age = int(input("Ingresar tu edad, porfavor: "))
    N1 = float(input("Ingresar la primer nota: "))
    N2 = float(input("ingresar la segunda nota: "))
    N3 = float(input("ingresar la tercera nota: "))


    if N1>=0 and N1<=5 and N2<=5 and N2>= 0 and N3<=5 and N3>=0 and age > 0: 
        return name, age, N1, N2, N3
    else:
         print("Error, ingresa las notas van de 0 a 5 y la edad de 0 en adelante: ")
         registrar_estudiante()    

def promedio(N1,N2,N3):
    prom= (N1+N2+N3)/3
    return prom
    
def evaluar_promedio(prom):
    if prom >= 4.0 :
        estado  = "Aprobado"
    elif prom >= 3.0 and prom < 4.0:
        estado = "En recuperación"
    elif prom < 3.0:
        estado = "Reprobado"
    return estado

def menu ():
        print(" -----BIENVENID@ AL SISTEMA DE ESTUDIANTES-----")
        print("""1. Registrar estudiante
2.Salir""")
        
while True:
     menu()
     opcion=  input("Seleccionar opción: ")
     if opcion == "1":
        name,age,N1,N2,N3 = registrar_estudiante()
        prom =promedio(N1,N2,N3)
        estado=evaluar_promedio(prom)
        print("Nombre:",name)
        print("Edad:",age)
        print("Promedio:",prom)
        print("Estado:",estado)
        sumprom=sumprom+prom
        estudiantes+=1
     elif opcion == "2":
         if estudiantes == 0:
             print(f"El total de estudiantes registrados es de: 0 y el promedio total del grupo es de: 0")
         else:
             print(f"El total de estudiantes registrados es de: {estudiantes} y el promedio total del grupo es de: {sumprom/estudiantes}") 
         break
     else:
         print("Opción no válida, por favor selecciona una opción del menú.")

       
          
          
        



