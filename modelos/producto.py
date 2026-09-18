class Producto:
    def __init__(self, id_producto: int, nombre: str, categoria: str, precio: float):
        self.id_producto = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            id_producto=int(data.get("id_producto")),
            nombre=str(data.get("nombre")),
            categoria=str(data.get("categoria")),
            precio=float(data.get("precio"))
        )
