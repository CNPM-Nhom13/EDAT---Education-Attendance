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


firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

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
