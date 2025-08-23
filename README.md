📸 Face Scan Attendance System
A robust and efficient attendance system that uses facial recognition to mark attendance. Built with Python, Django, and OpenCV, this application provides a seamless experience for capturing images, training the facial recognition model, and recording attendance with an option to export the data to an Excel file.

✨ Features
👨‍💻 User-Friendly Interface: A simple and intuitive web interface built with HTML, CSS, and JavaScript.

📷 Image Capture: Easily capture and register user images directly from the browser.

🤖 AI-Powered Training: One-click training of the facial recognition model on the registered images.

✅ Real-time Attendance: Mark attendance in real-time using a live camera feed.

📊 Attendance Database: View and manage attendance records within the application.

📄 Excel Export: Export attendance records to an Excel spreadsheet for easy record-keeping and analysis.

🚀 Scalable Architecture: Built on the powerful Flask web framework.

🛠️ Installation & Setup
Follow these steps to get the project up and running on your local machine.

1. Clone the repository:

       git clone https://github.com/kartkbhalodiya/Face_Scan_Attandance_OpenCV.git
       cd Face_Scan_Attandance_OpenCV

2. Create and activate a virtual environment:

Windows:

     python -m venv venv
     .\venv\Scripts\activate

macOS / Linux:

     python3 -m venv venv
     source venv/bin/activate

3. Install the dependencies:

        pip install -r requirements.txt

(Note: You may need to create a requirements.txt file by running pip freeze > requirements.txt in your current project setup)

4. Run the application:

        python manage.py runserver

5. Open your browser:

Navigate to http://12previ7.0.0.1:8000/ to see the application in action.

📖 How to Use
1. 🎓 Register a New Student

Navigate to the 'Register Students' section.

Enter the student's Name and ID.

Press the Spacebar to capture snapshots and Esc to finish.

2. ✅ Take Attendance

Go to the 'Take Attendance' section.

The camera will activate, automatically recognizing registered faces and marking their attendance.

3. 📊 View Records

Access the 'Admin' section to see all logged attendance.

     Username: admin

     Password: admin123

🖼️ Project Preview
Here's a sneak peek into the application's interface and functionality.

✨User Interface (Home Page)

<img width="1892" alt="Home Page" src="https://github.com/user-attachments/assets/8b5facd3-16ca-4dc5-8c60-67924459c107" />

✨Register a New Student

<img width="1888" alt="Register Student Page" src="https://github.com/user-attachments/assets/83b05b81-8d79-4d68-b64c-416ea325092f" />

✨Successful Data Entry with Images

<img width="1915" alt="Database view of new student" src="https://github.com/user-attachments/assets/2c52b1f4-8daf-4a34-ad62-0c2de5c5e0d5" />

✨Taking Student Attendance

<img width="1894" alt="Live attendance view" src="https://github.com/user-attachments/assets/6058cc03-fe3b-4d92-904a-6718444484fa" />

✨Successful Attendance Marking

<img width="1919" alt="Database view of marked attendance" src="https://github.com/user-attachments/assets/d407442a-1230-431d-b6fe-86687ea2da83" />

✨Admin Login Page

<img width="1914" alt="Admin login screen" src="https://github.com/user-attachments/assets/f20d91eb-4987-44cf-9b8e-cb7d0fcd5440" />

✨Today's Attendance View

<img width="1898" alt="Today's attendance records" src="https://github.com/user-attachments/assets/adf82c0d-615a-46e5-b0d4-188887fa657d" />

✨All Attendance Records

<img width="1896" alt="All attendance records" src="https://github.com/user-attachments/assets/f11f88c8-d396-46c2-95a2-35a6018b5ff9" />

✨Contact Us Page

<img width="1882" alt="Contact Us Page" src="https://github.com/user-attachments/assets/fa3cfbfe-5e3a-4ce3-8b33-ab5ae0962275" />

🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

📄 License
This project is distributed under the MIT License. See LICENSE for more information.
