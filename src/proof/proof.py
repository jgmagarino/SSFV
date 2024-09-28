# Importando los modulos
from src.modules.economicCalc_module import EconomicCalc
from src.modules.hsp_module import HSP
from src.modules.panel_module import Panel
from src.modules.systemCalc_module import SystemCalcPeakPower, SystemCalcArea
from src.modules.system_module import System
from src.modules.technology_module import Technology

# Importando las funciones mappers
from src.Mappers.hsp_mapper import get_hsp, get_all_hps, exist_hsp
from src.Mappers.technology_mapper import get_technology, get_all_technologies, exist_techno
from src.Mappers.panel_mapper import get_panel, get_all_panels, exist_panel
from src.Mappers.system_mapper import get_system, get_all_systems, exist_system
from src.Mappers.calc_mapper import (get_sys_calc, get_eco_calc, get_all_sys_calc, get_all_sys_eco_cal,
                                     exist_sys_calc, exist_eco_calc)

tech = Technology('silicio monocristalino', '7 - 9')  # Creando el objeto tecnologia
tech.save()  # Guardando el objeto tecnologia
tech.validate()  # Validando el objeto tecnologia
exist_techno(tech.technology)  # Verificando que existe el objeto tecnologia
print(tech.get_panels()) # Obteniendo los paneles donde se utiliza este objeto en forma de lista de tipo panel
# tech.delete() # Eliminando el objeto tecnologia


hsp = HSP('cienfuegos', 6.0)  # Creando el objeto Hora Solar Pico
hsp.save()  # Guardando el objeto hsp
hsp.validate()  # Validando el objeto hsp
exist_hsp(hsp.place)  # Verificando que existe el objeto hsp
# hsp.delete() # Eliminando el objeto hsp
print(hsp.get_system())  # Obteniendo los sistemas donde se utiliza este objeto en forma de lista de sistemas

panel = Panel("mejor", 245, 'silicio monocristalino', 2.3, 234, 32)  # Creando el objeto panel
panel.save()  # Guardando el objeto panel
panel.validate()  # Validando el objeto panel
exist_panel(panel.panel_id)  # Verificando que existe el objeto panel
# panel.delete() # Eliminando el objeto panel
print(panel.get_system())  # Obteniendo los sistemas donde se utiliza este objeto en forma de lista de sistemas

system = System("primero", "mejor", "cienfuegos", 1, True)  # Creando el objeto sistema
system.save()  # Guardando el objeto sistema
exist_system(system.name)  # Verificando que existe el objeto sistema
# system.delete() # Eliminando el objeto sistema

sys_calc = SystemCalcPeakPower(system, 250)  # Creando el objeto calculos del sistema
sys_calc.approx_peak_power(True)  # calculando la potencia pico aproximada del sistema
sys_calc.num_panels()  # calculando el numero de paneles del sistema
sys_calc.calc_peak_power()  # calculando la potencia pico a instalar en el sistema
sys_calc.calc_useful_energy()  # calculando la energia util del sistema
sys_calc.save()  # Guardando el objeto calculos del sistema
sys_calc.validate()  # Validando el objeto calculos del sistema
exist_sys_calc(sys_calc.system.name)  # Verificando que existe el objeto calculos del sistema
# sys_calc.delete() # Eliminando el objeto calculos del sistema

sys_calc_1 = SystemCalcArea(system, 800)  # Creando el objeto calculos del sistema
sys_calc_1.approx_required_surface(False)  # calculando el area aproximada del sistema
sys_calc_1.calc_useful_energy()  # calculando la energia util del sistema
sys_calc_1.num_panels()  # calculando el numero de paneles del sistema
sys_calc_1.calc_required_surface()  # calculando el area requerida del sistema
sys_calc_1.save()  # Guardando el objeto calculos del sistema
sys_calc_1.validate()  # Validando el objeto calculos del sistema
exist_sys_calc(sys_calc_1.system.name)  # Verificando que existe el objeto calculos del sistema
# sys_calc_1.delete() # Eliminando el objeto calculos del sistema

eco_calc = EconomicCalc(system, sys_calc)  # Creando el objeto calculos economicos del sistema
eco_calc.calc_cost()  # calculando el costo del sistema
eco_calc.calc_income()  # calculando los ingresos del sistema
eco_calc.calc_recovery_period()  # calculando el periodo de recuperacion de la inversion del sistema
eco_calc.save()  # Guardando el objeto calculos economicos del sistema
exist_eco_calc(eco_calc.system.name)  # Verificando que existe el objeto calculos economicos del sistema
# eco_calc.delete() # Eliminando el objeto calculos economicos del sistema

print(get_all_hps())  # Obteniendo todos los objetos tipo hsp
print(get_all_technologies())  # Obteniendo todos los objetos tipo tecnologia
print(get_all_panels())  # Obteniendo todos los objetos tipo panel
print(get_all_systems())  # Obteniendo todos los objetos tipo sistema
print(get_all_sys_calc())  # Obteniendo todos los objetos tipo calculos del sistema
print(get_all_sys_eco_cal())  # Obteniendo todos los objetos tipo calculos economicos del sistema

print(get_panel("mejor"))  # Obteniendo el objeto tipo panel
print(get_hsp('cienfuegos'))  # Obteniendo el objeto tipo hsp
print(get_technology('silicio monocristalino'))  # Obteniendo el objeto tipo tecnologia
print(get_system("primero"))  # Obteniendo el objeto tipo sistema
print(get_sys_calc("primero"))  # Obteniendo el objeto tipo calculos del sistema
print(get_eco_calc("primero"))  # Obteniendo el objeto tipo calculos economicos del sistema
