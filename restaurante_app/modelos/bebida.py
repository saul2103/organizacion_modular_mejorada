from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamanio: str, tipo_envase: str):
        super().__init__(codigo, nombre, categoria, precio)
        self.tamanio = tamanio
        self.tipo_envase = tipo_envase

    def mostrar_informacion(self) -> str:
        return (f"Código: {self.codigo} | Nombre: {self.nombre} | Categoría: {self.categoria} | "
                f"Precio: ${self.precio:.2f} | Tamaño: {self.tamanio} | Envase: {self.tipo_envase}")