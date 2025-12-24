import mysql.connector
print("MySQL connector installed successfully")
import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
from tkinter.constants import END


db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root123",
    database="mayur"
)
db_cursor = db_connection.cursor()

win = tk.Tk()
win.geometry("1350x700+0+0")
win.title("Student Management System")
win.config(bg="lightgray")

style = ttk.Style()

style.theme_use("default")

style.configure("Treeview",background="white",foreground="black",rowheight=25,fieldbackground="white")

style.map("Treeview",background=[("selected","darkred")])

title_label = tk.Label(win,text="Student Management System",font=("Arial",20,"bold"),padx=15,pady=15,border=0,relief=tk.GROOVE,bg="teal",foreground="white")

title_label.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(win,text="Student Records",font=("Arial",14),bg="lightgray",foreground="black",relief=tk.GROOVE)

detail_frame.place(x=40,y=90,width=420,height=570)

data_frame = tk.Frame(win,bg="teal",relief=tk.GROOVE)

data_frame.place(x=490,y=98,width=830,height=565)

id_lab = tk.Label(detail_frame,text="ID:",font=("Arial",16),bg="lightgray",foreground="black")

id_lab.place(x=20,y=15)

id_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="white",foreground="black")

id_ent.place(x=110,y=17,width=250,height=30)

name_lab = tk.Label(detail_frame,text="Name:",font=("Arial",16),bg="lightgray",foreground="black")

name_lab.place(x=20,y=65)

name_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="white",foreground="black")

name_ent.place(x=110,y=65,width=250,height=30)

gen_lab = tk.Label(detail_frame,text="Gender:",font=("Arial",16),bg="lightgray",foreground="black")

gen_lab.place(x=20,y=113)

gen_ent = ttk.Combobox(detail_frame,font=("Arial",16))

gen_ent["values"] = ("Male","Female","others")

gen_ent.place(x=110,y=113,width=250,height=30)

age_lab = tk.Label(detail_frame,text="Age:",font=("Arial",16),bg="lightgray",foreground="black")

age_lab.place(x=20,y=161)

age_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="white",foreground="black")

age_ent.place(x=110,y=161,width=250,height=30)

ent_lab = tk.Label(detail_frame,text="En-date:",font=("Arial",16),bg="lightgray",foreground="black")

ent_lab.place(x=20,y=209)

ent_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="white",foreground="black")

ent_ent.place(x=110,y=209,width=250,height=30)

mid_lab = tk.Label(detail_frame,text="PhoneNo:",font=("Arial",16),bg="lightgray",foreground="black")

mid_lab.place(x=20,y=257)

mid_ent = tk.Entry(detail_frame,bd=1,font=("Arial",16),bg="white",foreground="black")

mid_ent.place(x=110,y=257,width=250,height=30)

fin_lab = tk.Label(detail_frame,text="Location:",font=("Arial",16),bg="lightgray",foreground="black")

fin_lab.place(x=20,y=305)

fin_ent = tk.Entry(detail_frame,bd=1,font=("arial",16),bg="white",foreground="black")

fin_ent.place(x=110,y=305,width=250,height=30)

gpa_lab =tk.Label(detail_frame,text="Course:",font=("Arial",16),bg="lightgray",foreground="black")

gpa_lab.place(x=20,y=353)

gpa_ent = tk.Entry(detail_frame,bd=1,font=("arial",16),bg="white",foreground="black")

gpa_ent.place(x=110,y=353,width=250,height=30)

#database frame

main_frame = tk.Frame(data_frame,bg="teal",bd=2,relief=tk.GROOVE)

main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=("ID","Name","Gender","Age","EnrollDate","PhoneNo","Location","Course"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("ID",text="ID")
student_table.heading("Name",text="Name")
student_table.heading("Gender",text="Gender")
student_table.heading("Age",text="Age")
student_table.heading("EnrollDate",text="EnrollDate")
student_table.heading("PhoneNo",text="PhoneNo")
student_table.heading("Location",text="Location")
student_table.heading("Course",text="Course")

student_table["show"] = "headings"

student_table.column("ID",width=100)
student_table.column("Name",width=100)
student_table.column("Gender",width=100)
student_table.column("Age",width=100)
student_table.column("EnrollDate",width=100)
student_table.column("PhoneNo",width=100)
student_table.column("Location",width=100)
student_table.column("Course",width=100)

student_table.pack(fill=tk.BOTH, expand=True)

#functions

def add_record():
    
        query = "INSERT INTO students (id, name, gender, age, enroll_date, phone_no, location, course) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (id_ent.get(), name_ent.get(), gen_ent.get(), age_ent.get(), ent_ent.get(), mid_ent.get(), fin_ent.get(), gpa_ent.get())
        db_cursor.execute(query, values)
        db_connection.commit()

        update_treeview()

def delete_record():
    selected_item = student_table.selection()
    if selected_item:
        selected_id = student_table.item(selected_item[0], "values")[0]
        query = "DELETE FROM students WHERE id = %s"
        db_cursor.execute(query, (selected_id,))
        db_connection.commit()

        update_treeview()

def update_record():
    selected_item = student_table.selection()
    if selected_item:
        selected_id = student_table.item(selected_item[0], "values")[0]
    
        query = "UPDATE students SET name = %s, gender = %s, age = %s, enroll_date = %s, phone_no = %s, location = %s, course = %s WHERE id = %s"
        values = (name_ent.get(), gen_ent.get(), age_ent.get(), ent_ent.get(), mid_ent.get(), fin_ent.get(), gpa_ent.get(), selected_id)
        db_cursor.execute(query, values)
        db_connection.commit()

        update_treeview()

def delete_all_records():
        query = "TRUNCATE students"
        db_cursor.execute(query)
        db_connection.commit()
        
        print("All records cleared successfully")
        update_treeview()

def clear_entries():
    id_ent.delete(0, END)
    name_ent.delete(0, END)
    age_ent.delete(0, END)
    gen_ent.delete(0, END)
    ent_ent.delete(0, END)
    mid_ent.delete(0, END)
    fin_ent.delete(0, END)
    gpa_ent.delete(0, END)

def update_treeview():
    student_table.delete(*student_table.get_children())  # Clear the Treeview
    db_cursor.execute("SELECT * FROM students")
    records = db_cursor.fetchall()

    for count, record in enumerate(records):
        tag = "evenrow" if count % 2 == 0 else "oddrow"
        student_table.insert("", "end", iid=count, values=record, tags=(tag,))

def parse_date(date_str):
    try:
        # Attempt to parse the date input with dateutil.parser
        date_obj = parser.parse(date_str, fuzzy=True)
        if date_obj:
            return date_obj.strftime('%Y-%m-%d')  # Format the date as 'YYYY-MM-DD'
        else:
            return None  # Parsing failed
    except ValueError:
        return None

#buttons

btn_frame = tk.Frame(detail_frame, bg="lightgray", bd=0, relief=tk.GROOVE)
btn_frame.place(x=40, y=400, width=310, height=130)

add_btn = tk.Button(btn_frame, text="Add", bd=2, font=("Arial", 13), width=15, command=add_record)
update_btn = tk.Button(btn_frame, text="Update", bd=2, font=("Arial", 13), width=15, command=update_record)
cal_btn = tk.Button(btn_frame, text="Save", bd=2, font=("Arial", 13), width=15, command=update_record)
delete_btn = tk.Button(btn_frame, text="Delete", bd=2, font=("Arial", 13), width=15, command=delete_record)
clear_btn = tk.Button(btn_frame, text="Clear", bd=2, font=("Arial", 13), width=15, command=clear_entries)
delete_all_btn = tk.Button(btn_frame, text="Delete All", bd=2, font=("Arial", 13), width=15, command=delete_all_records)

add_btn.grid(row=0, column=0, padx=2, pady=2)
update_btn.grid(row=0, column=1, padx=2, pady=2)
delete_btn.grid(row=1, column=0, padx=2, pady=2)
delete_all_btn.grid(row=1, column=1, padx=2, pady=2)
clear_btn.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

update_treeview()

