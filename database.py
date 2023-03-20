import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_management"
)
c = mydb.cursor()


def create_table():
    c.execute("CREATE table IF NOT EXISTS student (SID varchar(25) NOT NULL, Fname varchar(255), Lname varchar(255),  Age int(3), Gender varchar(225) CHECK (Gender in ('M','F','m','f','Male','Female','male','female','MALE','FEMALE','Unknown','unknown','UNKNOWN')), Street varchar(255), City varchar(255), PIN varchar(15), Blood_Group varchar(5), ClassID int(5), PRIMARY KEY(SID), FOREIGN KEY(ClassID) REFERENCES class(ClassID));")

#Insert Commands
def add_student(SID, Fname, Lname, Age, Gender, Street, City, PIN, Blood_Group, ClassID):
    c.execute('INSERT INTO student (SID, Fname, Lname, Age, Gender, Street, City, PIN, Blood_Group, ClassID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',
              (SID, Fname, Lname, Age, Gender, Street, City, PIN, Blood_Group, ClassID))
    mydb.commit()

def add_teacher(TID, Fname, Lname, street, PIN, pno, joindate):
    c.execute('INSERT INTO teacher (TID, Fname, Lname, street, PIN, pno, joindate) VALUES (%s,%s,%s,%s,%s,%s,%s);',
              (TID, Fname, Lname, street, PIN, pno, joindate))
    mydb.commit()

def add_parentlg(SID, Fname, Lname, Email, Rel_W_Student, Address,P_No, Occupation):
    c.execute('INSERT INTO parent_lg (SID, Fname, Lname, Email, Rel_W_Student, Address,P_No, Occupation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',
              (SID, Fname, Lname, Email, Rel_W_Student, Address,P_No, Occupation))
    mydb.commit()

def add_class(Std, Sec, Year, ClassID):
    c.execute('INSERT INTO class (Std, Sec, Year, ClassID) VALUES (%s,%s,%s,%s);',
              (Std, Sec, Year, ClassID))
    mydb.commit()

def add_subject(Sub_ID, Name, Type, descr):
    c.execute('INSERT INTO subject (Sub_ID, Name, Type, descr) VALUES (%s,%s,%s,%s);',
              (Sub_ID, Name, Type, descr))
    mydb.commit()

def add_exam(Exam_ID, Name, Type, Date, Time, Sub_ID):
    c.execute('INSERT INTO exam (Exam_ID, Name, Type, Date, Time, Sub_ID) VALUES (%s,%s,%s,%s,%s,%s);',
              (Exam_ID, Name, Type, Date, Time, Sub_ID))
    mydb.commit()

def add_grade(SID, Exam_ID, percentage, grade):
    c.execute('INSERT INTO grades (SID, Exam_ID, percentage, grade) VALUES (%s,%s,%s,%s);',
              (SID, Exam_ID, percentage, grade))
    mydb.commit()

def add_achievement(SID, ach_name, ach_date, ach_desc):
    c.execute('INSERT INTO achievements (SID, ach_name, ach_date, ach_desc) VALUES (%s,%s,%s,%s);',
              (SID, ach_name, ach_date, ach_desc))
    mydb.commit()

def add_faculty(Sub_ID,TID):
    c.execute('INSERT INTO faculty (Sub_ID,TID) VALUES (%s,%s);',
              (Sub_ID,TID))
    mydb.commit()

def add_teaches(TID, ClassID):
    c.execute('INSERT INTO teaches (TID, ClassID) VALUES (%s,%s);',
              (TID, ClassID))
    mydb.commit()

def add_classexam(ClassID, Exam_ID):
    c.execute('INSERT INTO class_has_exam (ClassID, Exam_ID) VALUES (%s,%s);',
              (ClassID, Exam_ID))
    mydb.commit()

#View
def view_all_data():
    c.execute('SELECT * FROM student')
    data = c.fetchall()
    return data

def view_all_students():
    c.execute('SELECT * FROM student')
    data = c.fetchall()
    return data

def view_all_teachers():
    c.execute('SELECT * FROM teacher')
    data = c.fetchall()
    return data

def view_all_parentlgs():
    c.execute('SELECT * FROM parent_lg')
    data = c.fetchall()
    return data

def view_all_classes():
    c.execute('SELECT * FROM class')
    data = c.fetchall()
    return data

def view_all_subjects():
    c.execute('SELECT * FROM subject')
    data = c.fetchall()
    return data

def view_all_exams():
    c.execute('SELECT Exam_ID, Name, Type, Date, Sub_ID FROM exam')
    data = c.fetchall()
    return data

def view_all_grades():
    c.execute('SELECT * FROM grades')
    data = c.fetchall()
    return data

def view_all_achievements():
    c.execute('SELECT * FROM achievements')
    data = c.fetchall()
    return data

def view_all_faculty():
    c.execute('SELECT * FROM faculty')
    data = c.fetchall()
    return data

def view_all_teaches():
    c.execute('SELECT * FROM teaches')
    data = c.fetchall()
    return data

def view_all_classexam():
    c.execute('SELECT * FROM class_has_exam')
    data = c.fetchall()
    return data


#Extra
def view_only_student_names():
    c.execute('SELECT Fname, Lname FROM student')
    data = c.fetchall()
    return data

#View IDS
def view_only_student_ids():
    c.execute('SELECT SID FROM student')
    data = c.fetchall()
    return data

def view_only_teacher_ids():
    c.execute('SELECT TID FROM teacher')
    data = c.fetchall()
    return data

def view_only_class_ids():
    c.execute('SELECT ClassID FROM class')
    data = c.fetchall()
    return data

def view_only_exam_ids():
    c.execute('SELECT Exam_ID FROM exam')
    data = c.fetchall()
    return data

def view_only_subject_ids():
    c.execute('SELECT Sub_ID FROM subject')
    data = c.fetchall()
    return data

def view_only_rel():
    c.execute('SELECT distinct(Rel_W_Student) FROM parent_lg')
    data = c.fetchall()
    return data

#Get Details
def get_student_details(SID):
    c.execute('SELECT * FROM student WHERE SID="{}"'.format(SID))
    data = c.fetchall()
    return data

def get_teacher_details(TID):
    c.execute('SELECT * FROM teacher WHERE TID="{}"'.format(TID))
    data = c.fetchall()
    return data

def get_exam_details(Exam_ID):
    c.execute('SELECT * FROM exam WHERE Exam_ID="{}"'.format(Exam_ID))
    data = c.fetchall()
    return data

def get_grade_details(SID,Exam_ID):
    c.execute('SELECT * FROM grades WHERE SID="{}" and Exam_ID="{}"'.format(SID,Exam_ID))
    data = c.fetchall()
    return data

#Edit Details
def edit_student_details(new_SID, new_Fname, new_Lname, new_Age, new_Gender, new_Street, new_City, new_PIN, new_Blood_Group, new_ClassID, SID, Fname, Lname, Age, Gender, Street, City, PIN, Blood_Group, ClassID):
    c.execute("UPDATE student SET SID=%s, Fname=%s, Lname=%s, Age=%s, Gender=%s, Street=%s, City=%s, PIN=%s, Blood_Group=%s, ClassID=%s WHERE SID=%s and Fname=%s and Lname=%s and Age=%s and Gender=%s and Street=%s and City=%s and PIN=%s and Blood_Group=%s and ClassID=%s", (new_SID, new_Fname, new_Lname, new_Age, new_Gender, new_Street, new_City, new_PIN, new_Blood_Group, new_ClassID, SID, Fname, Lname, Age, Gender, Street, City, PIN, Blood_Group, ClassID))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_teacher_details(new_TID, new_Te_Fname,new_Te_Lname, new_Te_street, new_Te_PIN, new_Te_pno, new_joindate, TID, Te_Fname,Te_Lname,Te_street,Te_PIN,Te_pno,joindate):
    c.execute("UPDATE teacher SET TID=%s, Fname=%s, Lname=%s, street=%s, PIN=%s, pno=%s, joindate=%s WHERE TID=%s and Fname=%s and Lname=%s and street=%s and PIN=%s and pno=%s and joindate=%s", (new_TID, new_Te_Fname,new_Te_Lname, new_Te_street, new_Te_PIN, new_Te_pno, new_joindate, TID, Te_Fname,Te_Lname,Te_street,Te_PIN,Te_pno,joindate))
    mydb.commit()
    data = c.fetchall()
    return data

def edit_grade_details(new_SID, new_Exam_ID,new_percentage, new_grade, SID, Exam_ID, percentage, grade):
    c.execute("UPDATE grades SET SID=%s, Exam_ID=%s, percentage=%s, grade=%s WHERE SID=%s and Exam_ID=%s and percentage=%s and grade=%s", (new_SID, new_Exam_ID,new_percentage, new_grade, SID, Exam_ID, percentage, grade))
    mydb.commit()
    data = c.fetchall()
    return data

#Delete data
def delete_student_data(SID):
    c.execute('DELETE FROM student WHERE SID="{}"'.format(SID))
    mydb.commit()

def delete_teacher_data(TID):
    c.execute('DELETE FROM teacher WHERE TID="{}"'.format(TID))
    mydb.commit()

def delete_teaches_data(TID,ClassID):
    c.execute('DELETE FROM teaches WHERE TID="{}" and ClassID="{}"'.format(TID,ClassID))
    mydb.commit()

def delete_exam_for_class(Exam_ID,ClassID):
    c.execute('DELETE FROM class_has_exam WHERE Exam_ID="{}" and ClassID="{}"'.format(Exam_ID,ClassID))
    mydb.commit()

def delete_faculty_data(TID,Sub_ID):
    c.execute('DELETE FROM faculty WHERE TID="{}" and Sub_ID="{}"'.format(TID,Sub_ID))
    mydb.commit()

def delete_grade_data(SID,Exam_ID):
    c.execute('DELETE FROM grades WHERE SID="{}" and Exam_ID="{}"'.format(SID,Exam_ID))
    mydb.commit()

def delete_exam_data(Exam_ID):
    c.execute('DELETE FROM exam WHERE Exam_ID="{}"'.format(Exam_ID))
    mydb.commit()

def delete_class_data(ClassID):
    c.execute('DELETE FROM class WHERE ClassID="{}"'.format(ClassID))
    mydb.commit()

def delete_subject_data(Sub_ID):
    c.execute('DELETE FROM subject WHERE Sub_ID="{}"'.format(Sub_ID))
    mydb.commit()

def delete_parentlg_data(SID,Rel_W_Student):
    c.execute('DELETE FROM parent_lg WHERE SID="{}" and Rel_W_Student="{}"'.format(SID,Rel_W_Student))
    mydb.commit()


def disp_query(query):
    c.execute('{}'.format(query))
    data = c.fetchall()
    return data

