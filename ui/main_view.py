import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class MainView(tk.Tk):
    def __init__(self, usuario_actual):
        super().__init__()
        self.usuario_actual = usuario_actual
        self.title(f"Restaurante App - Usuario: {self.usuario_actual.username} ({self.usuario_actual.rol})")
        self.geometry("780x520")
        self.minsize(700, 480)

        self._crear_menu_superior()
        self._crear_contenedor_principal()
        self._cargar_datos_iniciales()

    def _crear_menu_superior(self):
        frame_top = ttk.Frame(self, padding=(15, 10))
        frame_top.pack(fill=tk.X)

        lbl_sesion = ttk.Label(
            frame_top, 
            text=f"Sesión iniciada: {self.usuario_actual.username} | Rol: {self.usuario_actual.rol}", 
            font=("Arial", 10, "italic")
        )
        lbl_sesion.pack(side=tk.LEFT)

    def _crear_contenedor_principal(self):
        # Contenedor Notebook (Pestañas)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

        # Pestaña 1: Gestión de Productos
        self.tab_productos = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_productos, text="  Gestión de Productos  ")
        self._construir_pestana_productos()

        # Pestaña 2: Consulta de Usuarios
        self.tab_usuarios = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_usuarios, text="  Usuarios del Sistema  ")
        self._construir_pestana_usuarios()

    # -------------------------------------------------------------
    # PESTAÑA: PRODUCTOS
    # -------------------------------------------------------------
    def _construir_pestana_productos(self):
        # Contenedor superior: Formulario y Acciones
        frame_form = ttk.LabelFrame(self.tab_productos, text=" Formulario de Producto ", padding=10)
        frame_form.pack(fill=tk.X, pady=(0, 10))

        # Campos organizados con grid
        ttk.Label(frame_form, text="ID Producto:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txt_id = ttk.Entry(frame_form, width=15)
        self.txt_id.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.txt_nombre = ttk.Entry(frame_form, width=25)
        self.txt_nombre.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)

        ttk.Label(frame_form, text="Categoría:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txt_categoria = ttk.Entry(frame_form, width=15)
        self.txt_categoria.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        ttk.Label(frame_form, text="Precio ($):").grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        self.txt_precio = ttk.Entry(frame_form, width=25)
        self.txt_precio.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)

        # Contenedor de Botones de Acción (exclusivamente con command=)
        frame_botones = ttk.Frame(frame_form, padding=(0, 10, 0, 0))
        frame_botones.grid(row=2, column=0, columnspan=4, sticky=tk.EW)

        btn_registrar = ttk.Button(frame_botones, text="Registrar", command=self._registrar_producto)
        btn_registrar.pack(side=tk.LEFT, padx=4)

        btn_cargar = ttk.Button(frame_botones, text="Cargar / Consultar", command=self._cargar_producto)
        btn_cargar.pack(side=tk.LEFT, padx=4)

        btn_actualizar = ttk.Button(frame_botones, text="Actualizar", command=self._actualizar_producto)
        btn_actualizar.pack(side=tk.LEFT, padx=4)

        btn_eliminar = ttk.Button(frame_botones, text="Eliminar", command=self._eliminar_producto)
        btn_eliminar.pack(side=tk.LEFT, padx=4)

        btn_limpiar = ttk.Button(frame_botones, text="Limpiar Campos", command=self._limpiar_formulario_productos)
        btn_limpiar.pack(side=tk.RIGHT, padx=4)

        # Contenedor inferior: Visualización de Productos (Treeview)
        frame_tabla = ttk.LabelFrame(self.tab_productos, text=" Listado de Productos en Carta ", padding=10)
        frame_tabla.pack(fill=tk.BOTH, expand=True)

        columnas = ("id", "nombre", "categoria", "precio")
        self.tabla_productos = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        self.tabla_productos.heading("id", text="ID")
        self.tabla_productos.heading("nombre", text="Nombre del Producto")
        self.tabla_productos.heading("categoria", text="Categoría")
        self.tabla_productos.heading("precio", text="Precio ($)")

        self.tabla_productos.column("id", width=70, anchor=tk.CENTER)
        self.tabla_productos.column("nombre", width=250, anchor=tk.W)
        self.tabla_productos.column("categoria", width=180, anchor=tk.W)
        self.tabla_productos.column("precio", width=90, anchor=tk.E)

        scroll_prod = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=self.tabla_productos.yview)
        self.tabla_productos.configure(yscroll=scroll_prod.set)

        self.tabla_productos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_prod.pack(side=tk.RIGHT, fill=tk.Y)

    # -------------------------------------------------------------
    # PESTAÑA: USUARIOS (Solo consulta)
    # -------------------------------------------------------------
    def _construir_pestana_usuarios(self):
        frame_usuarios = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios Registrados ", padding=10)
        frame_usuarios.pack(fill=tk.BOTH, expand=True)

        columnas = ("id", "username", "rol")
        self.tabla_usuarios = ttk.Treeview(frame_usuarios, columns=columnas, show="headings")
        self.tabla_usuarios.heading("id", text="ID")
        self.tabla_usuarios.heading("username", text="Usuario")
        self.tabla_usuarios.heading("rol", text="Rol Asignado")

        self.tabla_usuarios.column("id", width=80, anchor=tk.CENTER)
        self.tabla_usuarios.column("username", width=200, anchor=tk.W)
        self.tabla_usuarios.column("rol", width=150, anchor=tk.W)

        scroll_usr = ttk.Scrollbar(frame_usuarios, orient=tk.VERTICAL, command=self.tabla_usuarios.yview)
        self.tabla_usuarios.configure(yscroll=scroll_usr.set)

        self.tabla_usuarios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_usr.pack(side=tk.RIGHT, fill=tk.Y)

    # -------------------------------------------------------------
    # OPERACIONES Y LÓGICA DE INTERFAZ
    # -------------------------------------------------------------
    def _cargar_datos_iniciales(self):
        self._refrescar_tabla_productos()
        self._refrescar_tabla_usuarios()

    def _refrescar_tabla_productos(self):
        for fila in self.tabla_productos.get_children():
            self.tabla_productos.delete(fila)
        
        productos = RestauranteServicio.obtener_productos()
        for p in productos:
            self.tabla_productos.insert("", tk.END, values=(p.id_producto, p.nombre, p.categoria, f"{p.precio:.2f}"))

    def _refrescar_tabla_usuarios(self):
        for fila in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(fila)
        
        usuarios = RestauranteServicio.obtener_usuarios()
        for u in usuarios:
            self.tabla_usuarios.insert("", tk.END, values=(u.id_usuario, u.username, u.rol))

    def _limpiar_formulario_productos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_categoria.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_id.focus()

    def _registrar_producto(self):
        exito, msg = RestauranteServicio.registrar_producto(
            self.txt_id.get(),
            self.txt_nombre.get(),
            self.txt_categoria.get(),
            self.txt_precio.get()
        )
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._refrescar_tabla_productos()
            self._limpiar_formulario_productos()
        else:
            messagebox.showwarning("Advertencia", msg)

    def _cargar_producto(self):
        id_busqueda = self.txt_id.get().strip()
        if not id_busqueda:
            messagebox.showwarning("Campo Requerido", "Ingrese el ID del producto que desea cargar/consultar.")
            return

        prod, msg = RestauranteServicio.obtener_producto_por_id(id_busqueda)
        if prod:
            self.txt_nombre.delete(0, tk.END)
            self.txt_nombre.insert(0, prod.nombre)

            self.txt_categoria.delete(0, tk.END)
            self.txt_categoria.insert(0, prod.categoria)

            self.txt_precio.delete(0, tk.END)
            self.txt_precio.insert(0, str(prod.precio))
            messagebox.showinfo("Consulta", f"Producto cargado: {prod.nombre}")
        else:
            messagebox.showerror("No Encontrado", msg)

    def _actualizar_producto(self):
        exito, msg = RestauranteServicio.actualizar_producto(
            self.txt_id.get(),
            self.txt_nombre.get(),
            self.txt_categoria.get(),
            self.txt_precio.get()
        )
        if exito:
            messagebox.showinfo("Éxito", msg)
            self._refrescar_tabla_productos()
            self._limpiar_formulario_productos()
        else:
            messagebox.showwarning("Advertencia", msg)

    def _eliminar_producto(self):
        id_eliminar = self.txt_id.get().strip()
        if not id_eliminar:
            messagebox.showwarning("Campo Requerido", "Ingrese el ID del producto que desea eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto con ID {id_eliminar}?")
        if confirmar:
            exito, msg = RestauranteServicio.eliminar_producto(id_eliminar)
            if exito:
                messagebox.showinfo("Éxito", msg)
                self._refrescar_tabla_productos()
                self._limpiar_formulario_productos()
            else:
                messagebox.showerror("Error", msg)
