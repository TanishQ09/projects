from tkinter import *
import tkinter.messagebox as msg
from PIL import ImageTk, Image
import mysql.connector

cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
my_cursor = cnx.cursor()

def show():
    show_btn.place_forget()
    hide_btn.place(x=870, y=348)
    password.config(show="")

def hide():
    hide_btn.place_forget()
    show_btn.place(x=870, y=348)
    password.config(show="*")

def check_input():
    global log_name 
    log_name= user_name.get()
    global pass_word 
    pass_word = user_password.get()
    if not log_name:
        msg.showerror("Blank Field", "Username field is empty")
    elif not pass_word:
        msg.showerror("Blank Field", "Password field is empty")
    if log_name and pass_word:
        query="SELECT Login_id,Pass_word FROM login WHERE Login_id=%s and Pass_word=%s"
        data=(log_name,pass_word)
        my_cursor.execute(query,data)
        log_details = my_cursor.fetchone()

        if log_details != None:
            my_cursor.execute("SELECT Department FROM employee WHERE Employee_id=%s",(log_name,))
            dept = my_cursor.fetchone()
            if dept[0] == "HR" or dept[0] == "Admin":
                cnx.commit()
                cnx.close()
                root.destroy()
                import admin
            else:
                root.destroy()
                import user
        
        else:
            msg.showerror("Error !", "Invalid Username or Password !")


def change_pass():
    root.destroy()
    import change_password

def forgot_pass():
    root.destroy()
    import forgot_password

root = Tk()
root.geometry("1000x600")
root.title(" Employee Management System  ")
root.wm_iconbitmap("icon/ems.ico")

show_img = ImageTk.PhotoImage(Image.open('images/login/show.png').resize((20,20),Image.Resampling.LANCZOS))

hide_img = ImageTk.PhotoImage(Image.open('images/login/hide.png').resize((20,20),Image.Resampling.LANCZOS))

background_image = PhotoImage(file='images/login/login_bg.png')
Label(root, image=background_image).place(x=-2, y=0)

Label(text="Welcome Back !!", background="white",fg="black", font="Poppins 32").place(x=580, y=50)

Label(text="Login your account", background="white",fg="black", font="Poppins 18").place(x=640, y=130)

user_name = StringVar()
user_password = StringVar()

entry_bg_img = ImageTk.PhotoImage(Image.open('images/login/entry_bg.png'))

username_lbl = Label(root,text='Username :',bg='white',fg='black',font=('Poppins',12,'bold'))
username_lbl.place(x=550, y=200)

username_box = Label(root,image=entry_bg_img,bg='white')
username_box.place(x=550, y=225)

username = Entry(root,textvariable=user_name,background="#F5F5F5",bd=0, fg="black", font="Poppins 12")
username.place(x=555, y=235,width=345,height=30)

password_lbl = Label(root,text='Password :',bg='white',fg='black',font=('Poppins',12,'bold'))
password_lbl.place(x=550, y=305)

password_box = Label(root,image=entry_bg_img,bg='white')
password_box.place(x=550, y=330)

password = Entry(root,textvariable=user_password,background="#F5F5F5",bd=0, fg="black", font="Poppins 12",show="*")
password.place(x=555, y=340,width=345,height=30)

show_btn = Button(root, image=show_img,borderwidth=0, background="#F5F5F5", cursor="hand2",command=show)

show_btn.place(x=870, y=348)

hide_btn = Button(root, image=hide_img,borderwidth=0, background="#F5F5F5", cursor="hand2",command=hide)

signin_btn_img = PhotoImage(file='images/login/sign_in.png')
signin_btn = Button(root, image=signin_btn_img,borderwidth=0, background="white", cursor="hand2",command=check_input)
signin_btn.place(x=640, y=435)

Button(text="Sign in", background="black",fg="white",bd=0, activebackground='black',cursor="hand2",font="Poppins 16 bold",command=check_input).place(x=700, y=443)

Button(root,text='Change Password ',borderwidth=0, background="white", font="Poppins 14 bold",cursor="hand2",command=change_pass).place(x=470, y=550)

Button(root,text='Forgot Password ?',borderwidth=0, background="white", font="Poppins 14 bold",cursor="hand2",command=forgot_pass).place(x=800, y=550)

root.resizable(False, False)
root.mainloop()