"""
Aqui probare los componentes que voy creando
"""

class My:
    def __init__(self):
        self.a = 1

new = My()

new.a = 2

new.__init__()

print(new.a)