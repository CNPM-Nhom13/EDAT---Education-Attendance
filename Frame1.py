from tkinter import Entry, Frame, Tk, Label, Button, Checkbutton
import os, Frame2
from tkinter.constants import LEFT, RIGHT
from PIL import Image, ImageTk


class Frame1:
    def __init__(self, master):
        self.__master = master
        self.__frame1 = Frame(master)
        self.__GUIconfig()
        self.__frame1.pack(fill="both", expand=1)

    def __GUIconfig(self):
        img = ImageTk.PhotoImage(file=os.path.join(os.getcwd(), "resource\logo1.png"))
        self.__master.title("My Profile | Thuy Loi University")
        self.__master.geometry("1000x600")
        self.__master.resizable(False, False)
        self.__frame1.config(width=1000, height=600)
        label = Label(self.__frame1, image=img)
        label.image_names = img
        label.place(x=-2, y=0)
        self.__setEntry()
        Button(
            self.__frame1,
            text="Đăng nhập",
            font=("Arial", 15, "bold"),
            fg="green",
            command=self.__SignIn,
        ).place(x=750, y=330)

        Button(
            self.__frame1,
            text="Đăng nhập bằng khuôn mặt",
            font=("Arial", 15, "bold"),
            fg="red",
            command=self.__FaceSignIn,
        ).place(x=615, y=420)

    def __setEntry(self):
        Label(self.__frame1, text="Tên đăng nhập:", font=("Arial", 15, "bold")).place(
            x=600, y=120
        )
        entry1 = Entry(self.__frame1, width=20, font=("Arial", 20), justify=RIGHT)
        entry1.place(x=600, y=150)

        Label(self.__frame1, text="Mật Khẩu:", font=("Arial", 15, "bold")).place(
            x=600, y=220
        )
        entry2 = Entry(self.__frame1, width=20, font=("Arial", 20), justify=RIGHT)
        entry2.place(x=600, y=250)

    def forget(self):
        self.__frame1.forget()

    def pack(self):
        self.__frame1.pack(fill="both", expand=1)

    def __SignIn(self):
        self.__frame1.forget()
        # self.__frame2.pack()
        self.__frame2 = Frame2.Frame2(self.__master)
        self.__frame2.pack()

    def __FaceSignIn(self):
        pass

    def __Reset(self):
        self.__frame1.destroy()


"""
root = Tk()
mg = Frame1(root)
root.mainloop()
"""