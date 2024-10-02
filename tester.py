"""
Aqui probare los componentes que voy creando
"""
import random

# En talla
# from src.Mappers.hsp_mapper import *
# from src.modules.hsp_module import *

# En talla
# from src.Mappers.panel_mapper import *
# from src.modules.panel_module import *

from src.Mappers.technology_mapper import *

t = get_technology("silicio monocristalino")

print(f"{t.technology}, {t.get_min_surface_req()}")


