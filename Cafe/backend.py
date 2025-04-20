#Código backend cafetería
import json
import os

usuarios_file = "usuarios.json"
empleados_file = "empleados.json"
inventario_file = "inventario.json"
bebidas_file = "bebidas.json"
historial_pedidos_file = "historial_pedidos.json"
puntos_file = "puntos.json"

# Función para cargar datos desde un archivo JSON
def cargar_datos(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return json.load(file)

# Función para guardar datos en un archivo JSON
def guardar_datos(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Funciones de usuarios y empleados
def guardar_usuario(nombre, email, contrasena, edad):
    usuarios = cargar_datos(usuarios_file)
    usuarios.append({"nombre": nombre, "email": email, "contrasena": contrasena, "edad": edad})
    guardar_datos(usuarios_file, usuarios)

def guardar_empleado(nombre, email, contrasena, rol):
    empleados = cargar_datos(empleados_file)
    empleados.append({"nombre": nombre, "email": email, "contrasena": contrasena, "rol": rol})
    guardar_datos(empleados_file, empleados)

def validar_login(email, contrasena):
    empleados = cargar_datos(empleados_file)
    for emp in empleados:
        if emp["email"] == email and emp["contrasena"] == contrasena:
            return emp["rol"], emp["nombre"]
    
    usuarios = cargar_datos(usuarios_file)
    for user in usuarios:
        if user["email"] == email and user["contrasena"] == contrasena:
            return "cliente", user["nombre"]

    return None, None

# Funciones de Inventario
def cargar_inventario():
    return cargar_datos(inventario_file)

def guardar_inventario(inventario):
    guardar_datos(inventario_file, inventario)

def agregar_ingrediente(nombre, cantidad):
    inventario = cargar_inventario()
    cantidad = int(cantidad)  # Asegurar que la cantidad sea numérica
    
    for item in inventario:
        if item["ingrediente"] == nombre:
            item["cantidad"] += cantidad
            break
    else:
        inventario.append({"ingrediente": nombre, "cantidad": cantidad})
    
    guardar_inventario(inventario)

def eliminar_ingrediente(nombre):
    inventario = cargar_inventario()
    inventario = [item for item in inventario if item["ingrediente"] != nombre]
    guardar_inventario(inventario)

# Funciones para bebidas
def cargar_bebidas():
    try:
        with open("bebidas.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Reemplazar la función duplicada guardar_datos con esta versión unificada
def guardar_datos(filename, data):
    """Versión unificada para guardar datos en JSON"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar en {filename}: {e}")
        return False

def agregar_bebida(nombre_bebida, categoria, ingredientes, cantidades):
    try:
        with open("bebidas.json", "r", encoding="utf-8") as file:
            bebidas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        bebidas = []

    # Verificar si ya existe una bebida con ese nombre
    for bebida in bebidas:
        if bebida["nombre"].lower() == nombre_bebida.lower():
            return "Error: La bebida ya está registrada"

    nueva_bebida = {
        "nombre": nombre_bebida,
        "categoria": categoria,
        "ingredientes": ingredientes,
        "cantidades": cantidades
    }

    bebidas.append(nueva_bebida)

    with open("bebidas.json", "w", encoding="utf-8") as file:
        json.dump(bebidas, file, indent=4, ensure_ascii=False)

    return "Producto registrado exitosamente"

# ----------------------------
# Funciones para gestión de puntos (añadir al backend)
# ----------------------------

def cargar_puntos():
    """Carga el sistema de puntos de los clientes"""
    try:
        with open("puntos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def guardar_puntos(puntos_data):
    """Guarda los puntos de los clientes"""
    with open("puntos.json", "w", encoding="utf-8") as f:
        json.dump(puntos_data, f, indent=4, ensure_ascii=False)

# ----------------------------
# Funciones para historial de pedidos (añadir al backend)
# ----------------------------

def cargar_historial_pedidos():
    """Carga el historial de pedidos"""
    return cargar_datos(historial_pedidos_file)

def guardar_pedido(pedido):
    """Guarda un nuevo pedido en el historial"""
    historial = cargar_historial_pedidos()
    historial.append(pedido)
    guardar_datos(historial_pedidos_file, historial)

# ----------------------------
# Función para actualizar inventario (mejorada)
# ----------------------------

def actualizar_inventario(nombre_producto, cantidad_usada):
    """
    Actualiza el inventario al realizar una compra
    Args:
        nombre_producto: Nombre del producto comprado
        cantidad_usada: Cantidad de ingredientes usados (puede ser un factor)
    """
    try:
        bebidas = cargar_bebidas()
        inventario = cargar_inventario()
        
        # Encontrar la bebida/postre
        producto = next((b for b in bebidas if b["nombre"] == nombre_producto), None)
        if not producto:
            return False
        
        # Actualizar cada ingrediente
        for ingrediente, cantidad_str in zip(producto["ingredientes"], producto["cantidades"]):
            # Extraer el valor numérico (ej. "50ml" -> 50)
            cantidad_num = float(''.join(filter(str.isdigit, cantidad_str)))
            
            # Calcular cantidad total usada
            cantidad_total = cantidad_num * cantidad_usada
            
            # Buscar el ingrediente en inventario
            for item in inventario:
                if item["ingrediente"] == ingrediente:
                    item["cantidad"] -= cantidad_total
                    if item["cantidad"] < 0:  # No permitir valores negativos
                        item["cantidad"] = 0
                    break
        
        guardar_inventario(inventario)
        return True
    
    except Exception as e:
        print(f"Error al actualizar inventario: {e}")
        return False



