import streamlit as st
import pandas as pd
import mysql.connector
import time
from datetime import date
from streamlit_option_menu import option_menu



def insrt(mycursor,mydb):   
    selected=option_menu(
        menu_title = "Choose the table",
        options = ["Category","Offers","Employee"],      
        orientation="vertical",
    )
    if(selected=="Category"):
        with st.form(key="form1"):
            categorId=st.number_input('Enter the category id')
            catName =st.text_input(label='Enter the category name')
            submit=st.form_submit_button("Insert")

    if(selected=="Offers"):
        with st.form(key="form2"):
            # mycursor.execute("Select * from product")
            # df=pd.DataFrame(mycursor.fetchall())
            #st.table(df)
            prod_id= st.number_input('Enter the product id')      
            mycursor.execute("Select * from category")
            df=pd.DataFrame(mycursor.fetchall())
            #st.table(df)
            cat_id= st.selectbox('Enter the category id',df['cat_id'])
            discount=st.number_input('Enter the discount')
            validity=st.date_input('Enter the validity')  #date format yyyy-mm-dd
            submit=st.form_submit_button("Insert")
    if(selected=="Employee"):
        with st.form(key="form3"):
            emp_id=st.number_input("Select the employee_id to be inserted")
            emp_name=st.text_input("Input the employee name")
            ph_no=int(st.number_input("Enter the Phone Number of the employee"))
            address=st.text_input("Enter the address of employee")
            salary=st.number_input("Enter the salary of the employee")
            mycursor.execute("Select * from admin")
            df1=pd.DataFrame(mycursor.fetchall())
            admin_id=st.selectbox("Select the admin_id to be updated[admin_id]",df1['admin_id'])
            submit=st.form_submit_button("Insert")
    if(submit):
        if(selected=="Category"):
            try:
                #str1=f"insert into category values ({categorId},'{catName}')"
                mycursor.execute("insert into category values (%s,%s)",(categorId,catName))
                st.info("Insertion successful!!")
                mydb.commit()
            except mysql.connector.Error as e:
                st.warning(e)
        if(selected=="Offers"):
            try:
                #str1=f"insert into offers values ({prod_id},{cat_id},{discount},{validity})"
                mycursor.execute("insert into offers values (%s,%s,%s,%s)",(int(prod_id),int(cat_id),int(discount),validity))
                st.info("Insertion successful!!")
                mydb.commit()
            except mysql.connector.Error as e:
                st.warning(e)
        if(selected=="Employee"):
            try:
                #str1=f"insert into offers values ({prod_id},{cat_id},{discount},{validity})"
                mycursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s)",(int(emp_id),emp_name,int(ph_no),address,int(salary),int(admin_id)))
                st.info("Insertion successful!!")
                mydb.commit()
            except mysql.connector.Error as e:
                st.warning(e)
        
# def quer(mycursor):
#     with st.form(key="form1"):
#         str1=st.text_area("Enter the query here:")
#         submit=st.form_submit_button("Submit")
#         if(submit):
#             try:
#                 mycursor.execute(str1)
#                 df=pd.DataFrame(mycursor.fetchall())
#                 st.table(df)
#             except mysql.connector.Error as e:
#                 st.warning(e)


def updat(mycursor,mydb):
    selected=option_menu(
        menu_title = "Choose the table",
        options = ["Employee","Offers"],      
        orientation="horizontal",
    )
    if(selected=="Employee"):
        st.subheader("Update operation for Employee table")
        mycursor.execute("Select * from employee")
        st.write("Before updation")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form1"):
            str2="SELECT EXISTS (SELECT 1 FROM employee)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM employee)']):
                emp_id=st.selectbox("Select the employee_id to be updated[emp_id]",df['emp_id'])
                emp_name=st.text_input("Input the updated employee name")
                ph_no=int(st.number_input("Enter the updated Phone Number of the employee"))
                address=st.text_input("Enter the updated address of employee")
                salary=st.number_input("Enter the updated salary of the employee")
                mycursor.execute("Select * from admin")
                df1=pd.DataFrame(mycursor.fetchall())
                admin_id=st.selectbox("Select the admin_id to be updated[admin_id]",df1['admin_id'])
                submit=st.form_submit_button("Update")
                if(submit):
                    #str1=f"update employee set emp_name={emp_name},ph_no={ph_no},address={address},salary={salary},admin_id={admin_id} where emp_id={emp_id}"
                    try:
                        mycursor.execute("update employee set emp_name=%s,ph_no=%s,address=%s,salary=%s,admin_id=%s where emp_id=%s",(emp_name,ph_no,address,salary,admin_id,emp_id))
                        mydb.commit()
                        st.info("Updation successful")
                        st.write("After updation")
                        mycursor.execute("Select * from employee")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()
    if(selected=="Offers"):
        st.subheader("Update operation for Offers table")
        mycursor.execute("Select * from offers")
        st.write("Before updation")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form2"):
            str2="SELECT EXISTS (SELECT 1 FROM offers)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM offers)']):
                prod_id=st.selectbox("Select the product_id to be updated[prod_id]",df['prod_id'])
                cat_id=st.selectbox("Select the category_id to be updated",df['cat_id'])
                discount= st.number_input('Enter the discount rate')
                validity=st.date_input("Enter the updated validity")
                submit=st.form_submit_button("Update")
                if(submit):
                    #str1=f"update location set province='{province}',city='{city}' where location_id={location_id}"
                    try:
                        mycursor.execute("update offers set cat_id=%s,discount=%s,validity=%s where prod_id=%s",(cat_id,discount,validity,prod_id))
                        mydb.commit()
                        st.info("Updation successful")
                        st.write("After updation")
                        mycursor.execute("Select * from offers")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()


def delet(mycursor,mydb):
    selected=option_menu(
        menu_title = "Choose the table",
        options = ["Category","Employee"],      
        orientation="horizontal",
    )
    if(selected=="Category"):
        st.subheader("Delete operation available for Category table")
        mycursor.execute("Select * from category")
        st.write("Before deletion")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form1"):
            str2="SELECT EXISTS (SELECT 1 FROM category)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM category)']):
                select=st.selectbox("Select the Category to be deleted (CAT_ID)",df['cat_id'])
                submit=st.form_submit_button("Delete")
                if(submit):
                    try:
                        str1=f"delete from category where cat_id= {select}"
                        mycursor.execute(str1)
                        #mycursor.execute("delete from product where cat_id=%s",(select))
                        mydb.commit()
                        st.info("Deletion successful")
                        st.write("After deletion")
                        mycursor.execute("Select * from category")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()
    if(selected=="Employee"):
        st.subheader("Delete operation available for Employee Table")
        mycursor.execute("Select * from employee")
        st.write("Before deletion")
        df=pd.DataFrame(mycursor.fetchall())
        st.table(df)
        with st.form("form2"):
            str2="SELECT EXISTS (SELECT 1 FROM employee)"
            mycursor.execute(str2)
            if(mycursor.fetchone()['EXISTS (SELECT 1 FROM employee)']):
                select=st.selectbox("Select the employee Details to be deleted (emp_id)",df['emp_id'])
                submit=st.form_submit_button("Delete")
                if(submit):
                    try:
                        str1=f"delete from employee where emp_id= {select}"
                        mycursor.execute(str1)
                        mydb.commit()
                        st.info("Deletion successful")
                        st.write("After deletion")
                        mycursor.execute("Select * from employee")
                        df=pd.DataFrame(mycursor.fetchall())
                        st.table(df)
                    except mysql.connector.Error as e:
                        st.warning(e)
                        st.experimental_rerun()
                        
def read(mycursor):
    with st.form(key="form1"):
        mycursor.execute("show tables")
        df=pd.DataFrame(mycursor.fetchall())
        str1=st.selectbox('Select the table to view',df["Tables_in_super_market"])
        str2=f"select * from {str1}"
        submit=st.form_submit_button("Submit")
        if(submit):
            try:
                mycursor.execute(str2)
                df=pd.DataFrame(mycursor.fetchall())
                st.table(df)
            except mysql.connector.Error as e:
                st.warning(e)

# def prodcid(catid,mycursor):
#     if(catid!=-1):
#         mycursor.execute(f"Select * from product p,category c where p.cat_id=c.cat_id")
#         df=pd.DataFrame(mycursor.fetchall())
#         #st.table(df)
#         df=df[df['cat_id'] == catid]
#         df=(list(df)).append(-1)
#         prod_id=st.selectbox('Select the product id',df,df[len(df)-2])

        

def Employee(mycursor,mydb):
    selected=option_menu(
        menu_title = "Employee Portal",
        options = ["Insert","Update","Delete"],      
        orientation="horizontal",
    )
    if(selected=="Insert"):
        col1,col2=st.columns(2)
        with col1:
            selected=option_menu(
                menu_title = "Choose the table",
                options = ["Product","Offers","Customer"],      
                orientation="vertical",
            )
        if(selected=="Offers"):
            with st.form(key="form2"):
            # mycursor.execute("Select * from product")
            # df=pd.DataFrame(mycursor.fetchall())
            #st.table(df)
                prod_id= st.number_input('Enter the product id')      
                mycursor.execute("Select * from category")
                df=pd.DataFrame(mycursor.fetchall())
            #st.table(df)
                cat_id= st.selectbox('Enter the category id',df['cat_id'])
                discount=st.number_input('Enter the discount')
                validity=st.date_input('Enter the validity')  #date format yyyy-mm-dd
                submit=st.form_submit_button("Insert")    
        # if(selected=="Category"):
        #     with st.form(key="form1"):
        #         categorId=st.number_input('Enter the category id')
        #         catName =st.text_input(label='Enter the category name')
        #         submit=st.form_submit_button("Insert")

        if(selected=="Product"):
            with st.form(key="form2"):
                # mycursor.execute("Select * from product")
                # df=pd.DataFrame(mycursor.fetchall())
                # #st.table(df)
                prod_id= st.number_input('Enter the product id')
                prod_name=st.text_input('Enter the product name')     
                mycursor.execute("Select * from category")
                df=pd.DataFrame(mycursor.fetchall())
                #st.table(df)
                cat_id= st.selectbox('Enter the category id',df['cat_id'])
                price=st.number_input('Enter the price')
                submit=st.form_submit_button("Insert")
        if(selected=="Customer"):
            try:
                mycursor.execute("Select * from category")
                df1=pd.DataFrame(mycursor.fetchall())
                #df1.loc[len(df1)]=[' ',' ']
                # st.table(df1)
                df1=list(df1["cat_id"])
                cat_id= st.selectbox('Enter the category id',df1)
                mycursor.execute(f"Select * from product p,category c where p.cat_id=c.cat_id and c.cat_id={cat_id}")
                df=pd.DataFrame(mycursor.fetchall())
                if(df.empty!=True):
                    prod_id=st.selectbox('Select the product id',df)
                    str3=f"Select price from product where prod_id={prod_id}"
                    mycursor.execute(str3)  #"Select price from product where prod_id=%s",(prod_id)
                    df3=pd.DataFrame(mycursor.fetchall())
                    price=st.selectbox("Select the price",df3['price'])
                with st.form(key="form3"):
                    cust_id=st.number_input('Enter the customer id')
                    cust_name=st.text_input('Enter the customer name')
                    ph_no=st.number_input('Enter the phone number')
                    address=st.text_input('Enter the address')
                    pay_mode=st.text_input("Enter the payment mode")
                    mycursor.execute("Select * from employee")
                    df2=pd.DataFrame(mycursor.fetchall())
                    emp_id=st.selectbox("Select the employee id",df2['emp_id'])
                    #emp_id=st.number_input('Enter the employee id')
                    submit=st.form_submit_button("Print")
            except mysql.connector.Error as e:
                st.warning(e)
        if(submit):
            if(selected=="Offers"):
                try:
                #str1=f"insert into offers values ({prod_id},{cat_id},{discount},{validity})"
                    mycursor.execute("insert into offers values (%s,%s,%s,%s)",(int(prod_id),int(cat_id),int(discount),validity))
                    st.info("Insertion successful!!")
                    mydb.commit()
                except mysql.connector.Error as e:
                    st.warning(e)
           
            if(selected=="Product"):
                try:
                    mycursor.execute("insert into product values (%s,%s,%s,%s)",(prod_id,prod_name,cat_id,price))
                    st.info("Insertion successfull!!")
                    mydb.commit()
                except mysql.connector.Error as e:
                    st.warning(e)
            if(selected=="Customer"):
                try:
                    # mycursor.execute("select discount from offers where prod_id=%s and cat_id=%s",(prod_id,cat_id))
                    # df5=pd.DataFrame(mycursor.fetchall())
                    mycursor.execute("insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(int(cust_id),cust_name,int(ph_no),address,pay_mode,int(cat_id),int(prod_id),int(price),int(emp_id)))
                    # st.info("Insertion successfull!!")
                    mydb.commit()
                    mycursor.execute("select cust_name,ph_no,pay_mode,prod_name,p.price from customer c,product p where c.prod_id=p.prod_id and c.cust_name=%s and c.cat_id=p.cat_id and c.cust_id=%s",(cust_name,cust_id))
                    df6=pd.DataFrame(mycursor.fetchall())
                    df6=st.table(df6.T)
                    # st.info("Insertion successfull!!")
                except mysql.connector.Error as e:
                    st.warning(e)
    if(selected=="Update"):
        col1,col2=st.columns(2)
        with col1:
            seloct=option_menu(
                menu_title = "Choose the table",
                options = ["Product","Offers"],      
                orientation="vertical",
            )
        if(seloct=="Product"):
            st.subheader("Update operation for Product table")
            mycursor.execute("Select * from product")
            #st.write("Before updation")
            df=pd.DataFrame(mycursor.fetchall())
            #st.table(df)
            with st.form("form1"):
                str2="SELECT EXISTS (SELECT 1 FROM product)"
                mycursor.execute(str2)
                if(mycursor.fetchone()['EXISTS (SELECT 1 FROM product)']):
                    prod_id=st.selectbox("Select the prodcut_id to be updated[prod_id]",df['prod_id'])
                    prod_name=st.text_input("Input the updated product name")
                    mycursor.execute("Select * from category")
                    df=pd.DataFrame(mycursor.fetchall())
                    #st.table(df)
                    cat_id= st.selectbox('Enter the category id',df['cat_id'])
                    price=st.number_input("Enter the updated price of the product")
                    submit=st.form_submit_button("Update")
                    if(submit):
                        str1=f"update product set prod_name={prod_name},prod_name={prod_name},cat_id={cat_id},price={price} where prod_id={prod_id}"
                        try:
                            mycursor.execute(str1)
                            mydb.commit()
                            st.info("Updation successful")
                            st.write("After updation")
                            mycursor.execute("Select * from employee")
                            df=pd.DataFrame(mycursor.fetchall())
                            st.table(df)
                        except mysql.connector.Error as e:
                            st.warning(e)
                            st.experimental_rerun()
        if(seloct=="Offers"):
            st.subheader("Update operation for Offers table")
            mycursor.execute("Select * from offers")
            st.write("Before updation")
            df=pd.DataFrame(mycursor.fetchall())
            st.table(df)
            with st.form("form1"):
                str2="SELECT EXISTS (SELECT 1 FROM offers)"
                mycursor.execute(str2)
                if(mycursor.fetchone()['EXISTS (SELECT 1 FROM offers)']):
                    prod_id=st.selectbox("Select the product_id to be updated[prod_id]",df['prod_id'])
                    cat_id=st.selectbox("Select the category_id to be updated",df['cat_id'])
                    discount= st.number_input('Enter the discount rate')
                    validity=st.date_input("Enter the updated validity")
                    submit=st.form_submit_button("Update")
                    if(submit):
                        #str1=f"update location set province='{province}',city='{city}' where location_id={location_id}"
                        try:
                            mycursor.execute("update offers set cat_id=%s,discount=%s,validity=%s where prod_id=%s",(cat_id,discount,validity,prod_id))
                            mydb.commit()
                            st.info("Updation successful")
                            st.write("After updation")
                            mycursor.execute("Select * from offers")
                            df=pd.DataFrame(mycursor.fetchall())
                            st.table(df)
                        except mysql.connector.Error as e:
                            st.warning(e)
                            st.experimental_rerun()
    if(selected=="Delete"):
        col1,col2=st.columns(2)
        with col1:
            selected=option_menu(
                menu_title = "Choose the table",
                options = ["Product","Offers"],      
                orientation="horizontal",
            )
        if(selected=="Product"):
            st.subheader("Delete operation available for Product table")
            mycursor.execute("Select * from product")
            st.write("Before deletion")
            df=pd.DataFrame(mycursor.fetchall())
            st.table(df)
            with st.form("form1"):
                str2="SELECT EXISTS (SELECT 1 FROM product)"
                mycursor.execute(str2)
                if(mycursor.fetchone()['EXISTS (SELECT 1 FROM product)']):
                    select=st.selectbox("Select the Product to be deleted (PROD_ID)",df['prod_id'])
                    submit=st.form_submit_button("Delete")
                    if(submit):
                        try:
                            str1=f"delete from product where prod_id= {select}"
                            mycursor.execute(str1)
                            mydb.commit()
                            st.info("Deletion successful")
                            st.write("After deletion")
                            mycursor.execute("Select * from product")
                            df=pd.DataFrame(mycursor.fetchall())
                            st.table(df)
                        except mysql.connector.Error as e:
                            st.warning(e)
                            st.experimental_rerun()
        if(selected=="Offers"):
            st.subheader("Delete operation available for Offers Table")
            mycursor.execute("Select * from offers")
            st.write("Before deletion")
            df=pd.DataFrame(mycursor.fetchall())
            st.table(df)
            with st.form("form2"):
                str2="SELECT EXISTS (SELECT 1 FROM offers)"
                mycursor.execute(str2)
                if(mycursor.fetchone()['EXISTS (SELECT 1 FROM offers)']):
                    select=st.selectbox("Select the Offer Details to be deleted (prod_id)",df['prod_id'])
                    submit=st.form_submit_button("Delete")
                    if(submit):
                        try:
                            str1=f"delete from offers where prod_id= {select}"
                            mycursor.execute(str1)
                            mydb.commit()
                            st.info("Deletion successful")
                            st.write("After deletion")
                            mycursor.execute("Select * from offers")
                            df=pd.DataFrame(mycursor.fetchall())
                            st.table(df)
                        except mysql.connector.Error as e:
                            st.warning(e)
                            st.experimental_rerun()
