import streamlit as st
from database import add_student, add_teacher, add_parentlg, add_class, add_subject, add_exam, add_grade, add_achievement, add_faculty, add_teaches, add_classexam
from streamlit_option_menu import option_menu

def create():
    with st.sidebar:
        option = option_menu(
        menu_title=None,
        options=["Student", "Teacher", "Parent / LG", "Class", "Subject", "Exams", "Grades", "Achievements",'Faculty','Teacher to Class','Exam to Class'],
        icons=None)
    
    if option == "Student":
        st.subheader("Enter Student Details:")
        col1, col2 = st.columns(2)
        with col1:
            SID = st.text_input("SID:")
            St_Fname = st.text_input("First Name:")
            St_Lname = st.text_input("Last Type:")
            Age=st.number_input("Age:")
            Gender=st.text_input("Gender:")
        with col2:
            St_Street = st.text_input("Street:")
            St_City = st.text_input("City:")
            St_PIN = st.text_input("PIN:")
            Blood_Group = st.text_input("Blood Group:")
            ClassID = st.number_input("Class ID:")

        if st.button("Add Student"):
            add_student(SID, St_Fname, St_Lname, Age, Gender, St_Street, St_City, St_PIN, Blood_Group, ClassID)
            st.success("Successfully added Student: {}".format(SID))
    
    if option == "Teacher":
        st.subheader("Enter Teacher Details:")
        col1, col2 = st.columns(2)
        with col1:
            TID = st.text_input("TID:")
            Te_Fname = st.text_input("First Name:")
            Te_Lname = st.text_input("Last Type:")
            Te_street = st.text_input("Street:")
        with col2:
            Te_PIN = st.text_input("PIN:")
            Te_pno = st.text_input("Phone Number:")
            joindate = st.date_input("Date of Joining:")
        if st.button("Add Teacher"):
            add_teacher(TID, Te_Fname, Te_Lname, Te_street, Te_PIN, Te_pno, joindate)
            st.success("Successfully added teacher: {}".format(TID))
    
    if option == "Parent / LG":
        st.subheader("Enter Parent / LG Details:")
        col1, col2 = st.columns(2)
        with col1:
            SID = st.text_input("SID:")
            PLG_Fname = st.text_input("First Name:")
            PLG_Lname = st.text_input("Last Type:")
            PLG_Email = st.text_input("Email:")
        with col2:
            Rel_W_Student = st.text_input("Relation with student:")
            PLG_Address = st.text_input("Address:")
            PLG_P_No = st.text_input("Phone Number:")
            PLG_Occupation = st.text_input("Occupation:")
        if st.button("Add Parent / LG"):
            add_parentlg(SID, PLG_Fname, PLG_Lname, PLG_Email, Rel_W_Student, PLG_Address, PLG_P_No, PLG_Occupation)
            st.success("Successfully added parent / lg for: {}".format(SID))
    
    if option == "Class": 
        st.subheader("Enter Class Details:")
        ClassID = st.text_input("Class ID:")
        Std = st.text_input("Standard:")
        Sec = st.text_input("Section:")
        Year = st.text_input("Year:")
        if st.button("Add Class"):
            add_class(Std, Sec, Year, ClassID)
            st.success("Successfully added class: {}".format(ClassID))

    
    if option == "Subject":
        st.subheader("Enter Subject Details:")
        Sub_ID = st.text_input("Subject ID:")
        Sub_Name = st.text_input("Name:")
        Sub_Type = st.text_input("Type:")
        Sub_descr = st.text_input("Description:")
        if st.button("Add Subject"):
            add_subject(Sub_ID, Sub_Name, Sub_Type, Sub_descr)
            st.success("Successfully added Subject: {}".format(Sub_ID))

  
    if option == "Exams":
        st.subheader("Enter Exam Details:")
        Exam_ID = st.text_input("Exam ID:")
        Exam_Name = st.text_input("Name:")
        Exam_Type = st.text_input("Type:")
        Exam_Date = st.date_input("Date:")
        Exam_Time = st.time_input("Time:")
        E_Sub_ID = st.text_input("Subject ID:")
        if st.button("Add Exam"):
            add_exam(Exam_ID, Exam_Name, Exam_Type, Exam_Date, Exam_Time, E_Sub_ID)
            st.success("Successfully added exam: {}".format(Exam_ID))


    if option == "Grades":
        st.subheader("Enter Grade Details:")
        SID=st.text_input("SID:")
        Exam_ID = st.text_input("Exam ID:")
        percentage = st.number_input("Percentage:")
        grade = st.text_input("Grade:")
        if st.button("Add Grade"):
            add_grade(SID, Exam_ID, percentage, grade)
            st.success("Successfully added Grade for: {} - {}".format(SID,Exam_ID))
 
    if option == "Achievements":
        st.subheader("Enter Achievement Details:")
        SID=st.text_input("SID:")
        ach_name = st.text_input("Achievement Name:")
        ach_date = st.date_input("Date:")
        ach_desc = st.text_input("Description:")
        if st.button("Add Achievement"):
            add_achievement(SID, ach_name, ach_date, ach_desc)
            st.success("Successfully added Achievement for: {}".format(SID))
     
    if option == "Faculty":
        st.subheader("Enter Faculty Details:")
        Sub_ID=st.text_input("Subject ID:")
        TID = st.text_input("Teacher ID:")
        if st.button("Add Faculty"):
            add_faculty(Sub_ID,TID)
            st.success("Successfully added Faculty for: {} - {}".format(Sub_ID,TID))


    if option == "Teacher to Class":
        st.subheader("Enter Teacher and Class Details:")
        ClassID=st.text_input("Class ID:")
        TID = st.text_input("Teacher ID:")
        if st.button("Add Teacher to Class"):
            add_teaches(TID, ClassID)
            st.success("Successfully assigned Teacher {} to Class {}".format(TID, ClassID))

    if option == "Exam to Class":
        st.subheader("Enter Exam and Class Details:")
        ClassID=st.text_input("Class ID:")
        Exam_ID = st.text_input("Exam ID:")
        if st.button("Add Exam to Class"):
            add_classexam(ClassID, Exam_ID)
            st.success("Successfully assigned Exam {} to Class {}".format(Exam_ID,ClassID))