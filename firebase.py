import pyrebase, os


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

config_a = {
    "apiKey": "AIzaSyCb_ge32xry68dj8yHLcVD8bvTSsBYJR3Q",
    "authDomain": "htnam-72b75.firebaseapp.com",
    "databaseURL": "htnam-72b75.firebaseapp.com",
    "projectId": "htnam-72b75",
    "storageBucket": "htnam-72b75.appspot.com",
    "messagingSenderId": "264425807306",
    "appId": "1:264425807306:web:e5a50cd02888d3e655c333",
}

configDatabase = {
    "apiKey": "AIzaSyB_LH8lyCg4bdgUHZhsmeyNmUtOjoB22mA",
    "authDomain": "qlsv-ea25d.firebaseapp.com",
    "databaseURL": "https://qlsv-ea25d-default-rtdb.firebaseio.com/",
    "projectId": "qlsv-ea25d",
    "storageBucket": "qlsv-ea25d.appspot.com",
    "messagingSenderId": "911368744543",
    "appId": "1:911368744543:web:04dd657c6f99b2bf27f5ea",
    "measurementId": "G-1BKR6BV3NM",
}

firebase = pyrebase.initialize_app(config_a)
storage = firebase.storage()
database = pyrebase.initialize_app(configDatabase).database()

dtbLocalPath = dtbCloudPath = "database/database.db"
tnLocalPath = tnCloudPath = "recognizer/trainingData.yml"


def dowloadDtb():
    if not os.path.exists("database"):
        os.mkdir("database")
    storage.child(dtbCloudPath).download(dtbLocalPath, dtbCloudPath)


def dowloadTrainingData():
    if not os.path.exists("recognizer"):
        os.mkdir("recognizer")
    storage.child(tnCloudPath).download(tnLocalPath, tnCloudPath)


def uploadDtb():
    storage.child(dtbCloudPath).put(dtbLocalPath)


def uploadTrainingData():
    storage.child(tnCloudPath).put(tnLocalPath)


# setNewRecord
# database.child("1111").set({"Time": 5})

# getRecord
# e = database.child("1111").get()
# print(dict(e.val())["Time"])


# updateRecord
# database.child("1111").update({"Time": 20})


# delete "1111"
# database.child("1111").remove()
