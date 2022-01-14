import MemoryFail

MemoryCards = []

class MemoryCard:
    def __init__(self, name, brand, memory):
        self.name = name
        self.brand = brand
        self.memory = memory
        MemoryCards.append(self.name)
    
    def getSystemInfo(self):
        return [self.brand, self.name]

    def getRam(self):
        return self.memory

