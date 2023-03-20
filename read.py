import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_students, view_all_teachers, view_all_parentlgs, view_all_classes, view_all_subjects, view_all_exams, view_all_grades, view_all_achievements, view_all_faculty, view_all_teaches, view_all_classexam


def read():
    student_result = view_all_students()
    df1 = pd.DataFrame(student_result, columns=['SID', 'Fname', 'Lname', 'Age', 'Gender', 'Street', 'City', 'PIN', 'Blood_Group', 'ClassID'])
    with st.expander("View all Students"):
        st.dataframe(df1)
    
    teacher_result = view_all_teachers()
    df2 = pd.DataFrame(teacher_result, columns=['TID', 'Fname', 'Lname', 'street', 'PIN', 'pno', 'joindate'])
    with st.expander("View all Teachers"):
        st.dataframe(df2)
    
    plg_result = view_all_parentlgs()
    df3 = pd.DataFrame(plg_result, columns=['SID', 'Fname', 'Lname', 'Email', 'Rel_W_Student', 'Address','P_No', 'Occupation'])
    with st.expander("View all Parents / LGs"):
        st.dataframe(df3)
    
    class_result = view_all_classes()
    df4 = pd.DataFrame(class_result, columns=['Std', 'Sec', 'Year', 'ClassID'])
    with st.expander("View all Classes"):
        st.dataframe(df4)
    
    subject_result = view_all_subjects()
    df5 = pd.DataFrame(subject_result, columns=['Sub_ID', 'Name', 'Type', 'descr'])
    with st.expander("View all Subjects"):
        st.dataframe(df5)
    
    exam_result = view_all_exams()
    df6 = pd.DataFrame(exam_result, columns=['Exam_ID', 'Name', 'Type', 'Date', 'Sub_ID'])
    with st.expander("View all Exams"):
        st.dataframe(df6)
    
    grade_result = view_all_grades()
    df7 = pd.DataFrame(grade_result, columns=['SID', 'Exam_ID', 'percentage', 'grade'])
    with st.expander("View all Grades"):
        st.dataframe(df7)
    
    achievement_result = view_all_achievements()
    df8 = pd.DataFrame(achievement_result, columns=['SID', 'ach_name', 'ach_date', 'ach_desc'])
    with st.expander("View all Achievements"):
        st.dataframe(df8)
    
    faculty_result = view_all_faculty()
    df9 = pd.DataFrame(faculty_result, columns=['Sub_ID','TID'])
    with st.expander("View Faculty"):
        st.dataframe(df9)
    
    teaches_result = view_all_teaches()
    df10 = pd.DataFrame(teaches_result, columns=['TID', 'ClassID'])
    with st.expander("View Teacher-Class table"):
        st.dataframe(df10)
    
    classexam_result = view_all_classexam()
    df11 = pd.DataFrame(classexam_result, columns=['ClassID', 'Exam_ID'])
    with st.expander("View Exam-Class table"):
        st.dataframe(df11)
    