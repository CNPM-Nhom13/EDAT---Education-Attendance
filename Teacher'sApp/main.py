import threading, cv2, os, sqlite3, shutil, firebase, ConnectionCheck, time, Addstudent, ViewMyClass
from tkinter import Entry, Frame, Tk, Button, Label, Toplevel, ttk, messagebox
from PIL import Image, ImageTk
import numpy as np


class MyGui:
    def __init__(self, master):
        self.__master = master
        self.__face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.__id = 0
        self.__temp = 0
        self.__Config()

    def __Config(self):
        self.__master.geometry("600x520")
        self.__master.title("EDAT for teacher")
        self.__master.resizable(False, False)

        self.__frame = Frame(self.__master, width=600, height=520)
        self.__frameConfig()
        self.__frame1 = Frame(self.__master, width=600, height=520)

    def __frameConfig(self):
        self.__frame.pack()
        Label(self.__frame, text="ID GV:", font=("Arial", 20, "bold")).place(
            x=165, y=150
        )
        etr1 = Entry(self.__frame, font=("Arial", 20), width=10, justify="right")
        etr1.place(x=275, y=150)

        Label(self.__frame, text="PW GV:", font=("Arial", 20, "bold")).place(
            x=165, y=230
        )
        etr2 = Entry(self.__frame, font=("Arial", 20), width=10, justify="right")
        etr2.place(x=275, y=230)

        Button(
            self.__frame,
            text="Submit",
            font=("Arial", 20, "bold"),
            fg="green",
            command=lambda: self.__signIn(etr1, etr2),
        ).place(x=310, y=300)
        Button(
            self.__frame,
            text="Quit",
            font=("Arial", 20, "bold"),
            width=6,
            fg="red",
            command=self.__master.destroy,
        ).place(x=170, y=300)

    def __signIn(self, etr1, etr2):
        connection = False
        try:
            if not ConnectionCheck.internet_on():
                raise Exception
            else:
                connection = True
        except Exception:
            messagebox.showwarning("Lost Connection", "Không có kết nối mạng")
        if connection == True:
            id, pw = etr1.get(), etr2.get()

            if self.__id == "":
                messagebox.showwarning("Can't Sign In", "Tài khoản không được để trống")
            else:
                connect = sqlite3.connect(
                    os.path.join(os.getcwd(), r"database/database.db")
                )
                query = "SELECT * FROM teacher WHERE ID=" + str(id)
                cursor = connect.execute(query)

                isRecordExist = 0
                for row in cursor:
                    if int(id) == int(row[0]) and int(pw) == int(row[1]):
                        isRecordExist = 1

                if isRecordExist == 1:
                    self.__frame.forget()
                    self.__frame1Config()
                else:
                    messagebox.showwarning("Can't Sign In", "Sai ID hoặc PW")
        else:
            messagebox.showwarning("Lost Connection", "Không có kết nối mạng")

    def __frame1Config(self):
        self.__frame1.pack()
        frame = Frame(self.__frame1)
        Label(frame, text="Add face", font=("Arial", 20, "bold")).grid(
            row=0, column=0, columnspan=2
        )
        Label(frame, text="ID SV:", font=("Arial", 20, "bold")).grid(row=1, column=0)
        etr = Entry(frame, font=("Arial", 20), justify="right")
        etr.grid(row=1, column=1)
        frame.place(x=100, y=120)
        Button(
            self.__frame1,
            text="Submit",
            fg="green",
            font=("Arial", 20, "bold"),
            command=lambda: self.__getInfo(etr),
        ).place(x=330, y=230)

        Button(
            self.__frame1,
            text="Logout",
            fg="red",
            font=("Arial", 20, "bold"),
            command=self.__Logout,
        ).place(x=145, y=230)

        Button(
            self.__frame1,
            text="Add new student info",
            fg="Orange",
            font=("Arial", 20, "bold"),
            command=self.__addStudent,
        ).place(x=145, y=290)

        Button(
            self.__frame1,
            text="My class",
            fg="Purple",
            font=("Arial", 20, "bold"),
            command=self.__MyClass,
        ).place(x=230, y=360)

    def __Logout(self):
        self.__frame1.forget()
        self.__frameConfig()

    def __getInfo(self, etr):
        connection = False
        try:
            if not ConnectionCheck.internet_on():
                raise Exception
            else:
                connection = True
        except Exception:
            messagebox.showwarning("Lost Connection", "Không có kết nối mạng")
        if connection == True:
            self.__id = etr.get()

            if self.__id == "":
                messagebox.showwarning("Can't Sign In", "Tài khoản không được để trống")
            else:
                connect = sqlite3.connect(
                    os.path.join(os.getcwd(), r"database/database.db")
                )
                query = "SELECT * FROM people WHERE ID=" + str(self.__id)
                cursor = connect.execute(query)

                isRecordExist = 0
                for row in cursor:
                    if int(self.__id) == int(row[0]):
                        isRecordExist = 1

                if isRecordExist == 1:
                    self.__frame1.forget()
                    self.__frame2 = Frame(self.__master)
                    self.__label = Label(self.__frame2)
                    self.__label.pack()
                    self.__frame2.pack(fill="both", expand=1)
                    Button(
                        self.__frame2,
                        text="Next Step",
                        fg="Green",
                        font=("Arial", 15, "bold"),
                        command=self.__trainingData,
                    ).pack()

                    self.__getData()
                else:
                    messagebox.showwarning(
                        "Can't Sign In", "Sai ID hoặc không có trong hệ thống"
                    )
        else:
            messagebox.showwarning("Lost Connection", "Không có kết nối mạng")

    def __loading(self):
        ml = Tk()
        Label(
            ml, text="Signed in, loading", fg="Green", font=("Arial", 15, "bold")
        ).pack()
        ml.after(1300, ml.destroy)
        ml.mainloop()

    def __getData(self):
        th2 = threading.Thread(name="Thread-2", target=self.__loading)
        th2.start()
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.__getData1(cap)

    def __getData1(self, cap):
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = self.__face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if not os.path.exists("dataSet"):
                os.mkdir("dataSet")
            self.__temp += 1
            cv2.imwrite(
                r"dataSet\User." + str(self.__id) + "." + str(self.__temp) + ".jpg",
                gray[y : y + h, x : x + w],
            )
        if self.__temp >= 100:
            self.__temp = 0
            messagebox.showinfo("Get Info Done", "Lấy dữ liệu thành công")
        else:
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(img)
            self.__label.config(image=imgtk)
            self.__label.image_names = imgtk
            self.__label.after(10, lambda: self.__getData1(cap))

    def __prgbar(self, mpgb, thr2):
        thr2.start()
        for i in range(5):
            mpgb["value"] += 20
            time.sleep(1)
            self.__frame3.update_idletasks()

    def __trainingData(self):
        thr2 = threading.Thread(name="Thread-2", target=self.__trainingData1)
        self.__frame2.forget()
        self.__frame3 = Frame(self.__master)
        mpgb = ttk.Progressbar(
            self.__frame3, orient="horizontal", length=200, mode="determinate"
        )
        mpgb.pack(pady=200)
        Button(
            self.__frame3,
            text="Start training data",
            fg="Green",
            font=("Arial", 15, "bold"),
            command=lambda: self.__prgbar(mpgb, thr2),
        ).place(x=200, y=300)
        self.__frame3.pack(fill="both", expand=1)

    def __trainingData1(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        try:
            if os.path.exists("recognizer"):
                shutil.rmtree("recognizer")
        except:
            pass
        if not os.path.exists(r"recognizer\trainingData.yml"):
            if not os.path.exists("recognizer"):
                os.mkdir("recognizer")
            firebase.dowload()

        recognizer.read("recognizer\\trainingData.yml")
        path = "dataSet"
        ImgPaths = [
            os.path.join(path, i)
            for i in os.listdir(path)
            if i.startswith("User." + str(self.__id) + ".")
        ]
        faces, id = [], []
        for ImgPath in ImgPaths:
            faceNp = np.array(Image.open(ImgPath).convert("L"), "uint8")
            faces.append(faceNp)
            id.append(int(ImgPath.split(".")[1]))

        recognizer.update(faces, np.array(id))
        recognizer.save(r"recognizer\trainingData.yml")
        messagebox.showinfo("Done", "Training data success")
        self.__frame3.forget()
        self.__frame1Config()

    def __addStudent(self):
        try:
            if not ConnectionCheck.internet_on():
                messagebox.showwarning("Lost Connection", "Không có kết nối mạng")
            else:
                self.__frame1.forget()
                self.__addFrame = Addstudent.MyFrame(self.__master)
                self.__addFrame.pack()
                self.__frame1Config()
        except:
            messagebox.showwarning("Lost Connection", "Không có kết nối mạng")

    def __MyClass(self):
        self.__frame4 = ViewMyClass.MyFrame1(self.__frame1)
        self.__frame4.pack()


def dowloadDTB():
    try:
        if not ConnectionCheck.internet_on():
            messagebox.showwarning("Lost Connection", "Không có kết nối mạng")
        else:
            if not os.path.exists("database"):
                os.mkdir("database")
            firebase.dowloadDatabase()
    except:
        messagebox.showwarning("Lost Connection", "Không có kết nối mạng")


def dowloadTN():
    if ConnectionCheck.internet_on():
        if not os.path.exists("recognizer"):
            os.mkdir("recognizer")
        firebase.dowload()


def main():
    root = Tk()
    mg = MyGui(root)
    root.mainloop()
    try:
        if os.path.exists("dataSet"):
            shutil.rmtree("dataSet")
    except:
        pass
    firebase.uploadDatabase()
    firebase.upload()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    thr1 = threading.Thread(name="Thread-1", target=dowloadDTB)
    # Tạm thời tắt
    thr2 = threading.Thread(name="Thread-2", target=dowloadTN)
    thr3 = threading.Thread(name="Thread-3", target=firebase.config)

    thr1.start()
    thr2.start()
    thr3.start()
    main()
