import sys
import os

# Asegurar que la ruta raíz del proyecto esté en sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.login_view import LoginView
from ui.main_view import MainView

def iniciar_aplicacion():
    def abrir_menu_principal(usuario_autenticado):
        app_principal = MainView(usuario_autenticado)
        app_principal.mainloop()

    app_login = LoginView(on_login_success=abrir_menu_principal)
    app_login.mainloop()

if __name__ == "__main__":
    iniciar_aplicacion()
