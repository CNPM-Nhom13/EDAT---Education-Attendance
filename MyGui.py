from tkinter import Entry, Frame, Tk, Label, Button, Checkbutton
import os
from tkinter.constants import LEFT, RIGHT
from PIL import Image, ImageTk


class MyGui:
    def __init__(self, master):
        self.__master = master
        self.__entry1 = Entry(self.__master)
        self.__entry2 = Entry(self.__master)
        self.__GUIconfig()

    def __GUIconfig(self):
        img = ImageTk.PhotoImage(file=os.path.join(os.getcwd(), "resource\logo1.png"))
        self.__master.title("Test")
        self.__master.geometry("1000x600")
        label = Label(self.__master, image=img)
        label.image_names = img
        label.pack(side=LEFT)
        self.__setEntry()
        Button(
            self.__master,
            text="Đăng nhập",
            font=("Arial", 15, "bold"),
            fg="green",
            command=self.__SignIn,
        ).place(x=750, y=330)

        Button(
            self.__master,
            text="Đăng nhập bằng khuôn mặt",
            font=("Arial", 15, "bold"),
            fg="red",
            command=self.__FaceSignIn,
        ).place(x=615, y=420)

    def __setEntry(self):
        Label(self.__master, text="Tên đăng nhập:", font=("Arial", 15, "bold")).place(
            x=600, y=120
        )
        self.__entry1.config(width=20, font=("Arial", 20), justify=RIGHT)
        self.__entry1.place(x=600, y=150)

        Label(self.__master, text="Mật Khẩu:", font=("Arial", 15, "bold")).place(
            x=600, y=220
        )
        self.__entry2.config(width=20, font=("Arial", 20), justify=RIGHT)
        self.__entry2.place(x=600, y=250)

    def __SignIn(self):
        pass

    def __FaceSignIn(self):
        pass


root = Tk()
mg = MyGui(root)
root.mainloop()
