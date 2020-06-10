#Sorting Algorithms used in GUI
import time

def bubble_sort(data, drawGraph, sim_speed):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                #swapping bars of green(#4c602a) color and all other are red(#800000)
                drawGraph(data, ['#4c602a' if x == j or x == j+1 else '#800000' for x in range(len(data))])
                time.sleep(sim_speed)
    drawGraph(data, ['#4c602a' for x in range(len(data))])

# data = [10, 15, 5, 33, 7, 3]
# data = bubble_sort(data)
# print(data)