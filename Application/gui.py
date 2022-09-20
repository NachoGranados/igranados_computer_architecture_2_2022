from tkinter import *
from  tkinter import ttk
import tkinter
from threading import *
from models import *

# main window
class Window(tkinter.Tk):

    def __init__(root):

        # create CPUs
        root.cpu0 = CPU(0)
        root.cpu1 = CPU(1)
        root.cpu2 = CPU(2)
        root.cpu3 = CPU(3)

        # create CPUs array
        root.cpuArray = [root.cpu0, root.cpu1, root.cpu2, root.cpu3]

        # create main memory
        root.mainMemory = MainMemory()

        # create bus
        root.bus = Bus(root.cpuArray, root.mainMemory)

        tkinter.Tk.__init__(root)

        # window title
        root.title("Proyecto 1")
        
        # size
        root.geometry("1150x600")

        # disable resizing
        root.resizable(False,False)

        # title
        root.title = Label(root, text = "Modelo de Protocolo para Coherencia de Caché en Sistemas Multiprocesador", fg = '#4285f4', font = ("Italic", 25))
        root.title.place(x = 20, y = 27)

        # Create an instance of Style widget
        style = ttk.Style()
        style.theme_use("clam")

        # cpu tittle frame
        cpuTittleFrame = Frame(root)
        cpuTittleFrame.place(anchor = "center", relx = 0.5, rely = 0.189)

        # cpu tittle column
        cpuTittleColumn = ("Tittle")

        # treeview cpu0 title
        cpuTittleFrame.cpu0Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu0Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu0Title.column("Tittle", anchor = CENTER, width = 260, stretch = NO)

        cpuTittleFrame.cpu0Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu0Title.heading("Tittle", text = "N0", anchor = W)

        cpuTittleFrame.cpu0Title.pack(padx = 10, pady = 0, side = LEFT)

        # treeview cpu1 title
        cpuTittleFrame.cpu1Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu1Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu1Title.column("Tittle", anchor = CENTER, width = 260, stretch = NO)

        cpuTittleFrame.cpu1Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu1Title.heading("Tittle", text = "N1", anchor = W)

        cpuTittleFrame.cpu1Title.pack(padx = 10, pady = 0, side = LEFT)

        # treeview cpu2 title
        cpuTittleFrame.cpu2Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu2Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu2Title.column("Tittle", anchor = CENTER, width = 260, stretch = NO)

        cpuTittleFrame.cpu2Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu2Title.heading("Tittle", text = "N2", anchor = W)

        cpuTittleFrame.cpu2Title.pack(padx = 10, pady = 0, side = LEFT)

        # treeview cpu3 title
        cpuTittleFrame.cpu3Title = ttk.Treeview(cpuTittleFrame, columns = cpuTittleColumn, show = "headings", height = 0, selectmode = "none")

        cpuTittleFrame.cpu3Title.column("#0", width = 0, stretch = NO)
        cpuTittleFrame.cpu3Title.column("Tittle", anchor = CENTER, width = 260, stretch = NO)

        cpuTittleFrame.cpu3Title.heading("#0", text = "", anchor = CENTER)
        cpuTittleFrame.cpu3Title.heading("Tittle", text = "N3", anchor = W)

        cpuTittleFrame.cpu3Title.pack(padx = 10, pady = 0, side = LEFT)

        controller0 = root.cpu0.getController()
        cache0 = controller0.getCache()
        blocks0 = cache0.getBlocks()

        values0 = []

        for block in blocks0:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = block.getMemoryDirection()
            value = block.getValue()

            item = (number, state, memoryDirection, value)

            values0.append(item)

        # cpu frame
        cpuFrame = Frame(root)
        cpuFrame.place(anchor='center', relx = 0.5, rely = 0.3)

        # cpu columns
        cpuColumns = ("Block", "State", "Direction", "Value")

        # treeview cpu0
        cpuFrame.cpu0Treeview = ttk.Treeview(cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        cpuFrame.cpu0Treeview.column("#0", width = 0, stretch = NO)
        cpuFrame.cpu0Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu0Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu0Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        cpuFrame.cpu0Treeview.column("Value", anchor = CENTER, width = 80, stretch = NO)

        cpuFrame.cpu0Treeview.heading("#0", text = "", anchor = CENTER)
        cpuFrame.cpu0Treeview.heading("Block", text = "Block", anchor = CENTER)
        cpuFrame.cpu0Treeview.heading("State", text = "State", anchor = CENTER)
        cpuFrame.cpu0Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        cpuFrame.cpu0Treeview.heading("Value", text = "Value", anchor = CENTER)

        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values0[0])
        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values0[1])
        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values0[2])
        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values0[3])

        cpuFrame.cpu0Treeview.pack(padx = 10, pady = 0, side = LEFT)

        controller1 = root.cpu1.getController()
        cache1 = controller1.getCache()
        blocks1 = cache1.getBlocks()

        values1 = []

        for block in blocks1:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = block.getMemoryDirection()
            value = block.getValue()

            item = (number, state, memoryDirection, value)

            values1.append(item)

        # treeview cpu1
        cpuFrame.cpu1Treeview = ttk.Treeview(cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        cpuFrame.cpu1Treeview.column("#0", width = 0, stretch = NO)
        cpuFrame.cpu1Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu1Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu1Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        cpuFrame.cpu1Treeview.column("Value", anchor = CENTER, width = 80, stretch = NO)

        cpuFrame.cpu1Treeview.heading("#0", text = "", anchor = CENTER)
        cpuFrame.cpu1Treeview.heading("Block", text = "Block", anchor = CENTER)
        cpuFrame.cpu1Treeview.heading("State", text = "State", anchor = CENTER)
        cpuFrame.cpu1Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        cpuFrame.cpu1Treeview.heading("Value", text = "Value", anchor = CENTER)

        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values1[0])
        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values1[1])
        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values1[2])
        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values1[3])

        cpuFrame.cpu1Treeview.pack(padx = 10, pady = 0, side = LEFT)

        controller2 = root.cpu2.getController()
        cache2 = controller2.getCache()
        blocks2 = cache2.getBlocks()

        values2 = []

        for block in blocks2:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = block.getMemoryDirection()
            value = block.getValue()

            item = (number, state, memoryDirection, value)

            values2.append(item)

        # treeview cpu2
        cpuFrame.cpu2Treeview = ttk.Treeview(cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        cpuFrame.cpu2Treeview.column("#0", width = 0, stretch = NO)
        cpuFrame.cpu2Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu2Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu2Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        cpuFrame.cpu2Treeview.column("Value", anchor = CENTER, width = 80, stretch = NO)

        cpuFrame.cpu2Treeview.heading("#0", text = "", anchor = CENTER)
        cpuFrame.cpu2Treeview.heading("Block", text = "Block", anchor = CENTER)
        cpuFrame.cpu2Treeview.heading("State", text = "State", anchor = CENTER)
        cpuFrame.cpu2Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        cpuFrame.cpu2Treeview.heading("Value", text = "Value", anchor = CENTER)

        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values2[0])
        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values2[1])
        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values2[2])
        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values2[3])

        cpuFrame.cpu2Treeview.pack(padx = 10, pady = 0, side = LEFT)

        controller3 = root.cpu3.getController()
        cache3 = controller3.getCache()
        blocks3 = cache3.getBlocks()

        values3 = []

        for block in blocks3:
            number = "B" + str(block.getNumber())
            state = block.getState()
            memoryDirection = block.getMemoryDirection()
            value = block.getValue()

            item = (number, state, memoryDirection, value)

            values3.append(item)

        # treeview cpu3
        cpuFrame.cpu3Treeview = ttk.Treeview(cpuFrame, columns = cpuColumns, show = "headings", height = 4, selectmode = "none")

        cpuFrame.cpu3Treeview.column("#0", width = 0, stretch = NO)
        cpuFrame.cpu3Treeview.column("Block", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu3Treeview.column("State", anchor = CENTER, width = 50, stretch = NO)
        cpuFrame.cpu3Treeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        cpuFrame.cpu3Treeview.column("Value", anchor = CENTER, width = 80, stretch = NO)

        cpuFrame.cpu3Treeview.heading("#0", text = "", anchor = CENTER)
        cpuFrame.cpu3Treeview.heading("Block", text = "Block", anchor = CENTER)
        cpuFrame.cpu3Treeview.heading("State", text = "State", anchor = CENTER)
        cpuFrame.cpu3Treeview.heading("Direction", text = "Direction", anchor = CENTER)
        cpuFrame.cpu3Treeview.heading("Value", text = "Value", anchor = CENTER)

        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = values3[0])
        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = values3[1])
        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = values3[2])
        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = values3[3])

        cpuFrame.cpu3Treeview.pack(padx = 10, pady = 0, side = LEFT)

        # bus frame
        busFrame = Frame(root)
        busFrame.place(anchor = "center", relx = 0.5, rely = 0.48)

        busColumns = ("Bus")

        # treeview main memory
        busFrame.busTreeview = ttk.Treeview(busFrame, columns = busColumns, show = "headings", height = 2, selectmode = "none")

        busFrame.busTreeview.column("#0", width = 0, stretch = NO)
        busFrame.busTreeview.column("Bus", anchor = CENTER, width = 1112, stretch = NO)

        busFrame.busTreeview.heading("#0", text = "", anchor = CENTER)
        busFrame.busTreeview.heading("Bus", text = "", anchor = CENTER)

        busFrame.busTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("Bus"))

        busFrame.busTreeview.pack(padx = 0, pady = 0, side = BOTTOM)

        # main memory frame
        mainMemoryFrame = Frame(root)
        mainMemoryFrame.place(anchor = "center", relx = 0.5, rely = 0.73)

        mainMemoryColumns = ("Direction", "Value")

        dictionary = root.mainMemory.getDictionary()

        keys = dictionary.keys()

        keyArray = []

        for key in keys:
            keyArray.append(key)

        # treeview main memory
        mainMemoryFrame.mainMemoryTreeview = ttk.Treeview(mainMemoryFrame, columns = mainMemoryColumns, show = "headings", height = 8, selectmode = "none")

        mainMemoryFrame.mainMemoryTreeview.column("#0", width = 0, stretch = NO)
        mainMemoryFrame.mainMemoryTreeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        mainMemoryFrame.mainMemoryTreeview.column("Value", anchor = CENTER, width = 80, stretch = NO)

        mainMemoryFrame.mainMemoryTreeview.heading("#0", text = "", anchor = CENTER)
        mainMemoryFrame.mainMemoryTreeview.heading("Direction", text = "Direction", anchor = CENTER)
        mainMemoryFrame.mainMemoryTreeview.heading("Value", text = "Value", anchor = CENTER)

        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = (keyArray[0], dictionary[keyArray[0]]))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 1, text = "", values = (keyArray[1], dictionary[keyArray[1]]))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 2, text = "", values = (keyArray[2], dictionary[keyArray[2]]))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 3, text = "", values = (keyArray[3], dictionary[keyArray[3]]))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 4, text = "", values = (keyArray[4], dictionary[keyArray[4]]))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 5, text = "", values = (keyArray[5], dictionary[keyArray[5]]))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 6, text = "", values = (keyArray[6], dictionary[keyArray[6]]))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 7, text = "", values = (keyArray[7], dictionary[keyArray[7]]))

        mainMemoryFrame.mainMemoryTreeview.pack(side = BOTTOM)

        # instruction frame
        instructionFrame = Frame(root)
        instructionFrame.place(anchor = "center", relx = 0.168, rely = 0.75)

        instructionColumns = ("CPU", "Instruction", "Read Miss", "Write Miss")

        # treeview main memory
        instructionFrame.instructionTreeview = ttk.Treeview(instructionFrame, columns = instructionColumns, show = "headings", height = 4, selectmode = "none")

        instructionFrame.instructionTreeview.column("#0", width = 0, stretch = NO)
        instructionFrame.instructionTreeview.column("CPU", anchor = CENTER, width = 40, stretch = NO)
        instructionFrame.instructionTreeview.column("Instruction", anchor = CENTER, width = 150, stretch = NO)
        instructionFrame.instructionTreeview.column("Read Miss", anchor = CENTER, width = 80, stretch = NO)
        instructionFrame.instructionTreeview.column("Write Miss", anchor = CENTER, width = 80, stretch = NO)

        instructionFrame.instructionTreeview.heading("#0", text = "", anchor = CENTER)
        instructionFrame.instructionTreeview.heading("CPU", text = "CPU", anchor = CENTER)
        instructionFrame.instructionTreeview.heading("Instruction", text = "Instruction", anchor = CENTER)
        instructionFrame.instructionTreeview.heading("Read Miss", text = "Read Miss", anchor = CENTER)
        instructionFrame.instructionTreeview.heading("Write Miss", text = "Write Miss", anchor = CENTER)

        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("N0", None, "0", "0"))
        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("N1", None, "0", "0"))
        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("N2", None, "0", "0"))
        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("N3", None, "0", "0"))

        instructionFrame.instructionTreeview.pack(side = LEFT)

        # button frame
        buttonFrame = Frame(root)
        buttonFrame.place(anchor = "center", relx = 0.7985, rely = 0.687)

        # step by step button
        buttonFrame.stepByStepButton = Button(buttonFrame, text = "Step by Step", activebackground = "#FF8000", fg = "white", bg = "#4285f4", font = ("Italic", 13), width = 10, heigh = 1, command = root.stepByStep)
        buttonFrame.stepByStepButton.pack(padx = 10, pady = 0, side = LEFT)

        # continuos execution button
        buttonFrame.continuosExecutionButton = Button(buttonFrame, text = "Continuos Execution", activebackground = "#FF8000", fg = "white", bg = "#4285f4", font = ("Italic", 13), width = 20, heigh = 1, command = root.continuosExecution)
        buttonFrame.continuosExecutionButton.pack(padx = 10, pady = 0, side = LEFT)

        # pause button
        buttonFrame.pauseButton = Button(buttonFrame, text = "Pause", activebackground = "#FF8000", fg = "white", bg = "#4285f4", font = ("Italic", 13), width = 10, heigh = 1, command = root.pause)
        buttonFrame.pauseButton.pack(padx = 10, pady = 0, side = LEFT)

        # insert instruction tittle frame
        insertInstructionTittleFrame = Frame(root)
        insertInstructionTittleFrame.place(anchor = "center", relx = 0.795, rely = 0.8)

        # CPU label
        insertInstructionTittleFrame.cpuLabel = Label(insertInstructionTittleFrame, text = "CPU\n(number)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.cpuLabel.pack(padx = 10, pady = 0, side = LEFT)
        
        # instruction label
        insertInstructionTittleFrame.instructionLabel = Label(insertInstructionTittleFrame, text = " Instruction\n (capital)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.instructionLabel.pack(padx = 10, pady = 0, side = LEFT)

        # direction label
        insertInstructionTittleFrame.directionLabel = Label(insertInstructionTittleFrame, text = "  Direction\n  (bin)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.directionLabel.pack(padx = 10, pady = 0, side = LEFT)

        # value label
        insertInstructionTittleFrame.valueLabel = Label(insertInstructionTittleFrame, text = "     Value\n     (hex)", fg =  "#4285f4", font = ("Italic", 14))
        insertInstructionTittleFrame.valueLabel.pack(padx = 10, pady = 0, side = LEFT)

        # insert instruction frame
        insertInstructionFrame = Frame(root)
        insertInstructionFrame.place(anchor = "center", relx = 0.79999, rely = 0.865)

        # CPU textBox
        insertInstructionFrame.CpuTextBox = Entry(insertInstructionFrame, width = 10, font = ("Italic", 13))
        insertInstructionFrame.CpuTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # instruction textBox
        insertInstructionFrame.instructionTextBox = Entry(insertInstructionFrame, width = 10, font = ("Italic", 13))
        insertInstructionFrame.instructionTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # direction textBox
        insertInstructionFrame.directionTextBox = Entry(insertInstructionFrame, width = 10, font = ("Italic", 13))
        insertInstructionFrame.directionTextBox.pack(padx = 10, pady = 0, side = LEFT)

        # value textBox
        insertInstructionFrame.valueTextBox = Entry(insertInstructionFrame, width = 10, font = ("Italic", 13))
        insertInstructionFrame.valueTextBox.pack(padx = 10, pady = 0, side = LEFT)

        
        

        

        






















    def stepByStep(root):
        pass

    def continuosExecution(root):
        pass

    def pause(root):
        pass

    def edit(root):
        
        #selected_item = root.cpu0Treeview.focus()

        selected_item0 = root.cpuFrame.cpu0Treeview.item(0)
        selected_item1 = root.cpuFrame.cpu0Treeview.item(1)
        selected_item2 = root.cpuFrame.cpu0Treeview.item(2)
        selected_item3 = root.cpuFrame.cpu0Treeview.item(3)

        #print(selected_item)
        print(selected_item0)
        print(selected_item1)
        print(selected_item2)
        print(selected_item3)

        root.cpuFrame.cpu0Treeview.item(0, text="", values=("1", "2", "3", "4"))





"""
# create CPUs
cpu0 = CPU(0)
cpu1 = CPU(1)
cpu2 = CPU(2)
cpu3 = CPU(3)

# create CPUs array
cpuArray = [cpu0, cpu1, cpu2, cpu3]

# create main memory
mainMemory = MainMemory()

# create bus
bus = Bus(cpuArray, mainMemory)

# create threads
thread0 = Thread(target = cpu0.threadFunction, args=(bus,))
thread1 = Thread(target = cpu1.threadFunction, args=(bus,))
thread2 = Thread(target = cpu2.threadFunction, args=(bus,))
thread3 = Thread(target = cpu3.threadFunction, args=(bus,))

# start threads
thread0.start()
thread1.start()
thread2.start()
thread3.start()

# wait until threads are completely executed
thread0.join()
thread1.join()
thread2.join()
thread3.join()
"""

# window loop
Window().mainloop()

