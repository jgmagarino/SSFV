"""--------------------"""
"""Calculos del sistema"""
"""--------------------"""


def clac_approx_peak_power(Sr: float, Skwp: float):
    """
    Calculo aproximado de la potencia que se obtendra en un area especifica.

    :param Sr: area especificada para la construccion del sistema.
    :param Skwp: area requerida segun la tecnologia del panel para generar un kW
    :return: descripcion de los calculos realizados
    """
    return  (
            " Se realiza un calculo aproximado segun la tecnologia del panel para obtener "
            "la potencia que se generara en el area especificada. \n"
            "\n"
            "Datos: \n"
            f"Superficie disponible (Sr): {Sr} m^2 \n"
            f"Superficie reqierida segun la tecnologia del panel (Skwp): {Skwp} m^2/kWp\n"
            "\n"
            f"Calculo: \n"
            f"Ppg = Sr / Skwp = ({Sr}  / {Skwp} ) = "
            f"{Sr/Skwp} kWp \n"
            )

def calc_approx_area_required(Pinst: float, Skwp: float):
    """
    Calculo aproximado del area requerida segun la potencia que se quiere instalar.

    :param Pinst: potencia a instalar
    :param Skwp: area requerida segun la tecnologia del panel para generar un kW
    :return: descripcion de los calculos realizados
    """
    return  (
            "Se realiza un calculo aproccimado segun la tecnologia del panel para obtener "
            "el area requerida para la potencia que se quiere instalar. \n"
            "\n"
            "Datos: \n"
            f"Potencia a instalar (Pinst): {Pinst/1000} kW\n"
            f"Superficie reqierida segun la tecnologia del panel (Skwp): {Skwp} m^2/kWp\n"
            "\n"
            f"Calculo: \n"
            f"Sr = Pinst * Skwp = ({Pinst/1000} * {Skwp}) = {(Pinst/1000) * Skwp} m^2\n"
            )


def calc_number_of_panels_with_area(Ad: float, Ap: float, to_south: bool):
        """
        Calcula el numero de paneles que se podran comprar para un area disponible,
        la cantidad de paneles variaran en dependencia de si estaran orientados al sur
        o no.

        :param Ad: area disponible
        :param Ap: area del panel
        :param to_south: estan horientados al sur (True) o no (False)
        :return: descripcion de los calculos realizados
        """
        if to_south:
                return (
                        "Datos: \n"
                        f"Superficie disponible (Ad): {Ad} m^2 \n"
                        f"Area del panel (Ap): {Ap} m^2 \n"
                        f"\n"
                        f"Al estar los paneles dirigidos al sur, se hace un aumento del "
                        f"40% del area requerida debido a la sombra que proyectan "
                        f"(N = N / 1.4)\n"
                        f"\n"
                        f"Calculo: \n"
                        f"N = (Ad / Ap) / 1.4 = (({Ad} / {Ap}) /1.4) = "
                        f"{int((Ad / Ap) / 1.4)} \n"
                )
        else:
                return (
                        "Datos: \n"
                        f"Superficie disponible (Ad): {Ad} m^2 \n"
                        f"Area del panel (Ap): {Ap} m^2 \n"
                        "\n"
                        f"Calculo: \n"
                        f"N = Ad / Ap = ({Ad} / {Ap} ) = "
                        f"{int(Ad / Ap)} \n"
                    )


def calc_number_of_panels_with_peak_power(Eu: float, hsp: float, Pn: float):
        """
        Calcula el numero de paneles requerido para generar una potencia pico especifica.

        :param Eu: energia util del sistema
        :param hsp: hora solar pico
        :param Pn: potencia nominal del panel
        :return: descripcion de los calculos realizados
        """
        return (
                    "\n"
                    "Datos: \n"
                    f"Energia util (Eu): {Eu} Wh/día\n"
                    f"hora solar pico (hsp): {hsp} m^2/kWp\n"
                    f"Potencia nominal del panel (Pn): {Pn} W\n"
                    "\n"
                    f"Calculo: \n"
                    f"N = (Eu / (0.654 * hsp * Pn)) +1 = {Eu} / (0.654 * {hsp} * "
                    f"{Pn}) +1 = {int((Eu / (0.654 * hsp * Pn)) + 1)} \n"
                )


def calc_peak_power_with_area(N: int, Pn: float, to_south: bool):
        """
        Potencia pico que generara el sistema en dependencia de la cantidad de paneles
        y su potencia. Esto variara en dependencia de si estaran los paneles orientados al
        sur o no.

        :param N: numer de paneles
        :param Pn: potencia nominal del panel
        :param to_south: estan horientados al sur (True) o no (False)
        :return: descripcion de los calculos realizados
        """

        if to_south:
                return  (
                        "Potencia pico segun la cantidad de paneles que se usaran. \n"
                        "\n"
                        "Datos: \n"
                        f"Numero de paneles (N): {N} \n"
                        f"Potencia nominal del panel (Pn): {Pn} W \n"
                        "\n"
                        f"Calculo: \n"
                        f"Pp = N * Pn = {N} * {Pn} = "
                        f"{N * Pn} W"
                        )
        else:
                return (
                        "Potencia pico segun la cantidad de paneles que se usaran. \n"
                        "\n"
                        "Datos: \n"
                        f"Numero de paneles (N): {N} \n"
                        f"Potencia nominal del panel (Pn): {Pn} W \n"
                        "\n"
                        "Al no estar orientados al sur se hace un 20% de descuento de la potencia "
                        "que generara."
                        "\n"
                        f"Calculo: \n"
                        f"Pp = N * Pn * 0.8 = {N} * {Pn} * 0.8 = "
                        f"{N * Pn * 0.8} W"
                )

def calc_area_with_peak_power(N: int, Ap: float, to_south: bool):
        """
        Calcula el area requerida para un numero de paneles determinado.
        Esto varia en dependencia de si los paneles estaran orientados al sur o no.

        :param N: numero de paneles
        :param Ap: area del panel
        :param to_south: estan horientados al sur (True) o no (False)
        :return: descripcion de los calculos realizados
        """

        if to_south:
                return (
                "Al estar orientados al sur se requiere un aumento del 40% del"
                " area requerida debido a la sombra que proyectan los paneles. \n"
                "\n"
                "Datos: \n"
                f"Numero de paneles (N): {N} \n"
                f"Area del panel (Ap): {Ap} m^2\n"
                "\n"
                f"Calculo: \n"
                f"Ar = N * Ap * 1.4 = {N} * {Ap} * 1.4 = "
                f"{N * Ap * 1.4} m^2"
            )
        else:
                return (
                        "\n"
                        "Datos: \n"
                        f"Numero de paneles (N): {N} \n"
                        f"Area del panel (Ap): {Ap} m^2\n"
                        "\n"
                        f"Calculo: \n"
                        f"Ar = N * Ap = {N} * {Ap} = "
                        f"{N * Ap} m^2"
                )

def calc_userful_energy(Pp: float, hsp: float):
        """
        Calculo de la energia util del sistema.

        :param Pp: potencia pico del sistema
        :param hsp: hora solar pico
        :return: descripcion de los calculos realizados
        """

        return (
                "Datos: \n"
                f"Hora solar pico segun el lugar (hsp): {hsp} m^2/kWp\n"
                f"Potencia pico (Pinst): {Pp} W \n"
                "\n"
                f"Calculo: \n"
                f"Eu = hsp * Pinst = {hsp} * {Pp} = {Pp * hsp} Wh/día"
        )


"""-------------------"""
"""Calculos economicos"""
"""-------------------"""


def calc_cost(price: float, N: int):
        """
        Calcula el costo del sistema

        :param price: precio del panel
        :param N: numero de paneles que se usaran
        :return: descripcion de los calculos realizados
        """

        return (
                    "\n"
                    "Datos: \n"
                    f"Costo del panel : {price} cup \n"
                    f"Cantidad de paneles que se usaran: {N} \n"
                    "\n"
                    f"Calculo: \n"
                    f"CSSFV = costo_del_panel * N = ({price}  * {N} ) = "
                    f"{price * N} cup\n"
                    "\n"
                    "Si se cuentan gastos adicionasles como cableado, soportes etc, se"
                    "ria un aumento del 30% del costo de los paneles. \n"
                    f"CSSFV = costo_del_panel * N * 1.3 = ({price}  * {N} * 1.3) = {price * N * 1.3} cup\n"
                    "\n"
        )

def calc_income(userful_energy: float, price_kwh_SEN: float):
        """
        Calcula los ingresos del sistema

        :param userful_energy: energia util
        :param price_kwh_SEN: precio del kwh SEN
        :return: descripcion de los calculos realizados
        """

        userful_energy_year = round((userful_energy/1000) * 365, 2)
        return (
            "\n"
            "Datos: \n"
            f"Energia util generada (Eu): {userful_energy} W/dia = "
            f"{userful_energy_year} kW/año \n"
            f"Precio del kWhSEN : {price_kwh_SEN} cup \n"
            "\n"
            f"Calculo: \n"
            f" Ig = Eu * Precio del kWhSEN = ({price_kwh_SEN} * "
            f"{userful_energy_year} ) = "
            f"{userful_energy_year * price_kwh_SEN} cup/año\n"
        )

def calc_recovery(cost: float, income: float):
        """
        Periodo de recuperacion simple

        :param cost: costo del sistema
        :param income: ingresos del sistema
        :return: descripcion de los calculos realizados
        """

        return (
                    "\n"
                    "Datos: \n"
                    f"CSSFV: {cost} cup \n"
                    f"Ig : {income} cup/año \n"
                    "\n"
                    f"Calculo: \n"
                    f" PSRI = CSSFV / Ig = ({cost} / {income} ) = "
                    f"{round(cost / income, 2)} años\n"
        )