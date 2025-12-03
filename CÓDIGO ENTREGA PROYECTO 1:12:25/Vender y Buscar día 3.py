import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog # Día 2 agregamos simpledialog
from datetime import datetime

# Inventario Inicial, incluye 10 productos
inventario = [
    {"id": "001", "modelo": "Ampolla Madagascar Centella Asiática", "marca": "SKIN 1004", "precio": 300.00, "cantidad": "100ml", "stock": 20, "descripcion": "Repara la piel dañada"},
    {"id": "002", "modelo": "Heartleaf Quercetinol Pore Deep Cleansing Foam", "marca": "Anua", "precio": 250.00, "cantidad": "150ml", "stock": 30, "descripcion": "Espuma limpiadora"},
    {"id": "003", "modelo": "Daily sun cream with Vaseline Jelly", "marca": "Vaseline", "precio": 180.00, "cantidad": "50ml", "stock": 10, "descripcion": "Protector solar"},
    {"id": "004", "modelo": "Bean Essence", "marca": "Mixsoon", "precio": 360.00, "cantidad": "50ml", "stock": 15, "descripcion": "Sérum refrescante"},
    {"id": "005", "modelo": "Rice Cream", "marca": "I'm from", "precio": 345.00, "cantidad": "50g", "stock": 3, "descripcion": "Crema humectante de arroz"},
    {"id": "006", "modelo": "The Juicy Lasting Tint", "marca": "Romand", "precio": 300.00, "cantidad": "10g", "stock": 23, "descripcion": "Tinta jugosa con terminado brilloso"},
    {"id": "007", "modelo": "Black Rice Hyaluronic Toner", "marca": "Haruharu", "precio": 250.00, "cantidad": "150ml", "stock": 9, "descripcion": "Tónico libre de alcohol y fragancias"},
    {"id": "008", "modelo": "345 Relief Cream", "marca": "Dr.Althea", "precio": 410.00, "cantidad": "50ml", "stock": 17, "descripcion": "Calma piel irritada y con imperfecciones"},
    {"id": "009", "modelo": "Collagen Night Wrapping Mask", "marca": "Medicube", "precio": 300.00, "cantidad": "75ml", "stock": 30, "descripcion": "Mejora la elasticidad e hidratación de la piel"},
    {"id": "010", "modelo": "Collagen Lifting Eye Cream", "marca": "Tirtir", "precio": 360.00, "cantidad": "15ml", "stock": 5, "descripcion": "Colágeno de origen vegetal"},
]

historial_ventas = []
STOCK_MINIMO = 3

def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida con estadísticas rápidas"""
    global boton_activo
    texto.delete(1.0, tk.END)
    activar_boton(btn_home)
    
    total_modelos = len(inventario)
    total_productos = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(1 for v in historial_ventas if datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M").date() == datetime.now().date())
    productos_stock_bajo = sum(1 for t in inventario if t['stock'] > 0 and t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "     🧸       🎀      🧸  \n\n")
    texto.insert(tk.END, "--------------------------------------------------------\n\n")
    texto.insert(tk.END, "  Bienvenido a ÉCLAT! 💆🏻‍♀️ \n\n")
    texto.insert(tk.END, "--------------------------------------------------------\n\n")
    
    texto.insert(tk.END, "RESUMEN RÁPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"Modelos Únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total de Productos en Stock: {total_productos}\n")
    texto.insert(tk.END, f"Ventas Registradas (Hoy): {ventas_hoy}\n")
    
    if productos_stock_bajo > 0:
        texto.insert(tk.END, f" ⚠️ ¡ALERTA DE STOCK BAJO!: {productos_stock_bajo} productos necesitan reabastecimiento.\n", "alerta")
    else:
        texto.insert(tk.END, "¡Inventario en buen estado!\n")
    
    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")

# día 2
def validar_numero_positivo (valor, nombre_campo):
    """Valida que el valor sea un número positivo."""
    try:
        num = float(valor)
        if num < 0:
            messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' no puede ser negativo.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error de Validación", f"El campo'{nombre_campo}' debe ser un número válido.")
        return None
    
# día 2 
def generar_nuevo_id():
    """Genera un nuevo ID consecutivo basado en el ID numérico más alto actual."""
    if not inventario:
        return "001"

    max_id = 0
    for producto in inventario:
        try:
            num_id = int(producto['id'])
            if num_id > max_id:
                max_id = num_id
        except ValueError:
            continue

        return str(max_id + 1).zfill(3)
    
# día 2
def mostrar_inventario():
    """Muestra el listado completo del inventario."""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "= INVENTARIO COMPLETO =\n\n")
    activar_boton(btn1)

    if not inventario:
        texto.insert(tk.END, "X No hay producto en el inventario\n")
    else:
        texto.insert(tk.END, f"{'ID':<4} | {'MODELO' :<25} | {'PRECIO' :<10} | {'CANTIDAD' :<6} | {'MARCA' :<10} | {'STOCK' :<5}\n")
        texto.insert(tk.END, "-"*70 + "\n")

        for productos in inventario:
            linea = f"{productos['id']:<4} | {productos['modelo']:<25} | ${productos['precio']:<9,.0f} | {productos['cantidad']:<6} | {productos['marca']:<10} | {productos['stock']:<5}"
            texto.insert(tk.END, linea)

            if productos['stock'] > 0 and productos['stock'] <= STOCK_MINIMO:
                texto.inser(tk.END, "STOCK BAJO", "alerta")
            elif productos['stock'] == 0:
                texto.insert(tk.END, "AGOTADO", "agotado")
            
            texto.insert(tk.END, "\n")

        texto.insert(tk.END, "\nUsa el botón 'AGREGAR' para incorporar nuevos productos.\n")

# día 2
def agregar_productos():
    """Agrega un nuevo producto al inventario."""
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    modelo = simpledialog.askstring("Agregar Productos", "1. Nombre del modelo (Obligatorio):", parent = ventana)
    if not modelo: return

    marca = simpledialog.askstring("Agregar Productos", "2. Marca/Categoría (Obligatorio:)", parent= ventana)
    if not marca: return

    precio_str = simpledialog.askstring("Agregar Productos", "3. Precio unitario (Obligatorio):", parent= ventana)
    if not precio_str: return
    precio_validado = validar_numero_positivo(precio_str, "Precio")
    if precio_validado is None: return

    cantidad = simpledialog.askstring("Agregar Productos", "4. Cantidad (Obligatorio):", parent= ventana)
    if not cantidad: return

    stock_str = simpledialog.askstring("Agregar Productos", "5. Cantidad inicial (Stock) (Obligatorio):", parent= ventana)
    if not stock_str: return
    stock_validado = validar_numero_positivo(stock_str, "Cantidad inicial")
    if stock_validado is None: return

    descripcion = simpledialog.askstring("Agregar Productos", "6. Descripción adicional (Opcional):", parent= ventana)

    nuevo_producto = {
        "id": new_id,
        "modelo": modelo,
        "marca": marca,
        "precio": float(precio_validado),
        "cantidad": cantidad,
        "stock": int(stock_validado),
        "descripcion": descripcion if descripcion else "Sin descripción"
    }

    inventario.append(nuevo_producto)

    messagebox.showinfo("Éxito", f"'{modelo}' agregado con ID {new_id} al inventario.")
    mostrar_inventario()

# día 3
def buscar_producto():
    """Busca un producto en el inventario por ID, Modelo, Marca o Cantidad."""
    activar_boton(btn4)

    if not inventario:
        messagebox.showwarning("Sin inventario", "No hay productos disponibles para buscar", parent=ventana)
        return
    
    criterio_busqueda = simpledialog.askstring("Buscar Producto",
                                               "Busca por: ID, Modelo, Marca o Cantidad:",
                                               parent= ventana)
    
    if not criterio_busqueda:
        return
    
    criterio = criterio_busqueda.lower()
    resultados = []

    for producto in inventario:
        if (criterio in producto ['id'].lower() or
            criterio in producto['modelo'].lower() or
            criterio in producto['marca'].lower() or
            criterio in producto['cantidad'].lower()):
            resultados.append(producto)
    
    texto.delete(1.0, tk.END)
    texto.insert(tk.END,f"RESULTADOS DE BÚSQUEDA: '{criterio_busqueda}' ===\n\n")

    if not resultados:
        texto.insert(tk.END,"X No se encontraron resultados\n")
    else:
        texto.insert(tk.END, f"Se encontraron {len(resultados)} producto(s):\n\n")
        texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<25} | {'PRECIO':<10} | {'CANTIDAD':<6} | {'MARCA':<10} | {'STOCK':<5}\n")
        texto.inserr(tk.END, "-"*70 + "\n")

        for producto in resultados:
            linea = f"{producto['id']:<4} | {producto['modelo']:<25} | ${producto['precio']:<9,.0f} | {producto['cantidad']:<6} | {producto['marca']:<10} | {producto['stock']:<5}"
            texto.insert(tk.END, linea)

            if producto['stock'] > 0 and producto['stock'] <=STOCK_MINIMO:
                texto.insert(tk.END, "STOCK BAJO", "alerta")
            elif producto['stock'] == 0:
                texto.insert(tk.END, "AGOTADO", "agotado")
            
            texto.insert(tk.END, "\n")

# día 3
def vender_producto():
    """Registra una venta de productos y actualiza el inventario."""
    activar_boton(btn3)

    if not inventario:
        messagebox.showwarning("Sin inventario", "No hay productos disponibles para vender", parent=ventana)
        return
    
    opciones = "\n".join([f"{i+1}. ID:{t['id']} - {t['modelo']} ({t['marca']}) - Stock: {t['stock']}" for i, t in enumerate(inventario)])
    seleccion = simpledialog.askinteger("Vender Producto", f"Selecciona el NÚMERO del producto a vender:\n\n{opciones}", parent=ventana)

    if not seleccion or seleccion < 1 or seleccion > len(inventario):
        if seleccion is not None: messagebox.showerror("Error", "Selección inválida o cancelada.")
        return
    
    producto_a_vender = inventario[seleccion - 1]

    if producto_a_vender['stock'] <= 0:
        messagebox.showwarning("Sin stock", "Este modelo está agotado", parent=ventana)
        return
    
    cantidad_str = simpledialog.askstring("Vender Producto", f"¿Cuántas unidades de '{producto_a_vender['modelo']}' quieres vender?", parent=ventana)
    if not cantidad_str: return

    cantidad_validada = validar_numero_positivo(cantidad_str,"Cantidad a vender")
    if cantidad_validada is None: return
    cantidad = int(cantidad_validada)

    if cantidad > producto_a_vender['stock']:
        messagebox.showerror("Error de Venta", f"Solo hay {producto_a_vender['stock']} unidades disponibles. No se puede vender {cantidad}.", parent=ventana)
        return
    
    monto_total = cantidad = producto_a_vender['precio']

    producto_a_vender['stock'] -= cantidad

    registro_venta = {
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "id_producto": producto_a_vender['modelo'],
        "cantidad": cantidad,
        "precio_unitario": producto_a_vender['precio'],
        "total": monto_total
    }

    historial_ventas.append(registro_venta)

    messagebox.showinfo("Venta Registrada",
                        f"Se vendieron {cantidad} unidades de '{producto_a_vender['modelo']}'\n"
                        f"Monto Total: ${monto_total:,.2f}")
    
    mostrar_resumen_venta(registro_venta)

# día 3
def mostrar_resumen_venta(venta):
    """Muestra el resumen detallado de la venta realizada."""
    texto.delete(1.0,tk.END)
    texto.insert(tk.END, "=VENTA REGISTRADA =\n\n")

    texto.inser(tk.END, "DETALLES DE LA VENTA:\n", "título")
    texto.insert(tk.END, f"Fecha y Hora: {venta['fecha']}\n")
    texto.insert(tk.END, f"Producto ID: {venta['id_producto']}\n")
    texto.insert(tk.END, f"Nombre: {venta['modelo']}\n")
    texto.insert(tk.END, f"Cantidad: {venta['cantidad']} unidades\n")
    texto.insert(tk.END, f"Precio Unitario: ${venta['precio_unitario']:,.2f}\n")
    texto.insert(tk.END, f"TOTAL: ${venta['total']:,.2f}\n", "total")

    texto.insert(tk.END, "\n¡La venta ha sido registrada exitosamente!\n")

#Botones
def activar_boton(boton):
    """Actualiza el color del botón activo."""
    global boton_activo
    
    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg="#000000")
        
    if boton:
        boton.config(bg="#a98fcd")
        boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg="#a98fcd")

def on_leave(e, boton):
    if boton != boton_activo:
        boton.config(bg="#000000")

#Parte grafica
ventana = tk.Tk()
ventana.title("🧸  🎀  ÉCLAT 🎀    🧸")
ventana.geometry("1200x800")
ventana.configure(bg="#f5f5f5")

boton_activo = None

titulo = tk.Label(ventana, text="🧸  🎀  ÉCLAT 🎀    🧸", 
                  font=("Helvetica", 32, "bold"), bg="#f5f5f5", fg="#000000")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS)", 
                     font=("Helvetica", 12), bg="#f5f5f5", fg="#666666")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)

btn_style = {"font": ("Albert Sans", 11, "bold"), "bg": "#000000", "fg": "white", 
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

# día 2 
btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)

# día 2
btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn1.grid(row=0, column=1, padx=8)

# día 2
btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_productos, **btn_style)
btn2.grid(row=0, column=2, padx=8)

# día 3
btn3 = tk.Button(frame_botones, text="VENDER", command=agregar_productos, **btn_style)
btn3.grid(row=0, column=3, padx=8)
# día 3 
btn4 = tk.Button(frame_botones, text="BUSCAR", command=agregar_productos, **btn_style)
btn4.grid(row=0, column=4, padx=8)

# día 1 
for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

texto = scrolledtext.ScrolledText(ventana,
                                  font= ("Open Sans", 11),
                                  bg= "#ffffff", fg= "#000000",
                                  height=18,
                                  padx=20, pady=20,
                                  relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground= "#000000")
texto.tag_config("alerta", background= "#ffe5e5", foreground= "#8700ee", font= ("Open Sans", 11, "bold"))
texto.tag_config("agotado", background= "#fddede", foreground= "#8700ee", font= ("Open Sans", 11, "bold"))

# día 2
footer = tk.Label(ventana, text= " © 2025 ÉCLAT | DÍA 2 (MARTES) - Boton Inventario y Agregar Productos",
                  font= ("Helvetica", 10), bg= "#f5f5f5", fg= "#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()


