import datetime
from streamlit_option_menu import option_menu
import pandas as pd
import streamlit as st
from database import view_all_students, view_all_teachers, view_all_grades, view_only_student_ids,view_only_teacher_ids,view_only_exam_ids, get_student_details,get_teacher_details,get_grade_details, edit_student_details,edit_teacher_details,edit_grade_details


def update():
    with st.sidebar:
        option = option_menu(
        menu_title=None,
        options=["Student", "Teacher", "Grades"],
        icons=None)

    if option == "Student":
        st.subheader("Edited Student Details:")
        result = view_all_students()
        # st.write(result)
        df = pd.DataFrame(result, columns=['SID', 'Fname', 'Lname', 'Age', 'Gender', 'Street', 'City', 'PIN', 'Blood_Group', 'ClassID'])
        with st.expander("Current students"):
            st.dataframe(df)
        list_of_students = [i[0] for i in view_only_student_ids()]
        selected_student = st.selectbox("Student to Edit", list_of_students)
        selected_result = get_student_details(selected_student)
        # st.write(selected_result)
        if selected_result:
            SID = selected_result[0][0]
            Fname = selected_result[0][1]
            Lname = selected_result[0][2]
            Age = selected_result[0][3]
            Gender = selected_result[0][4]
            Street = selected_result[0][5]
            City = selected_result[0][6]
            PIN = selected_result[0][7]
            Blood_Group = selected_result[0][8]
            ClassID = selected_result[0][9]

            # Layout of Create

            col1, col2 = st.columns(2)
            
            with col1:
                new_SID = st.text_input("SID:",SID)
                new_Fname = st.text_input("First Name:",Fname)
                new_Lname = st.text_input("Last Type:",Lname)
                new_Age=st.text_input("Age:",Age)
                new_Gender=st.text_input("Gender:",Gender)
            with col2:
                new_Street = st.text_input("Street:",Street)
                new_City = st.text_input("City:",City)
                new_PIN = st.text_input("PIN:",PIN)
                new_Blood_Group = st.text_input("Blood Group:",Blood_Group)
                new_ClassID = st.number_input("Class ID:",ClassID)

            if st.button("Update Student"):
                edit_student_details(new_SID, new_Fname,new_Lname, new_Age, new_Gender, new_Street, new_City, new_PIN, new_Blood_Group, new_ClassID, SID, Fname,Lname,  Age, Gender, Street, City, PIN, Blood_Group, ClassID)
                st.success("Successfully updated:: {} to ::{}".format(SID, new_SID))

        result2 = view_all_students()
        df2 = pd.DataFrame(result2, columns=['SID', 'Fname', 'Lname', 'Age', 'Gender', 'Street', 'City', 'PIN', 'Blood_Group', 'ClassID'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    if option == "Teacher":
        st.subheader("Edited Teacher Details:")
        result = view_all_teachers()
        # st.write(result)
        df = pd.DataFrame(result, columns=['TID', 'Fname', 'Lname', 'street', 'PIN', 'pno', 'joindate'])
        with st.expander("Current teachers"):
            st.dataframe(df)
        list_of_teachers = [i[0] for i in view_only_teacher_ids()]
        selected_teacher = st.selectbox("Teacher to Edit", list_of_teachers)
        selected_result = get_teacher_details(selected_teacher)
        # st.write(selected_result)
        if selected_result:
                TID = selected_result[0][0]
                Te_Fname = selected_result[0][1]
                Te_Lname = selected_result[0][2]
                Te_street = selected_result[0][3]
                Te_PIN = selected_result[0][4]
                Te_pno = selected_result[0][5]
                joindate = selected_result[0][6]

                col1, col2 = st.columns(2)
                
                with col1:
                    new_TID = st.text_input("TID:",TID)
                    new_Te_Fname = st.text_input("First Name:",Te_Fname)
                    new_Te_Lname = st.text_input("Last Type:",Te_Lname)
                    new_Te_street = st.text_input("Street:",Te_street)
                with col2:
                    new_Te_PIN = st.text_input("PIN:",Te_PIN)
                    new_Te_pno = st.text_input("Phone Number:",Te_pno)
                    new_joindate = st.date_input("Date of Joining:",joindate)

        if st.button("Update Teacher"):
                edit_teacher_details(new_TID, new_Te_Fname,new_Te_Lname, new_Te_street, new_Te_PIN, new_Te_pno, new_joindate, TID, Te_Fname,Te_Lname,Te_street,Te_PIN,Te_pno,joindate)
                st.success("Successfully updated:: {} to ::{}".format(TID, new_TID))

        result2 = view_all_teachers()
        df2 = pd.DataFrame(result2, columns=['TID', 'Fname', 'Lname', 'street', 'PIN', 'pno', 'joindate'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Grades": 
        st.subheader("Edited Grade Details:")
        result = view_all_grades()
        # st.write(result)
        df = pd.DataFrame(result, columns=['SID', 'Exam_ID', 'percentage', 'grade'])
        with st.expander("Current grade"):
            st.dataframe(df)
        list_of_exams = [i[0] for i in view_only_exam_ids()]
        selected_exam = st.selectbox("Grade to Edit", list_of_exams)
        list_of_students = [i[0] for i in view_only_student_ids()]
        selected_student = st.selectbox("Student to Edit", list_of_students)
        selected_result = get_grade_details(selected_student,selected_exam)
        # st.write(selected_result)
        if selected_result:
                SID = selected_result[0][0]
                Exam_ID = selected_result[0][1]
                percentage = selected_result[0][2]
                grade = selected_result[0][3]

                new_SID=st.text_input("SID:",SID)
                new_Exam_ID = st.text_input("Exam ID:",Exam_ID)
                new_percentage = st.text_input("Percentage:",float(percentage))
                new_grade = st.text_input("Grade:",grade)

        if st.button("Update Grade"):
                edit_grade_details(new_SID, new_Exam_ID,new_percentage, new_grade, SID, Exam_ID, percentage, grade)
                st.success("Successfully updated grade of {} for exam {}".format(SID, Exam_ID))

        result2 = view_all_grades()
        df2 = pd.DataFrame(result2, columns=['SID', 'Exam_ID', 'percentage', 'grade'])
        with st.expander("Updated data"):
            st.dataframe(df2)