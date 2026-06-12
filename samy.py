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