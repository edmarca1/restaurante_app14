import tkinter as tk
from tkinter import ttk, messagebox
from servicios.restaurante_servicio import RestauranteServicio

class LoginView(tk.Tk):
    def __init__(self, on_login_success):
        super().__init__()
        self.title("Acceso al Sistema - Restaurante")
        self.geometry("380x300")
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')

        self.on_login_success = on_login_success
        self._crear_interfaz()

    def _crear_interfaz(self):
        contenedor = ttk.Frame(self, padding="25")
        contenedor.pack(fill=tk.BOTH, expand=True)

        lbl_titulo = ttk.Label(contenedor, text="Gestión de Restaurante", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=(0, 20))

        frame_form = ttk.LabelFrame(contenedor, text=" Credenciales de Acceso ", padding="15")
        frame_form.pack(fill=tk.X, expand=True)

        ttk.Label(frame_form, text="Usuario:").grid(row=0, column=0, sticky=tk.W, pady=6)
        self.txt_usuario = ttk.Entry(frame_form, width=22)
        self.txt_usuario.grid(row=0, column=1, pady=6, padx=(10, 0))
        self.txt_usuario.focus()

        ttk.Label(frame_form, text="Contraseña:").grid(row=1, column=0, sticky=tk.W, pady=6)
        self.txt_password = ttk.Entry(frame_form, show="*", width=22)
        self.txt_password.grid(row=1, column=1, pady=6, padx=(10, 0))

        btn_ingresar = ttk.Button(contenedor, text="Iniciar Sesión", command=self._login)
        btn_ingresar.pack(pady=(18, 0), fill=tk.X)

    def _login(self):
        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get().strip()

        user_obj, mensaje = RestauranteServicio.autenticar_usuario(usuario, password)

        if user_obj:
            self.destroy()
            self.on_login_success(user_obj)
        else:
            messagebox.showerror("Error de Autenticación", mensaje)
