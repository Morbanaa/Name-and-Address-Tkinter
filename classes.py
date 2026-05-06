# Teddy Rodd
# Morbanaa Studios
# Name and Address

from tkinter import *

class My_Gui:
    width = 800
    height = 400
    def __init__(self):
        
        # Window Set Up
        self.window = Tk()
        self.window.title("Name and Address Program")
        self.window.geometry(f"{self.width}x{self.height}")
        self.icon = PhotoImage(file="M.png")
        self.window.iconphoto(True,self.icon)
        self.window.config(background="grey")

        # Labels
        self.label = Label(self.window,text="") # Starts Empty
        self.label.pack()

        # Show Info Button
        self.button_info = Button(self.window,
                             text="Show Info",
                             command=self.show_info,
                             font=('arial',50))
        self.button_info.place(x=50,y=self.height-200)

        # Exit Button
        self.button_info = Button(self.window,
                            text="Exit",
                            command=self.window.destroy,
                            font=('arial',50))
        self.button_info.place(x=self.width-200,y=self.height-200)

        self.window.mainloop()

    def show_info(self):
        self.label.config(text="Teddy Rodd\n408 West Jefferson Ave\nWheaton Il 60187")
