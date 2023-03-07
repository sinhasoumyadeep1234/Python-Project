from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import  pymysql


#---------functions--------#

def  clear():
    emailEntry.delete(0,END)
    UsernameEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    ConfirmPasswordEntry.delete(0,END)
    check.set(0)
def login_page():
    signup_window.destroy()
    import signin
def connect_database():
    if emailEntry.get()=='' or UsernameEntry.get()=='' or PasswordEntry.get()=='' or ConfirmPasswordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif PasswordEntry.get() != ConfirmPasswordEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Check The Terms And Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','FATAL ERROR!! Connection to Database Failed!!!')
            return          #if error happens then don't run the below code

        #we again creating an try except block because if we again run the code it will show database already created hence to prevent the database creation again and again we are puttting the codes of creatinng of table and database inside the try and except block
        try:
            #database creation
            query='create database userdata'
            mycursor.execute(query)

            #using the database
            query='use userdata'
            mycursor.execute(query)

            #creating a table to store the username & password
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            query='use userdata'
            mycursor.execute(query)

    #if someone tries to create account with same username that already present in the database
        query='select * from data where username=%s'
        mycursor.execute(query,(UsernameEntry.get()))
        row=mycursor.fetchone()
        if row != None:     #means there exists a same row  with the given username for to be unique the row value should be null
            messagebox.showerror('Error', 'ERROR!! Username Already Exists!!!')
        else:
            #Inserting username email and password provided to the table
            query='Insert into data(email,username,password) values (%s,%s,%s)' #%s will replace the values entered in the text field
            mycursor.execute(query,(emailEntry.get(),UsernameEntry.get(),PasswordEntry.get()))
            con.commit()            #to view or aplly our changes
            con.close()             #closing the connection
            messagebox.showinfo('Success','Yeee!! Registration is successfull!!')

            #function call to clear all the entered data from screen
            clear()
            signup_window.destroy()
            import signin

#-----GUI------#
signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(0,0)
signup_window.geometry("790x512+400+120")
backgroundImage=ImageTk.PhotoImage(file='demo2.jpeg')
bgLabel=Label(signup_window,image=backgroundImage)
bgLabel.grid()      #in we use grid in place of "Place" method then we dont have to adjust window size according to the bg image it happens automatically#

#heading#
frame=Frame(signup_window,bg='white')
frame.place(x=453,y=40)     #we are keeping our labels and everthing insode frame because if we use frame we dont have to give any x,y coordinate values it will adjust sizes by itself#
heading=Label(frame,text='CREATE  AN  ACCOUNT',font=('High Tower Text',16,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)        #padx,y vertical and horizontal spacing

#---Text fields--#

emailLabel=Label(frame,text='Email',font=('High Tower Text',12,'bold'),bg='white',fg='Firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=10,pady=(10,0))      #sticky w(West) means email will be aligned leftmost side of the frame#
emailEntry=Entry(frame,width=30,font=('Times new roman',13),bg='Light blue',fg='Black')
emailEntry.grid(row=2,column=0,sticky='w',padx=10)


UsernameLabel=Label(frame,text='Username',font=('High Tower Text',12,'bold'),bg='white',fg='Firebrick1')
UsernameLabel.grid(row=3,column=0,sticky='w',padx=10,pady=(10,0))
UsernameEntry=Entry(frame,width=30,font=('Times new roman',13),bg='light green',fg='Black')
UsernameEntry.grid(row=4,column=0,sticky='w',padx=10)


PasswordLabel=Label(frame,text='Password',font=('High Tower Text',12,'bold'),bg='white',fg='Firebrick1')
PasswordLabel.grid(row=5,column=0,sticky='w',padx=10,pady=(10,0))
PasswordEntry=Entry(frame,width=30,font=('Times new roman',13),bg='Misty Rose2',fg='Black')
PasswordEntry.grid(row=6,column=0,sticky='w',padx=10)


ConfirmPasswordLabel=Label(frame,text='Confirm Password',font=('High Tower Text',12,'bold'),bg='white',fg='Firebrick1')
ConfirmPasswordLabel.grid(row=7,column=0,sticky='w',padx=10,pady=(10,0))
ConfirmPasswordEntry=Entry(frame,width=30,font=('Times new roman',13),bg='plum1',fg='Black')
ConfirmPasswordEntry.grid(row=8,column=0,sticky='w',padx=10)

#checkbuttton#
check=IntVar()  #to store 0/1 for tick and untick
termsandconditions=Checkbutton(frame,text='I agree to the terms and conditions',font=('Times new roman',12,'bold'),bg='white',fg='firebrick2',activebackground='white',activeforeground='red',cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10)

signupButton=Button(frame,text='SIGN UP',font=('Open Sans',16,'bold'),bg='firebrick1',bd=7,fg='white',width=15,activeforeground='white',activebackground='firebrick1',cursor='hand2',command=connect_database)
signupButton.grid(row=10,column=0)

#already have an account#

alreadyaccountLabel=Label(frame,text='Already have an account?',font=('Open Sans',9,'bold'),bg='white',fg='blue')
alreadyaccountLabel.grid(row=11,column=0,sticky='w',padx=10,pady=10)

#login button#

loginButton=Button(frame,text='LOG IN',font=('Open Sans',10,'bold underline'),bg='white',bd=0,fg='red',width=15,activeforeground='Blue',activebackground='White',cursor='hand2',command=login_page)
loginButton.grid(row=11,column=0,sticky='E',padx=4)

signup_window.mainloop()