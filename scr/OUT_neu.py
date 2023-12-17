class NeuOut:
    def __init__(self, value, weight, type):
        self.weight = weight
        self.value = value
        self.max_i = value.lenght()
        self.returnV = 0
        self.type = type

    def sum(self):
        for i in range(self.max_i):
            self.returnV += self.value[i]*self.weight[i]

    def getValue(self):
        return self.returnV
