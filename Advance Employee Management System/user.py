from tkinter import *
import webbrowser
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkvideo import *
import mysql.connector
import login
import io

def home():
    profile_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=73)
    home_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=white_home,bg='#7DA2F5').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=175)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=225)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    home_frame.place(x=260,y=10)
    player = tkvideo("videos/home/home_slogan.mp4",slogan_lbl, loop = 0,size = (430,160))
    player.play()
    slogan_lbl.place(x=30,y=150)


def profile():
    home_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=123)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=white_profile,bg='#7DA2F5').place(x=20,y=125)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=175)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=225)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
        my_cursor = cnx.cursor()
        my_cursor.execute("SELECT * FROM employee WHERE Employee_id = %s", (login.user_name.get(),))
        user_details = my_cursor.fetchone()
    except Exception as e:
        msg.showerror('Error',f'Due to {str(e)}')
    name_lbl.configure(text = f'{user_details[1]} {user_details[2]}')
    fetch_image = Image.open(io.BytesIO(user_details[18]))
    fetch_image = fetch_image.resize((160,160))
    fetch_image = ImageTk.PhotoImage(fetch_image)
    profile_img_lbl.configure(image = fetch_image)
    gender_val.configure(text = user_details[3])
    dob_val.configure(text = user_details[4])
    phone_val.configure(text = f'+91 {user_details[10]}')
    email_val.configure(text = user_details[11])
    id_val.configure(text = f'{user_details[6]} ({user_details[5]})')
    doj_val.configure(text = user_details[7])
    department_val.configure(text = user_details[8])
    designation_val.configure(text = user_details[9])
    salary_val.configure(text = f'₹ {user_details[12]}')
    team_val.configure(text = user_details[19])
    project_val.configure(text = user_details[20])
    location_val.configure(text = user_details[13])
    street_city_val.configure(text = f'{user_details[14]}, {user_details[15]},')
    state_pin_val.configure(text = f'{user_details[16]} - {user_details[17]}')
    profile_frame.place(x=260,y=10)
    profile_lbl.place(x=0,y=0)
    hi_lbl.place(x=35,y=10)
    name_lbl.place(x=80,y=10)
    profile_img_lbl.place(x=450,y=10)
    gender_box.place(x=150,y=210)
    gender_lbl.place(x=160,y=215)
    gender_val.place(x=160,y=235)
    dob_box.place(x=630,y=210)
    dob_lbl.place(x=640,y=215)
    dob_val.place(x=640,y=235)
    phone_box.place(x=150,y=270)
    phone_lbl.place(x=160,y=275)
    phone_val.place(x=160,y=295)
    email_box.place(x=630,y=270)
    email_lbl.place(x=640,y=275)
    email_val.place(x=640,y=295)
    id_box.place(x=150,y=330)
    id_lbl.place(x=160,y=335)
    id_val.place(x=160,y=355)
    doj_box.place(x=630,y=330)
    doj_lbl.place(x=640,y=335)
    doj_val.place(x=640,y=355)
    department_box.place(x=150,y=390)
    department_lbl.place(x=160,y=395)
    department_val.place(x=160,y=415)
    designation_box.place(x=630,y=390)
    designation_lbl.place(x=640,y=395)
    designation_val.place(x=640,y=415)
    salary_box.place(x=150,y=450)
    salary_lbl.place(x=160,y=455)
    salary_val.place(x=160,y=475)
    team_box.place(x=630,y=450)
    team_lbl.place(x=640,y=455)
    team_val.place(x=640,y=475)
    project_box.place(x=150,y=510)
    project_lbl.place(x=160,y=515)
    project_val.place(x=160,y=535)
    location_box.place(x=630,y=510)
    location_lbl.place(x=640,y=515)
    location_val.place(x=640,y=535)
    address_box.place(x=150,y=570)
    address_lbl.place(x=160,y=575)
    street_city_val.place(x=160,y=595)
    state_pin_val.place(x=160,y=620)

def leave():
    home_frame.place_forget()
    profile_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=173)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    leave_icon = Label(frame,image=white_leave,bg='#7DA2F5').place(x=20,y=175)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=225)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    leave_frame.place(x=260,y=10)
    leave_bg_lbl.place(x=0,y=0)
    leave_desc_frame.place(x=30,y=50,width=940,height=260)
    from_lbl.place(x=10,y=10)
    from_entry_box.place(x=130,y=10)
    from_entry.place(x=135,y=20,width=290)
    to_lbl.place(x=520,y=10)
    to_entry_box.place(x=600,y=10)
    to_entry.place(x=605,y=20,width=290)
    no_of_days_lbl.place(x=10,y=60)
    no_of_days_entry_box.place(x=130,y=60)
    no_of_days_entry.place(x=135,y=70,width=290)
    leave_reason_lbl.place(x=10,y=110)
    leave_reason_entry_box.place(x=130,y=110)
    leave_reason_entry.place(x=135,y=120,width=430,height=40)
    apply_btn.place(x=420,y=185)
    apply_btn_lbl.place(x=460,y=187)
    Previous_leaves_lbl.place(x=30,y=350)
    leave_member_frame.place(x=30,y=390)
    leave_table_frame.place(x=0,y=0,width=940,height=230)
    leave_scroll_x.pack(side=BOTTOM,fill=X)
    leave_scroll_y.pack(side=RIGHT,fill=Y)
    leave_members_table.pack(fill=BOTH,expand=1)
    fetch_leave()

def apply_leave():
    if not leave_from_var.get() or not leave_to_var.get() or not leave_day_var.get() or not leave_reason_entry.get(1.0,'end-1c'):
        msg.showerror('Error','All fields are required')
    else:
        ask = msg.askquestion('Apply Leave','Are you sure you want to apply for leave?')
        if ask == 'yes':
            try:
                cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
                my_cursor = cnx.cursor()
                my_cursor.execute("INSERT INTO employee_leave(Employee_id,From_date,To_date,Leave_days,Leave_reason,Leave_status) VALUES (%s,%s,%s,%s,%s,%s)",(login.user_name.get(),leave_from_var.get(),
                leave_to_var.get(),
                leave_day_var.get(),
                leave_reason_entry.get(1.0,'end-1c'),
                'PENDING'))
                cnx.commit()
                cnx.close()
                msg.showinfo('Success','Leave request sent successfully')
                fetch_leave()
            except Exception as e:
                msg.showerror('Error',f'Error Due to: {str(e)}')
                
        else:
            pass

def fetch_leave():
    cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
    my_cursor = cnx.cursor()
    my_cursor.execute("SELECT * FROM employee_leave WHERE Employee_id=%s",(login.user_name.get(),))
    data = my_cursor.fetchall()
    if len(data) != 0:
        leave_members_table.delete(*leave_members_table.get_children())
        for i in data:
            leave_members_table.insert('',END,values=i)
        cnx.commit()
    cnx.close()

def resign():
    home_frame.place_forget()
    profile_frame.place_forget()
    leave_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=223)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=175)
    resign_icon = Label(frame,image=white_resign,bg='#7DA2F5').place(x=20,y=225)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    resign_frame.place(x=260,y=10)
    resign_bg_lbl.place(x=0,y=0)
    resign_desc_frame.place(x=30,y=50,width=940,height=300)
    resign_emp_id_lbl.place(x=10,y=10)
    resign_emp_id_entry_box.place(x=150,y=8)
    resign_emp_id_entry.place(x=155,y=18,width=290)
    resign_date_lbl.place(x=10,y=80)
    resign_date_entry_box.place(x=150,y=78)
    resign_date_entry.place(x=155,y=88,width=290)
    resign_reason_lbl.place(x=10,y=150)
    resign_reason_entry_box.place(x=150,y=148)
    resign_reason_entry.place(x=155,y=158,width=430,height=40)
    apply_resign_btn.place(x=420,y=225)
    apply_resign_btn_lbl.place(x=460,y=227)

def apply_resign():
    if not resign_date_var.get() or not resign_reason_entry.get(1.0,'end-1c'):
        msg.showerror('Error','Resignation date and reason are required')
    else:
        ask = msg.askquestion('Confirm','Are you sure you want to resign?')
        if ask == 'yes':
            try:
                cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
                my_cursor = cnx.cursor()
                my_cursor.execute("INSERT INTO resign(Application_id,Resign_date,Resign_reason,Resign_status) VALUES (%s,%s,%s,%s)",(login.user_name.get(),resign_date_var.get(),resign_reason_entry.get(1.0,'end-1c'),'PENDING'))
                cnx.commit()
                cnx.close()
                msg.showinfo('Success','Resignation request sent successfully')
            except:
                msg.showerror('Error','Something went wrong')
        else:
            pass

def help_support():
    home_frame.place_forget()
    profile_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=523)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=175)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=225)
    help_support_icon = Label(frame,image=white_help,bg='#7DA2F5').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    help_support_frame.place(x=260,y=10)
    help_support_bg_lbl.place(x=0,y=0)
    tell_us_lbl = Label(help_support_frame,bg='#EEEEEE')
    player = tkvideo("videos/help_support/tell_us.mp4",tell_us_lbl, loop = 0,size = (460,70))
    player.play()
    tell_us_lbl.place(x=300,y=166)
    msg_lbl.place(x=65,y=420)
    msg_entry_lbl.place(x=60,y=450)
    msg_entry.place(x=70,y=460,width=880,height=130)
    send_btn_lbl.place(x=850,y=616)
    send_btn.place(x=875,y=623)

def send_msg():
    if not msg_entry.get(1.0,'end-1c'):
        msg.showerror('Error','Message cannot be empty')
    else:
        try:
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("INSERT INTO enquiry(Employee_id,Message,Reply) VALUES(%s,%s,%s)",(login.log_name,msg_entry.get(1.0,'end-1c')," "))
            cnx.commit()
            cnx.close()
            msg.showinfo('Message','Thank you for writing to us. We will get back to you soon.')
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')
    
def info():
    home_frame.place_forget()
    profile_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    navigation_bar.place(x=0,y=573)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=175)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=225)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=white_info,bg='#7DA2F5').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    info_frame.place(x=260,y=10)
    info_bg_lbl.place(x=0,y=0)
    insta_btn.place(x=900,y=620)
    linkedin_btn.place(x=945,y=620)

def logout():
    home_frame.place_forget()
    profile_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=623)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=175)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=225)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=white_logout,bg='#7DA2F5').place(x=20,y=625)
    ask = msg.askquestion('Logout','Are you sure you want to logout?')
    if ask == 'yes':
        root.destroy()
        import login
    else:
        home()
        root.update()

        logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
        logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)



'''Instagram Linker'''

def insta():
    url = "https://www.instagram.com/tanishq_buddy/"
    webbrowser.open_new(url)

'''Linkedin Linker'''

def linkedin():
    url = "https://www.linkedin.com/in/tanish-gupta-85a440211/"
    webbrowser.open_new(url)

'''intialization of root window and its properties'''

root = Tk()
root.geometry("1280x690")
root.title(" Advance Employee Management System  ")
root.config(background="#5183F1")
root.wm_iconbitmap("icon/ems.ico")

style = ttk.Style()
style.configure("Treeview.Heading", font=('Poppins', 12,))
style.configure("Treeview.Item", font=('Poppins', 10),padding=5)

'''Navigation bar'''
ems_icon_img = ImageTk.PhotoImage(Image.open('Navbar Components/ems.png').resize((45,45),Image.Resampling.LANCZOS))

'''Blue icons'''
blue_home = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/home.png').resize((35,35),Image.Resampling.LANCZOS))

blue_profile = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/profile.png').resize((35,35),Image.Resampling.LANCZOS))

blue_leave = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/leave.png').resize((35,35),Image.Resampling.LANCZOS))

blue_resign = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/resign.png').resize((35,35),Image.Resampling.LANCZOS))

blue_help = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/help_support.png').resize((35,35),Image.Resampling.LANCZOS))

blue_info = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/info.png').resize((35,35),Image.Resampling.LANCZOS))

blue_logout = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/logout.png').resize((35,35),Image.Resampling.LANCZOS))


'''white icons'''
white_home = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/home.png').resize((35,35),Image.Resampling.LANCZOS))

white_profile = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/profile.png').resize((35,35),Image.Resampling.LANCZOS))

white_leave = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/leave.png').resize((35,35),Image.Resampling.LANCZOS))

white_resign = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/resign.png').resize((35,35),Image.Resampling.LANCZOS))

white_help = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/help_support.png').resize((35,35),Image.Resampling.LANCZOS))

white_info = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/info.png').resize((35,35),Image.Resampling.LANCZOS))

white_logout = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/logout.png').resize((35,35),Image.Resampling.LANCZOS))

'''Navigation background image'''
navigation = ImageTk.PhotoImage(Image.open('Navbar Components/button.png'))

'''Frame for Navigation bar'''
frame = Frame(root,bg='#5183F1',width=260,height=720)
frame.place(x=0,y=0)

ems_icon = Label(frame,image=ems_icon_img,bg='#5183F1')

home_icon = Label(frame,image=blue_home,bg='#5183F1')
home_icon.place(x=20, y=75)

profile_icon = Label(frame,image=blue_profile,bg='#5183F1')
profile_icon.place(x=20, y=125)

leave_icon = Label(frame,image=blue_leave,bg='#5183F1')
leave_icon.place(x=20, y=175)

resign_icon = Label(frame,image=blue_resign,bg='#5183F1')
resign_icon.place(x=20, y=225)

help_icon = Label(frame,image=blue_help,bg='#5183F1')
help_icon.place(x=20,y=525)

info_icon = Label(frame,image=blue_info,bg='#5183F1')
info_icon.place(x=20, y=575)

logout_icon = Label(frame,image=blue_logout,bg='#5183F1')
logout_icon.place(x=20, y=625)

navigation_bar = Label(frame,image=navigation,bg='#5183F1')

'''Buttons for navgation'''

home_btn = Button(frame,text='Home',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=home)
home_btn.place(x=65,y=79)

profile_btn = Button(frame,text='Profile',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=profile)
profile_btn.place(x=65,y=129)

leave_btn = Button(frame,text='Apply for Leave',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=leave)
leave_btn.place(x=65,y=179)

resign_btn = Button(frame,text='Apply Resignation',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=resign)
resign_btn.place(x=65,y=229)

help_support_btn = Button(frame,text='Help & Support',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=help_support)
help_support_btn.place(x=65,y=529)

info_btn = Button(frame,text='Info',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=info)
info_btn.place(x=65,y=579)

logout_btn = Button(frame,text='Logout',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=logout)
logout_btn.place(x=65,y=629)

'''home window'''
home_frame = Frame(root,bg='#5183F1',width=1000,height=670)

home_bg = ImageTk.PhotoImage(Image.open('images/home/home_bg.png'))

home_lbl = Label(home_frame,image=home_bg,bg='#5183F1')
home_lbl.place(x=0,y=0)

slogan_lbl = Label(home_frame)
player = tkvideo("videos/home/home_slogan.mp4",slogan_lbl, loop = 0,size = (430,160))
player.play()

slogan_lbl.place(x=30,y=150,width=430,height=160)

home_frame.place(x=260,y=10)

'''profile window'''
profile_frame = Frame(root,bg='#5183F1',width=1000,height=670)

profile_bg = ImageTk.PhotoImage(Image.open('images/profile/profile_bg.png'))

profile_lbl = Label(profile_frame,image=profile_bg,bg='#5183F1')

hi_lbl = Label(profile_frame,text='Hi,',bg='white',fg='black',font=('Poppins',25))

user_name = "Tanish Gupta"

name_lbl = Label(profile_frame,text=user_name,bg='white',fg='#5183F1',font=('Poppins',25))

profile_img = ImageTk.PhotoImage(Image.open('images/profile/emp1.png').resize((160,160),Image.Resampling.LANCZOS))

profile_img_lbl = Label(profile_frame,image=profile_img,bg='white')

entry_bg_img = ImageTk.PhotoImage(Image.open('images/profile/entry_bg.png'))

gender_box = Label(profile_frame,image=entry_bg_img,bg='white')

gender_lbl = Label(profile_frame,text='Gender :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

gender_val = Label(profile_frame,text='Male',bg='#F5F5F5',fg='black',font=('Poppins',13))

dob_box = Label(profile_frame,image=entry_bg_img,bg='white')

dob_lbl = Label(profile_frame,text='DOB (Date of Birth) :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

dob_val = Label(profile_frame,text='11/09/2002',bg='#F5F5F5',fg='black',font=('Poppins',13))

phone_box = Label(profile_frame,image=entry_bg_img,bg='white')

phone_lbl = Label(profile_frame,text='Phone No. :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

phone_val = Label(profile_frame,text='+91 9358174158',bg='#F5F5F5',fg='black',font=('Poppins',13))

email_box = Label(profile_frame,image=entry_bg_img,bg='white')

email_lbl = Label(profile_frame,text='Email - ID :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

email_val = Label(profile_frame,text='gtanish544@gmail.com',bg='#F5F5F5',fg='black',font=('Poppins',13))

id_box = Label(profile_frame,image=entry_bg_img,bg='white')

id_lbl = Label(profile_frame,text='ID :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

id_val = Label(profile_frame,text='9358174158 (Aadhar Number)',bg='#F5F5F5',fg='black',font=('Poppins',13))

doj_box = Label(profile_frame,image=entry_bg_img,bg='white')

doj_lbl = Label(profile_frame,text='DOJ (Date of Joining) :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

doj_val = Label(profile_frame,text='12/10/2022',bg='#F5F5F5',fg='black',font=('Poppins',13))

department_box = Label(profile_frame,image=entry_bg_img,bg='white')

department_lbl = Label(profile_frame,text='Department :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

department_val = Label(profile_frame,text='HR',bg='#F5F5F5',fg='black',font=('Poppins',13))

designation_box = Label(profile_frame,image=entry_bg_img,bg='white')

designation_lbl = Label(profile_frame,text='Designation :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

designation_val = Label(profile_frame,text='HR Manager',bg='#F5F5F5',fg='black',font=('Poppins',13))

salary_box = Label(profile_frame,image=entry_bg_img,bg='white')

salary_lbl = Label(profile_frame,text='Salary :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

salary_val = Label(profile_frame,text='₹ 2500000',bg='#F5F5F5',fg='black',font=('Poppins',13))

team_box = Label(profile_frame,image=entry_bg_img,bg='white')

team_lbl = Label(profile_frame,text='Team :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

team_val = Label(profile_frame,text='Duo',bg='#F5F5F5',fg='black',font=('Poppins',13))

project_box = Label(profile_frame,image=entry_bg_img,bg='white')

project_lbl = Label(profile_frame,text='Project :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

project_val = Label(profile_frame,text='HR Management Delhi',bg='#F5F5F5',fg='black',font=('Poppins',13))

location_box = Label(profile_frame,image=entry_bg_img,bg='white')

location_lbl = Label(profile_frame,text='Location :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

location_val = Label(profile_frame,text='Gurgaon',bg='#F5F5F5',fg='black',font=('Poppins',13))

address_entry_img = ImageTk.PhotoImage(Image.open('images/profile/address_entry.png'))

address_box = Label(profile_frame,image=address_entry_img,bg='white')

address_lbl = Label(profile_frame,text='Address :',bg='#F5F5F5',fg='black',font=('Poppins',10,'bold'))

street_city_val = Label(profile_frame,text='Gahoi Dham, Shiv Shankar Colony, Near Sarani Gate, Chhatarpur,',bg='#F5F5F5',fg='black',font=('Poppins',13))

state_pin_val = Label(profile_frame,text='Madhya Pradesh - 471001',bg='#F5F5F5',fg='black',font=('Poppins',13))

'''Leave Window'''
leave_frame = Frame(root,bg='#5183F1',width=1000,height=670)

leave_bg = ImageTk.PhotoImage(Image.open('images/leave/leave_bg.png'))

leave_bg_lbl = Label(leave_frame,image=leave_bg,bg='#5183F1')

leave_desc_frame = LabelFrame(leave_frame,text='  Leave Description :  ',bg='white',fg='black',font=('Poppins',12))

'''Variables'''
leave_from_var = StringVar()
leave_to_var = StringVar()
leave_day_var = IntVar()


from_lbl = Label(leave_desc_frame,text='From :',bg='white',fg='black',font=('Poppins',14))

leave_entry_img = ImageTk.PhotoImage(Image.open('images/leave/entry_bg.png'))

from_entry_box = Label(leave_desc_frame,image=leave_entry_img,bg='white')

from_entry = Entry(leave_desc_frame,textvariable=leave_from_var,bg='#F5F5F5',fg='black',font=('Poppins',14),bd=0)

to_lbl = Label(leave_desc_frame,text='To :',bg='white',fg='black',font=('Poppins',14))

to_entry_box = Label(leave_desc_frame,image=leave_entry_img,bg='white')

to_entry = Entry(leave_desc_frame,textvariable=leave_to_var,bg='#F5F5F5',fg='black',font=('Poppins',14),bd=0)

no_of_days_lbl = Label(leave_desc_frame,text='No. of Days :',bg='white',fg='black',font=('Poppins',14))

no_of_days_entry_box = Label(leave_desc_frame,image=leave_entry_img,bg='white')

no_of_days_entry = Entry(leave_desc_frame,textvariable=leave_day_var,bg='#F5F5F5',fg='black',font=('Poppins',14),bd=0)

leave_reason_lbl = Label(leave_desc_frame,text='Reason :',bg='white',fg='black',font=('Poppins',14))

reason_entry_img = ImageTk.PhotoImage(Image.open('images/leave/reason_entry.png'))

leave_reason_entry_box = Label(leave_desc_frame,image=reason_entry_img,bg='white')

leave_reason_entry = Text(leave_desc_frame,bg='#F5F5F5',fg='black',font=('Poppins',14),bd=0,wrap=WORD)

apply_btn_img = ImageTk.PhotoImage(Image.open('images/leave/apply_btn.png'))

apply_btn = Button(leave_desc_frame,image=apply_btn_img,bg='white',bd=0,cursor='hand2',command=apply_leave)

apply_btn_lbl = Button(leave_desc_frame,text='Apply',bg='black',fg='white',activebackground='black',activeforeground='black',font=('Poppins',16,'bold'),bd=0,cursor='hand2',command=apply_leave)

Previous_leaves_lbl = Label(leave_frame,text='Recent Leave History :',bg='white',fg='black',font=('Poppins',18))

leave_member_frame = Frame(leave_frame,bg='white',bd=0,relief=RIDGE,width=940,height=250)

leave_table_frame = Frame(leave_member_frame,bd=0)

leave_scroll_x = Scrollbar(leave_table_frame,orient=HORIZONTAL,repeatdelay=0,width=12,bd=0)
leave_scroll_y = Scrollbar(leave_table_frame,orient=VERTICAL,repeatdelay=0,width=12,bd=0)

leave_members_table = ttk.Treeview(leave_table_frame,columns=('emp_id','from_date','to_date','no_of_day','reason','leave_status',))

leave_members_table.heading('emp_id',text='Employee_id',)
leave_members_table.heading('from_date',text='From',)
leave_members_table.heading('to_date',text='To')
leave_members_table.heading('no_of_day',text='No. of Days')
leave_members_table.heading('reason',text='Reason')
leave_members_table.heading('leave_status',text='Leave Status')

leave_members_table['show'] = 'headings'

leave_members_table.column('emp_id',width=100)
leave_members_table.column('from_date',width=60)
leave_members_table.column('to_date',width=60)
leave_members_table.column('no_of_day',width=60)
leave_members_table.column('reason',width=300)
leave_members_table.column('leave_status',width=100)

leave_scroll_x.config(command=leave_members_table.xview)
leave_scroll_y.config(command=leave_members_table.yview)

'''Resign Window'''
resign_frame = Frame(root,bg='#5183F1',width=1000,height=670)

resign_bg = ImageTk.PhotoImage(Image.open('images/resign/resign_bg.png'))

resign_bg_lbl = Label(resign_frame,image=resign_bg,bg='#5183F1')

resign_desc_frame = LabelFrame(resign_frame,text='  Resignation Form :  ',bg='white',fg='black',font=('Poppins',12))

resign_entry_img = ImageTk.PhotoImage(Image.open('images/resign/entry_bg.png'))

'''Variables'''
resign_emp_id_var = StringVar()
resign_date_var = StringVar()

resign_emp_id_lbl = Label(resign_desc_frame,text='Employee ID :',bg='white',fg='black',font=('Poppins',14))

resign_emp_id_entry_box = Label(resign_desc_frame,image=resign_entry_img,bg='white')

resign_emp_id_entry = Entry(resign_desc_frame,textvariable=resign_emp_id_var,bg='#F5F5F5',fg='black',font=('Poppins',14),bd=0)

resign_date_lbl = Label(resign_desc_frame,text='Relieving Date :',bg='white',fg='black',font=('Poppins',14))

resign_date_entry_box = Label(resign_desc_frame,image=resign_entry_img,bg='white')

resign_date_entry = Entry(resign_desc_frame,textvariable=resign_date_var,bg='#F5F5F5',fg='black',font=('Poppins',14),bd=0)

resign_reason_lbl = Label(resign_desc_frame,text='Reason :',bg='white',fg='black',font=('Poppins',14))

resign_reason_entry_box = Label(resign_desc_frame,image=reason_entry_img,bg='white')

resign_reason_entry = Text(resign_desc_frame,bg='#F5F5F5',fg='black',font=('Poppins',14),bd=0,wrap=WORD)

resign_btn_img = ImageTk.PhotoImage(Image.open('images/resign/apply_btn.png'))

apply_resign_btn = Button(resign_desc_frame,image=resign_btn_img,bg='white',bd=0,cursor='hand2',command=apply_resign)

apply_resign_btn_lbl = Button(resign_desc_frame,text='Apply',bg='black',fg='white',activebackground='black',activeforeground='black',font=('Poppins',16,'bold'),bd=0,cursor='hand2',command=apply_resign)

'''help support window'''
help_support_frame = Frame(root,bg='#5183F1',width=1000,height=670)

help_support_bg = ImageTk.PhotoImage(Image.open('images/help_support/help_bg.png'))

help_support_bg_lbl = Label(help_support_frame,image=help_support_bg,bg='#5183F1')

msg_lbl = Label(help_support_frame,text='Message : ',bg='white',fg='black',font=('Poppins',16,'bold'))

msg_entry_img = ImageTk.PhotoImage(Image.open('images/help_support/message_entry.png'))

msg_entry_lbl = Label(help_support_frame,image=msg_entry_img,bg='white')

msg_entry = Text(help_support_frame,bg='#F5F5F5',fg='black',font=('Poppins',16),bd=0,wrap='word')

send_img = ImageTk.PhotoImage(Image.open('images/help_support/send_btn.png'))

send_btn_lbl = Button(help_support_frame,image=send_img,bg='white',activebackground='white',cursor='hand2',bd=0,command=send_msg)

send_btn = Button(help_support_frame,text='Send',bg='#5183F1',fg='#F5F5F5',bd=0,activebackground='#5183F1',activeforeground='black',cursor='hand2',font=('Poppins',14),command=send_msg)

'''info window'''
info_frame = Frame(root,bg='#5183F1',width=1000,height=670)

info_bg = ImageTk.PhotoImage(Image.open('images/info/info_bg.png'))

info_bg_lbl = Label(info_frame,image=info_bg,bg='#5183F1')

'''Instagram Button'''
insta_btn_img = ImageTk.PhotoImage(Image.open('images/info/instagram.png').resize((40,40),Image.Resampling.LANCZOS))

insta_btn = Button(info_frame, image=insta_btn_img, borderwidth=0, background="white", cursor="hand2", command=insta)

'''Linkedin Button'''
linkedin_img = ImageTk.PhotoImage(Image.open('images/info/linkedin.png').resize((40,40),Image.Resampling.LANCZOS))

linkedin_btn = Button(info_frame, image=linkedin_img, borderwidth=0, background="white", cursor="hand2", command=linkedin)

root.resizable(False,False)
root.mainloop()