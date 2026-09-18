# Restaurante App - Semana 14

## Propósito de la Actividad
Evolucionar la aplicación gráfica de escritorio restaurante_app mediante el uso adecuado de componentes y contenedores de Tkinter/ttk, manteniendo una arquitectura modular por capas (datos, modelos, servicios, interfaz y punto de entrada) y la persistencia en archivos JSON.

---

## Estructura del Proyecto

```text
restaurante_app14/
│
├── datos/
│   ├── productos.json       # Persistencia de productos
│   └── usuarios.json        # Persistencia de usuarios
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py          # Clase Producto y serialización
│   └── usuario.py           # Clase Usuario y serialización
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py  # Lectura y escritura segura en JSON
│   └── restaurante_servicio.py # Lógica de negocio, validaciones y CRUD
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py        # Ventana de autenticación
│   └── main_view.py         # Interfaz con componentes y contenedores
│
├── main.py                  # Punto de entrada de la aplicación
└── README.md                # Documentación del proyecto
