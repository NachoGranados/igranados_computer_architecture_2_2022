from tkinter import *
from  tkinter import ttk
import tkinter











# main window
class Window(tkinter.Tk):

    def __init__(root):

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

        # cpu frame
        cpuFrame = Frame(root)
        cpuFrame.place(anchor='center', relx=0.5, rely=0.3)

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

        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("B0", "S", "0b000", "0x0a"))
        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("B1", "S", "0b110", "0x22"))
        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("B2", "M", "0b101", "0x08"))
        cpuFrame.cpu0Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("B3", "M", "0b011", "0x1e"))

        cpuFrame.cpu0Treeview.pack(padx = 10, pady = 0, side = LEFT)

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

        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("B0", "I", "0b000", "0x1e"))
        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("B1", "I", "0b010", "0x22"))
        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("B2", "I", "0b011", "0x12"))
        cpuFrame.cpu1Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("B3", "S", "0b111", "0x26"))

        cpuFrame.cpu1Treeview.pack(padx = 10, pady = 0, side = LEFT)

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

        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("B0", "M", "0b010", "0xc8"))
        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("B1", "S", "0b110", "0x22"))
        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("B2", "I", "0b111", "0x6c"))
        cpuFrame.cpu2Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("B3", "I", "0b011", "0x1c"))

        cpuFrame.cpu2Treeview.pack(padx = 10, pady = 0, side = LEFT)

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

        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("B0", "I", "0b110", "0x0a"))
        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("B1", "M", "0b011", "0x08"))
        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("B2", "S", "0b100", "0x1c"))
        cpuFrame.cpu3Treeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("B3", "M", "0b001", "0x2c"))

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

        # treeview main memory
        mainMemoryFrame.mainMemoryTreeview = ttk.Treeview(mainMemoryFrame, columns = mainMemoryColumns, show = "headings", height = 8, selectmode = "none")

        mainMemoryFrame.mainMemoryTreeview.column("#0", width = 0, stretch = NO)
        mainMemoryFrame.mainMemoryTreeview.column("Direction", anchor = CENTER, width = 80, stretch = NO)
        mainMemoryFrame.mainMemoryTreeview.column("Value", anchor = CENTER, width = 80, stretch = NO)

        mainMemoryFrame.mainMemoryTreeview.heading("#0", text = "", anchor = CENTER)
        mainMemoryFrame.mainMemoryTreeview.heading("Direction", text = "Direction", anchor = CENTER)
        mainMemoryFrame.mainMemoryTreeview.heading("Value", text = "Value", anchor = CENTER)

        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("0b000", "0x0a"))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("0b001", "0x22"))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("0b010", "0x08"))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("0b011", "0x1c"))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 4, text = "", values = ("0b100", "0x08"))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 5, text = "", values = ("0b101", "0x22"))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 6, text = "", values = ("0b110", "0x22"))
        mainMemoryFrame.mainMemoryTreeview.insert(parent = "", index = "end", iid = 7, text = "", values = ("0b111", "0x26"))

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

        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 0, text = "", values = ("N0", "WRITE 0b0000; 0x0000", "0", "0"))
        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 1, text = "", values = ("N1", "WRITE 0b0001; 0x0001", "0", "0"))
        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 2, text = "", values = ("N2", "WRITE 0b0010; 0x0010", "0", "0"))
        instructionFrame.instructionTreeview.insert(parent = "", index = "end", iid = 3, text = "", values = ("N3", "WRITE 0b0011; 0x0011", "0", "0"))

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




        #Button
        #root.buttonEdit= Button(root, text="Ingresar", activebackground="#4285f4", fg = "white", bg = "#db4437", font = ("Serif", 13), width=20, heigh=3, command=root.edit)
        #root.buttonEdit.place(x=300, y=700)

    def edit(root):
        
        #selected_item = root.cpu0Treeview.focus()

        selected_item0 = root.cpu0Treeview.item(0)
        #selected_item1 = root.cpu0Treeview.item(1)
        #selected_item2 = root.cpu0Treeview.item(2)
        #selected_item3 = root.cpu0Treeview.item(3)

        #print(selected_item)
        print(selected_item0)
        #print(selected_item1)
        #print(selected_item2)
        #print(selected_item3)

        #root.cpu0Treeview.index(0)

        root.cpu0Treeview.item(0, text="", values=("1", "2", "3", "4"))



#Ventana Calculadora
class calculadora(tkinter.Tk):
    def __init__(self):
        global nombre
        tkinter.Tk.__init__(self)
        self.title("Cálculos")
        self.geometry("650x300")

        #Label
        self.nombre= Label(self, text= "Hola "+ nombre, fg =  "#4285f4", font = ("Serif", 18))
        self.nombre.place(x=250, y= 5)

        self.labelFibonacci= Label(self, text= "Fibonacci: ", fg =  "#4285f4", font = ("Serif", 14))
        self.labelFibonacci.place(x=100, y= 50)

        self.labelFactorial= Label(self, text= "Factorial: ", fg =  "#4285f4", font = ("Serif", 14))
        self.labelFactorial.place(x=100, y= 100)

        self.labelRaizCuadrada= Label(self, text= "Raiz Cuadrada: ", fg =  "#4285f4", font = ("Serif", 14))
        self.labelRaizCuadrada.place(x=100, y= 150)

        #TextBox
        self.textBoxFibonacci = Entry(self, width=7, font = ("Serif", 13))
        self.textBoxFibonacci.place(x=250, y= 50)

        self.textBoxFactorial = Entry(self, width=7, font = ("Serif", 13))
        self.textBoxFactorial.place(x=250, y= 100)

        self.textBoxRaizCuadrada= Entry(self, width=7, font = ("Serif", 13))
        self.textBoxRaizCuadrada.place(x=250, y= 150)

        self.textBoxFibonacciResult = Entry(self, width=12, font = ("Serif", 13))
        self.textBoxFibonacciResult.place(x=450, y= 50)

        self.textBoxFactorialResult = Entry(self, width=12, font = ("Serif", 13))
        self.textBoxFactorialResult.place(x=450, y= 100)

        self.textBoxRaizCuadradaResult = Entry(self, width=12, font = ("Serif", 13))
        self.textBoxRaizCuadradaResult.place(x=450, y= 150)

        #Button
        self.buttonFibonacci= Button(self, text="Calcular",width=7, activebackground="#4285f4",command= self.displayFibonacci, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.buttonFibonacci.place(x=350, y=50)

        self.buttonFactorial= Button(self, text="Calcular",width=7, activebackground="#4285f4",command= self.displayFactorial, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.buttonFactorial.place(x=350, y=100)

        self.buttonRaizCuadrado= Button(self, text="Calcular",width=7, activebackground="#4285f4",command= self.displayRaizCuadrada, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.buttonRaizCuadrado.place(x=350, y=150)

        self.buttonSalir= Button(self, text="Salir",width=7, activebackground="#4285f4",command= self.salir, fg = "white", bg = "#db4437", font = ("Serif", 13))
        self.buttonSalir.place(x=300, y=250)

    def displayFibonacci(self):
        #Obtener el texto
        entry = self.textBoxFibonacci.get()
        #Convertir el texto a entero
        number = int (entry)
        #Calcular el resultado
        resultado = fibonacci(number)
        #Borrar el resultado anterior
        self.textBoxFibonacciResult.delete(0, END)
        #Insertar el resultado nuevo
        self.textBoxFibonacciResult.insert(0,resultado)

    #Similares a "displayFibonacci", pero con otras funciones
    def displayFactorial(self):
        entry = self.textBoxFactorial.get()
        number = int (entry)
        resultado = factorial(number)
        self.textBoxFactorialResult.delete(0, END)
        self.textBoxFactorialResult.insert(0,resultado)

    def displayRaizCuadrada(self):
        entry = self.textBoxRaizCuadrada.get()
        number = int (entry)
        resultado = raizCuadrada(number)
        self.textBoxRaizCuadradaResult.delete(0, END)
        self.textBoxRaizCuadradaResult.insert(0,resultado)

    #Regresar a la ventana anterior
    def salir(self):
        #Destruir esta ventana
        self.destroy()
        #Crear una nueva ventana de tipo menu
        menu().mainloop()

#Parte lógica
def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero-1)+fibonacci(numero-2)

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

def raizCuadrada(numero):
    return math.sqrt(numero)

#Nombre usado de forma global
nombre = ""
def cambiarNombre (nuevo):
    global nombre
    nombre = nuevo

#Loop de la ventana
Window().mainloop()
