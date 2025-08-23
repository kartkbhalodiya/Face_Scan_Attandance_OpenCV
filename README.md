📸 Face Scan Attendance System
A robust and efficient attendance system that uses facial recognition to mark attendance. Built with Python, Django, and OpenCV, this application provides a seamless experience for capturing images, training the facial recognition model, and recording attendance with an option to export the data to an Excel file.

✨ Features
👨‍💻 User-Friendly Interface: A simple and intuitive web interface built with HTML, CSS, and JavaScript.

📷 Image Capture: Easily capture and register user images directly from the browser.

🤖 AI-Powered Training: One-click training of the facial recognition model on the registered images.

✅ Real-time Attendance: Mark attendance in real-time using a live camera feed.

📊 Attendance Database: View and manage attendance records within the application.

📄 Excel Export: Export attendance records to an Excel spreadsheet for easy record-keeping and analysis.

🚀 Scalable Architecture: Built on the powerful Django web framework.

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

Navigate to http://127.0.0.1:8000/ to see the application in action.

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

🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is distributed under the MIT License. See LICENSE for more information.
