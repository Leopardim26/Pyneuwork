class Neuron:
    def __init__(self, weight):
        self.weight = weight
        self.en = 0
        self.out = 0

    def treinar(self):
        weight+=0.1

    def activeFunction(self, min):
        if(self.out >= min):
            return 1
        else: 
            return 0
        
    def enAdd(self, value):
        self.en = value
    
    def outAdd(self, value):
        self.out = value