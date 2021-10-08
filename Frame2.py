import sqlite3, os, Frame1, MyMainException, cv2, time, firebase, threading
from tkinter import Frame, Tk, Button, Label, Entry, ttk, messagebox
from PIL import Image, ImageTk

onlTime = 0
ClassStatus = 0


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
        Tlg = ImageTk.PhotoImage(file=os.path.join(os.getcwd(), r"resource\tlogo.png"))
        bg = Label(self.__frame2, image=img)
        bg.image_names = img
        bg.place(x=-2, y=0)
        tlabel = Label(self.__frame2, image=Tlg)
        tlabel.image_names = Tlg
        tlabel.place(x=8, y=8)

        Button(
            self.__frame2,
            text="Đăng xuất",
            fg="red",
            font=("Arial", 15, "bold"),
            width=23,
            borderwidth=4,
            command=self.__SignOut,
        ).place(x=10, y=185)

        imgbt = ImageTk.PhotoImage(file=os.getcwd() + r"\resource\q.png")
        bt1 = Button(
            self.__frame2,
            text="Điểm danh",
            font=("Arial", 20, "bold"),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
            command=self.__Attendance,
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
            command=self.__showInfo,
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
            command=self.__updateInfo,
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
            command=self.__ctdt,
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
            command=self.__CommingSoon,
        )
        bt5.image_names = imgbt
        bt5.place(x=10, y=531)

    def pack(self):
        self.__frame2.pack(fill="both", expand=1)

    def __SignOut(self):
        self.__master.unbind("<Return>")
        Frame1.MyID = None
        self.__frame2.forget()
        self.__frame1 = Frame1.Frame1(self.__master)
        self.__frame1.pack()

    def __showInfo(self):
        self.__master.unbind("<Return>")
        connect = sqlite3.connect(os.path.join(os.getcwd(), r"database\database.db"))
        self.__cursor = connect.execute(
            "SELECT * FROM people WHERE ID=" + str(Frame1.MyID)
        )
        record = None
        for i in self.__cursor:
            record = i
        img = ImageTk.PhotoImage(file=os.getcwd() + r"\resource\frame2b.png")
        imgbt = ImageTk.PhotoImage(file=os.getcwd() + r"\resource\frame2ba.png")
        imgbtt = ImageTk.PhotoImage(file=os.getcwd() + r"\resource\frame2bb.png")

        lb2b = Label(self.__frame2, image=img)
        lb2b.image_names = img
        lb2b.place(x=310, y=10)

        lbName = Label(
            self.__frame2,
            text=record[2],
            font=("Arial", 20),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        lbName.image_names = imgbt
        lbName.place(x=347, y=140)

        lbName = Label(
            self.__frame2,
            text=record[3],
            font=("Arial", 20),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        lbName.image_names = imgbt
        lbName.place(x=667, y=140)

        lbName = Label(
            self.__frame2,
            text=record[4],
            font=("Arial", 20),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        lbName.image_names = imgbt
        lbName.place(x=347, y=232)

        lbName = Label(
            self.__frame2,
            text=record[5],
            font=("Arial", 20),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        lbName.image_names = imgbt
        lbName.place(x=667, y=232)

        lbName = Label(
            self.__frame2,
            text=record[6],
            font=("Arial", 20),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        lbName.image_names = imgbt
        lbName.place(x=347, y=324)

        lbName = Label(
            self.__frame2,
            text=record[8],
            font=("Arial", 20),
            width=283,
            height=50,
            image=imgbt,
            compound="center",
        )
        lbName.image_names = imgbt
        lbName.place(x=667, y=324)

        lbName = Label(
            self.__frame2,
            text=record[7],
            font=("Arial", 15),
            width=605,
            height=50,
            image=imgbtt,
            compound="center",
        )
        lbName.image_names = imgbtt
        lbName.place(x=347, y=416)

        lbName = Label(
            self.__frame2,
            text=record[9],
            font=("Arial", 15),
            width=605,
            height=50,
            image=imgbtt,
            compound="center",
        )
        lbName.image_names = imgbtt
        lbName.place(x=347, y=508)
        connect.commit()
        connect.close()

    def __ctdt(self):
        self.__master.unbind("<Return>")
        mj = (
            "cntt"
            if Frame1.MyMajor == "Công Nghệ Thông Tin"
            else "kte"
            if Frame1.MyMajor == "Kinh Tế"
            else "ck"
        )
        img = ImageTk.PhotoImage(file="resource\{}.png".format(mj))
        lb = Label(self.__frame2, image=img)
        lb.image_names = img
        lb.place(x=310, y=10)

    def __updateInfo(self):
        frame3 = Frame(self.__frame2)
        frame3.place(x=310, y=10)
        img = ImageTk.PhotoImage(file=r"resource\frame2c.png")
        lb = Label(frame3, image=img)
        lb.image_names = img
        lb.pack()

        etrName = Entry(frame3, font=("Arial", 15))
        etrName.place(x=300, y=130)

        options = ["", "Nam", "Nữ", "Khác"]
        etrGender = ttk.Combobox(frame3, font=("Arial", 15), width=18, values=options)
        etrGender.current(0)
        etrGender.place(x=300, y=210)

        etrSDT = Entry(frame3, font=("Arial", 15))
        etrSDT.place(x=300, y=290)

        etrFolk = Entry(frame3, font=("Arial", 15))
        etrFolk.place(x=300, y=370)

        etrAddress = Entry(frame3, font=("Arial", 15))
        etrAddress.place(x=300, y=450)

        lst = [etrName, etrGender, etrSDT, etrFolk, etrAddress]

        self.__master.bind("<Return>", lambda e: self.__modifyInfo(lst, frame3))
        Button(
            frame3,
            text="Submit",
            fg="Green",
            font=("Arial", 20, "bold"),
            command=lambda e: self.__modifyInfo(lst, frame3),
        ).place(
            x=280,
            y=490,
        )

    def __modifyInfo(self, lst, frame3):
        try:
            slst = [i.get() for i in lst]
            MyMainException.checkInfo(slst)
            connect = sqlite3.connect(
                os.path.join(os.getcwd(), r"database\database.db")
            )
            connect.execute(
                "UPDATE people SET NAME='"
                + str(slst[0])
                + "', GENDER='"
                + str(slst[1])
                + "', SDT='"
                + str(slst[2])
                + "', FOLK='"
                + str(slst[3])
                + "', ADDRESS='"
                + str(slst[4] + "' WHERE ID=" + str(Frame1.MyID))
            )
            connect.commit()
            connect.close()
            messagebox.showinfo("Done", "Chỉnh sửa thông tin thành công")
            frame3.forget()
        except (
            MyMainException.NameException,
            MyMainException.GenderException,
            MyMainException.SDTException,
            MyMainException.FolkException,
            MyMainException.AddressException,
        ) as e:
            e.warning()
        except Exception:
            messagebox.showwarning("Error", "Chỉnh sửa thông tin thất bại")

    def __Attendance(self):
        threading.Thread(target=self.__getClassStatus).start()
        global onlTime
        self.__master.unbind("<Return>")
        frame4 = Frame(self.__frame2, width=684, height=585)
        frame4.place(x=310, y=10)
        imgl = ImageTk.PhotoImage(file=os.getcwd() + r"\resource\atlg1.jpg")
        lb = Label(frame4, image=imgl)
        lb.image_names = imgl
        lb.place(x=0, y=0)
        Button(
            frame4,
            text="Join",
            font=("Arial", 15, "bold"),
            fg="Green",
            command=self.__joinClass,
        ).place(x=300, y=265)

    def __joinClass(self):
        self.__startime = self.__endtime = onlTime + time.time()
        threading.Thread(target=self.__getClassStatus).start()
        global ClassStatus
        if int(ClassStatus) == 1:
            frame5 = Frame(self.__frame2, width=684, height=585, bg="White")
            frame5.place(x=310, y=10)
            lb = Label(frame5)
            lb.place(x=20, y=0)
            self.__camOn = 1
            Button(
                frame5,
                text="Leave",
                font=("Arial", 20, "bold"),
                fg="Red",
                command=self.__leaveClass,
            ).place(x=290, y=500)

            face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
            )
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            threading.Thread(
                name="Thread-1",
                target=recognizer.read(os.getcwd() + r"\recognizer\trainingData.yml"),
            ).start()
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
            self.__showFrame(lb, cap, face_cascade, recognizer)
        else:
            messagebox.showinfo("Thông báo", "Lớp học chưa bắt đầu")

    def __showFrame(self, lb, cap, face_cascade, recognizer):
        threading.Thread(target=self.__getClassStatus).start()
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y : y + h, x : x + w]
            id, tl = recognizer.predict(roi_gray)
            if tl < 85:
                cv2.putText(
                    frame,
                    str(id),
                    (x + 10, y - 10),
                    cv2.FONT_HERSHEY_PLAIN,
                    1,
                    (0, 0, 255),
                    2,
                )
        imgtk = ImageTk.PhotoImage(
            Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        )
        lb.config(image=imgtk)
        lb.image_names = imgtk
        global onlTime
        t = self.__endtime - self.__startime + onlTime
        if (round(t, 1) - 0.5) % 10 == 0 and t != 0:
            threading.Thread(target=firebase.updateTime(Frame1.MyID, t)).start()
        self.__endtime = onlTime + time.time()

        global ClassStatus
        if int(ClassStatus) == 0:
            onlTime = 0
            messagebox.showinfo("Thông báo", "Lớp học đã kết thúc")
            self.__leaveClass()
        elif self.__camOn == 1:
            lb.after(10, lambda: self.__showFrame(lb, cap, face_cascade, recognizer))

    def __leaveClass(self):
        global ClassStatus
        if int(ClassStatus) == 1:
            global onlTime
            onlTime = int(self.__endtime - self.__startime + onlTime)
        self.__camOn = 0
        cv2.destroyAllWindows()
        self.__Attendance()

    def __getClassStatus(self):
        global ClassStatus
        ClassStatus = int(firebase.getClassStatus())

    def __CommingSoon(self):
        self.__master.unbind("<Return>")
        self.__config()


"""root = Tk()
t = Frame2(root)
root.mainloop()"""
