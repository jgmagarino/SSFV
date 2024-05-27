"""

 Los Paneles, las tecnologias y las horas solares pico son objetos de los cuales solo
se necesita la informacion almacenada en ellos, no tienen ninguna funcion especial.

 Se guardan en un dict para facilitar su guardado y gestion debido a sus caracteristicas.

"""


def crear_tecnologia(material: str, area: float) -> dict:
    return {"material": material, "area": area}


def crear_panel(identificador: int, potencia_pico: float,
                precio: float, precio_kwh_sen: float) -> dict:
    return {"identificador": identificador,
            "potencia_pico": potencia_pico,
            "precio": precio,
            "precio_kwh_sen": precio_kwh_sen}


def crear_hsp(zona: str, valor: float) -> dict:
    return {"zona": zona, "valor": valor}
