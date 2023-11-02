import mysql.connector
import streamlit as st
from crud1 import *
from streamlit_option_menu import option_menu
from mainpg import *

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()

mydb = mysql.connector.connect(

     host="localhost",
     user="root",
     database="super_market"
)

# @st.experimental_memo
# def get_img_as_base64(file):
#     with open(file,"rb") as f:
#         data=f.read()
#     return base64.b16encode(data).decode()
#imag=get_img_as_base64("image.jpg")

page_bg_img="""
<style>
[data-testid="stAppViewContainer"]
{
    background-image:url("https://wallpaperaccess.com/full/1624848.jpg");
    background-repeat: no-repeat;
    background-size: 100% 100%;
}
[data-testid="stVerticalBlock"]
{
    background-color: black;
    opacity:0.8;
    border-radius: 25px;
    position: relative;
}
[data-testid="stHeader"]
{
    background-color: lightblue;
    opacity: 0.1;
}
[class="css-10trblm e16nr0p30"]     
{
    color: red;
    text-align: center;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

mycursor = mydb.cursor(dictionary=True)



def show_main_page():
     
    main(mycursor,mydb)

def login(user,password):
    userr=str(user)
    passwordd=str(password)
    mycursor.execute("Select admin_name,pswrd from admin where admin_name=(%s) and pswrd=(%s)",(userr,passwordd))
    x=mycursor.fetchall()
    if(x):
        return 1
    else:
        return 0

def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False

def show_logout_page():
    loginSection.empty()
    with logOutSection:
        col1, col2, col3,col4,col5,col6,col7= st.columns(7)
        with col7:
            st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)

def LoggedIn_Clicked(userName, password):
    if login(userName, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name or password")

def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label=" ", value="", placeholder="Enter your user name",label_visibility="visible")
            password = st.text_input (label=" ", value="",placeholder="Enter password", type="password",label_visibility="visible")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))
            

with headerSection:
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.title("Login Page")
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            #st.success("Login Successfull")
            show_logout_page()   
            show_main_page()  
        else:
            st.title("Login Page")
            show_login_page()


    

    
