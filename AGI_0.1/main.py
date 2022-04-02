#concept:
#network is randomly generated
#evolver attempts to alter the network that minimizes its cost
#best eveolver is picked, ideally from multiple iterations
#this is just a concept, im probably gonna write the actual thing in a lower level lang, and use hw accel.


#one step towards agi..
import math



from multiprocessing import connection
import evolver
import network



def main():
    width = 32
    neurons = 128
    inputs = 2
    hiddens = 124
    outputs = 2
    #connections = neurons - inputs
    connections = 10
    network0 = network.Network(neurons, connections, inputs, hiddens, outputs, 0)
    network0.InitNetwork(1)
    #network0.saveNeurons()
    #network0.loadNeurons()
    #print(network0.neurons[1])

    iteration = 0
    network0.neurons[0].activation = 1.0
    network0.neurons[1].activation = 0.5
    network0.neurons[0].isActive = True
    network0.neurons[1].isActive = True
    while True:
        network0.neurons[0].activation = math.sin(iteration/5)
        network0.neurons[1].activation = math.cos(iteration/5)
        network0.neurons[0].isActive = True
        network0.neurons[1].isActive = True
        visualizer.PrintStates(network0, iteration, width)
        
        network0.Propagate()
        network0.SaveNeurons()
        iteration +=1
        input()


main()

  


