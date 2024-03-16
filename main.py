import tkinter as tk
from tkinter import font

root = tk.Tk()
#Tab name 
root.title("Simple Calculator")
#Entry box and w/l of Calulator
e = tk.Entry(root, width = 35, borderwidth = 5)
e.grid(row= 0, column = 0, columnspan = 3, padx =5 , pady = 10)

root.configure(bg = "gray75")

custom_font = font.Font(family="Arial", size=13, weight = "normal")
root.option_add("*Font", custom_font)
#Buttons methods
def button_click(number):
  current = e.get()
  e.delete(0,tk.END)
  e.insert(0,str(current) + str(number))
  
def button_clear():
  e.delete(0,tk.END)
  
def button_add():
  first_number = e.get()
  global fst_num
  global math 
  math = "addition"
  fst_num = int(first_number)
  e.delete(0,tk.END)
  
def button_equal():
  second_number = e.get()
  e.delete(0,tk.END)
  
  if math == "addition":
    e.insert(0,fst_num + int(second_number))
  if math == "subtraction":
    e.insert(0,fst_num - int(second_number))
  if math == "multiplication":
    e.insert(0,fst_num * int(second_number))
  if math == "division":
    e.insert(0,fst_num / int(second_number))
    
def button_subtract():
  first_number = e.get()
  global fst_num
  global math 
  math = "subtraction"
  fst_num = int(first_number)
  e.delete(0,tk.END)
  
def button_multiply():
  first_number = e.get()
  global fst_num
  global math 
  math = "multiplication"
  fst_num = int(first_number)
  e.delete(0,tk.END)
  
def button_divide():
  first_number = e.get()
  global fst_num
  global math 
  math = "division"
  fst_num = int(first_number)
  e.delete(0,tk.END)
  
#Define Buttons
button_1 = tk.Button(root, text = "1", padx = 40, pady= 20,command = lambda: button_click(1), bg = "gray65",fg = "white")
button_2 = tk.Button(root, text = "2", padx = 40, pady= 20,command=  lambda: button_click(2),bg = "gray65",fg = "white")
button_3 = tk.Button(root, text = "3", padx = 40, pady= 20,command=  lambda: button_click(3),bg = "gray65",fg = "white")
button_4 = tk.Button(root, text = "4", padx = 40, pady= 20,command=  lambda: button_click(4),bg = "gray65",fg = "white")
button_5 = tk.Button(root, text = "5", padx = 40, pady= 20,command=  lambda: button_click(5),bg = "gray65",fg = "white")
button_6 = tk.Button(root, text = "6", padx = 40, pady= 20,command=  lambda: button_click(6),bg = "gray65",fg = "white")
button_7 = tk.Button(root, text = "7", padx = 40, pady= 20,command=  lambda: button_click(7),bg = "gray65",fg = "white")
button_8 = tk.Button(root, text = "8", padx = 40, pady= 20,command=  lambda: button_click(8),bg = "gray65",fg = "white")
button_9 = tk.Button(root, text = "9", padx = 40, pady= 20,command=  lambda: button_click(9),bg = "gray65",fg = "white")
button_0 = tk.Button(root, text = "0", padx = 40, pady= 20,command=  lambda: button_click(0),bg = "gray65",fg = "white")
button_equal = tk.Button(root, text = "=", padx = 39, pady= 20,command = button_equal, bg = "orange" ,fg = "white")
button_add= tk.Button(root, text = "+", padx = 35, pady= 20,command= button_add,bg = "orange" ,fg = "white" )
button_subtract= tk.Button(root, text = "-", padx = 39, pady= 20,command= button_subtract,bg = "orange" ,fg = "white")
button_multiply= tk.Button(root, text = "x", padx = 39, pady= 20,command= button_multiply,bg = "orange" ,fg = "white")
button_divide= tk.Button(root, text = "/", padx = 40, pady= 20,command= button_divide,bg = "orange" ,fg = "white")
button_clear = tk.Button(root, text = "Clear", padx = 22, pady= 20,command= button_clear,bg = "orange" ,fg = "white")


#Buttons Figuration
button_1.grid(row= 3, column = 0)
button_2.grid(row= 3, column = 1)
button_3.grid(row= 3, column = 2)

button_4.grid(row= 2, column = 0)
button_5.grid(row= 2, column = 1)
button_6.grid(row= 2, column = 2)

button_7.grid(row=1, column = 0 )
button_8.grid(row=1, column = 1)
button_9.grid(row=1, column = 2)

button_0.grid(row= 4, column = 0 )

button_equal.grid(row=4, column = 1)
button_clear.grid(row=4,column = 2)

button_add.grid(row=4, column = 3 )
button_subtract.grid(row=3, column = 3 )
button_multiply.grid(row=2, column = 3)
button_divide.grid(row=1,column =3 )


tk.mainloop()