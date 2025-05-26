import importlib
import importlib.readers # Para usar o .reload() para recarregar o módulo chamado várias vezes

import importlib_singleton_m
print(importlib_singleton_m.variavel)

for i in range(10):
    importlib.reload(importlib_singleton_m)
