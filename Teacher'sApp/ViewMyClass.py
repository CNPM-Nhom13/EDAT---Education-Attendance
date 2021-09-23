from tkinter import Tk, Frame, Label, Button, Entry, messagebox, ttk
import sqlite3, firebase, threading


class MyFrame1:
    def __init__(self, master):
        self.__master = master
        self.__SvTime = tuple("0" for i in range(8))
        self.__frame = Frame(self.__master, width=600, height=520)
        self.__connect = sqlite3.connect(r"database\database.db")
        cursor = self.__connect.execute("SELECT * FROM people")
        self.__lstsv = [i for i in cursor]
        self.__frameConfig()
        self.__connect.commit()
        self.__connect.close()

    def __frameConfig(self):
        self.__frame.pack()

        self.__sta = Button(
            self.__frame,
            text="Start Lesson",
            font=("Arial", 20, "bold"),
            fg="green",
            command=self.__start,
        )
        self.__sta.place(x=200, y=0)
        self.__sto = Button(
            self.__frame,
            text="Stop Lesson",
            font=("Arial", 20, "bold"),
            fg="red",
            command=self.__stop,
        )
        Button(
            self.__frame,
            text="Back",
            font=("Arial", 20, "bold"),
            fg="orange",
            command=self.__frame.forget,
        ).place(x=250, y=465)

    def __start(self):
        self.__sta.place_forget()
        self.__sto = Button(
            self.__frame,
            text="Stop Lesson",
            font=("Arial", 20, "bold"),
            fg="red",
            command=self.__stop,
        )
        self.__sto.place(x=200, y=0)

        self.__frame1 = Frame(self.__frame, width=600, height=420)
        self.__frame1.place(x=0, y=60)
        self.__frame1Config()

    def __stop(self):
        self.__frame1.place_forget()
        self.__sto.place_forget()
        self.__sta = Button(
            self.__frame,
            text="Start Lesson",
            font=("Arial", 20, "bold"),
            fg="green",
            command=self.__start,
        )
        self.__sta.place(x=200, y=0)

    def __frame1Config(self):
        Label(
            self.__frame1, text="Danh sách sinh viên", font=("Arial", 20, "bold")
        ).grid(row=0, column=0, columnspan=4)
        self.__table()

        for q in range(len(self.__lstsv)):
            Label(self.__frame1, text=str(q + 1), font=("Arial", 15)).grid(
                row=q + 2, column=0
            )
            Label(self.__frame1, text=self.__lstsv[q][3], font=("Arial", 15)).grid(
                row=q + 2, column=1
            )
            Label(self.__frame1, text=self.__lstsv[q][2], font=("Arial", 15)).grid(
                row=q + 2, column=2
            )
            Label(
                self.__frame1,
                text=str(0),
                font=("Arial", 15),
            ).grid(row=q + 2, column=3)
        self.__frame1.after(3000, self.__updateTime)

    def __updateTime(self):
        thr1 = threading.Thread(name=("Thr1"), target=self.__getSvTime)
        thr1.start()
        for q in range(len(self.__SvTime)):
            Label(
                self.__frame1,
                text=str(self.__SvTime[q]),
                font=("Arial", 15),
            ).grid(row=q + 2, column=3)
        self.__frame1.after(5000, self.__updateTime)

    def __getSvTime(self):
        self.__SvTime = tuple(
            firebase.getTime(self.__lstsv[i][0]) for i in range(len(self.__lstsv))
        )

    def __table(self):
        for q in range(len(self.__lstsv) + 1):
            Label(
                self.__frame1,
                width=10,
                height=2,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=0)
            Label(
                self.__frame1,
                width=25,
                height=2,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=1)
            Label(
                self.__frame1,
                width=35,
                height=2,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=2)
            Label(
                self.__frame1,
                width=14,
                height=2,
                relief="solid",
                borderwidth=1,
            ).grid(row=q + 1, column=3)
        Label(self.__frame1, text="STT", font=("Arial", 15)).grid(row=1, column=0)
        Label(self.__frame1, text="Mã sinh viên", font=("Arial", 15)).grid(
            row=1, column=1
        )
        Label(self.__frame1, text="Họ tên", font=("Arial", 15)).grid(row=1, column=2)
        Label(self.__frame1, text="Thời gian", font=("Arial", 15)).grid(row=1, column=3)

    def forget(self):
        self.__frame.forget()

    def pack(self):
        self.__frame.pack()


"""root = Tk()
mf = MyFrame1(root)
root.mainloop()"""
