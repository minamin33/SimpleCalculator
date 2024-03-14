import tkinter as tk


class NumberButton:
  def __init__(self, root, value, callback):
    self.root = root
    self.value = value
    self.callback = callback
    self.button = tk.Button(self.root, text = str(self.value),
                            padx = 40, pady= 20, command = lambda: callback(self.value))


class CalculatorWindow:
  def __init__(self):
    self.root = tk.Tk()
    #Tab name 
    self.root.title("Simple Calculator")
    self.e = tk.Entry(self.root, width = 33, borderwidth = 5)
    self.e.grid(row= 0, column = 0, columnspan = 3, padx =5, pady = 10)
    self.first_number = 0
    self.operator = ""
    self.create_buttons()
    self.create_button_grid()

  def start(self):
    self.root.mainloop()

  def button_click(self, number):
    current = self.e.get()
    self.e.delete(0,tk.END)
    self.e.insert(0,str(current) + str(number))

  def button_clear(self):
    self.e.delete(0,tk.END)

  def button_add(self):
    self.first_number = int(self.e.get())
    self.operator = "addition"
    self.e.delete(0,tk.END)
    
  def button_equal(self):
    second_number = int(self.e.get())
    self.e.delete(0,tk.END)
    if self.operator == "addition":
      self.e.insert(0, self.first_number + second_number)
    elif self.operator == "subtraction":
      self.e.insert(0, self.first_number - second_number)
    elif self.operator == "multiplication":
      self.e.insert(0, self.first_number * second_number)
    elif self.operator == "division":
      self.e.insert(0, self.first_number / second_number)

  def button_subtract(self):
    self.first_number = int(self.e.get())
    self.operator = "subtraction"
    self.e.delete(0,tk.END)

  def button_multiply(self):
    self.first_number = int(self.e.get())
    self.operator = "multiplication"
    self.e.delete(0,tk.END)

  def button_divide(self):
    self.first_number = int(self.e.get())
    self.operator = "division"
    self.e.delete(0,tk.END)

  def create_buttons(self):
    self.button_1 = NumberButton(self.root, 1, self.button_click)
    self.button_2 = NumberButton(self.root, 2, self.button_click)
    self.button_3 = NumberButton(self.root, 3, self.button_click)
    self.button_4 = NumberButton(self.root, 4, self.button_click)
    self.button_5 = NumberButton(self.root, 5, self.button_click)
    self.button_6 = NumberButton(self.root, 6, self.button_click)
    self.button_7 = NumberButton(self.root, 7, self.button_click)
    self.button_8 = NumberButton(self.root, 8, self.button_click)
    self.button_9 = NumberButton(self.root, 9, self.button_click)
    self.button_0 = NumberButton(self.root, 0, self.button_click)

    self.button_equal = tk.Button(self.root, text = "=", padx = 39, pady= 20,command=  self.button_equal)
    self.button_add= tk.Button(self.root, text = "+", padx = 38, pady= 20,command= self.button_add)
    self.button_subtract= tk.Button(self.root, text = "-", padx = 40, pady= 20,command= self.button_subtract)
    self.button_multiply= tk.Button(self.root, text = "x", padx = 39, pady= 20,command= self.button_multiply)
    self.button_divide= tk.Button(self.root, text = "/", padx = 40, pady= 20,command= self.button_divide)
    self.button_clear = tk.Button(self.root, text = "Clear", padx = 29, pady= 20,command= self.button_clear)

  def create_button_grid(self):
    self.button_1.button.grid(row= 3, column = 0)
    self.button_2.button.grid(row= 3, column = 1)
    self.button_3.button.grid(row= 3, column = 2)

    self.button_4.button.grid(row= 2, column = 0)
    self.button_5.button.grid(row= 2, column = 1)
    self.button_6.button.grid(row= 2, column = 2)

    self.button_7.button.grid(row=1, column = 0 )
    self.button_8.button.grid(row=1, column = 1)
    self.button_9.button.grid(row=1, column = 2)

    self.button_0.button.grid(row= 4, column = 0 )

    self.button_equal.grid(row=4, column = 1)
    self.button_clear.grid(row=4,column = 2)

    self.button_add.grid(row=4, column = 3 )
    self.button_subtract.grid(row=3, column = 3 )
    self.button_multiply.grid(row=2, column = 3)
    self.button_divide.grid(row=1,column =3 )

