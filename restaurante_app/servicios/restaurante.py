from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self._buscar_producto_por_codigo(producto.codigo):
            return False
        self._productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        if self._buscar_cliente_por_identificacion(cliente.identificacion):
            return False
        self._clientes.append(cliente)
        return True

    def listar_productos(self) -> List[str]:
        return [producto.mostrar_informacion() for producto in self._productos]

    def listar_clientes(self) -> List[str]:
        return [cliente.mostrar_informacion() for cliente in self._clientes]

    def _buscar_producto_por_codigo(self, codigo: str) -> Union[Producto, None]:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def _buscar_cliente_por_identificacion(self, identificacion: str) -> Union[Cliente, None]:
        for cliente in self._clientes:
            if cliente.identificacion == identificacion:
                return cliente
        return None

    @staticmethod
    def validar_codigo(codigo: str) -> str:
        codigo_limpio = codigo.strip()
        if not codigo_limpio:
            raise ValueError("El código no puede estar vacío.")
        if len(codigo_limpio) < 3:
            raise ValueError("El código debe tener al menos 3 caracteres.")
        if not codigo_limpio.isalnum():
            raise ValueError("El código solo puede contener letras y números.")
        return codigo_limpio

    @staticmethod
    def validar_nombre(nombre: str) -> str:
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise ValueError("El nombre no puede estar vacío.")
        if len(nombre_limpio) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        if not all(caracter.isalpha() or caracter.isspace() for caracter in nombre_limpio):
            raise ValueError("El nombre solo puede contener letras y espacios.")
        return nombre_limpio

    @staticmethod
    def validar_categoria(categoria: str) -> str:
        categoria_limpia = categoria.strip()
        if not categoria_limpia:
            raise ValueError("La categoría no puede estar vacía.")
        if len(categoria_limpia) < 3:
            raise ValueError("La categoría debe tener al menos 3 caracteres.")
        if not all(caracter.isalpha() or caracter.isspace() for caracter in categoria_limpia):
            raise ValueError("La categoría solo puede contener letras y espacios.")
        return categoria_limpia

    @staticmethod
    def validar_precio(precio: str) -> float:
        try:
            precio_limpio = precio.strip().replace(',', '.')
            valor = float(precio_limpio)
            if valor <= 0:
                raise ValueError("El precio debe ser mayor que cero.")
            if valor > 999999.99:
                raise ValueError("El precio no puede ser mayor a 999,999.99.")
            return round(valor, 2)
        except ValueError:
            raise ValueError("El precio debe ser un número válido (ej: 10.50).")

    @staticmethod
    def validar_identificacion(identificacion: str) -> str:
        id_limpio = identificacion.strip()
        if not id_limpio:
            raise ValueError("La identificación no puede estar vacía.")
        if not id_limpio.isdigit():
            raise ValueError("La identificación solo puede contener números.")
        if len(id_limpio) < 6:
            raise ValueError("La identificación debe tener al menos 6 dígitos.")
        return id_limpio

    @staticmethod
    def validar_correo(correo: str) -> str:
        correo_limpio = correo.strip()
        if not correo_limpio:
            raise ValueError("El correo no puede estar vacío.")
        if '@' not in correo_limpio or '.' not in correo_limpio:
            raise ValueError("El correo debe ser válido (ej: usuario@dominio.com).")
        partes = correo_limpio.split('@')
        if len(partes) != 2 or not partes[0] or not partes[1]:
            raise ValueError("El correo debe tener un formato válido.")
        if len(correo_limpio) < 5:
            raise ValueError("El correo es demasiado corto.")
        return correo_limpio

    @staticmethod
    def validar_tamanio(tamanio: str) -> str:
        tamanio_limpio = tamanio.strip()
        if not tamanio_limpio:
            raise ValueError("El tamaño no puede estar vacío.")
        if not any(char.isdigit() for char in tamanio_limpio):
            raise ValueError("El tamaño debe incluir una cantidad (ej: 500ml).")
        if len(tamanio_limpio) < 2:
            raise ValueError("El tamaño debe tener al menos 2 caracteres.")
        return tamanio_limpio

    @staticmethod
    def validar_tipo_envase(tipo_envase: str) -> str:
        envase_limpio = tipo_envase.strip()
        if not envase_limpio:
            raise ValueError("El tipo de envase no puede estar vacío.")
        if len(envase_limpio) < 3:
            raise ValueError("El tipo de envase debe tener al menos 3 caracteres.")
        if not all(caracter.isalpha() or caracter.isspace() for caracter in envase_limpio):
            raise ValueError("El tipo de envase solo puede contener letras y espacios.")
        return envase_limpio