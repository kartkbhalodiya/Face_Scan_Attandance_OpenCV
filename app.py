from flask import Flask, render_template, request
import cv2
import numpy as np
import face_recognition

import os
from datetime import datetime
from datetime import date
import sqlite3
import pandas as pd
import json
from flask import session

name = "FRAMS"
app = Flask(__name__)

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == "POST":
        return render_template('index.html')
    else:
        return "Everything is okay!"

@app.route('/name', methods=['GET', 'POST'])
def name():
    if request.method == "POST":
        name1 = request.form['name1']
        name2 = request.form['name2']

        cam = cv2.VideoCapture(0)

        while True:
            ret, frame = cam.read()
            if not ret:
                print("Failed to grab frame")
                break
            cv2.imshow("Press Space to capture image", frame)

            k = cv2.waitKey()
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = name1 + ".png"
                path ="Training Images"
                cv2.imwrite(os.path.join(path, img_name), frame)
                print("{} written!".format(img_name))

        cam.release()
        cv2.destroyAllWindows()
        return render_template('image.html')
    else:
        return 'All is not well'

@app.route("/", methods=["GET", "POST"])
def recognize():
    if request.method == "POST":
        path = 'Training images'
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            if curImg is not None:
                images.append(curImg)
                classNames.append(os.path.splitext(cl)[0])
        print(classNames)
        
        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)
                if len(encode) > 0:
                    encodeList.append(encode[0])
                else:
                    print("Can't be encoded")
            return encodeList

        def markData(name):
            print("The Attended Person is ", name)
            now = datetime.now()
            dtString = now.strftime('%H:%M')
            today = date.today()
            d1 = today.strftime('%b-%d-%Y')
            print("Today's date:", today)
            conn = sqlite3.connect('information.db')
            conn.execute('''CREATE TABLE IF NOT EXISTS Attendance
                            (NAME TEXT NOT NULL,
                             Time TEXT NOT NULL, Date TEXT NOT NULL)''')
                       
            conn.execute("INSERT OR IGNORE INTO Attendance (NAME, Time, Date) values (?, ?, ?)", (name, dtString, today,))
            conn.commit()
            cursor = conn.execute("SELECT NAME, Time, Date from Attendance")
                                                                  
            for line in cursor:
                print("Name Updated :", line[0])
                print("Time Updated :", line[1])

        def markAttendance(name):
            with open('attendance.csv', 'r+', errors='ignore') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    print(myDataList)
                    entry = line.split(',')
                    nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M')
                    f.writelines(f'\n{name},{dtString}')
                    
        encodeListKnown = findEncodings(images)
        print('Encoding Complete')

        cap = cv2.VideoCapture(0)

        while True:
            success, img = cap.read()
            if not success:
                print("Failed to capture frame")
                break
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if faceDis[matchIndex] < 0.50:
                    name = classNames[matchIndex].upper()
                    markAttendance(name)
                    markData(name)
                else:
                    name = 'Unknown'
                
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow('Punch your Attendance', img)
            c = cv2.waitKey(1)
            if c == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

        return render_template('first.html')
    else:
        return render_template('main.html')

@app.route('/login', methods=['POST'])
def login():
    json_data = json.loads(request.data.decode())
    username = json_data['username']
    password = json_data['password']
    df = pd.read_csv('cred.csv')
    if len(df.loc[df['username'] == username]['password'].values) > 0:
        if df.loc[df['username'] == username]['password'].values[0] == password:
            session['username'] = username
            return 'success'
        else:
            return 'failed'
    else:
        return 'failed'

@app.route('/checklogin')
def checklogin():
    if 'username' in session:
        return session['username']
    return 'False'

@app.route('/how', methods=["GET", "POST"])
def how():
    return render_template('form.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    if request.method == "POST":
        today = date.today()
        print(today)
        conn = sqlite3.connect('information.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        print("Opened database successfully")
        cursor = cur.execute("SELECT DISTINCT NAME, Time, Date from Attendance where Date=?", (today,))
        rows = cur.fetchall()
        print(rows)
        conn.close()
        return render_template('form2.html', rows=rows)
    else:
        return render_template('form1.html')

@app.route('/whole', methods=["GET", "POST"])
def whole():
    today = date.today()
    print(today)
    conn = sqlite3.connect('information.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    print("Opened database successfully")
    cursor = cur.execute("SELECT DISTINCT NAME, Time, Date from Attendance")
    rows = cur.fetchall()
    return render_template('form3.html', rows=rows)

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
