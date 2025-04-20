#Código frontend cafeteria
import customtkinter as ctk
from tkinter import messagebox
from backend import guardar_usuario, guardar_empleado, validar_login, agregar_ingrediente, eliminar_ingrediente, cargar_inventario,guardar_datos,agregar_bebida,cargar_bebidas, guardar_puntos, cargar_puntos, guardar_inventario, cargar_datos
import datetime


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

ventana_inicio = ctk.CTk()
ventana_inicio.title("Inicio")
ventana_inicio.geometry("400x300")

def abrir_registro_cliente():
    ventana_inicio.withdraw()
    ventana_cliente.deiconify()

def abrir_registro_empleado():
    ventana_inicio.withdraw()
    ventana_empleado.deiconify()

def abrir_login():
    ventana_inicio.withdraw()
    ventana_login.deiconify()

def volver_a_inicio(ventana):
    ventana.withdraw()
    ventana_inicio.deiconify()

# Interfaz de Inicio
ctk.CTkLabel(ventana_inicio, text="Seleccione una opción", font=("Arial", 20)).pack(pady=20)
ctk.CTkButton(ventana_inicio, text="Registrar Cliente", command=abrir_registro_cliente).pack(pady=5)
ctk.CTkButton(ventana_inicio, text="Registrar Empleado", command=abrir_registro_empleado).pack(pady=5)
ctk.CTkButton(ventana_inicio, text="Iniciar Sesión", command=abrir_login).pack(pady=5)

# -------------------------------------------
# Ventana de Registro de Cliente
ventana_cliente = ctk.CTkToplevel(ventana_inicio)
ventana_cliente.title("Registro de Cliente")
ventana_cliente.geometry("400x500")
ventana_cliente.withdraw()

def registrar_usuario():
    nombre_cliente = entry_nombre.get()
    email = entry_email.get()
    contrasena = entry_contrasena.get()
    edad = entry_edad.get()

    if not nombre_cliente or not email or not contrasena or not edad:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número válido")
        return

    guardar_usuario(nombre_cliente, email, contrasena, edad)
    messagebox.showinfo("Éxito", "Cliente registrado correctamente")
    volver_a_inicio(ventana_cliente)

ctk.CTkLabel(ventana_cliente, text="Registro de Cliente", font=("Arial", 20)).pack(pady=10)
entry_nombre = ctk.CTkEntry(ventana_cliente, width=300, placeholder_text="Nombre")
entry_email = ctk.CTkEntry(ventana_cliente, width=300, placeholder_text="Email")
entry_contrasena = ctk.CTkEntry(ventana_cliente, width=300, show="*", placeholder_text="contrasena")
entry_edad = ctk.CTkEntry(ventana_cliente, width=300, placeholder_text="Edad")
for widget in [entry_nombre, entry_email, entry_contrasena, entry_edad]:
    widget.pack(pady=5)
ctk.CTkButton(ventana_cliente, text="Registrar", command=registrar_usuario).pack(pady=10)
ctk.CTkButton(ventana_cliente, text="Volver", command=lambda: volver_a_inicio(ventana_cliente)).pack(pady=5)

# -------------------------------------------
# Ventana de Registro de Empleado
ventana_empleado = ctk.CTkToplevel(ventana_inicio)
ventana_empleado.title("Registro de Empleado")
ventana_empleado.geometry("400x450")
ventana_empleado.withdraw()

def registrar_empleado():
    nombre = entry_emp_nombre.get()
    email = entry_emp_email.get()
    contrasena = entry_emp_contrasena.get()
    rol = entry_emp_rol.get()

    if not nombre or not email or not contrasena or not rol:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    guardar_empleado(nombre, email, contrasena, rol)
    messagebox.showinfo("Éxito", "Empleado registrado correctamente")
    volver_a_inicio(ventana_empleado)

ctk.CTkLabel(ventana_empleado, text="Registro de Empleado", font=("Arial", 20)).pack(pady=10)
entry_emp_nombre = ctk.CTkEntry(ventana_empleado, width=300, placeholder_text="Nombre")
entry_emp_email = ctk.CTkEntry(ventana_empleado, width=300, placeholder_text="Email")
entry_emp_contrasena = ctk.CTkEntry(ventana_empleado, width=300, show="*", placeholder_text="contrasena")
entry_emp_rol = ctk.CTkEntry(ventana_empleado, width=300, placeholder_text="Rol (gerente, barista.)")
for widget in [entry_emp_nombre, entry_emp_email, entry_emp_contrasena, entry_emp_rol]:
    widget.pack(pady=5)
ctk.CTkButton(ventana_empleado, text="Registrar", command=registrar_empleado).pack(pady=10)
ctk.CTkButton(ventana_empleado, text="Volver", command=lambda: volver_a_inicio(ventana_empleado)).pack(pady=5)

# -------------------------------------------
# Ventana de Login
ventana_login = ctk.CTkToplevel(ventana_inicio)
ventana_login.title("Login")
ventana_login.geometry("400x300")
ventana_login.withdraw()

ctk.CTkLabel(ventana_login, text="Iniciar Sesión", font=("Arial", 20)).pack(pady=10)

# Definimos los Entry antes de usarlos en la función iniciar_sesion
entry_login_email = ctk.CTkEntry(ventana_login, width=300, placeholder_text="Email")
entry_login_contrasena = ctk.CTkEntry(ventana_login, width=300, show="*", placeholder_text="contrasena")
entry_login_email.pack(pady=5)
entry_login_contrasena.pack(pady=5)

def iniciar_sesion():
    email = entry_login_email.get()
    contrasena = entry_login_contrasena.get()

    tipo_usuario, nombre = validar_login(email, contrasena)
    print(f"Tipo de usuario: {tipo_usuario}, Nombre: {nombre}")  # Mensaje de depuración

    if tipo_usuario:
        messagebox.showinfo("Éxito", f"Bienvenido, {nombre}")
        ventana_login.withdraw()

        if tipo_usuario == "gerente":
            abrir_entorno_gerente(nombre)
        elif tipo_usuario == "barista":
            abrir_entorno_barista(nombre)    
        else:
            abrir_entorno_cliente(nombre,email)
    else:
        messagebox.showerror("Error", "Credenciales incorrectas")

ctk.CTkButton(ventana_login, text="Ingresar", command=iniciar_sesion).pack(pady=10)
ctk.CTkButton(ventana_login, text="Volver", command=lambda: volver_a_inicio(ventana_login)).pack(pady=5)

# -------------------------------------------
def abrir_entorno_gerente(nombre):
    ventana_gerente = ctk.CTkToplevel()
    ventana_gerente.title("Entorno del Gerente")
    ventana_gerente.geometry("600x600")

    pestañas = ctk.CTkTabview(ventana_gerente)
    pestañas.pack(expand=True, fill="both")

    # --------- Pestaña de Inventario ---------
    tab_inventario = pestañas.add("Inventario")

    ctk.CTkLabel(tab_inventario, text="Gestión de Inventario", font=("Arial", 16)).pack(pady=10)

    entry_ingrediente = ctk.CTkEntry(tab_inventario, width=300, placeholder_text="Ingrediente")
    entry_cantidad = ctk.CTkEntry(tab_inventario, width=300, placeholder_text="Cantidad")
    entry_ingrediente.pack(pady=5)
    entry_cantidad.pack(pady=5)

    def actualizar_lista():
        lista_inventario.delete("1.0", "end")
        inventario = cargar_inventario()
        for item in inventario:
            lista_inventario.insert("end", f"{item['ingrediente']}: {item['cantidad']}\n")

    ctk.CTkButton(tab_inventario, text="Agregar", command=lambda: [agregar_ingrediente(entry_ingrediente.get(), entry_cantidad.get()), actualizar_lista()]).pack(pady=5)
    ctk.CTkButton(tab_inventario, text="Eliminar", command=lambda: [eliminar_ingrediente(entry_ingrediente.get()), actualizar_lista()]).pack(pady=5)

    lista_inventario = ctk.CTkTextbox(tab_inventario, width=400, height=150)
    lista_inventario.pack(pady=10)

    actualizar_lista()

    # --- Pestaña de Precios ---
    tab_precios = pestañas.add("Asignar Precios")

    bebidas = cargar_bebidas()
    seleccion_bebida = ctk.StringVar()
    lista_nombres = [b["nombre"] for b in bebidas]
    combo_bebidas = ctk.CTkOptionMenu(tab_precios, values=lista_nombres, variable=seleccion_bebida)
    combo_bebidas.pack(pady=10)

    # Entrys de precio
    entry_chico = ctk.CTkEntry(tab_precios, placeholder_text="Precio chico")
    entry_mediano = ctk.CTkEntry(tab_precios, placeholder_text="Precio mediano")
    entry_grande = ctk.CTkEntry(tab_precios, placeholder_text="Precio grande")
    entry_extra = ctk.CTkEntry(tab_precios, placeholder_text="Precio ingrediente extra")
    entry_postre = ctk.CTkEntry(tab_precios, placeholder_text="Precio postre")

    # Mostrar campos según categoría
    def mostrar_campos_precio(*args):
        for entry in [entry_chico, entry_mediano, entry_grande, entry_extra, entry_postre]:
            entry.pack_forget()

        nombre = seleccion_bebida.get()
        bebida = next((b for b in bebidas if b["nombre"] == nombre), None)
        if bebida:
            if bebida["categoria"] in ["Bebida fria", "Bebida caliente"]:
                entry_chico.pack(pady=3)
                entry_mediano.pack(pady=3)
                entry_grande.pack(pady=3)
                entry_extra.pack(pady=3)
            elif bebida["categoria"] == "Postre":
                entry_postre.pack(pady=3)


    def guardar_precios():
        bebida_nombre = seleccion_bebida.get()
        precios = {}
        for bebida in bebidas:
            if bebida["nombre"] == bebida_nombre:
                if bebida["categoria"] in ["Bebida fria", "Bebida caliente"]:
                    precios = {
                        "chico": entry_chico.get(),
                        "mediano": entry_mediano.get(),
                        "grande": entry_grande.get(),
                        "extra": entry_extra.get()
                    }
                else:  # Postres
                    precios = {
                        "precio": entry_postre.get(),
                        "extra": entry_extra.get()
                    }
                bebida["precios"] = precios
                break

        guardar_datos("bebidas.json", bebidas)
        messagebox.showinfo("Éxito", "Precios asignados correctamente.")

    def llenar_campos_precio(event=None):
        nombre = seleccion_bebida.get()
        for bebida in bebidas:
            if bebida["nombre"] == nombre:
                entry_chico.delete(0, "end")
                entry_mediano.delete(0, "end")
                entry_grande.delete(0, "end")
                entry_postre.delete(0, "end")
                entry_extra.delete(0, "end")

                precios = bebida.get("precios", {})
                if bebida["categoria"] in ["Bebida fria", "Bebida caliente"]:
                    entry_chico.insert(0, precios.get("chico", ""))
                    entry_mediano.insert(0, precios.get("mediano", ""))
                    entry_grande.insert(0, precios.get("grande", ""))
                    entry_extra.insert(0, precios.get("extra", ""))
                else:
                    entry_postre.insert(0, precios.get("precio", ""))
                    entry_extra.insert(0, precios.get("extra", ""))
                break

    combo_bebidas.configure(command=lambda _: [mostrar_campos_precio(), llenar_campos_precio()])
    if lista_nombres:
        seleccion_bebida.set(lista_nombres[0])
        mostrar_campos_precio()
        llenar_campos_precio()

    ctk.CTkButton(tab_precios, text="Guardar Precio", command=guardar_precios).pack(pady=10)

    # --- Botón de Cierre ---
    ctk.CTkButton(ventana_gerente, text="Cerrar Sesión", command=ventana_gerente.destroy).pack(pady=10)

# Entorno barista
def abrir_entorno_barista(nombre):
    ventana_barista = ctk.CTkToplevel()
    ventana_barista.title("Entorno del Barista")
    ventana_barista.geometry("600x500")

    ctk.CTkLabel(ventana_barista, text=f"Bienvenido, {nombre}. Entorno del Barista", font=("Arial", 16)).pack(pady=10)
    
    tabview = ctk.CTkTabview(ventana_barista, width=550, height=420)
    tabview.pack(pady=10)
    tabview.add("Registrar Producto")
    tabview.add("Productos Registrados")

    # Variables compartidas
    entry_nombre = ctk.CTkEntry(tabview.tab("Registrar Producto"), width=400, placeholder_text="Nombre del producto")
    entry_ingredientes = ctk.CTkEntry(tabview.tab("Registrar Producto"), width=400, placeholder_text="Ingredientes (separados por coma)")
    entry_cantidades = ctk.CTkEntry(tabview.tab("Registrar Producto"), width=400, placeholder_text="Cantidades (ej. 50ml, 30gr)")
    combo_categoria = ctk.CTkOptionMenu(tabview.tab("Registrar Producto"), values=["Bebida fria", "Bebida caliente", "Postre"])
    combo_categoria.set("Bebida caliente")

    for widget in [entry_nombre, entry_ingredientes, entry_cantidades, combo_categoria]:
        widget.pack(pady=5)

    def registrar_bebida():
        nombre = entry_nombre.get().strip()
        ingredientes = [i.strip() for i in entry_ingredientes.get().split(",")]
        cantidades = [c.strip() for c in entry_cantidades.get().split(",")]
        categoria = combo_categoria.get()

        # Limpiar espacios en blanco
        ingredientes = [i.strip() for i in ingredientes]
        cantidades = [c.strip() for c in cantidades]

        if not nombre or not ingredientes or not cantidades or not categoria:
            messagebox.showerror("Error", "Todos los campos deben estar llenos")
            return

        mensaje = agregar_bebida(nombre, categoria, ingredientes, cantidades)
        messagebox.showinfo("Resultado", mensaje)

    ctk.CTkButton(tabview.tab("Registrar Producto"), text="Registrar Producto", command=registrar_bebida).pack(pady=10)
    ctk.CTkButton(tabview.tab("Registrar Producto"), text="Cerrar Sesión", command=ventana_barista.destroy).pack(pady=5)

    # --- Pestaña Productos Registrados ---
    lista_bebidas = cargar_bebidas()
    seleccion = ctk.StringVar()

    lista_nombres = [b["nombre"] for b in lista_bebidas]
    combo_bebidas = ctk.CTkOptionMenu(tabview.tab("Productos Registrados"), values=lista_nombres, variable=seleccion)
    combo_bebidas.pack(pady=10)

    entry_mod_nombre = ctk.CTkEntry(tabview.tab("Productos Registrados"), width=400, placeholder_text="Nombre")
    entry_mod_ingredientes = ctk.CTkEntry(tabview.tab("Productos Registrados"), width=400, placeholder_text="Ingredientes")
    entry_mod_cantidades = ctk.CTkEntry(tabview.tab("Productos Registrados"), width=400, placeholder_text="Cantidades")
    combo_mod_categoria = ctk.CTkOptionMenu(tabview.tab("Productos Registrados"), values=["Bebida fria", "Bebida caliente", "Postre"])
    combo_mod_categoria.set("Bebida caliente")

    for widget in [entry_mod_nombre, entry_mod_ingredientes, entry_mod_cantidades, combo_mod_categoria]:
        widget.pack(pady=5)

    def llenar_campos(event=None):
        nombre = seleccion.get()
        for bebida in lista_bebidas:
            if bebida["nombre"] == nombre:
                entry_mod_nombre.delete(0, "end")
                entry_mod_ingredientes.delete(0, "end")
                entry_mod_cantidades.delete(0, "end")
                entry_mod_nombre.insert(0, bebida["nombre"])
                entry_mod_ingredientes.insert(0, ", ".join(bebida["ingredientes"]))
                entry_mod_cantidades.insert(0, ", ".join(bebida["cantidades"]))
                combo_mod_categoria.set(bebida["categoria"])
                break

    combo_bebidas.configure(command=lambda _: llenar_campos())

    def modificar_producto():
        nombre_original = seleccion.get()
        nuevo_nombre = entry_mod_nombre.get()
        nuevos_ingredientes = [i.strip() for i in entry_mod_ingredientes.get().split(",")]
        nuevas_cantidades = [c.strip() for c in entry_mod_cantidades.get().split(",")]
        nueva_categoria = combo_mod_categoria.get()

        for bebida in lista_bebidas:
            if bebida["nombre"] == nombre_original:
                bebida["nombre"] = nuevo_nombre
                bebida["ingredientes"] = nuevos_ingredientes
                bebida["cantidades"] = nuevas_cantidades
                bebida["categoria"] = nueva_categoria
                guardar_datos("bebidas.json", lista_bebidas)
                messagebox.showinfo("Modificación", "Producto modificado con éxito")
                actualizar_lista_productos()
                return

    def eliminar_producto():
        nombre = seleccion.get()
        bebidas_actuales = cargar_bebidas()
        nuevas_bebidas = [b for b in bebidas_actuales if b["nombre"] != nombre]
    
        if len(nuevas_bebidas) == len(bebidas_actuales):
            messagebox.showerror("Error", "Producto no encontrado.")
            return

        guardar_datos("bebidas.json", nuevas_bebidas)
        messagebox.showinfo("Eliminado", f"'{nombre}' eliminado con éxito")
        actualizar_lista_productos()

    ctk.CTkButton(tabview.tab("Productos Registrados"), text="Modificar Producto", command=modificar_producto).pack(pady=5)
    ctk.CTkButton(tabview.tab("Productos Registrados"), text="Eliminar Producto", command=eliminar_producto).pack(pady=5)
    

    def actualizar_lista_productos():
        nonlocal lista_bebidas
        lista_bebidas = cargar_bebidas()
        nombres = [b["nombre"] for b in lista_bebidas]
        combo_bebidas.configure(values=nombres)

        if nombres:
            seleccion.set(nombres[0])
            llenar_campos()
        else:
            seleccion.set("")
            entry_mod_nombre.delete(0, "end")
            entry_mod_ingredientes.delete(0, "end")
            entry_mod_cantidades.delete(0, "end")
            combo_mod_categoria.set("Bebida caliente")
    
    ctk.CTkButton(tabview.tab("Productos Registrados"), text="Actualizar Lista", command=actualizar_lista_productos).pack(pady=5)        
# -------------------------------------------
#Entorno cliente
import json
import os
import customtkinter as ctk
from tkinter import messagebox

def abrir_entorno_cliente(nombre_cliente,email):
    seleccion_bebidas = {}
    ventana_cliente = ctk.CTkToplevel()
    ventana_cliente.title("Entorno del Cliente")
    ventana_cliente.geometry("700x700")

    ctk.CTkLabel(ventana_cliente, text=f"Bienvenido, {nombre_cliente}.", font=("Arial", 16)).pack(pady=10)

    pestañas = ctk.CTkTabview(ventana_cliente)
    pestañas.pack(expand=True, fill="both")

    # Cargar puntos iniciales
    puntos_data = cargar_puntos()
    puntos_acumulados = puntos_data.get(email, 0)

    # Ingredientes extra fijos
    opciones_personalizacion = ["Leche deslactosada", "Leche de avena", "Azúcar extra", "Bombones", "Crema batida"]
    precio_extra = 10

    # Cargar bebidas desde bebidas.json
    with open("bebidas.json", "r", encoding="utf-8") as file:
        bebidas = json.load(file)

    # Calcular precio "extra" común desde el primer producto (se asume igual para todos)
    for b in bebidas:
        if "extra" in b:
            precio_extra = float(b["extra"])
            break

    def calcular_puntos(total_gastado):
        nonlocal puntos_acumulados  # Esto permite modificar la variable del ámbito superior
        puntos_ganados = int((total_gastado // 100) * 10)  # 10 puntos por cada $100
        puntos_acumulados += puntos_ganados
        
        # Actualizar datos en backend
        puntos_data[email] = puntos_acumulados
        guardar_puntos(puntos_data)
        
        # Actualizar label
        lbl_puntos.configure(text=f"Tienes {puntos_acumulados} puntos")
        return puntos_ganados

    def personalizar_bebida(bebida):
        ventana_personalizar = ctk.CTkToplevel()
        ventana_personalizar.title(f"Personalizar {bebida['nombre']}")
        ventana_personalizar.geometry("500x500")
    
        # Aquí podemos agregar controles para personalizar la bebida, como tamaños, extras, etc.
        ctk.CTkLabel(ventana_personalizar, text=f"Personaliza tu {bebida['nombre']}").pack(pady=10)
    
        if bebida["categoria"] != "Postre":
            # Selección de tamaño
            tamano_var = ctk.StringVar(value="chico")  # Valor por defecto
            ctk.CTkLabel(ventana_personalizar, text="Selecciona el tamaño:").pack(pady=5)

            tamano_options = ["chico", "mediano", "grande"]
            for tamano in tamano_options:
                ctk.CTkRadioButton(ventana_personalizar, text=tamano.capitalize(), variable=tamano_var, value=tamano).pack()

            # Selección de ingredientes extras
            extras_var = ctk.StringVar(value="")
            ctk.CTkLabel(ventana_personalizar, text="Selecciona ingredientes extra:").pack(pady=5)

            opciones_personalizacion = ["Leche deslactosada", "Leche de avena", "Azúcar extra", "Bombones", "Crema batida"]
            for extra in opciones_personalizacion:
                ctk.CTkCheckBox(ventana_personalizar, text=extra, variable=extras_var, onvalue=extra, offvalue="").pack()

            def guardar_personalizacion():
                # Crear una clave única basada en el nombre, tamaño y extras
                clave_unica = f"{bebida['nombre']}_{tamano_var.get()}_{'+'.join(extras_var.get().split())}"
                seleccion_bebidas[clave_unica] = {
                    "nombre": bebida["nombre"],
                    "tamano": tamano_var.get(),
                    "extras": [extra for extra in opciones_personalizacion if extra in extras_var.get()]
                }
                ventana_personalizar.destroy()  # Destruir la ventana después de guardar

        else:
            # Si es postre, solo seleccionamos la cantidad
            cantidad_var = ctk.IntVar(value=1)
            ctk.CTkLabel(ventana_personalizar, text="Selecciona la cantidad:").pack(pady=10)

            for cantidad in range(1, 6):  # Limitar la cantidad de postres a 5
                ctk.CTkRadioButton(ventana_personalizar, text=f"{cantidad} pz", variable=cantidad_var, value=cantidad).pack()

            def guardar_personalizacion():
                clave_unica = f"{bebida['nombre']}_{cantidad_var.get()}_postre"
                seleccion_bebidas[clave_unica] = {
                    "nombre": bebida["nombre"],
                    "cantidad": cantidad_var.get()
                }
                ventana_personalizar.destroy()  # Destruir la ventana después de guardar

        # Mover el botón de "Guardar" aquí para asegurarse de que la ventana no se destruya antes de ser interactuada
        ctk.CTkButton(ventana_personalizar, text="Guardar", command=guardar_personalizacion).pack(pady=10)


     # ---------------- Pestaña de Productos ----------------
    tab_productos = pestañas.add("Productos")

    ctk.CTkLabel(tab_productos, text="Menú de Productos", font=("Arial", 18)).pack(pady=10)

    contenedor_scroll = ctk.CTkScrollableFrame(tab_productos, width=650, height=420)
    contenedor_scroll.pack(pady=5)

    categorias_ordenadas = [("Bebida caliente", "☕ Bebidas Calientes"), ("Bebida fria", "❄️ Bebidas Frías"), ("Postre", "🍰 Postres")]

    for categoria_key, categoria_titulo in categorias_ordenadas:
        ctk.CTkLabel(contenedor_scroll, text=categoria_titulo, font=("Arial", 16)).pack(anchor="w", pady=(10, 4), padx=10)

        productos_categoria = [b for b in bebidas if b["categoria"] == categoria_key]

        contenedor_productos = ctk.CTkFrame(contenedor_scroll, fg_color="transparent")
        contenedor_productos.pack(anchor="w", padx=10)

        for bebida in productos_categoria:
            nombre = bebida["nombre"]
            categoria = bebida["categoria"]
            seleccion_bebidas[nombre] = {}

            card = ctk.CTkFrame(contenedor_productos, width=300, height=100, corner_radius=10)
            card.pack_propagate(False)
            card.pack(side="left", padx=10, pady=5)

            # Ícono según categoría
            icono = "☕" if categoria == "Bebida Caliente" else "❄️" if categoria == "Bebida Fría" else "🍪"
            titulo = f"{icono} {nombre}"
            ctk.CTkLabel(card, text=titulo, font=("Arial", 14, "bold"), anchor="w").pack(anchor="w", padx=10, pady=(5, 0))

            # Precios
            if categoria == "Postre":
                precio_texto = f"Precio: ${bebida.get('precio', 0)}"
            else:
                precios = bebida.get("precios", {})
                precio_texto = f"CH ${precios.get('chico', '?')} | MD ${precios.get('mediano', '?')} | GD ${precios.get('grande', '?')}"

            ctk.CTkLabel(card, text=precio_texto, font=("Arial", 12), anchor="w").pack(anchor="w", padx=10)

            ctk.CTkButton(card, text="Personalizar", width=120, command=lambda b=bebida: personalizar_bebida(b)).pack(pady=5) 

    # ---------------- Pestaña de Carrito Mejorada ----------------
    tab_carrito = pestañas.add("Carrito")
    ctk.CTkLabel(tab_carrito, text="Carrito de Compras", font=("Arial", 16)).pack(pady=10)
    
    # Frame principal con scroll
    carrito_frame = ctk.CTkScrollableFrame(tab_carrito, width=600, height=300)
    carrito_frame.pack(pady=5)
    
    # Diccionario para mantener referencia a los widgets de cada producto
    carrito_widgets = {}
    
    total_compra = ctk.CTkLabel(tab_carrito, text="Total: $0", font=("Arial", 14, "bold"))
    total_compra.pack(pady=10)
    
    def actualizar_carrito():
        # Limpiar el frame del carrito
        for widget in carrito_frame.winfo_children():
            widget.destroy()
        
        carrito_widgets.clear()
        total = 0
        
        for idx, (identificador, datos) in enumerate(seleccion_bebidas.items()):
            if "nombre" not in datos:
                continue

            # Frame para cada producto del carrito
            producto_frame = ctk.CTkFrame(carrito_frame, fg_color=("gray90", "gray20"))
            producto_frame.pack(fill="x", pady=5, padx=5)
            
            # Obtener información del producto
            nombre = datos["nombre"]
            categoria = next((b["categoria"] for b in bebidas if b["nombre"] == nombre), "Desconocida")
            
            # Calcular precio
            if categoria == "Postre":
                cantidad = datos.get("cantidad", 1)
                precio_unitario = float(next((b.get("precio", 0) for b in bebidas if b["nombre"] == nombre), 0))
                precio = precio_unitario * cantidad
                descripcion = f"{nombre} - {cantidad} unidad(es)"
            else:
                tamano = datos.get("tamano", "mediano")
                extras = datos.get("extras", [])
                precio = float(next((b.get("precios", {}).get(tamano, 0) for b in bebidas if b["nombre"] == nombre), 0))
                precio += len(extras) * precio_extra
                descripcion = f"{nombre} ({tamano}) - Extras: {', '.join(extras) if extras else 'Ninguno'}"
            
            total += precio
            
            # Widgets para mostrar el producto
            lbl_producto = ctk.CTkLabel(producto_frame, text=descripcion, font=("Arial", 12))
            lbl_precio = ctk.CTkLabel(producto_frame, text=f"${precio:.2f}", font=("Arial", 12, "bold"))
            
            # Botones de acción
            btn_frame = ctk.CTkFrame(producto_frame, fg_color="transparent")
            
            btn_editar = ctk.CTkButton(
                btn_frame, 
                text="✏️ Editar", 
                width=80,
                command=lambda id=identificador: editar_producto_carrito(id)
            )
            
            btn_eliminar = ctk.CTkButton(
                btn_frame, 
                text="🗑️ Eliminar", 
                width=80,
                fg_color="#d9534f",
                hover_color="#a94442",
                command=lambda id=identificador: eliminar_producto_carrito(id)
            )
            
            # Grid layout para organizar los elementos
            lbl_producto.grid(row=0, column=0, padx=5, pady=5, sticky="w")
            lbl_precio.grid(row=0, column=1, padx=5, pady=5)
            btn_frame.grid(row=0, column=2, padx=5, pady=5)
            btn_editar.pack(side="left", padx=2)
            btn_eliminar.pack(side="left", padx=2)
            
            # Guardar referencia a los widgets
            carrito_widgets[identificador] = {
                "frame": producto_frame,
                "descripcion": descripcion,
                "precio": precio
            }
        
        total_compra.configure(text=f"Total: ${total:.2f}")
        calcular_puntos(total)
    
    def editar_producto_carrito(identificador):
        datos = seleccion_bebidas[identificador]
        nombre = datos["nombre"]
        bebida = next((b for b in bebidas if b["nombre"] == nombre), None)
        
        if bebida:
            # Abrir ventana de personalización similar a la original
            ventana_editar = ctk.CTkToplevel()
            ventana_editar.title(f"Editar {nombre}")
            ventana_editar.geometry("400x400")
            
            if bebida["categoria"] != "Postre":
                # Edición para bebidas
                tamano_var = ctk.StringVar(value=datos.get("tamano", "mediano"))
                ctk.CTkLabel(ventana_editar, text="Tamaño:").pack(pady=5)
                
                for tamano in ["chico", "mediano", "grande"]:
                    ctk.CTkRadioButton(
                        ventana_editar, 
                        text=tamano.capitalize(), 
                        variable=tamano_var, 
                        value=tamano
                    ).pack(anchor="w")
                
                # Extras seleccionados previamente
                extras_seleccionados = datos.get("extras", [])
                ctk.CTkLabel(ventana_editar, text="Extras:").pack(pady=5)
                
                extras_vars = {}
                for extra in opciones_personalizacion:
                    extras_vars[extra] = ctk.BooleanVar(value=extra in extras_seleccionados)
                    ctk.CTkCheckBox(
                        ventana_editar, 
                        text=extra, 
                        variable=extras_vars[extra]
                    ).pack(anchor="w")
                
                def guardar_cambios():
                    nuevos_extras = [extra for extra, var in extras_vars.items() if var.get()]
                    seleccion_bebidas[identificador].update({
                        "tamano": tamano_var.get(),
                        "extras": nuevos_extras
                    })
                    actualizar_carrito()
                    ventana_editar.destroy()
                
            else:
                # Edición para postres
                cantidad_var = ctk.IntVar(value=datos.get("cantidad", 1))
                ctk.CTkLabel(ventana_editar, text="Cantidad:").pack(pady=10)
                
                for cantidad in range(1, 6):
                    ctk.CTkRadioButton(
                        ventana_editar, 
                        text=f"{cantidad} unidad(es)", 
                        variable=cantidad_var, 
                        value=cantidad
                    ).pack(anchor="w")
                
                def guardar_cambios():
                    seleccion_bebidas[identificador].update({
                        "cantidad": cantidad_var.get()
                    })
                    actualizar_carrito()
                    ventana_editar.destroy()
            
            ctk.CTkButton(
                ventana_editar, 
                text="Guardar Cambios", 
                command=guardar_cambios
            ).pack(pady=15)
            
            ctk.CTkButton(
                ventana_editar, 
                text="Cancelar", 
                command=ventana_editar.destroy
            ).pack(pady=5)
    
    def eliminar_producto_carrito(identificador):
        confirmacion = messagebox.askyesno(
            "Confirmar Eliminación",
            "¿Estás seguro de que quieres eliminar este producto del carrito?"
        )
        if confirmacion:
            del seleccion_bebidas[identificador]
            actualizar_carrito()
    
    # Botón para actualizar el carrito (útil durante desarrollo)
    ctk.CTkButton(
        tab_carrito, 
        text="Actualizar Carrito", 
        command=actualizar_carrito
    ).pack(pady=5)
    
    
    # ---------------- Pestaña de Puntos ----------------
    tab_puntos = pestañas.add("Puntos")
    ctk.CTkLabel(tab_puntos, text="Sistema de Puntos", font=("Arial", 16)).pack(pady=10)
    
    
    # Label para mostrar puntos (asegúrate de tener esto en tu pestaña de puntos)
    lbl_puntos = ctk.CTkLabel(tab_puntos, text=f"Tienes {puntos_acumulados} puntos", font=("Arial", 16))
    lbl_puntos.pack(pady=10)

    def verificar_disponibilidad(nombre_producto, producto_info):
        try:
            bebida = next((b for b in bebidas if b["nombre"] == nombre_producto), None)
            if not bebida:
                return False, f"Producto '{nombre_producto}' no encontrado."

            inventario = cargar_inventario()
            ingredientes = bebida.get("ingredientes", [])
            cantidades = bebida.get("cantidades", [])

            for ingrediente, cantidad_str in zip(ingredientes, cantidades):
                try:
                    cantidad_necesaria = float(''.join(filter(str.isdigit, cantidad_str))) * producto_info.get("cantidad", 1)
                except ValueError:
                    return False, f"Formato de cantidad inválido para ingrediente: {ingrediente}"

                item = next((i for i in inventario if i["ingrediente"] == ingrediente), None)
                if not item:
                    return False, f"Falta el ingrediente: {ingrediente}"
                if item["cantidad"] < cantidad_necesaria:
                    return False, f"Ingrediente insuficiente: {ingrediente} (necesario: {cantidad_necesaria}, disponible: {item['cantidad']})"

            return True, ""
        except Exception as e:
            return False, f"Error al verificar disponibilidad: {e}"

    def confirmar_compra():
        try:
            if not seleccion_bebidas:
                messagebox.showwarning("Carrito Vacío", "No hay productos en el carrito para confirmar")
                return

            actualizar_carrito()
            total = float(total_compra.cget("text").replace("Total: $", ""))

            # Verificar disponibilidad antes de continuar
            for identificador, datos in seleccion_bebidas.items():
                if "nombre" not in datos:
                    continue  # Saltar si el producto está mal registrado

                nombre_producto = datos["nombre"]
                disponible, mensaje = verificar_disponibilidad(nombre_producto, datos)
                if not disponible:
                    messagebox.showerror("Stock insuficiente", f"No se puede procesar el pedido: {mensaje}")
                    return  # Detener el proceso si falla cualquier verificación

            # Continuar con compra si hay stock
            pedido = {
                "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "cliente": nombre_cliente,
                "email": email,
                "productos": [],
                "total": total,
                "estado": "completado"
            }

            for identificador, datos in seleccion_bebidas.items():
                if "nombre" not in datos:
                    continue

                nombre_producto = datos["nombre"]
                producto_info = {
                    "nombre": nombre_producto,
                    "cantidad": datos.get("cantidad", 1) if "cantidad" in datos else 1
                }

                if "tamano" in datos:
                    producto_info.update({
                        "tipo": "bebida",
                        "tamano": datos["tamano"],
                        "extras": datos.get("extras", [])
                    })
                else:
                    producto_info["tipo"] = "postre"

                pedido["productos"].append(producto_info)
                actualizar_inventario(nombre_producto, producto_info)

            guardar_pedido(pedido)
            seleccion_bebidas.clear()
            actualizar_carrito()

            messagebox.showinfo(
                "Compra Confirmada",
                f"¡Gracias por tu compra, {nombre_cliente}!\n\n"
                f"Total: ${total:.2f}\n"
                f"Puntos acumulados: {int(total // 100) * 10}\n\n"
                "Se ha enviado un comprobante a tu correo."
            )

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al procesar tu compra:\n{str(e)}")

    # Botón para confirmar compra
    ctk.CTkButton(
        tab_carrito,
        text="✅ Confirmar Compra",
        fg_color="#5cb85c",
        hover_color="#4cae4c",
        font=("Arial", 14, "bold"),
        command=confirmar_compra
    ).pack(pady=15)

    # Funciones auxiliares necesarias
    def guardar_pedido(pedido):
        """Guarda el pedido en el historial"""
        try:
            historial = cargar_datos("historial_pedidos.json")
            historial.append(pedido)
            guardar_datos("historial_pedidos.json", historial)
        except Exception as e:
            print(f"Error al guardar pedido: {e}")

    def actualizar_inventario(nombre_producto, producto_info):
        """Reduce las cantidades del inventario según lo comprado"""
        try:
            bebida = next((b for b in bebidas if b["nombre"] == nombre_producto), None)
            if not bebida:
                return

            inventario = cargar_inventario()
        
            for ingrediente, cantidad in zip(bebida["ingredientes"], bebida["cantidades"]):
                # Convertir cantidad (ej. "50ml" o "30gr") a número
                cantidad_num = float(''.join(filter(str.isdigit, cantidad)))
            
                # Ajustar por cantidad de productos (ej. 2 cafés)
                cantidad_total = cantidad_num * producto_info["cantidad"]
            
                # Actualizar inventario
                for item in inventario:
                    if item["ingrediente"] == ingrediente:
                        item["cantidad"] -= cantidad_total
                        break
        
            guardar_inventario(inventario)
        except Exception as e:
            print(f"Error al actualizar inventario: {e}")

    
    ctk.CTkButton(ventana_cliente, text="Cerrar Sesión", command=ventana_cliente.destroy).pack(pady=10)

ventana_inicio.mainloop()
 