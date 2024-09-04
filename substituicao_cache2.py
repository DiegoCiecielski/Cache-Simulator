class Cache:
    def __init__(self, size=4):
        self.size = size
        self.cache = []
        self.hits = 0
        self.misses = 0

    def access(self, address, data):
        raise NotImplementedError("Deve ser implementado na subclasse")

    def __repr__(self):
        return str(self.cache)

    def reset(self):
        self.cache = []
        self.hits = 0
        self.misses = 0

class FIFOCache(Cache):
    def __init__(self, size=4):
        super().__init__(size)

    def access(self, address, data):
        if address in self.cache:
            self.hits += 1
        else:
            self.misses += 1
            if len(self.cache) >= self.size:
                self.cache.pop(0)
            self.cache.append(address)

class LRUCache(Cache):
    def __init__(self, size=4):
        super().__init__(size)

    def access(self, address, data):
        if address in self.cache:
            self.cache.remove(address)
            self.hits += 1
        else:
            self.misses += 1
            if len(self.cache) >= self.size:
                self.cache.pop(0)
        self.cache.append(address)

class LFUCache(Cache):
    def __init__(self, size=4):
        super().__init__(size)
        self.usage = []

    def reset(self):
        super().reset()
        self.usage = []

    def access(self, address, data):
        if address in self.cache:
            index = self.cache.index(address)
            self.usage[index] += 1
            self.hits += 1
        else:
            self.misses += 1
            if len(self.cache) >= self.size:
                lfu_index = self.usage.index(min(self.usage))
                self.cache.pop(lfu_index)
                self.usage.pop(lfu_index)
            self.cache.append(address)
            self.usage.append(1)

def simulate(cache, requests):
    memory = ['A', 'B', 'C', 'D', 'E', 'F']
    log = []
    for req in requests:
        address = ord(req) - ord('A')
        data = memory[address]
        cache.access(address, data)
        log.append(f"Cache após acessar {req} ({address}): {cache}")
    return log, cache.hits, cache.misses

requests_1 = ['A', 'B', 'C', 'A', 'A', 'B', 'B', 'C', 'A', 'D', 'E', 'F', 'B', 'A', 'B', 'C', 'D']
requests_2 = ['A', 'D', 'C', 'B', 'A', 'B', 'D', 'C', 'A', 'D', 'E', 'F', 'B', 'A', 'F', 'C', 'D']
requests_3 = ['A', 'D', 'C', 'B', 'A', 'B', 'D', 'C', 'A', 'D', 'E', 'F', 'B', 'A', 'F', 'C', 'D',
              'A', 'B', 'C', 'A', 'A', 'B', 'B', 'C', 'A', 'D', 'E', 'F', 'B', 'C', 'D', 'C', 'D']

caches = {'FIFO': FIFOCache(), 'LRU': LRUCache(), 'LFU': LFUCache()}

for nome, cache in caches.items():
    print(f"\nSimulação da Cache {nome} para a Lista de Requisições 1:")
    cache.reset()
    log, hits, misses = simulate(cache, requests_1)
    for etapa in log:
        print(etapa)
    print(f"Hits: {hits}, Misses: {misses}")

    print(f"\nSimulação da Cache {nome} para a Lista de Requisições 2:")
    cache.reset()
    log, hits, misses = simulate(cache, requests_2)
    for etapa in log:
        print(etapa)
    print(f"Hits: {hits}, Misses: {misses}")

    print(f"\nSimulação da Cache {nome} para a Lista de Requisições 3:")
    cache.reset()
    log, hits, misses = simulate(cache, requests_3)
    for etapa in log:
        print(etapa)
    print(f"Hits: {hits}, Misses: {misses}")
