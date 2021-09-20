from tkinter import Entry, Frame, Tk, Label, Button, Checkbutton, messagebox
import os, Frame2, urllib, sqlite3
from tkinter.constants import LEFT, RIGHT
from PIL import Image, ImageTk
import urllib.request, urllib.error

MyID = None


class Frame1:
    def __init__(self, master):
        self.__master = master
        self.__frame1 = Frame(master)
        self.__GUIconfig()
        self.__frame1.pack(fill="both", expand=1)

    def __GUIconfig(self):
        img = ImageTk.PhotoImage(file=os.path.join(os.getcwd(), "resource\logo1.png"))
        self.__master.title("EDAT | Thuy Loi University")
        self.__master.geometry("1000x600")
        self.__master.resizable(False, False)
        self.__frame1.config(width=1000, height=600)
        label = Label(self.__frame1, image=img)
        label.image_names = img
        label.place(x=-2, y=0)
        etr1, etr2 = self.__setEntry()
        Button(
            self.__frame1,
            text="Đăng nhập",
            font=("Arial", 15, "bold"),
            fg="green",
            command=lambda: self.__SignIn(etr1, etr2),
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

        Label(
            self.__frame1,
            text="Mật Khẩu:",
            font=("Arial", 15, "bold"),
        ).place(x=600, y=220)
        entry2 = Entry(
            self.__frame1, width=20, font=("Arial", 20), show="*", justify=RIGHT
        )
        entry2.place(x=600, y=250)
        return entry1, entry2

    def forget(self):
        self.__frame1.forget()

    def pack(self):
        self.__frame1.pack(fill="both", expand=1)

    def __checkConnection(self):
        try:
            urllib.request.urlopen("http://www.google.com", timeout=1)
            return True
        except urllib.error.URLError as e:
            return False

    def __SignIn(self, etr1, etr2):
        if self.__checkConnection() == False:
            messagebox.showwarning("Lost Connection", "Không có kết nối mạng")
        else:
            id, pw = etr1.get(), etr2.get()
            if id == "" or pw == "":
                messagebox.showwarning(
                    "Error", "Tài khoản và mật khẩu không được để trống"
                )
            else:
                global MyID
                MyID = id
                connect = sqlite3.connect(
                    os.path.join(os.getcwd(), r"database\database.db")
                )
                cursor = connect.execute("SELECT * FROM people WHERE ID=" + str(id))
                isRecordExist = 0
                for row in cursor:
                    if str(id) == str(row[0]) and str(pw) == str(row[1]):
                        isRecordExist = 1
                if isRecordExist == 1:
                    self.__frame1.forget()
                    self.__frame2 = Frame2.Frame2(self.__master)
                    self.__frame2.pack()
                else:
                    messagebox.showwarning(
                        "Error", "Tên đăng nhập hoặc mật khẩu không đúng"
                    )
                connect.commit()
                connect.close()

    def __FaceSignIn(self):
        pass

    def __Reset(self):
        self.__frame1.destroy()


"""
root = Tk()
mg = Frame1(root)
root.mainloop()
"""
