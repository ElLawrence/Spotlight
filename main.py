from typing import Mapping
import pyrebase

import getpass


firebaseConfig = {
  "apiKey": "AIzaSyAAKCoiOFPBvX1-dhZl9sQTAS2BMS1qPsA",
  "authDomain": "spotlight-9df3f.firebaseapp.com",
  "projectId": "spotlight-9df3f",
  "storageBucket": "spotlight-9df3f.appspot.com",
  "messagingSenderId": "511254312338",
  "appId": "1:511254312338:web:5d2cfcb1621614151bbd4b",
  "measurementId": "G-GWQ5TP662C",
  "databaseURL": "https://spotlight-9df3f-default-rtdb.firebaseio.com/"
}


firebase = pyrebase.initialize_app(firebaseConfig)


auth = firebase.auth()
storage = firebase.storage()
db = firebase.database()
nameData = {}

email = ""
password = ""


def signup() :
  print("signing up...")
  email = input("Please enter your email address: ")
  password = input("Please enter your password: ")

  try:
    user = auth.create_user_with_email_and_password(email, password)
    print("Account created")
    nameData = {'name': email, 'password': password}
  except:
    print("Email already exists")



def login() :
  print("logging in...")
  email = input("Please enter your email address: ")
  password = input("Please enter your password: ")

  try: 
    login = auth.sign_in_with_email_and_password(email, password)
    nameData = {'Name':email}
    print("Logged in")
  except:
    print("Invalid email or password")


def addUser() :
  db.child("users").push(nameData)
 
  


def post():
  post = input("Type post here: ")
  db.child("posts").push({'post':post})
  


def displayPosts() :
  print(db.child("posts"))



def main() :
  askLogIn = input("Are you a new user?[y/n] ")

  if askLogIn == "y" or askLogIn == "Y":
    signup()  
    addUser()
    login()
  else :
    login()

  askPost = input("Would you like to post?[y/n] ")

  if askPost == "y" or askPost == "Y":
    post()

  displayPosts()



  




main()


