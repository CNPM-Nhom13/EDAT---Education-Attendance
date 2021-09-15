from tkinter import Frame, Tk, Button, Label, Entry
from PIL import ImageTk
import os, Frame1


class Frame2:
    def __init__(self, master):
        self.__master = master
        self.__frame2 = Frame(master)
        self.__config()

    def forget(self):
        self.__frame2.forget()

    def __config(self):
        img = ImageTk.PhotoImage(
            file=os.path.join(os.getcwd(), r"resource\bgframe2.png")
        )
        bg = Label(self.__frame2, image=img)
        bg.image_names = img
        bg.place(x=-2, y=0)

        Button(
            self.__frame2,
            text="Đăng xuất",
            fg="red",
            font=("Arial", 15, "bold"),
            width=10,
            command=self.__SignOut,
        ).place(x=10, y=187)

    def pack(self):
        self.__frame2.pack(fill="both", expand=1)

    def __SignOut(self):
        self.__frame2.forget()
        self.__frame1 = Frame1.Frame1(self.__master)
        self.__frame1.pack()


# root = Tk()
# root.mainloop()
