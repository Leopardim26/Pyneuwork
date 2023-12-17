import math

class NeuMid:
    def __init__(self, value, weight, type):
        self.weight = weight
        self.value = value
        self.max_i = value.lenght()
        self.returnV = 0
        self.result = 0
        self.type = type

    def sum(self):
        for i in range(self.max_i):
            self.returnV += self.value[i]*self.weight[i]

    def activeFunction(self):
        if type == "Binary":
            if self.returnV > 0: self.result = 1
            else: self.result = 0
        elif type == "Sigmoid":
            self.result = 1/1+(math.e**-self.returnV)
        elif type == "Tangent":
            self.result = ((math.e**self.returnV)-(math.e**-self.returnV))/((math.e**self.returnV)+(math.e**-self.returnV))