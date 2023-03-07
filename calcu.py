from tkinter import *
from PIL import ImageTk

#---functions----#
#1.button click show on screen#
def btn_click(number):
    global val
    val=val+str(number)
    data.set(val)
#2.clearscreen button#
def btnClear():
    global val
    val=''
    data.set('')
#3.eqaul button#
def btnEquals():
    global val
    result=str(eval(val))
    data.set(result)

#4.Back to login page#
def login():
    calc_window.destroy()
    import signin
#5.Quit screen#
def quit_sc():
    calc_window.destroy()

#---GUI------------#
calc_window=Tk()
calc_window.title('Calculator')
calc_window.geometry("1080x720+250+25")
calc_window.resizable(0,0)
back_image=ImageTk.PhotoImage(file='new.jpeg')
back_label=Label(calc_window,image=back_image)
back_label.grid()

#calculator entry screen
#justify right= typing will start from right towards left#
val=''
data=StringVar()

display=Entry(calc_window,textvariable=data,bd=31,justify='right',bg='khaki1',font=('arial',20))
display.place(x=370,y=180)

#buttons
#--------1st row-----------#
btn7=Button(calc_window,text='7',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(7),bg='misty rose')
btn7.place(x=370,y=272)
btn8=Button(calc_window,text='8',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(8),bg='misty rose')
btn8.place(x=466,y=272)
btn9=Button(calc_window,text='9',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(9),bg='misty rose')
btn9.place(x=562,y=272)
btn_mul=Button(calc_window,text='X',font=('Times New Roman',20,'bold'),bd='5',width='4',fg='Black',activeforeground='black',activebackground='white',command=lambda:btn_click('*'),bg='aquamarine')
btn_mul.place(x=658,y=272)

#-----2nd row-------------#
btn4=Button(calc_window,text='4',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(4),bg='misty rose')
btn4.place(x=370,y=332)
btn5=Button(calc_window,text='5',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(5),bg='misty rose')
btn5.place(x=466,y=332)
btn6=Button(calc_window,text='6',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(6),bg='misty rose')
btn6.place(x=562,y=332)
btn_minus=Button(calc_window,text='-',font=('Arial',20,'bold'),bd='3',width='4',fg='Black',activeforeground='black',activebackground='white',command=lambda:btn_click('-'),bg='aquamarine')
btn_minus.place(x=658,y=332)

#-----3rd row-------------#
btn1=Button(calc_window,text='1',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(1),bg='misty rose')
btn1.place(x=370,y=392)
btn2=Button(calc_window,text='2',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(2),bg='misty rose')
btn2.place(x=466,y=392)
btn3=Button(calc_window,text='3',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(3),bg='misty rose')
btn3.place(x=562,y=392)
btn_plus=Button(calc_window,text='+',font=('Times new roman',20,'bold'),bd='6',width='4',fg='Black',activeforeground='black',activebackground='white',command=lambda:btn_click('+'),bg='aquamarine')
btn_plus.place(x=658,y=391)

#-----4th row-------------#
btnC=Button(calc_window,text='C',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='black',activeforeground='black',activebackground='white',command=btnClear,bg='dodger blue')
btnC.place(x=370,y=452)
btn0=Button(calc_window,text='0',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='red',activeforeground='black',activebackground='white',command=lambda:btn_click(0),bg='misty rose')
btn0.place(x=466,y=452)
btndot=Button(calc_window,text='.',font=('Times New Roman',20,'bold'),bd='5',width='5',fg='black',activeforeground='black',activebackground='white',command=lambda:btn_click('.'),bg='gold')
btndot.place(x=562,y=452)
btn_div=Button(calc_window,text='÷',font=('Times new roman',20,'bold'),bd='6',width='4',fg='Black',activeforeground='black',activebackground='white',command=lambda:btn_click('/'),bg='aquamarine')
btn_div.place(x=658,y=452)

#-----5th row------------#
btn_calcu=Button(calc_window,text='=',font=('Times new roman',20,'bold'),bd='6',width='22',fg='Black',activeforeground='black',activebackground='white',command=btnEquals,bg='firebrick1')
btn_calcu.place(x=370,y=512)

heading=Label(calc_window,text='Calculator',font=('High Tower Text',25,'bold'),fg='red',bg='Antique white1')
heading.place(x=472,y=10)

l1=Label(calc_window,text='Made by MR.SINHA',font=('High Tower Text',15),bg='Antique white1',fg='black',width='30')
l1.place(x=370,y=574)

btn_login=Button(calc_window,text='Back to login page',font=('Times new roman',20,'bold'),bd='6',width='22',fg='Black',activeforeground='black',activebackground='white',command=login,bg='cyan')
btn_login.place(x=370,y=604)

btn_quit=Button(calc_window,text='Quit',font=('Times new roman',20,'bold'),bd='2',width=5,fg='Black',activeforeground='black',activebackground='white',command=quit_sc,bg='red')
btn_quit.place(x=500,y=665)

calc_window.mainloop()