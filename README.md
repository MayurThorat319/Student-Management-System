🎓 Student Management System (Python + MySQL)

A GUI-based Student Management System built using Python (Tkinter) with MySQL database integration.
This application allows users to add, view, update, and delete student records, with all data stored permanently in a MySQL database.

📌 Features

🧑‍🎓 Add new student records

✏️ Update existing student details

🗑️ Delete single or all records

📋 View all students in a table (Treeview)

💾 Data stored securely in MySQL database

🖥️ User-friendly GUI using Tkinter

🔄 Real-time refresh after database operations

🛠️ Technologies Used

Python 3

Tkinter (GUI)

MySQL

mysql-connector-python

ttk Treeview

🗄️ Database Structure

Database Name: abc
Table Name: students

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    age INT,
    enroll_date DATE,
    phone_no VARCHAR(15),
    location VARCHAR(100),
    course VARCHAR(100)
);

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/student-management-system.git
cd student-management-system

2️⃣ Install Required Package
pip install mysql-connector-python

3️⃣ Configure MySQL Connection

Update the database credentials in the code:

db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="**",
    password="***",
    database="***"
)


Make sure:

MySQL server is running

Database and table exist

▶️ How to Run the Application
python GUI\ Project.py

The GUI window will open with:
Student entry form (left)
Student records table (right)

🧪 CRUD Operations
Action	Description
Add	Insert new student record into MySQL
Update	Modify selected student data
Delete	Remove selected student
Delete All	Clear entire table
Clear	Reset input fields

👨‍💻 Author
Mayur Thorat
📍 Navi Mumbai
💻 Python | Tkinter | MySQL
