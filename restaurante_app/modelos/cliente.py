class Cliente:

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion = self._validar_texto(identificacion, "La identificacion no debe estar vacia.")
        self.nombre = self._validar_nombre(nombre)
        self.correo = self._validar_correo(correo)

    @staticmethod
    def _validar_texto(valor: str, mensaje_error: str) -> str:
        valor_limpio = valor.strip()
        if not valor_limpio:
            raise ValueError(mensaje_error)
        return valor_limpio

    @staticmethod
    def _validar_nombre(nombre: str) -> str:
        nombre_limpio = nombre.strip()
        if not nombre_limpio:
            raise ValueError("El nombre no debe estar vacio.")
        partes = nombre_limpio.split()
        if len(partes) < 2:
            raise ValueError("El nombre debe incluir al menos nombre y apellido.")
        return " ".join(p.capitalize() for p in partes)

    @staticmethod
    def _validar_correo(correo: str) -> str:
        correo_limpio = correo.strip()
        if not correo_limpio:
            raise ValueError("El correo no puede estar vacio.")
        posicion_arroba = correo_limpio.find("@")
        if posicion_arroba == -1 or "." not in correo_limpio[posicion_arroba + 1:]:
            raise ValueError("El correo debe contener @ y un punto despues del @.")
        return correo_limpio

    def mostrar_informacion(self) -> str:
        return (
            f"Identificacion: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
