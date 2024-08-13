"""

 Los paneles, las tecnologias y las horas solares pico son objetos de los cuales solo
se necesita la informacion almacenada en ellos, no tienen ninguna funcion especial.

 Se guardan en un dict para facilitar su guardado y gestion debido a sus caracteristicas.

"""

from objetos.json_manager import add_element


def crear_tecnologia(material: str, area: float) -> dict:
    """
    Crea un elemento de tipo 'tecnologia' y lo añade automaticamente al json correspondiente.

    :param material: material de la tecnologia creada, este a su vez es el identificador de cada una.
    :param area: area que requiere cada tecnologia para generar energia.
    :return: retorna el nuevo elemento creado
    """
    element = {"material": material, "area": area}

    add_element("../salva/Tecnologias.json", element)

    return element


def crear_panel(identificador: int, potencia_pico: float, material_celdas: str, area: float,
                precio: float, precio_kwh_sen: float) -> dict:
    """
    Crea un elemento de tipo 'panel' y lo añade automaticamente al json correspondiente.

    :param identificador: llave primaria del elemento de tipo 'panel'.
    :param potencia_pico: potencia que genera el panel.
    :param material_celdas: material de las celdas del panel, independientes a la tecnologia.
    :param area: area que ocupa el panel.
    :param precio: precio de cada panel de este tipo
    :param precio_kwh_sen: precio de cada kw que genera el panel.
    :return: retorna el nuevo elemento creado.
    """
    element = {"identificador": identificador,
               "potencia_pico": potencia_pico,
               "material_celdas": material_celdas,
               "area": area,
               "precio": precio,
               "precio_kwh_sen": precio_kwh_sen}

    add_element("../salva/Paneles.json", element)

    return element


def crear_hsp(zona: str, valor: float) -> dict:
    """
    Crea un elemento de tipo 'Hsp (Hora solar pico)' y lo añade automaticamente al json correspondiente.

    :param zona: zona en especifico de donde se tiene registrado una hsp.
    :param valor: potencia que genera el hsp.
    :return: retorna el nuevo elemento creado.
    """
    element = {"zona": zona, "valor": valor}

    add_element("../salva/Hsp.json", element)

    return element
