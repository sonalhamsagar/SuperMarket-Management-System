import mysql.connector
import streamlit as st
from crud1 import *
from streamlit_option_menu import option_menu



def main(mycursor,mydb):
    if(st.session_state['loggedIn']):
        st.title("Supermarket Management System")
                                                                                                # selected=option_menu(
        selected=st.sidebar.selectbox("Menu",["Insert","Update","Delete","Read","Employee"])    #         menu_title = None,
                                                                                                #         options = ["Insert","Update","Delete","Query"],
                                                                                                #         orientation="horizontal",
                                                                                                #     )
        if selected=="Insert":
            st.subheader("Insert a record")
            insrt(mycursor,mydb)

        if selected=="Update":
            st.subheader("Update")
            updat(mycursor,mydb)

        if selected=="Delete":
            st.subheader("Delete")
            delet(mycursor,mydb)
        
        if selected=="Read":
            st.subheader("Read")
            read(mycursor)

        if selected=="Employee":
            st.subheader("Employee")
            Employee(mycursor,mydb)

        # if selected=="Query":
        #     st.subheader("Query")        selected=st.sidebar.selectbox("Menu",["Insert","Update","Delete","Read","Employee","Query"])
        #     quer(mycursor)
    else:
        st.error("Invalid Username/Password")

        
     

