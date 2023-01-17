from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox as msg
import mysql.connector

cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
my_cursor = cnx.cursor()

def back_to_login():
    root.destroy()
    import login

def show():
    show_btn.place_forget()
    hide_btn.place(x=370, y=123)
    old_password.config(show="")

def hide():
    hide_btn.place_forget()
    show_btn.place(x=370, y=123)
    old_password.config(show="*")

def show2():
    show_btn2.place_forget()
    hide_btn2.place(x=370, y=193)
    new_password.config(show="")

def hide2():
    hide_btn2.place_forget()
    show_btn2.place(x=370, y=193)
    new_password.config(show="*")

def change_pass():
    if not username_val.get() or not old_password_val.get() or not new_password_val.get() or not confirm_password_val.get():
        msg.showerror("Blank Field", "Please fill all the fields")
    elif new_password_val.get() != confirm_password_val.get():
        msg.showerror("Password Mismatch", "New Password and Confirm Password do not match")

    elif username_val.get() and old_password_val.get() :
        try:
            query="SELECT Login_id,Pass_word FROM login WHERE Login_id=%s and Pass_word=%s"
            data=(username_val.get(),old_password_val.get())
            my_cursor.execute(query,data)
            user_details = my_cursor.fetchone()

            if user_details != None:
                my_cursor.execute("UPDATE login SET Pass_word=%s WHERE Login_id=%s",(new_password_val.get(),username_val.get()))
                cnx.commit()
                cnx.close()
                msg.showinfo('Success','Password has been changed successfully')
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')
        username_lbl.place_forget()
        username_box.place_forget()
        username.place_forget()
        old_password_lbl.place_forget()
        old_password_box.place_forget()
        old_password.place_forget()
        show_btn.place_forget()
        hide_btn.place_forget()
        new_password_lbl.place_forget()
        new_password_box.place_forget()
        new_password.place_forget()
        show_btn2.place_forget()
        hide_btn2.place_forget()
        confirm_password_lbl.place_forget()
        confirm_password_box.place_forget()
        confirm_password.place_forget()
        change_btn.place_forget()
        change_btn_lbl.place_forget()
        change_btn.config(command=back_to_login)
        change_btn.place(x=128, y=310)
        change_btn_lbl.config(text="Back to Login",command=back_to_login)
        change_btn_lbl.place(x=195, y=315)


root = Tk()
root.geometry("500x360")
root.title(" Change Password ")
root.wm_iconbitmap("icon/ems.ico")
root.configure(bg="white")
show_img = ImageTk.PhotoImage(Image.open('images/Change_password/show.png').resize((20,20),Image.Resampling.LANCZOS))

hide_img = ImageTk.PhotoImage(Image.open('images/Change_password/hide.png').resize((20,20),Image.Resampling.LANCZOS))

entry_bg_img = ImageTk.PhotoImage(Image.open('images/change_password/entry_bg.png'))

'''Variables'''
username_val = StringVar()
old_password_val = StringVar()
new_password_val = StringVar()
confirm_password_val = StringVar()

username_lbl = Label(root,text='Username :',bg='white',fg='black',font=('Poppins',10,'bold'))
username_lbl.place(x=100, y=20)

username_box = Label(root,image=entry_bg_img,bg='white')
username_box.place(x=100, y=45)

username = Entry(root,textvariable=username_val,background="#F5F5F5",bd=0, fg="black", font="Poppins 12")
username.place(x=105, y=50,width=250,height=28)

old_password_lbl = Label(root,text='Old Password :',bg='white',fg='black',font=('Poppins',10,'bold'))
old_password_lbl.place(x=100, y=90)

old_password_box = Label(root,image=entry_bg_img,bg='white')
old_password_box.place(x=100, y=115)

old_password = Entry(root,textvariable=old_password_val,background="#F5F5F5",bd=0, fg="black", font="Poppins 12",show="*")
old_password.place(x=105, y=120,width=250,height=28)

show_btn = Button(root,image=show_img,bg='#F5F5F5',bd=0,command=show)
show_btn.place(x=370, y=123)

hide_btn = Button(root,image=hide_img,bg='#F5F5F5',bd=0,command=hide)

new_password_lbl = Label(root,text='New Password :',bg='white',fg='black',font=('Poppins',10,'bold'))
new_password_lbl.place(x=100, y=160)

new_password_box = Label(root,image=entry_bg_img,bg='white')
new_password_box.place(x=100, y=185)

new_password = Entry(root,textvariable=new_password_val,background="#F5F5F5",bd=0, fg="black", font="Poppins 12",show="*")
new_password.place(x=105, y=190,width=250,height=28)

show_btn2 = Button(root,image=show_img,bg='#F5F5F5',bd=0,command=show2)
show_btn2.place(x=370, y=193)

hide_btn2 = Button(root,image=hide_img,bg='white',bd=0,command=hide2)

confirm_password_lbl = Label(root,text='Confirm Password :',bg='white',fg='black',font=('Poppins',10,'bold'))
confirm_password_lbl.place(x=100, y=230)

confirm_password_box = Label(root,image=entry_bg_img,bg='white')
confirm_password_box.place(x=100, y=255)

confirm_password = Entry(root,textvariable=confirm_password_val,background="#F5F5F5",bd=0, fg="black", font="Poppins 12",show="*")
confirm_password.place(x=105, y=260,width=250,height=28)

change_btn_img = ImageTk.PhotoImage(Image.open('images/Change_password/change_btn.png'))

change_btn = Button(root, image=change_btn_img,borderwidth=0, background="white", cursor="hand2",command=change_pass)
change_btn.place(x=128, y=310)

change_btn_lbl = Button(text="Change Password", background="black",fg="white",bd=0, activebackground='black',cursor="hand2",font="Poppins 12 bold",command=change_pass)
change_btn_lbl.place(x=180, y=315)

root.resizable(False, False)
root.mainloop()
