from tkinter import *
from turtle import back

class My_Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Name and Address Program")
        self.window.geometry("800x800")
        self.icon = PhotoImage(file="M.png")
        self.window.iconphoto(True,self.icon)
        self.window.config(background="grey")

        # Show Info Button
        self.button_info = Button(self.window,
                             text="Show Info",
                             command=self.show_info,
                             font=('arial',50))
        self.button_info.pack()

        # Exit Button
        self.button_info = Button(self.window,
                            text="Exit",
                            command=self.window.destroy,
                            font=('arial',50))
        self.button_info.pack()

        self.window.mainloop()

    def show_info():
        pass
