import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from query import query

def main():
    st.title("School Management System")
    menu1 = ["Add Entries", "View Database", "Update Entries", "Remove Entries", "Type Query"]
    choice1 = st.sidebar.selectbox("Menu", menu1)

    create_table()
    if choice1 == "Add Entries":
        create()

    elif choice1 == "View Database":
        st.subheader("View Tables:")
        read()

    elif choice1 == "Update Entries":
        update()

    elif choice1 == "Remove Entries":
        delete()

    elif choice1 == "Type Query":
        st.subheader("Enter query:")
        query()

    else:
        st.subheader("About School Management")


if __name__ == '__main__':
    main()