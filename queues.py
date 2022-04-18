"""

queues

"""

from collections import deque

mi_fila=deque()
mi_fila.append(5)
mi_fila.append(10)
mi_fila.append(15)
print(str(mi_fila))
mi_fila.popleft()
print(str(mi_fila))