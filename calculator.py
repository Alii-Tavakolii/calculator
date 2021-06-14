import tkinter
from tkinter import *

# ================== root sets ======================

bgcolor = 'blue'
root = Tk()
root.geometry("200x200")
root.resizable(width=False, height=False)
root.title('Calculator')
# root.configure(bg=bgcolor)



# ================== Inputs ======================

firstInputEntry = Entry(root)
firstInputEntry.place(x=10, y=10)

secondInputEntry = Entry(root)
secondInputEntry.place(x=10, y=40)
operationInput = ""


# ================== Labels ======================

ansLabel = Label(root)
ansLabel.place(x=10, y=160)
prevLabel = Label(root)
prevLabel.place(x=10, y=140)

def setPrv():
    prevLabel.config(text=f"{firstInputEntry.get()} {operationInput} {secondInputEntry.get()}")


# ================== Calculate ======================

def calcFunc():
    global operationInput

    try:
        firstNum = int(firstInputEntry.get())
        secondNum = int(secondInputEntry.get())
        operationInput[0]
    except:
        ansLabel.config(text="Error")
        firstInputEntry.delete(0)
        secondInputEntry.delete(0)
        operationInput = ''
        return

    # print(operationInput)

    setPrv()
    if operationInput == '+':
        ansStr = firstNum + secondNum
        ansLabel.config(text=f"= {ansStr}")
        return
    if operationInput == '-':
        ansStr = firstNum - secondNum
        ansLabel.config(text=f"= {ansStr}")
        return
    if operationInput == '*':
        ansStr = firstNum * secondNum
        ansLabel.config(text=f"= {ansStr}")
        return
    if operationInput == '/':
        ansStr = firstNum / secondNum
        ansLabel.config(text=f"= {ansStr}")
        return


# ================== button ======================

calcBtn = Button(root, text="Calculate !", command= calcFunc).place(x=10, y=110)

def setInput(Inp):
    global operationInput
    operationInput = Inp
    # setPrv()
    # print("now")

plusBtn = Button(root, text='+', command= lambda: setInput('+')).place(x=10, y=70)
minusBtn = Button(root, text='-', command= lambda: setInput('-')).place(x=32, y=70)
mulBtn = Button(root, text='*', command= lambda: setInput('*')).place(x=50, y=70)
divBtn = Button(root, text='/', command= lambda: setInput('/')).place(x=70, y=70)

root.mainloop()  # view the window
