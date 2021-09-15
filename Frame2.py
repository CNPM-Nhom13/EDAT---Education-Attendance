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

        imgbt = ImageTk.PhotoImage(file=os.getcwd() + r"\resource\q.png")
        bt1 = Button(
            self.__frame2,
            text="Điểm danh",
            font=("Arial", 20, "bold"),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        bt1.image_names = imgbt
        bt1.place(x=10, y=243)

        bt2 = Button(
            self.__frame2,
            text="Thông tin chi tiết",
            font=("Arial", 20, "bold"),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        bt2.image_names = imgbt
        bt2.place(x=10, y=315)

        bt3 = Button(
            self.__frame2,
            text="Sửa thông tin",
            font=("Arial", 20, "bold"),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        bt3.image_names = imgbt
        bt3.place(x=10, y=387)

        bt4 = Button(
            self.__frame2,
            text="Chương trình đào tạo",
            font=("Arial", 20, "bold"),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        bt4.image_names = imgbt
        bt4.place(x=10, y=459)

        bt5 = Button(
            self.__frame2,
            text="Comming Soon",
            font=("Arial", 20, "bold"),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        bt5.image_names = imgbt
        bt5.place(x=10, y=531)

    def pack(self):
        self.__frame2.pack(fill="both", expand=1)

    def __SignOut(self):
        self.__frame2.forget()
        self.__frame1 = Frame1.Frame1(self.__master)
        self.__frame1.pack()


# root = Tk()
# root.mainloop()
