#GYM FitPass

planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
    
}


inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
    
}

def opciones_menu():
    print("[1] Cupos por tipo de plan")
    print("[2] Búsqueda de planes por rango de precio")
    print("[3] Actualizar precio de plan")
    print("[4] Agregar plan")
    print("[5] Eliminar plan")
    print("[6] Salir")

#Al agregar usar numero INT
def leer_opcion():
    try:    
        opc = input("Ingresa una opcion")
        if opc == "":
            print("No puede quedar vacio.")
            return False
        opc = int(opc)
        if 1 <= opc <=6:
            return opc
        else:
            print("Solo puedes agregar numeros entre 1 y 6.")
            return False
    except ValueError:
        print("Debes seleccionar una opcion valida.")
        return False
    

def busqueda_opcion_1(tipo_plan):
    
    if tipo_plan== "":
        print("No pueded quedar vacio.")
        return False
    print("Paso")
    return tipo_plan

def busqueda( planes, inscripciones):
    tipo_plan = input("Ingresa el tipo de plan a buscar: (anual, mensual, trimestral)").strip().lower()
    plan = busqueda_opcion_1(tipo_plan)
    encontrado = False
    for codigo in planes:
        if tipo_plan in planes [codigo][1]:
            print(f"Codigo del plan: {codigo} | Cupos disponibles: {inscripciones[codigo][1]}")
            encontrado = True
            return
        if not encontrado:
            print("No se encontro plan con ese nombre. Intenta nuevamente.")
            return

#busqueda( planes, inscripciones)


def final_2():
    try:
        num1 = int(input("Ingresa el primer valor:"))
        if num1 <= 0:
                print("El numero debe ser mayor a 0.")
                return
    except ValueError:
        print("Error, solo puedes agregar numeros")    
    
    return num1

def opc_2(planes, inscripciones):
    num1 = final_2()
    num2 = final_2()
    if  num2 < num1:
        print("El primer numero no puede ser mas grande que el segundo.")
        return False
    encontrado = False
    for codigo in inscripciones:
        if num1 <= inscripciones[codigo][0] <= num2 and  inscripciones[codigo][1] > 0:
            print(f"Nombre Plan: {planes[codigo][0]} | Codigo: {codigo}")
    if not encontrado :
        print("No se encontraron resultados.") 

#opc_2(planes, inscripciones)

# que recorra el diccionario y retorne True si el código existe, o False si no existe.
def buscar_codigo(codigo): 
    if codigo == "":
        print("No puede quedar vacio.")
    if codigo in planes:
        return True
    else:
        return False
    
def num(num):


def opcion_3( ):
    codigo = input("Ingresa el codigo a buscar:").upper()
    codigo_v=buscar_codigo(codigo)
    if codigo_v is False:
        return
    
    nuevo_precio = input("Ingresa el nuevo valor:")
    precio_v = num(nuevo_precio)
    if precio_v is False:
        return
    
    actualizar_precio(codigo,nuevo_precio)


def actualizar_precio(codigo, nuevo_precio):
    if codigo not in inscripciones:
        print("No esta inscrito")
        return False
    nuevo_precio1 = int(nuevo_precio)
    inscripciones[codigo] = nuevo_precio1
    print("Precio actualizado")
    return True

#opcion_3()

#código, nombre, tipo, duración, acceso a piscina, inclusión de clases, horario, precio y cupos

def v_texto(texto):
    if texto == "":
        print("No puede quedar vacio.")
        return False

    return True

#Agregar .upper()
def v_codigo(codigo):
    if codigo == "":
        print("No puede quedar vacio.")
        return False
    if codigo in planes:
        return False
    else:
        return True
    
def numero_mayor_q(num):
    try:
        if num == "":
            return False
        num1 = int(num)
        if num1 < 0: 
            return False
        else:
            return True
    except ValueError:
        
        return False

def numero_igual_q(num):
    try:
        if num == "":
            return False
        num1 = int(num)
        if num1 <= 0:
            
            return False
        else:
            return True
    except ValueError:
        
        return False

def tipo1(tipo):
    if 1 <= tipo <=3:
        return True
    else:
        return False


def acceso(ap):
    if ap == "":
        None
    if ap == "s":
        return True
    if ap == "n":
        return False
    else:
        return None


#validar false por codigo
def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos):
    planes[codigo] = [nombre,tipo,duracion,acceso_piscina, incluye_clases, horario,precio,cupos]
    inscripciones[codigo] = [precio, cupos]
    print("Se agrego el plan")
    return True



def opc_4():
    while True:    
        codigo = input("Ingresa el nuevo codigo para agregar: ").upper()
        codigo_v = v_codigo(codigo)
        if codigo_v is False:
            print("Codigo ya existe .")
            return False
        
        nombre = input("Ingresa el nombre del plan:")
        nombre_v = v_texto(nombre)
        if nombre_v is False:
            print("Nombre invalido")
            return False
        
        tipo = int(input("Ingresa el tipo  [1] anual, [2]trimestral, [3] semestral:"))
        tipo_v = tipo1(tipo)
        if tipo_v is False:
            print("Tipo invalido debes agregar numero entre 1 y 3")
            return False
            
        if tipo == 1:
            tipo = "anual"
            
        if tipo ==2:
            tipo = "trismestral"
            
        if tipo == 3:
            tipo = "semestral"
        
        duracion = input("Ingresa el tiempo de uso del plan: ")
        duracion_v = numero_mayor_q(duracion)
        if duracion_v is False:
            print("Debes agregar un numero mayor a 0")
            return False
        
        acceso_piscina1 = input("Ingreso a piscina  s = si quieres  n = no quiero acceso: ").lower()
        accceso_piscina_v = acceso(acceso_piscina1)
        if accceso_piscina_v is None:
            print("Dato mal ingresado solo puedes agregar s o n")
            return
        if acceso_piscina1 == "s":
            acceso_piscina1 =True
        if acceso_piscina1 == "n":
            acceso_piscina1 = False

        incluye_clases1 = input("Acceso a clases extras?  s = si quieres  n = no quiero acceso: ").lower()
        incluye_clases1_v = acceso(incluye_clases1)
        if incluye_clases1_v  is None:
            print("Dato mal ingresado solo puedes agregar s o n")
            return False
        if incluye_clases1 == "s":
            incluye_clases1 = True
        if incluye_clases1 == "n":
            incluye_clases1 == False

        horario = input("Ingresa cuando se usara el gym ( mañana, tarde, libre, noche)").lower()
        horario_v = v_texto(horario)
        if horario_v is False:
            return False
        
        precio = input("Ingresa el valor total: ")
        precio_v = numero_mayor_q(precio)
        if precio_v is False:
            print("Error, debes agregar un valor valido (100000)")
            return False
        
        cupos = input("Ingresa los cupos disponibles: ")
        cupos_v = numero_igual_q(cupos)
        if cupos_v is False:
            print("Error, debes agregar un numero")
            return False

        agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina1, incluye_clases1, horario, precio, cupos)
        break
  

def eliminar_plan():
    codigo = input("Ingresa el codigo a buscar: ").lower
    codigo_v = buscar_codigo(codigo)
    if codigo_v is False:
        print("Codigo no existe")
        return False
    if codigo in inscripciones:
        eliminar = inscripciones.pop(codigo)
        eliminar2 = planes.pop(codigo)    
        print(f"Plan eliminado: {eliminar}")
        print(f"Plan eliminado: {eliminar2}")
        return True
    


def menu_general():
    while True:
        opciones_menu()
        opc = leer_opcion()
        if opc ==1:
            busqueda(planes, inscripciones)
        if opc == 2:
            opc_2(planes, inscripciones)
        if opc == 3:
            opcion_3 ()
        if opc == 4:
            opc_4()
        if opc == 5:
            eliminar_plan()
        if opc == 6:
            print("Programa finalizado")
            break


menu_general()