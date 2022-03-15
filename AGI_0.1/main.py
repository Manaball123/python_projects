#concept:
#network is randomly generated
#evolver attempts to alter the network that minimizes its cost
#best eveolver is picked, ideally from multiple iterations
#this is just a concept, im probably gonna write the actual thing in a lower level lang, and use hw accel.


#one step towards agi..


import evolver
import network
import visualizer

def main():
    width = 32
    neurons = 400
    inputs = 2
    hiddens = 396
    outputs = 2
    network0 = network.Network(neurons, neurons - 3, inputs, hiddens, outputs, 0)
    network0.InitNetwork(0.1)
    #network0.saveNeurons()
    #network0.loadNeurons()
    #print(network0.neurons[1])
    iteration = 0
    network0.neurons[0].activation = 1.0
    network0.neurons[1].activation = 0.5
    network0.neurons[0].isActive = True
    network0.neurons[1].isActive = True
    while True:
        visualizer.PrintStates(network0, iteration, width)
        network0.Propagate()
        iteration +=1
        input()


main()

