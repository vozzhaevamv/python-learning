class Counter:
    def __init__(self, start=0):
        self.value = start

    def increase(self):
        self.value += 1

c = Counter()
c.increase()
c.increase()
print(c.value)
d = Counter(10)
d.increase()
print(d.value)


class Calculator:
    def __init__(self):
        self.history = []
        
    def add(self,a,b):
        result = a + b 
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    
c = Calculator()
print(c.add(2, 3))
print(c.history)