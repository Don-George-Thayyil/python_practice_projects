from tkinter import*

root = Tk()
root.title("Calculator")


#function

def evaluate():
    process = e.get()
    ans = eval(process)
    e.delete(0,END)
    e.insert(0,ans)

def clear():
    e.delete(0, END)

def math(number):
    perm = e.get()

    if perm == "":
                 e.insert(0,number)
    else:
        e.delete(0,END)
        e.insert(0,str(perm)+str(number))
            


def addButton(don):
    direc = e.get()
    if direc == "enter number":
        e.delete(0,END)
        math(don)

    else:
        math(don)
    


#buttons and entry spaces

e = Entry(root)
e.insert(0,"enter number")

b1 = Button(root, text = "1",padx =20, pady =15,command = lambda: addButton(1))
b2 = Button(root, text = "2",padx =20, pady =15,command = lambda: addButton(2))
b3 = Button(root, text = "3",padx =20, pady =15,command = lambda: addButton(3))
b4 = Button(root, text = "4",padx =20, pady =15,command = lambda: addButton(4))
b5 = Button(root, text = "5",padx =20, pady =15,command = lambda: addButton(5))
b6 = Button(root, text = "6",padx =20, pady =15,command = lambda: addButton(6))
b7 = Button(root, text = "7",padx =20, pady =15,command = lambda: addButton(7))
b8 = Button(root, text = "8",padx =20, pady =15,command = lambda: addButton(8))
b9 = Button(root, text = "9",padx =20, pady =15,command = lambda: addButton(9))
b0 = Button(root, text = "0",padx =20, pady =15,command = lambda: addButton(0))
bAdd = Button(root, text = "+",padx =20, pady =15,command = lambda: addButton("+"))
bSub = Button(root, text = "-",padx =20, pady =15,command = lambda: addButton("-"))
bMul = Button(root, text = "*",padx =20, pady =15,command = lambda: addButton("*"))
bDiv = Button(root, text = "/",padx =20, pady =15,command = lambda: addButton("/"))
bClr = Button(root, text = "C",padx =20, pady =15,command = lambda: clear())
bEql = Button(root, text = "=",padx =75, pady =15,command = lambda: evaluate())



#packing
e.grid(row = 0, column = 0,padx = 10, pady = 10, columnspan = 3)

b1.grid(row =1, column =0)
b2.grid(row =1, column =1)
b3.grid(row =1, column =2)

b4.grid(row =2, column =0)
b5.grid(row =2, column =1)
b6.grid(row =2, column =2)

b7.grid(row =3, column =0)
b8.grid(row =3, column =1)
b9.grid(row =3, column =2)
b0.grid(row =4, column =0)

bAdd.grid(row =4, column =1)
bSub.grid(row =4, column =2)
bMul.grid(row =5, column =0)
bDiv.grid(row =5, column =1)
bClr.grid(row =5, column =2)
bEql.grid(row =6, column =0, columnspan = 3)
