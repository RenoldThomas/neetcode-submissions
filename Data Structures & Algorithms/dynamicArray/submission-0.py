class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dynamicArray = []
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.dynamicArray[i]

    def set(self, i: int, n: int) -> None:
        self.dynamicArray[i] = n

    def pushback(self, n: int) -> None:
        if (len(self.dynamicArray) >= self.capacity):
            self.resize()
            self.dynamicArray.append(n)
        else:
            self.dynamicArray.append(n)

    def popback(self) -> int:
        return self.dynamicArray.pop()
 
    def resize(self) -> None:
        self.capacity = 2 * self.capacity

    def getSize(self) -> int:
        return len(self.dynamicArray)
        
    def getCapacity(self) -> int:
        return self.capacity
