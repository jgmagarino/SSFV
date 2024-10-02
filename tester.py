"""
Aqui probare los componentes que voy creando
"""
from components.show_components import *
from src.Mappers.hsp_mapper import get_hsp
from src.Mappers.panel_mapper import *
from src.Mappers.system_mapper import *

l = get_all_systems()

print([i.description for i in l])