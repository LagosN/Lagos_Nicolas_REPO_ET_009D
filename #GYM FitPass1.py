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
