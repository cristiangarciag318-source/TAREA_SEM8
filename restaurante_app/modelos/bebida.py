from modelos.producto import Producto


class Bebida(Producto):

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str,
        tipo_envase: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano = self._validar_tamano(tamano)
        self.tipo_envase = self._validar_texto(tipo_envase, "El tipo de envase no puede estar vacio.")

    @staticmethod
    def _validar_tamano(tamano: str) -> str:
        tamano_limpio = tamano.strip()
        if not tamano_limpio:
            raise ValueError("El tamano no puede estar vacio.")
        tamanos_validos = ("pequeño", "mediano", "grande", "personal")
        unidades = ("ml", "l", "cl", "oz")
        es_descriptivo = tamano_limpio.lower() in tamanos_validos
        tiene_unidad = any(tamano_limpio.lower().endswith(u) for u in unidades)
        if not es_descriptivo and not tiene_unidad:
            raise ValueError("El tamano debe ser descriptivo (pequeño, mediano, grande) o incluir unidad (ml, L).")
        return tamano_limpio

    def mostrar_informacion(self) -> str:
        return (
            f"{super().mostrar_informacion()} | "
            f"Tamano: {self.tamano} | "
            f"Tipo de envase: {self.tipo_envase}"
        )
