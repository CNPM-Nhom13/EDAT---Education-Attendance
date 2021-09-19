import pyrebase


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


def delete():
    storage.delete(cloud_path)
