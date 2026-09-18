import os
from modelos.usuario import Usuario
from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio

# Obtiene la ruta base del proyecto de forma dinámica y exacta
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class RestauranteServicio:
    RUTA_USUARIOS = os.path.join(BASE_DIR, "datos", "usuarios.json")
    RUTA_PRODUCTOS = os.path.join(BASE_DIR, "datos", "productos.json")

    # --- Métodos de Usuarios ---
    @classmethod
    def autenticar_usuario(cls, username, password):
        if not username or not password:
            return None, "Debe ingresar usuario y contraseña."
        
        datos = ArchivoServicio.leer_json(cls.RUTA_USUARIOS)
        for d in datos:
            if d.get("username") == username and d.get("password") == password:
                return Usuario.from_dict(d), "Acceso correcto."
        return None, "Credenciales incorrectas."

    @classmethod
    def obtener_usuarios(cls):
        datos = ArchivoServicio.leer_json(cls.RUTA_USUARIOS)
        return [Usuario.from_dict(d) for d in datos]

    # --- Métodos de Productos (CRUD) ---
    @classmethod
    def obtener_productos(cls):
        datos = ArchivoServicio.leer_json(cls.RUTA_PRODUCTOS)
        return [Producto.from_dict(d) for d in datos]

    @classmethod
    def obtener_producto_por_id(cls, id_producto):
        try:
            id_num = int(id_producto)
        except (ValueError, TypeError):
            return None, "El ID debe ser numérico."

        datos = ArchivoServicio.leer_json(cls.RUTA_PRODUCTOS)
        for d in datos:
            if d.get("id_producto") == id_num:
                return Producto.from_dict(d), "Producto encontrado."
        return None, f"No se encontró el producto con ID {id_num}."

    @classmethod
    def registrar_producto(cls, id_producto, nombre, categoria, precio):
        if not str(id_producto).strip() or not str(nombre).strip() or not str(categoria).strip() or not str(precio).strip():
            return False, "Todos los campos son obligatorios."

        try:
            id_num = int(id_producto)
            precio_num = float(precio)
        except ValueError:
            return False, "ID debe ser entero y Precio un valor numérico válido."

        if precio_num < 0:
            return False, "El precio no puede ser negativo."

        datos = ArchivoServicio.leer_json(cls.RUTA_PRODUCTOS)
        if any(d.get("id_producto") == id_num for d in datos):
            return False, f"El ID {id_num} ya está asignado a otro producto."

        nuevo_prod = Producto(id_num, nombre.strip(), categoria.strip(), precio_num)
        datos.append(nuevo_prod.to_dict())
        ArchivoServicio.guardar_json(cls.RUTA_PRODUCTOS, datos)
        return True, "Producto registrado exitosamente."

    @classmethod
    def actualizar_producto(cls, id_producto, nombre, categoria, precio):
        if not str(id_producto).strip() or not str(nombre).strip() or not str(categoria).strip() or not str(precio).strip():
            return False, "Todos los campos son obligatorios para actualizar."

        try:
            id_num = int(id_producto)
            precio_num = float(precio)
        except ValueError:
            return False, "ID debe ser entero y Precio un valor numérico válido."

        if precio_num < 0:
            return False, "El precio no puede ser negativo."

        datos = ArchivoServicio.leer_json(cls.RUTA_PRODUCTOS)
        encontrado = False
        for i, d in enumerate(datos):
            if d.get("id_producto") == id_num:
                datos[i] = Producto(id_num, nombre.strip(), categoria.strip(), precio_num).to_dict()
                encontrado = True
                break

        if not encontrado:
            return False, f"No se encontró el producto con ID {id_num} para actualizar."

        ArchivoServicio.guardar_json(cls.RUTA_PRODUCTOS, datos)
        return True, "Producto actualizado correctamente."

    @classmethod
    def eliminar_producto(cls, id_producto):
        try:
            id_num = int(id_producto)
        except (ValueError, TypeError):
            return False, "El ID debe ser numérico."

        datos = ArchivoServicio.leer_json(cls.RUTA_PRODUCTOS)
        nuevos_datos = [d for d in datos if d.get("id_producto") != id_num]

        if len(nuevos_datos) == len(datos):
            return False, f"No se encontró el producto con ID {id_num} para eliminar."

        ArchivoServicio.guardar_json(cls.RUTA_PRODUCTOS, datos)
        return True, f"Producto con ID {id_num} eliminado exitosamente."