#Sorting Algorithms used in GUI

#HEX CODES Used:

#Yellow : #FFD300
#Blue : #104a8e
#Green : #4c602a
#Red : #800000

import time

#______________________________________________BUBBLE SORT_____________________________________________
def bubble_sort(data, drawGraph, sim_speed):
    for _ in range(len(data)-1):
        flag = 0
        for j in range(len(data)-1-_):
            drawGraph(data, ['#FFD300' if x == j or x == j+1 else '#4c602a' if x > len(data)-1-_ else '#800000' for x in range(len(data))])
            time.sleep(sim_speed)

            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = 1
                #swapping bars of yellow(#FFD300) color and all other are red(#800000) and sorted are Green(#4c602a)
                drawGraph(data, ['#FFD300' if x == j or x == j+1 else '#4c602a' if x > len(data)-1-_ else '#800000' for x in range(len(data))])
                time.sleep(sim_speed)
        if flag == 0:
            break

#______________________________________________INSERTION SORT__________________________________________

def insertion_sort(data, drawGraph, sim_speed):
    drawGraph(data, ['#4c602a' if x == 0 else '#800000' for x in range(len(data))])
    time.sleep(sim_speed)   
    
    for i in range(1, len(data)):
        key = data[i]
        j = i-1        

        while j>=0 and data[j] > key:
            #key represented by Blue
            drawGraph(data, ['#104a8e' if x == i else '#FFD300' if x == j else '#4c602a' if x < i else '#800000' for x in range(len(data))])
            time.sleep(sim_speed)
        
            data[j+1], data[j] = data[j], data[j+1]

            drawGraph(data, ['#104a8e' if x == i else '#FFD300' if x == j else '#4c602a' if x < i else '#800000' for x in range(len(data))])
            time.sleep(sim_speed)
        
            j -= 1

        data[j+1], key = key, data[j+1]

        drawGraph(data, ['#104a8e' if x == i else '#4c602a' if x < i else '#800000' for x in range(len(data))])
        time.sleep(sim_speed)

#______________________________________________SELECTION SORT__________________________________________
def selection_sort(data, drawGraph, sim_speed):
    for i in range(len(data)):
        #index of minimum element
        min_index = i
        drawGraph(data, ['#4c602a' if x < i else '#104a8e' if x == min_index else '#800000' for x in range(len(data))])
        time.sleep(sim_speed)
        
        for j in range(i+1, len(data)):
            
            drawGraph(data, ['#104a8e' if x == min_index else '#4c602a' if x < i else '#FFD300' if x == j  else '#800000' for x in range(len(data))])
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