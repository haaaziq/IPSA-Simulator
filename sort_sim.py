from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random

root = Tk()
root.title('IPSA Simulator')
root.iconbitmap('3.ico')
root.configure(background = 'black')
root.minsize(240,200)
root.maxsize(250,200)

#Variables
Algorithm_selected_var = StringVar()

#Title 
title = Label(root, text="IPSA SIMULATOR", fg='white', bg='black', font=('Times', '18', "underline"))
title.grid(row=0, column=0, pady=15, columnspan=3)

#-------------------------------------------TOP MAIN UI----------------------------------------------------
#MAIN UI Function

def open_mainUI():
    #DEFINE Toplevel()
    top = Toplevel()
    top.title("IPSA Simulator")
    top.iconbitmap('3.ico')
    top.minsize(400,300)
    # top.maxsize(520,450)
    top.configure(background='#444')
    
    #top frame
    top_UI_frame = Frame(top, width=500, height=150, bg='#333')
    top_UI_frame.grid(row=0, column=0)

    #FUNCTIONS
    def drawGraph(data):
        #delete previous data if present
        canvas.delete('all')
        canvasHeight = 300
        canvasWidth = 500
        #width of bar graphs to be generated
        barGraphWidth = canvasWidth / (len(data) + 1)
        #bar graph should not start at border
        offset = 30
        #spacing b/w bars
        spacing = 10
        #Normalizing size of bar graph
        normalizedData = [ i/max(data) for i in data]
        #iterating through the data
        for i, heightBar in enumerate(normalizedData):
            #coords for creating BarGraph
            #topLeft coords
            x1 = offset + i*barGraphWidth + spacing
            y1 = canvasHeight - heightBar*250
            #bottomRight coords
            x2 = (i+1)*barGraphWidth + offset
            y2 = canvasHeight

            canvas.create_rectangle(x1, y1, x2, y2, fill='#800000')
            #number written over the Bar Graph
            canvas.create_text(x1, y1, anchor=SW, text=str(data[i]))

    def simulate():
        # data = [10, 3, 12, 6, 1, 13, 15, 20]
        #Importing values from Entry Boxes
        size = int(sizeInput.get())
        minVal = int(minValue.get())
        maxVal = int(maxValue.get())

        if minVal > maxVal:
            minVal, maxVal = maxVal, minVal

        if minVal < 0:
            minVal = 0

        if maxVal > 100:
            maxVal = 100

        if size  > 15:
            size = 15

        if size  < 3:
            size = 5

        createdData = []
        #creating random data of given size
        for i in range(0, size):
            createdData.append(random.randrange(minVal, maxVal+1))

        drawGraph(createdData)

    #Row[0] on top_UI_frame --> Row[0] on Top Level
    Label(top_UI_frame, text='Size: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=0, column=0, padx=10, pady=10, sticky=W)
    sizeInput = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    sizeInput.grid(row=0, column=1, padx=10, pady=10, sticky=W)

    Label(top_UI_frame, text='Min. Value: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=0, column=2, padx=10, pady=10, sticky=W)
    minValue = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    minValue.grid(row=0, column=3, padx=10, pady=10, sticky=W)

    Label(top_UI_frame, text='Max. Value: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=0, column=4, padx=10, pady=10, sticky=W)
    maxValue = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    maxValue.grid(row=0, column=5, padx=10, pady=10, sticky=W)
    
    # #Row[1] on top_UI_frame
    # Label(top_UI_frame, text='Enter Data: ', bg='#333', fg='#fff', font=('Helvetica', '10', 'bold')).grid(row=1, column=0, padx=10, pady=10, sticky=W)
    # enterData = Entry(top_UI_frame, width=10, font=('Helvetica', '10', 'bold'))
    # enterData.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    #Row[1] on top_UI_frame
    Button(top_UI_frame, text="START Simulation", font=('Helvetica', '8', 'bold'), command=simulate, bg='#800000', fg='#fff').grid(row=1, column=0, pady=10, sticky=W+E, columnspan=6)


    #Row[1]
    #CANVAS on Toplevel
    canvas = Canvas(top, width=500, height=300, bg='white')
    canvas.grid(row=1, column=0, padx=10, pady=5)
    
    #Row[3] Close Button
    close_top_btn = Button(top, text="CLOSE", font=('Helvetica', '8', 'bold'), command=top.destroy)
    close_top_btn.grid(row=2, column=0, pady=10, sticky=W+E)

#----------------------------------------------------------------------------------------------------------------------

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

#Select Button
select_btn = Button(Initial_UI_frame, text="Select", command=open_mainUI)
select_btn.grid(row=2, column=0, pady=10, columnspan=3, sticky=W+E)


root.mainloop()