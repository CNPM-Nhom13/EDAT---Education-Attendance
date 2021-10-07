from tkinter import Entry, Frame, Tk, Label, Button, Checkbutton, Toplevel, messagebox
import cv2, os, Frame2, urllib, sqlite3, urllib.request, urllib.error, MyMainException
from PIL import Image, ImageTk

MyID = MyMajor = None


class Frame1:
    def __init__(self, master):
        self.__master = master
        self.__frame1 = Frame(master)
        self.__GUIconfig()
        self.__frame1.pack(fill="both", expand=1)

    def __GUIconfig(self):
        NowFrame = "1"
        img = ImageTk.PhotoImage(file=os.path.join(os.getcwd(), "resource\logo1.png"))
        self.__master.title("EDAT | Thuy Loi University")
        self.__master.geometry("1000x600")
        self.__master.resizable(False, False)
        self.__frame1.config(width=1000, height=600)
        label = Label(self.__frame1, image=img)
        label.image_names = img
        label.place(x=-2, y=0)
        etr1, etr2 = self.__setEntry()
        self.__master.bind("<Return>", lambda e: self.__SignIn(etr1, etr2))
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

        Button(
            self.__frame1,
            text="Quên mật khẩu",
            font=("Arial", 10, "bold"),
            fg="#009BFA",
            command=self.__forgetPW,
            borderwidth=0,
        ).place(x=600, y=290)

    def __setEntry(self):
        Label(self.__frame1, text="Tên đăng nhập:", font=("Arial", 15, "bold")).place(
            x=600, y=120
        )
        entry1 = Entry(self.__frame1, width=20, font=("Arial", 20), justify="right")
        entry1.place(x=600, y=150)

        Label(
            self.__frame1,
            text="Mật Khẩu:",
            font=("Arial", 15, "bold"),
        ).place(x=600, y=220)
        entry2 = Entry(
            self.__frame1, width=20, font=("Arial", 20), show="*", justify="right"
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
            try:
                if type(etr1) == type("a"):
                    id, pw = etr1, etr2
                    MyMainException.checkID(id)
                else:
                    id, pw = etr1.get(), etr2.get()
                    MyMainException.checkID(id)
                    MyMainException.checkPW(pw)

                global MyID, MyMajor
                MyID = id
                connect = sqlite3.connect(
                    os.path.join(os.getcwd(), r"database\database.db")
                )
                cursor = connect.execute("SELECT * FROM people WHERE ID=" + str(id))
                isRecordExist = 0
                if pw != "PASS":
                    for row in cursor:
                        if str(id) == str(row[0]) and str(pw) == str(row[1]):
                            isRecordExist = 1
                            MyMajor = row[7]
                else:
                    isRecordExist = 1
                if isRecordExist == 1:
                    self.__master.unbind("<Return>")
                    self.__frame1.forget()
                    self.__frame2 = Frame2.Frame2(self.__master)
                    self.__frame2.pack()
                else:
                    messagebox.showwarning(
                        "Error", "Tên đăng nhập hoặc mật khẩu không đúng"
                    )
                connect.commit()
                connect.close()
            except (MyMainException.IDException, MyMainException.PWException) as e:
                e.warning()
            # except Exception:
            #    messagebox.showwarning("Error", "Đăng nhập không thành công")

    def __forgetPW(self):
        messagebox.showinfo(
            "Forgot Password",
            "Bạn hãy liên hệ với văn phòng khoa để được cấp lại mật khẩu",
        )

    def __FaceSignIn(self):
        # tl = Toplevel(self.__frame1)
        # tl.geometry("300x300")
        lst = [0]
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(os.path.join(os.getcwd(), r"recognizer/trainingData.yml"))
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            _, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = face_cascade.detectMultiScale(gray)
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_gray = gray[y : y + h, x : x + w]
                id, tl = recognizer.predict(roi_gray)
                if tl < 80:
                    cv2.putText(
                        frame,
                        str(id),
                        (x + 10, y - 10),
                        cv2.FONT_HERSHEY_PLAIN,
                        1,
                        (0, 0, 255),
                        2,
                    )
                    lst.append(str(id))
                else:
                    lst.append(str(0))
            cv2.imshow("Detecting Face", frame)
            idn = max(lst, key=lst.count)
            if cv2.waitKey(1) & lst.count(idn) == 30 or len(lst) > 50:
                break
        cv2.destroyAllWindows()
        if idn == "0":
            messagebox.showwarning(
                "Error",
                "\tĐăng nhập không thành công\nKhông có dữ liệu nhận dạng khuôn mặt hoặc tài khoản",
            )
        else:
            self.__SignIn(idn, "PASS")

    def __Reset(self):
        self.__frame1.destroy()


"""root = Tk()
mg = Frame1(root)
root.mainloop()"""
