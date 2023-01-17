from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as msg
import smtplib
import mysql.connector

cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
my_cursor = cnx.cursor()

def back_to_login():
    root.destroy()
    import login

def forgot_pass():
    if not username_inp.get():
        msg.showerror("Blank Field", "Username field is empty")
    elif not email_inp.get():
        msg.showerror("Blank Field", "Email field is empty")
    if username_inp.get() and email_inp.get():
        query="SELECT Employee_id,Email_id FROM employee WHERE Employee_id=%s and Email_id=%s"
        data=(username_inp.get(),email_inp.get())
        my_cursor.execute(query,data)
        user_details = my_cursor.fetchone()

        if user_details != None:
            my_cursor.execute("SELECT Pass_word FROM login WHERE Login_id=%s",(username_inp.get(),))
            data = my_cursor.fetchone()
            my_cursor.execute("SELECT First_name,Last_name FROM employee WHERE Employee_id=%s",(username_inp.get(),))
            name = my_cursor.fetchone()
            username_lbl.place_forget()
            username_box.place_forget()
            username.place_forget()
            email_lbl.place_forget()
            email_box.place_forget()
            email.place_forget()
            change_btn.place_forget()
            change_btn_lbl.place_forget()
            from_ = "gtanish544@gmail.com"
            to_ = email_inp.get()
            subject = "Account Password"
            name=f'{name[0]} {name[1]}'
            password = data[0]
            body = f"Hi , {name}\nYour Password is {password} !!!\n\nThank You"
            mesage = f"Subject : {subject}\n\n{body}"
            pwd = "owkazpyhirsijoew"
            cntn = smtplib.SMTP("smtp.gmail.com",587)
            cntn.starttls()
            cntn.login(from_,pwd)
            cntn.sendmail(from_,to_,mesage)
            cntn.close()
            msg.showinfo("Success","Password Sent to your Email")
            change_btn.config(command=back_to_login)
            change_btn.place(x=88, y=160)
            change_btn_lbl.config(text="Back to Login",command=back_to_login)
            change_btn_lbl.place(x=150, y=164)

        
        else:
            msg.showerror("Error !", "Invalid Employee ID or Email !")
    
    

root = Tk()
root.geometry("400x200")
root.title(" Forgot Password ")
root.wm_iconbitmap("icon/ems.ico")
root.configure(bg="white")

entry_bg_img = ImageTk.PhotoImage(Image.open('images/change_password/entry_bg.png'))

username_lbl = Label(root,text='Employee ID :',bg='white',fg='black',font=('Poppins',10,'bold'))
username_lbl.place(x=80, y=20)

username_box = Label(root,image=entry_bg_img,bg='white')
username_box.place(x=70, y=40)

username_inp = StringVar()
email_inp = StringVar()

username = Entry(root,textvariable=username_inp,background="#F5F5F5",bd=0, fg="black", font="Poppins 12")
username.place(x=75, y=45,width=250,height=28)

email_lbl = Label(root,text='Email - ID :',bg='white',fg='black',font=('Poppins',10,'bold'))
email_lbl.place(x=80, y=90)

email_box = Label(root,image=entry_bg_img,bg='white')
email_box.place(x=70, y=110)

email = Entry(root,textvariable=email_inp,background="#F5F5F5",bd=0, fg="black", font="Poppins 12")
email.place(x=75, y=115,width=250,height=28)

change_btn_img = ImageTk.PhotoImage(Image.open('images/Forgot_password/forgot_btn.png').resize((250,35),Image.Resampling.LANCZOS))
change_btn = Button(root, image=change_btn_img,borderwidth=0, background="white", cursor="hand2",command=forgot_pass)
change_btn.place(x=88, y=160)

change_btn_lbl = Button(text="Sent Password", background="black",fg="white",bd=0, activebackground='black',activeforeground='white',cursor="hand2",font="Poppins 12 bold",command=forgot_pass)

change_btn_lbl.place(x=150, y=164)

root.resizable(False, False)
root.mainloop()
