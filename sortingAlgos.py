#Sorting Algorithms used in GUI
import time

#______________________________________________BUBBLE SORT_____________________________________________
def bubble_sort(data, drawGraph, sim_speed):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                #swapping bars of green(#4c602a) color and all other are red(#800000)
                drawGraph(data, ['#4c602a' if x == j or x == j+1 else '#800000' for x in range(len(data))])
                time.sleep(sim_speed)


#______________________________________________INSERTION SORT__________________________________________
def insertion_sort(data, drawGraph, sim_speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            drawGraph(data, ['#4c602a' if x == j or x == j+1 else '#800000' for x in range(len(data))])
            time.sleep(sim_speed)
            j -= 1
        data[j+1] = key

#______________________________________________SELECTION SORT__________________________________________
def selection_sort(data, drawGraph, sim_speed):
    for i in range(len(data)):
        #index of minimum element
        min_index = i
        drawGraph(data, ['#4c602a' if x < i else '#104a8e' if x == min_index else '#800000' for x in range(len(data))])
        time.sleep(sim_speed)
        
        for j in range(i+1, len(data)):
            
            drawGraph(data, ['#104a8e' if x == min_index else '#4c602a' if x == j or x < i else '#800000' for x in range(len(data))])
            time.sleep(sim_speed)
            
            if data[min_index] > data[j]:
                
                drawGraph(data, ['#104a8e' if x == min_index or x == j else '#4c602a' if x < i else '#800000' for x in range(len(data))])
                time.sleep(sim_speed)
                
                min_index = j
                
                drawGraph(data, ['#104a8e' if x == min_index else '#4c602a' if x < i  else '#800000' for x in range(len(data))])
                time.sleep(sim_speed)
        
        #minimum element to left
        data[i], data[min_index] = data[min_index], data[i]
        
        drawGraph(data, ['#4c602a' if x < i else '#104a8e' if x == min_index or x == i else '#800000' for x in range(len(data))])
        time.sleep(sim_speed)
#_________________________________________________________________________________________________________