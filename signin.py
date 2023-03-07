from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#-----------------------------------------Functions-----------------------------------------#

#1.Function to delete username on click#

def user_enter(capture):            #capture or any other variable name we are to capture the value passed during clicking on the box#
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

#2.Function to delete password field#

def password_enter(capture):            #capture or any other variable name we are to capture the value passed during clicking on the box#
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#3.Function to hide and show password according to the icon#

def hide():
    openeye.config(file='closeye.png')      #config will change the icon from open eye to close eye on click and also the password visibility but only for the 1st time#
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

#4.Function "show" to hide continuously change the icons as per click and also the password visibility#
#this will work as a loop between the two functions#

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

#5. Loop between two windows

def sign_up():
    login_window.destroy()
    import signup

#6 adding functionality to login page

def login_user():
    if usernameEntry.get()=='' or usernameEntry.get()=='Username' or passwordEntry.get()=='' or passwordEntry.get()=='Password':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','FATAL ERROR!! Connection to Database Failed!!!')
            return
        # using the database
        query = 'use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:           #if we are getting none that means there is no row having with that username or password
            messagebox.showerror('Error','Invalid Username Or Password !!!')
        else:
            messagebox.showinfo('Welcome', 'Successfully logged in..Please Click OK to continue')
            login_window.destroy()
            import calcu




#7 forget password function

def forget_pass():
    # 8 submit button function in reset password page
    def change_password():
        if user_entry.get()=='' or pass_entry.get()=='' or con_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required!!',parent=window)     #we want the message over the reset password screen which is on the top level
        elif pass_entry.get() != con_entry.get():
            messagebox.showerror('Error','New Password And Confirm Password Did Not Matched!!',parent=window)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='1234',database='userdata')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'FATAL ERROR!! Connection to Database Failed!!!')
                return

            query='select * from data where username=%s'
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error','Incorrect Username',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query, (pass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success!!','Password reset was successfull..Please login with the new credentials',parent=window)
                window.destroy()

    window=Toplevel()       #creating a new window
    window.title('Change Password')
    window.geometry("612x408+490+170")
    window.resizable(0,0)
    bgPic=ImageTk.PhotoImage(file='istockphoto-1283543880-612x612.png')
    bgLabel=Label(window,image=bgPic)
    bgLabel.grid()
    headingLabel = Label(window, text='Reset Password', font=('Times New Roman',25), bg='white', fg='firebrick1')
    headingLabel.place(x=345, y=35)
    backgLabel=Label(window,width=30,height=15,bg='white')   #white box on which we are writing because bg image contained some pre text
    backgLabel.place(x=345,y=90)
    backgLabel2 = Label(window, width=32, height=19,bg='PaleTurquoise1')
    backgLabel2.place(x=335, y=80)
    user_Label= Label(window, text='Username', font=('Arial', 15), bg='PaleTurquoise1', fg='Black')
    user_Label.place(x=338,y=85)
    user_entry=Entry(window,width=24,font=('Times new roman',13),bg='papaya whip',fg='Black')
    user_entry.place(x=340,y=115)
    l3 = Label(window, text='Made by MR.SINHA', font=('High Tower Text', 15), bg='white', fg='black')
    l3.place(x=90, y=320)
    pass_Label = Label(window, text='New Password', font=('Arial', 15), bg='PaleTurquoise1', fg='Black')
    pass_Label.place(x=338, y=150)
    pass_entry = Entry(window, width=24, font=('Times new roman', 13), bg='papaya whip', fg='Black')
    pass_entry.place(x=340, y=180)
    conpass_Label = Label(window, text='Confirm New Password', font=('Arial', 15), bg='PaleTurquoise1', fg='Black')
    conpass_Label.place(x=338, y=215)
    con_entry = Entry(window, width=24, font=('Times new roman', 13), bg='papaya whip', fg='Black')
    con_entry.place(x=340, y=245)
    consubmitButton = Button(window, text='SUBMIT', font=('Open Sans', 16, 'bold'), bd=6, fg='white', bg='firebrick1',width=6, activeforeground='white', activebackground='firebrick1', cursor='hand2',command=change_password)
    consubmitButton.place(x=400, y=290)
    window.mainloop()


#------GUI part------#
login_window = Tk()   #Tk is the class name and login_window is the object variable used to access methods inside Tk class#
#Now we will add the background image since it is a JPEG type not an PNG we have to install pillow module using the command: pip install pillow..in the terminal#
#--Import the library using command: from PIL import ImageTk--#

login_window.geometry("790x512+400+120") #790*512 dim of the image & +400+200 is the position where in our screen we want our form#
login_window.resizable(0,0) #(0,0)means false value & hence window can't be maximize now we restricted this because if we maximize we can see empty spaces on our screen#
login_window.title('Login Page')    #title of the page#
bgImage=ImageTk.PhotoImage(file='demo2.jpeg')

bgLabel=Label(login_window,image=bgImage) #for creating an image we first create label then add the picture in it#
#----we write the word "login_window" so that we can see it on our screen----#

#bgLabel.grid(row=0,column=0)  #specifies the position of the image 00 means at top left corner#

bgLabel.place(x=0,y=0) #same as above but the difference is that window will not automatically resize#

#----Now we will write in the white space of the bg image----#

heading=Label(login_window,text='USER LOGIN',font=('High Tower Text',25,'bold'),bg='white',fg='firebrick1') #we have created the label but not yet placed it#
#----bg = label bg color & fg = text color----#
heading.place(x=490,y=60)       #Now placed#

l1=Label(login_window,text='Made by MR.SINHA',font=('High Tower Text',15),bg='Antique white1',fg='black')
l1.place(x=0,y=483)


#-------Now we are adding the text field for username-------#

usernameEntry=Entry(login_window,width=31,font=('Arial',13,'bold'),bd=0,fg='Black')
usernameEntry.place(x=465,y=140)        #positioning the text field#
usernameEntry.insert(0,'Username')   #pretext#

#now this pretext must be deleted when we click on the box to write something hence we will bind it with a function#

usernameEntry.bind('<FocusIn>',user_enter)   #focus in command is used when we basically entering something on enter is the function name we will define it at the top of our code#

#-----giving line under username using frame class------# 
frame1=Frame(login_window,width=273,height=2,bg='firebrick1')
frame1.place(x=465,y=161)


#-------Now we are adding the text field for password same as above-------#

passwordEntry=Entry(login_window,width=31,font=('Arial',13,'bold'),bd=0,fg='Black')
passwordEntry.place(x=465,y=210)        #positioning the text field#
passwordEntry.insert(0,'Password')   #pretext#

#now this pretext must be deleted when we click on the box to write something hence we will bind it with a function#

passwordEntry.bind('<FocusIn>',password_enter)   #focus in command is used when we basically entering something  on enter is the function name we will define it at the top of our code#

#-----giving line under password using frame class------#
frame2=Frame(login_window,width=273,height=2,bg='firebrick1')
frame2.place(x=465,y=232)

#----Button for eye icon---- bd=border=no border or 0 ,bg=background color=white and while clicking on the button it still shows grey animation which is called active background color we also remove that by white and when we click on the button it should change its cursor to hand hand2 is used as a style#
#command= hide(hide is a function which will change the open eye icon to close eye and also changes the password to *** simultaneously..we will define hide top of our code)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=715,y=205)

#---forget password----#

forgetButton=Button(login_window,text='Forgot Password?',fg='firebrick',font=('Arial',11,'bold'),bd=0,bg='white',activebackground='white',cursor='hand2',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=605,y=240)

#---login button----#

loginButton=Button(login_window,text='LOGIN',font=('Open Sans',16,'bold'),bd=7,fg='white',bg='firebrick1',width=15,activeforeground='white',activebackground='firebrick1',cursor='hand2',command=login_user)
loginButton.place(x=502,y=290)

#----OR label-------#

orLabel=Label(login_window,text='------------------OR-----------------',font=('Open Sans',16,),fg='firebrick1',bg='white')
orLabel.place(x=462,y=360)

#------Facebook/google/twitter/icon-----#

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=552,y=400)

twitter_logo=PhotoImage(file='twitter.png')
t_Label=Label(login_window,image=twitter_logo,bg='white')
t_Label.place(x=590,y=400)

google_logo=PhotoImage(file='google.png')
go_Label=Label(login_window,image=google_logo,bg='white')
go_Label.place(x=628,y=400)

#----Don't have an account----#

signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=480,y=450)

#----Create an account button----#

newaccountButton=Button(login_window,text='Create new account',font=('Open Sans',9,'bold underline'),bd=0,fg='blue',bg='white',activeforeground='blue',activebackground='white',cursor='hand2',command=sign_up)
newaccountButton.place(x=620,y=450)

#---Display the form---#

login_window.mainloop()   #mainloop is used to view the window using the object variable login_window run to see the empty window#
