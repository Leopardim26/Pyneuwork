from neural import Neuron

nw = Neuron(1)

nw.enAdd(int(input()))
nw.outAdd(nw.en*1/4)
print(nw.activeFunction(1))
