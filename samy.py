""" El complejo educacional “Chile 2030”, desea realizar una
aplicación computacional que le permita registrar en sus
establecimientos los alumnos a sus cursos """
while True:
    try:
        cant_alumnos=int(input("ingrese la cantidad de  alumnos a registrar"))
        if cant_alumnos>0 and cant_alumnos<=30:
            break
    except ValueError:
        print("la cantidad no puede ser superior a 30 y debe ser un numero positivo")
lista_alumnos=[]
for i in range(cant_alumnos):
        print("datos del alumno nro",i+1)
        alumno={}
        alumno["nombre"]=input("ingrese nombre del alumno")
        alumno["direccion"]=input("ingrese direccion del alumno")
        alumno["telefono"]=input("ingrese telefono del alumno")
        lista_alumnos.append(alumno)
for alumno in lista_alumnos:
    print("--------------------")
    print(alumno["nombre"])
    print("--------------------")
    print(alumno["direccion"])
    print("--------------------")
    print(alumno["telefono"])