import threading
import pyrebase, sqlite3

config = {
    "apiKey": "AIzaSyB_LH8lyCg4bdgUHZhsmeyNmUtOjoB22mA",
    "authDomain": "qlsv-ea25d.firebaseapp.com",
    "databaseURL": "qlsv-ea25d.firebaseapp.com",
    "projectId": "qlsv-ea25d",
    "storageBucket": "qlsv-ea25d.appspot.com",
    "messagingSenderId": "911368744543",
    "appId": "1:911368744543:web:04dd657c6f99b2bf27f5ea",
    "measurementId": "G-1BKR6BV3NM",
}

configDtb = {
    "apiKey": "AIzaSyB_LH8lyCg4bdgUHZhsmeyNmUtOjoB22mA",
    "authDomain": "qlsv-ea25d.firebaseapp.com",
    "databaseURL": "https://qlsv-ea25d-default-rtdb.firebaseio.com/",
    "projectId": "qlsv-ea25d",
    "storageBucket": "qlsv-ea25d.appspot.com",
    "messagingSenderId": "911368744543",
    "appId": "1:911368744543:web:04dd657c6f99b2bf27f5ea",
    "measurementId": "G-1BKR6BV3NM",
}


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
database = pyrebase.initialize_app(configDtb).database()

local_path = "recognizer/trainingData.yml"
cloud_path = "recognizer/trainingData.yml"


def dowload():
    storage.child(cloud_path).download(local_path, cloud_path)


def dowloadDatabase():
    storage.child("database/database.db").download(
        r"database\database.db", "database/database.db"
    )


def upload():
    storage.child(cloud_path).put(local_path)


def uploadDatabase():
    storage.child("database/database.db").put("database/database.db")


def delete():
    storage.delete(cloud_path)


def resetTime(id):
    database.child("ID").child(str(id)).update({"Time": 0})


def getTime(id):
    return database.child("ID").get().val().get(str(id))["Time"]


def updateTime(id, t):
    database.child("ID").child(str(id)).update({"Time": t})


def config():
    database.remove()
    connect = sqlite3.connect(r"database\database.db")
    cursor = connect.execute("SELECT * FROM people")
    lst = [i[0] for i in cursor]
    for i in lst:
        updateTime(str(i), 0)
    connect.commit()
    connect.close()
