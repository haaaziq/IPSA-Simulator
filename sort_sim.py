from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
from sortingAlgos import bubble_sort, insertion_sort, selection_sort

root = Tk()
root.title('IPSA Simulator')
root.iconbitmap('3.ico')
root.configure(background = 'black')
root.minsize(307,212)
root.maxsize(320,212)

#Variables
Algorithm_selected_var = StringVar()
data = []

#Title 
title = Label(root, text="IPSA SIMULATOR", fg='white', bg='black', font=('Times', '18', "underline"))
title.grid(row=0, column=0, pady=15, columnspan=3)

#_____________________________________________TOP MAIN UI______________________________________________
#MAIN UI Function

def open_mainUI():
    #DEFINE Toplevel()
    top = Toplevel()
    top.title("IPSA Simulator")
    top.iconbitmap('3.ico')
    #Fixed window size
    top.minsize(593,492)
    # top.maxsize(595,493)
    top.configure(background='#444')

    #Disabling widgets of root UI
    select_btn.configure(state=DISABLED)
    algo_menu.configure(state=DISABLED)
    speedScale.configure(state=DISABLED)
    
    #top frame
    top_UI_frame = Frame(top, width=500, height=150, bg='#333')
    top_UI_frame.grid(row=0, column=0)

    #FUNCTIONS
    def drawGraph(data, barColor):
        #delete previous data if present
        canvas.delete('all')
        canvasHeight = 300
        canvasWidth = 500
        
        #width of bar graphs to be generated
        barGraphWidth = canvasWidth / (len(data) + 1)
        #bar graph should not start at border
        offset = 60
        #spacing b/w bars
        spacing = 10
        #Normalizing size of bar graph
        normalizedData = [ i/max(data) for i in data]

        #iterating through the data
        for i, heightBar in enumerate(normalizedData):
            #coords for creating BarGraph
            #topLeft coords
            x1 = i*barGraphWidth + offset + spacing
            y1 = canvasHeight - heightBar*250
            #bottomRight coords
            x2 = (i+1)*barGraphWidth + offset
            y2 = canvasHeight

            canvas.create_rectangle(x1, y1, x2, y2, fill=barColor[i])
            #number written over the Bar Graph
            canvas.create_text(x1, y1, anchor=SW, text=str(data[i]))

        #updating top window after drawing data after every single change
        top.update_idletasks()

    def generate():
        global data
        
        if sizeInput.get()=='' and minValue.get()=='' and maxValue.get()=='': 
            #Importing values from Input Data Entry Box
            userData = list(inputData.get().split())
            ipData = [ int(i) for i in userData]
            data = ipData

        else:
            inputData.delete(0, END)
            #Importing values from Entry Boxes
            size = int(sizeInput.get())
            minVal = int(minValue.get())
            maxVal = int(maxValue.get())

            #removing errors
            if minVal > maxVal:
                minVal, maxVal = maxVal, minVal

            if minVal < 0:
                minVal = 0

            if maxVal > 100:
                maxVal = 100

            if size  > 15:
                size = 15       #maxm 15 values only be generated randomly

            if size  < 3:
                size = 5

            createdData = []
            #creating random data of given size
            for i in range(0, size):
                createdData.append(random.randrange(minVal, maxVal+1))
            data = createdData

        #initially whole created array is red(#800000)
        drawGraph(data, ['#800000' for x in range(len(data))])

    def startAlgorithm():
        global data

        #when empty data array
        if not data:
            return

        else:
            if Algorithm_selected_var.get() == "Bubble Sort":
                bubble_sort(data, drawGraph, speedScale.get())

            elif Algorithm_selected_var.get() == "Insertion Sort":
                insertion_sort(data, drawGraph, speedScale.get())

            elif Algorithm_selected_var.get() == "Selection Sort":
                selection_sort(data, drawGraph, speedScale.get())

            drawGraph(data, ['#4c602a' for x in range(len(data))])

    def close_topUI():
        top.destroy()
        #Enabling Select button of root UI
        select_btn.configure(state=NORMAL)
        algo_menu.configure(state=NORMAL)
        speedScale.configure(state=NORMAL)


    #Row[0] on top_UI_frame --> Row[0] on Top Level
    #Size Entry
    Label(top_UI_frame, text='Size: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=0, column=0, padx=10, pady=10, sticky=W)
    sizeInput = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    sizeInput.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    #Min. Value Entry
    Label(top_UI_frame, text='Min. Value: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=0, column=2, padx=10, pady=10, sticky=W)
    minValue = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    minValue.grid(row=0, column=3, padx=10, pady=10, sticky=W)

    #Max. Value Entry
    Label(top_UI_frame, text='Max. Value: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=0, column=4, padx=10, pady=10, sticky=W)
    maxValue = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    maxValue.grid(row=0, column=5, padx=10, pady=10, sticky=W)
    
    #Row[1] on top_UI_frame
    Label(top_UI_frame, text='Input Data: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=1, column=0, padx=10, pady=10, sticky=W)
    inputData = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    inputData.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky=W+E)

    #Generate Data Button
    Button(top_UI_frame, text="Generate Data", font=('Helvetica', '8', 'bold'), command=generate, bg='#4c602a', fg='#fff').grid(row=1, column=4, pady=10, sticky=W+E, columnspan=2)

    #Row[2] on top_UI_frame
    Button(top_UI_frame, text="START Simulation", font=('Helvetica', '8', 'bold'), command=startAlgorithm, bg='#800000', fg='#fff').grid(row=2, column=0, pady=10, sticky=W+E, columnspan=6)


    #Row[1]
    #CANVAS on Toplevel
    canvas = Canvas(top, width=570, height=300, bg='white')
    canvas.grid(row=1, column=0, padx=10, pady=5)
    
    #Row[3] Close Button
    close_top_btn = Button(top, text="CLOSE", font=('Helvetica', '8', 'bold'), command=close_topUI)
    close_top_btn.grid(row=2, column=0, pady=10, sticky=W+E)

#________________________________________________________________________________________________________________________________________________________________

#INITIAL UI

Initial_UI_frame = Frame(root, width=250, height=100, bg='#333')
Initial_UI_frame.grid(row=1, column=0)

#Initial UI area
#Dropdown for selecting Algorithm

options_algo = [
    "Bubble Sort",
    "Insertion Sort",
    "Selection Sort"
]
Algorithm_selected_var.set("Bubble Sort")

#Algorithm Label
Label(Initial_UI_frame, text='Algorithm: ', bg='#333', fg='#fff', font=('Helvetica', '10', "bold")).grid(row=1, column=0, padx=10, pady=10, sticky=W)

#OptionMenu
algo_menu = OptionMenu(Initial_UI_frame, Algorithm_selected_var, *options_algo)
algo_menu.grid(row=1, column=1, padx=20, pady=10, sticky=E)

#Simulation Speed Scale
Label(Initial_UI_frame, text='Simulation Speed [s]:', bg='#333', fg='#fff', font=('Helvetica', '10', "bold")).grid(row=2, column=0, padx=10, pady=10, sticky=W)
speedScale = Scale(Initial_UI_frame, from_=0.1, to=3.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL)
speedScale.grid(row=2, column=1, padx=5, pady=5) 

#Select Button
select_btn = Button(Initial_UI_frame, text="Select", command=open_mainUI)
select_btn.grid(row=3, column=0, pady=10, columnspan=3, sticky=W+E)


root.mainloop()