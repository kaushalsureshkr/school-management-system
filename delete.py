import pandas as pd
import streamlit as st
from database import view_all_students, view_all_teachers, view_all_parentlgs, view_all_classes, view_all_subjects, view_all_exams, view_all_grades, view_all_achievements, view_all_faculty, view_all_teaches, view_all_classexam, view_only_student_names, view_only_student_ids,view_only_teacher_ids,view_only_rel,view_only_subject_ids,view_only_class_ids,view_only_exam_ids, delete_student_data,delete_teaches_data, delete_exam_for_class,delete_faculty_data,delete_grade_data,delete_exam_data,delete_class_data,delete_subject_data,delete_parentlg_data,delete_teacher_data
from streamlit_option_menu import option_menu

def delete():
    with st.sidebar:
        option = option_menu(
        menu_title=None,
        options=["Student", "Teacher", "Parent / LG", "Class", "Subject", "Exams", "Grades",'Faculty','Teacher to Class','Exam to Class'],
        icons=None)

    if option == "Student":
        st.subheader("Delete Student:")
        result = view_all_students()
        df = pd.DataFrame(result, columns=['SID', 'Fname', 'Lname', 'Age', 'Gender', 'Street', 'City', 'PIN', 'Blood_Group', 'ClassID'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_students = [i[0] for i in view_only_student_ids()]
        selected_student = st.selectbox("Student to Delete", list_of_students)
        st.warning("Do you want to delete ::{}? Student data will be deleted from all tables.".format(selected_student))
        if st.button("Delete student"):
            delete_student_data(selected_student)
            st.success("Student has been deleted successfully")
        new_result = view_all_students()
        df2 = pd.DataFrame(new_result, columns=['SID', 'Fname', 'Lname', 'Age', 'Gender', 'Street', 'City', 'PIN', 'Blood_Group', 'ClassID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Teacher":
        st.subheader("Delete Teacher:")
        teacher_result = view_all_teachers()
        df2 = pd.DataFrame(teacher_result, columns=['TID', 'Fname', 'Lname', 'street', 'PIN', 'pno', 'joindate'])
        with st.expander("View all Teachers"):
            st.dataframe(df2)

        list_of_teachers = [i[0] for i in view_only_teacher_ids()]
        selected_teacher = st.selectbox("Teacher", list_of_teachers)
        st.warning("Do you want to delete ::{}? Teacher data will be deleted from all tables.".format(selected_teacher))
        if st.button("Delete teacher"):
            delete_teacher_data(selected_teacher)
            st.success("Teacher has been deleted successfully")
        new_result = view_all_teachers()
        df2 = pd.DataFrame(new_result, columns=['TID', 'Fname', 'Lname', 'street', 'PIN', 'pno', 'joindate'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Parent / LG":
        st.subheader("Delete Parent / LG:")
        plg_result = view_all_parentlgs()
        df3 = pd.DataFrame(plg_result, columns=['SID', 'Fname', 'Lname', 'Email', 'Rel_W_Student', 'Address','P_No', 'Occupation'])
        with st.expander("View all Parents / LGs"):
            st.dataframe(df3)

        list_of_students = [i[0] for i in view_only_student_ids()]
        selected_student = st.selectbox("Student", list_of_students)
        list_of_rel = [i[0] for i in view_only_rel()]
        selected_rel = st.selectbox("Relation", list_of_rel)
        st.warning("Do you want to delete {} of {}?".format(selected_rel,selected_student))
        if st.button("Delete parent / lg"):
            delete_parentlg_data(selected_student,selected_rel)
            st.success("Parent / LG has been deleted successfully")
        new_result = view_all_parentlgs()
        df2 = pd.DataFrame(new_result, columns=['SID', 'Fname', 'Lname', 'Email', 'Rel_W_Student', 'Address','P_No', 'Occupation'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Class":
        st.subheader("Delete Class:")
        class_result = view_all_classes()
        df4 = pd.DataFrame(class_result, columns=['Std', 'Sec', 'Year', 'ClassID'])
        with st.expander("View all Classes"):
            st.dataframe(df4)   
        list_of_classes = [i[0] for i in view_only_class_ids()]
        selected_class = st.selectbox("Class", list_of_classes)
        st.warning("Do you want to delete ::{}? Class data will be deleted from all tables.".format(selected_class))
        if st.button("Delete class"):
            delete_class_data(selected_class)
            st.success("Class has been deleted successfully")
        new_result = view_all_classes()
        df2 = pd.DataFrame(new_result, columns=['Std', 'Sec', 'Year', 'ClassID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Subject":
        st.subheader("Delete Subject:")
        subject_result = view_all_subjects()
        df5 = pd.DataFrame(subject_result, columns=['Sub_ID', 'Name', 'Type', 'descr'])
        with st.expander("View all Subjects"):
            st.dataframe(df5)

        list_of_subjects = [i[0] for i in view_only_subject_ids()]
        selected_subject = st.selectbox("Subject", list_of_subjects)
        st.warning("Do you want to delete ::{}? Subject data will be deleted from all tables.".format(selected_subject))
        if st.button("Delete subject"):
            delete_subject_data(selected_subject)
            st.success("Subject has been deleted successfully")
        new_result = view_all_subjects()
        df2 = pd.DataFrame(new_result, columns=['Sub_ID', 'Name', 'Type', 'descr'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Exams":
        st.subheader("Delete Exam:")
        exam_result = view_all_exams()
        df6 = pd.DataFrame(exam_result, columns=['Exam_ID', 'Name', 'Type', 'Date', 'Sub_ID'])
        with st.expander("View all Exams"):
            st.dataframe(df6)

        list_of_exams = [i[0] for i in view_only_exam_ids()]
        selected_exam = st.selectbox("Exam", list_of_exams)
        st.warning("Do you want to delete ::{}? Exam data will be deleted from all tables.".format(selected_exam))
        if st.button("Delete exam"):
            delete_exam_data(selected_exam)
            st.success("Exam has been deleted successfully")
        new_result = view_all_exams()
        df2 = pd.DataFrame(new_result, columns=['Exam_ID', 'Name', 'Type', 'Date', 'Sub_ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Grades":
        st.subheader("Delete Grade:")
        grade_result = view_all_grades()
        df7 = pd.DataFrame(grade_result, columns=['SID', 'Exam_ID', 'percentage', 'grade'])
        with st.expander("View all Grades"):
            st.dataframe(df7)

        list_of_students = [i[0] for i in view_only_student_ids()]
        selected_student = st.selectbox("Student to Delete", list_of_students)
        list_of_exams = [i[0] for i in view_only_exam_ids()]
        selected_exam = st.selectbox("Exam", list_of_exams)
        st.warning("Do you want to delete grade of {} for {}?".format(selected_student,selected_exam))
        if st.button("Delete grade"):
            delete_grade_data(selected_student,selected_exam)
            st.success("Grade has been deleted successfully")
        new_result = view_all_grades()
        df2 = pd.DataFrame(new_result, columns=['SID', 'Exam_ID', 'percentage', 'grade'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Faculty":
        st.subheader("Delete Faculty:")
        faculty_result = view_all_faculty()
        df9 = pd.DataFrame(faculty_result, columns=['Sub_ID','TID'])
        with st.expander("View Faculty"):
            st.dataframe(df9)

        list_of_subjects = [i[0] for i in view_only_subject_ids()]
        selected_subject = st.selectbox("Subject", list_of_subjects)
        list_of_teachers = [i[0] for i in view_only_teacher_ids()]
        selected_teacher = st.selectbox("Teacher", list_of_teachers)
        st.warning("Do you want to delete {} for {}?".format(selected_teacher,selected_subject))
        if st.button("Delete Faculty"):
            delete_faculty_data(selected_teacher,selected_subject)
            st.success("Faculty has been deleted successfully")
        new_result = view_all_faculty()
        df2 = pd.DataFrame(new_result, columns=['Sub_ID','TID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Teacher to Class":
        st.subheader("Delete Teacher to Class:")
        teaches_result = view_all_teaches()
        df10 = pd.DataFrame(teaches_result, columns=['TID', 'ClassID'])
        with st.expander("View Teacher-Class table"):
            st.dataframe(df10)

        list_of_classes = [i[0] for i in view_only_class_ids()]
        selected_class = st.selectbox("Class", list_of_classes)
        list_of_teachers = [i[0] for i in view_only_teacher_ids()]
        selected_teacher = st.selectbox("Teacher", list_of_teachers)
        st.warning("Do you want to delete {} for {}?".format(selected_teacher,selected_class))
        if st.button("Delete Teacher for Class"):
            delete_teaches_data(selected_teacher,selected_class)
            st.success("Teacher for Class has been deleted successfully")
        new_result = view_all_teaches()
        df2 = pd.DataFrame(new_result, columns=['TID', 'ClassID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    
    if option == "Exam to Class":
        st.subheader("Delete Exam to Class:")
        classexam_result = view_all_classexam()
        df11 = pd.DataFrame(classexam_result, columns=['ClassID', 'Exam_ID'])
        with st.expander("View Exam-Class table"):
            st.dataframe(df11)

        list_of_classes = [i[0] for i in view_only_class_ids()]
        selected_class = st.selectbox("Class", list_of_classes)
        list_of_exams = [i[0] for i in view_only_exam_ids()]
        selected_exam = st.selectbox("Exam", list_of_exams)
        st.warning("Do you want to delete {} for {}?".format(selected_exam,selected_class))
        if st.button("Delete Exam for Class"):
            delete_exam_for_class(selected_exam,selected_class)
            st.success("Exam for class has been deleted successfully")
        new_result = view_all_classexam()
        df2 = pd.DataFrame(new_result, columns=['ClassID', 'Exam_ID'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    