# Lógica de reemplazo de páginas (FIFO, LRU, OPT)

from collections import deque, defaultdict

class PageReplacementSimulator:
    def __init__(self, frames):
        self.frames = frames
        self.memoria = set()
        self.page_table = {}
        self.fifo_queue = deque()
        self.lru_stack = []
        self.referencias_usadas = 0
        self.page_faults = 0
        self.reemplazos = 0
        self.escritos_disco = 0

    def reset(self):
        self.memoria = set()
        self.page_table = {}
        self.fifo_queue = deque()
        self.lru_stack = []
        self.referencias_usadas = 0
        self.page_faults = 0
        self.reemplazos = 0
        self.escritos_disco = 0

    def simular_fifo(self, referencias):
        self.reset()
        for op, direccion in referencias:
            pagina = direccion // 4096
            if pagina not in self.memoria:
                self.page_faults += 1
                if len(self.memoria) == self.frames:
                    victima = self.fifo_queue.popleft()
                    if self.page_table[victima]['dirty']:
                        self.escritos_disco += 1
                    self.memoria.remove(victima)
                    self.reemplazos += 1
                self.memoria.add(pagina)
                self.fifo_queue.append(pagina)
                self.page_table[pagina] = {'dirty': op == 'W'}
            else:
                if op == 'W':
                    self.page_table[pagina]['dirty'] = True
        return self.page_faults, self.reemplazos, self.escritos_disco

    def simular_lru(self, referencias):
        self.reset()
        for op, direccion in referencias:
            pagina = direccion // 4096
            if pagina not in self.memoria:
                self.page_faults += 1
                if len(self.memoria) == self.frames:
                    victima = self.lru_stack.pop(0)
                    if self.page_table[victima]['dirty']:
                        self.escritos_disco += 1
                    self.memoria.remove(victima)
                    self.reemplazos += 1
                self.memoria.add(pagina)
                self.lru_stack.append(pagina)
                self.page_table[pagina] = {'dirty': op == 'W'}
            else:
                self.lru_stack.remove(pagina)
                self.lru_stack.append(pagina)
                if op == 'W':
                    self.page_table[pagina]['dirty'] = True
        return self.page_faults, self.reemplazos, self.escritos_disco

    def simular_opt(self, referencias):
        self.reset()
        futuras_referencias = defaultdict(list)
        for i, (_, direccion) in enumerate(referencias):
            pagina = direccion // 4096
            futuras_referencias[pagina].append(i)

        for i, (op, direccion) in enumerate(referencias):
            pagina = direccion // 4096
            futuras_referencias[pagina].pop(0)

            if pagina not in self.memoria:
                self.page_faults += 1
                if len(self.memoria) == self.frames:
                    futuro_usos = {}
                    for p in self.memoria:
                        if futuras_referencias[p]:
                            futuro_usos[p] = futuras_referencias[p][0]
                        else:
                            futuro_usos[p] = float('inf')
                    victima = max(futuro_usos, key=futuro_usos.get)
                    if self.page_table[victima]['dirty']:
                        self.escritos_disco += 1
                    self.memoria.remove(victima)
                    self.reemplazos += 1
                self.memoria.add(pagina)
                self.page_table[pagina] = {'dirty': op == 'W'}
            else:
                if op == 'W':
                    self.page_table[pagina]['dirty'] = True
        return self.page_faults, self.reemplazos, self.escritos_disco

