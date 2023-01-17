from tkinter import *
import webbrowser
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from matplotlib.pyplot import show
from tkvideo import *
import mysql.connector
from login import log_name
import io
import smtplib

'''Home Window'''

def home():
    profile_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=73)
    home_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=white_home,bg='#7DA2F5').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    home_frame.place(x=260,y=10)
    player = tkvideo("videos/home/home_slogan.mp4",slogan_lbl, loop = 0,size = (430,160))
    player.play()
    slogan_lbl.place(x=30,y=150)

'''Profile Window'''

def profile():
    home_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=123)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=white_profile,bg='#7DA2F5').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
        my_cursor = cnx.cursor()
        my_cursor.execute("SELECT * FROM employee WHERE Employee_id = %s", (log_name,))
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
    profile_img_lbl.place(x=450,y=25)
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

'''Show Member Window'''

def show_members():
    home_frame.place_forget()
    profile_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=173)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=white_members,bg='#7DA2F5').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    show_member_frame.place(x=260,y=10)
    member_bg_lbl.place(x=0,y=0)
    search_by.place(x=35,y=75)
    search_value_lbl.place(x=305,y=45)
    search_box_lbl.place(x=300,y=70)
    search_entry.place(x=310,y=80,width=280)
    search_btn.place(x=630,y=65)
    search_lbl_btn.place(x=670,y=70)
    show_btn.place(x=800,y=65)
    show_lbl_btn.place(x=835,y=70)
    members_frame.place(x=15,y=160)
    table_frame.place(x=0,y=0,width=960,height=475)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    members_table.pack(fill=BOTH,expand=1)

'''Show Users Record'''

def show_all_user():
    cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
    my_cursor = cnx.cursor()
    show_search.set('')
    search_by.current(0)
    my_cursor.execute("SELECT * FROM employee")
    data = my_cursor.fetchall()
    if len(data) != 0:
        members_table.delete(*members_table.get_children())
        for i in data:
            members_table.insert('',END,values=i)
        cnx.commit()
    cnx.close()

'''Search Employee Record'''

def search_emp_data():
    if not show_search.get():
        msg.showerror('Error','Search value is required')
    elif not show_search_by.get():
        msg.showerror('Error','Select option from list')
    else:
        try:
            search_emp_by = ''
            if show_search_by.get() == 'Employee ID':
                search_emp_by = 'Employee_id'
            elif show_search_by.get() == 'Name':
                search_emp_by = 'First_name'
            elif show_search_by.get() == 'E - mail':
                search_emp_by = 'Email_id'
            elif show_search_by.get() == 'Phone No.':
                search_emp_by = 'Phone_no'
            elif show_search_by.get() == 'Department':
                search_emp_by = 'Department'
            elif show_search_by.get() == 'City':
                search_emp_by = 'City'
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("SELECT * FROM employee WHERE " +str(search_emp_by)+" LIKE '%"+str(show_search.get())+"%'")
            data = my_cursor.fetchall()
            if len(data) != 0:
                members_table.delete(*members_table.get_children())
                for i in data:
                    members_table.insert('',END,values=i)
                cnx.commit()
                cnx.close()
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')

'''Add Member Window'''

def add_member():
    home_frame.place_forget()
    profile_frame.place_forget()
    show_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=223)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=white_add,bg='#7DA2F5').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    add_member_frame.place(x=260,y=10)
    window_bg_lbl.place(x=0,y=0)
    user_img_lbl.place(x=450,y=5)
    upload_btn.place(x=500,y=175)
    add_first_name_lbl.place(x=40,y=185)
    add_first_name_box.place(x=30,y=205)
    add_first_name_entry.place(x=35,y=215,width=290)
    add_last_name_lbl.place(x=360,y=185)
    add_last_name_box.place(x=350,y=205)
    add_last_name_entry.place(x=355,y=215,width=290)
    add_gender_entry.place(x=670,y=212)
    add_dob_lbl.place(x=40,y=245)
    add_dob_box.place(x=30,y=265)
    add_dob_entry.place(x=35,y=275,width=290)
    add_id_entry.place(x=350,y=272)
    add_id_no_lbl.place(x=680,y=245)
    add_id_no_box.place(x=670,y=265)
    add_id_no_entry.place(x=675,y=275,width=290)
    add_doj_lbl.place(x=40,y=305)
    add_doj_box.place(x=30,y=325)
    add_doj_entry.place(x=35,y=330,width=290)
    add_department_entry.place(x=350,y=332)
    add_designation_lbl.place(x=680,y=305)
    add_designation_box.place(x=670,y=325)
    add_designation_entry.place(x=675,y=335,width=290)
    add_emp_id_lbl.place(x=40,y=365)
    add_emp_id_box.place(x=30,y=385)
    add_emp_id_entry.place(x=35,y=395,width=290)
    add_phone_lbl.place(x=360,y=365)
    add_phone_box.place(x=350,y=385)
    add_phone_entry.place(x=355,y=395,width=290)
    add_email_lbl.place(x=680,y=365)
    add_email_box.place(x=670,y=385)
    add_email_entry.place(x=675,y=395,width=290)
    add_salary_lbl.place(x=40,y=425)
    add_salary_box.place(x=30,y=445)
    add_salary_entry.place(x=35,y=455,width=290)
    add_location_lbl.place(x=360,y=425)
    add_location_box.place(x=350,y=445)
    add_location_entry.place(x=355,y=455,width=290)
    add_address_box.place(x=30,y=485,width=940,height=135)
    add_locality_lbl.place(x=15,y=-3)
    add_locality_box.place(x=5,y=17)
    add_locality_entry.place(x=15,y=27,width=900)
    add_city_lbl.place(x=15,y=55)
    add_city_box.place(x=5,y=75)
    add_city_entry.place(x=15,y=85,width=290)
    add_pincode_lbl.place(x=330,y=55)
    add_pincode_box.place(x=320,y=75)
    add_pincode_entry.place(x=330,y=85,width=290)
    add_state_entry.place(x=640,y=82)
    add_btn.place(x=465,y=622)
    add_btn_lbl.place(x=473,y=629)

'''Upload Photo'''

def upload_photo():
    user_img
    global filename,img
    f_types = [('Jpg Files', '*.jpg'),('PNG Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(Image.open(filename).resize((180,160),Image.Resampling.LANCZOS))
    user_img_lbl.configure(image=img,bg='white')

'''Add Member'''

def add_user():
    if not f_name.get() or not l_name.get() or not gender.get() or not dob.get() or not id_type.get() or not id_no.get() or not doj.get() or not department.get() or not designation.get() or not employee_id.get() or not phone_no.get() or not email_id.get() or not salary.get() or not location.get() or not locality.get() or not city.get() or not state.get() or not pincode.get():
        msg.showerror('Error','All the fields are required')

    else:
        try:
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            global filename
            my_cursor = cnx.cursor()
            fob = open(filename,'rb')
            fob = fob.read()
            my_cursor.execute("INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(employee_id.get(),
                            f_name.get(),
                            l_name.get(),
                            gender.get(),
                            dob.get(),
                            id_type.get(),
                            id_no.get(),
                            doj.get(),
                            department.get(),
                            designation.get(),
                            phone_no.get(),
                            email_id.get(),
                            salary.get(),
                            location.get(),
                            locality.get(),
                            city.get(),
                            pincode.get(),
                            state.get(),
                            fob,
                            'NULL',
                            'NULL'))
            my_cursor.execute("INSERT INTO login VALUES(%s,%s)",(employee_id.get(),'Buddy@123'))
            cnx.commit()
            cnx.close()
            msg.showinfo('Success','Employee has been added successfully')
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')

'''Update User Window'''

def update_user():
    home_frame.place_forget()
    profile_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=273)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=white_update,bg='#7DA2F5').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    update_profile_lbl.configure(image = update_profile_img)
    update_user_frame.place(x=260,y=10)
    update_user_bg_lbl.place(x=0,y=0)
    update_emp_id_lbl.place(x=60,y=20)
    update_profile_lbl.place(x=45,y=60)
    change_upload_btn.place(x=57,y=240)
    update_first_name_lbl.place(x=50,y=300)
    update_last_name_lbl.place(x=50,y=350)
    update_gender_lbl.place(x=50,y=400)
    update_dob_lbl.place(x=50,y=450)
    update_doj_lbl.place(x=50,y=500)
    update_department_lbl.place(x=50,y=550)
    update_search_by.place(x=290,y=42)
    update_search_lbl.place(x=545,y=15)
    update_search_box.place(x=535,y=35)
    update_search_entry.place(x=540,y=45,width=250)
    update_search_btn.place(x=820,y=30)
    update_search_btn_lbl.place(x=860,y=37)
    update_member_frame.place(x=290,y=90)
    update_table_frame.place(x=0,y=0,width=690,height=140)
    update_scroll_x.pack(side=BOTTOM,fill=X)
    update_scroll_y.pack(side=RIGHT,fill=Y)
    update_members_table.pack(fill=BOTH,expand=1)
    update_team_lbl.place(x=320,y=235)
    update_team_box.place(x=310,y=255)
    update_team_entry.place(x=315,y=265,width=290)
    update_project_lbl.place(x=660,y=235)
    update_project_box.place(x=650,y=255)
    update_project_entry.place(x=655,y=265,width=290)
    update_phone_lbl.place(x=320,y=295)
    update_phone_box.place(x=310,y=315)
    update_phone_entry.place(x=315,y=325,width=290)
    update_email_lbl.place(x=660,y=295)
    update_email_box.place(x=650,y=315)
    update_email_entry.place(x=655,y=325,width=290)
    update_designation_lbl.place(x=320,y=355)
    update_designation_box.place(x=310,y=375)
    update_designation_entry.place(x=315,y=385,width=290)
    update_salary_lbl.place(x=660,y=355)
    update_salary_box.place(x=650,y=375)
    update_salary_entry.place(x=655,y=385,width=290)
    update_location_lbl.place(x=320,y=415)
    update_location_box.place(x=310,y=435)
    update_location_entry.place(x=315,y=445,width=290)
    update_address_box.place(x=310 ,y=475,width=650,height=140)
    update_locality_lbl.place(x=15,y=-4)
    update_locality_box.place(x=5,y=16)
    update_locality_entry.place(x=10,y=26,width=360)
    update_city_lbl.place(x=395,y=-4)
    update_city_box.place(x=385,y=16)
    update_city_entry.place(x=390,y=26,width=240)
    update_pincode_lbl.place(x=15,y=54)
    update_pincode_box.place(x=5,y=74)
    update_pincode_entry.place(x=10,y=84,width=240)
    update_state_entry.place(x=390,y=81)
    update_record_btn.place(x=465,y=618)
    update_record_btn_lbl.place(x=505,y=625)
    delete_record_btn.place(x=650,y=618)
    delete_record_btn_lbl.place(x=690,y=625)
    fetch_all()
    update_members_table.bind("<ButtonRelease>",get_cursor)

'''Change Photo'''

def change_photo():
    update_profile_img
    global filename, img
    f_types = [('Jpg Files', '*.jpg'),('PNG Files', '*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(Image.open(filename).resize((180,160),Image.Resampling.LANCZOS))
    update_profile_lbl.configure(image=img,bg='#E3EFFB')

'''Fetch Employee Record'''

def fetch_all():
    cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
    my_cursor = cnx.cursor()
    my_cursor.execute("SELECT Employee_id,First_name,Last_name,Gender,Dob,Doj,Department,Designation,Phone_no,Email_id,Salary,Team_name,Project_name,Location,locality,City,Pincode,State,Profile_img FROM employee")
    data = my_cursor.fetchall()
    if len(data) != 0:
        update_members_table.delete(*update_members_table.get_children())
        for i in data:
            update_members_table.insert('',END,values=i)
        cnx.commit()
    cnx.close()

'''Get Information to Field'''

def get_cursor(ev=''):
    cursor_row = update_members_table.focus()
    content = update_members_table.item(cursor_row)
    row = content['values']
    update_emp_id.set(row[0])
    update_emp_id_lbl.configure(text=f'Employee ID : {row[0]}')
    update_first_name_lbl.configure(text=f'First Name : {row[1]}')
    update_last_name_lbl.configure(text=f'Last Name : {row[2]}')
    update_gender_lbl.configure(text=f'Gender : {row[3]}')
    update_dob_lbl.configure(text=f'DOB : {row[4]}')
    update_doj_lbl.configure(text=f'DOJ : {row[5]}')
    update_department_lbl.configure(text=f'Department : {row[6]}')
    update_team.set(row[11])
    update_project.set(row[12])
    update_phone.set(row[8])
    update_email.set(row[9])
    update_designation.set(row[7])
    update_salary.set(row[10])
    update_location.set(row[13])
    update_locality.set(row[14])
    update_city.set(row[15])
    update_pincode.set(row[16])
    update_state.set(row[17])

'''Update Employee Data'''

def update_emp_data():
    if not update_team.get() or not update_project.get() or not update_phone.get() or not update_email.get() or not update_designation.get() or not update_salary.get() or not update_location.get() or not update_locality.get() or not update_city.get() or not update_pincode.get() or not update_state.get():
        msg.showerror('Error','All the fields are required')
    else:
        try:
            global filename
            fob = open(filename,'rb')
            fob = fob.read()
            ask = msg.askquestion('Update','Are you sure you want to update the data?')
            if ask == 'yes':
                cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
                my_cursor = cnx.cursor()
                if not fob:
                    fob = 'NULL'
                my_cursor.execute("UPDATE employee SET Team_name=%s,Project_name=%s,Phone_no=%s,Email_id=%s,Designation=%s,Salary=%s,Location=%s,Locality=%s,City=%s,Pincode=%s,State=%s,Profile_img=%s WHERE employee_id=%s",(update_team.get(),
                                update_project.get(),
                                update_phone.get(),
                                update_email.get(),
                                update_designation.get(),
                                update_salary.get(),
                                update_location.get(),
                                update_locality.get(),
                                update_city.get(),
                                update_pincode.get(),
                                update_state.get(),
                                fob,
                                update_emp_id.get()))
            else:
                if not ask:
                    return
            cnx.commit()
            fetch_all()
            cnx.close()
            msg.showinfo('Success','Employee data has been updated successfully')
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')

'''Delete Employee Data'''

def delete_emp_data():
    if not update_emp_id.get():
        msg.showerror('Error','Employee details are required')
    else:
        try:
            ask = msg.askquestion('Delete','Are you sure you want to delete the data?')
            if ask == 'yes':
                cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
                my_cursor = cnx.cursor()
                sql = "DELETE FROM employee WHERE Employee_id=%s"
                val = (update_emp_id.get(),)
                my_cursor.execute(sql,val)
            else:
                if not ask:
                    return
            cnx.commit()
            fetch_all()
            cnx.close()
            msg.showinfo('Success','Employee data has been deleted successfully')
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')

'''Search Update Record'''

def search_update_emp_data():
    if not update_search_val.get():
        msg.showerror('Error','Search value is required')
    elif not update_search_by_val.get():
        msg.showerror('Error','Select option from list')
    else:
        try:
            search_emp_by = ''
            if update_search_by_val.get() == 'Employee ID':
                search_emp_by = 'Employee_id'
            elif update_search_by_val.get() == 'Name':
                search_emp_by = 'First_name'
            elif update_search_by_val.get() == 'E - mail':
                search_emp_by = 'Email_id'
            elif update_search_by_val.get() == 'Phone No.':
                search_emp_by = 'Phone_no'
            elif update_search_by_val.get() == 'Department':
                search_emp_by = 'Department'
            elif update_search_by_val.get() == 'Location':
                search_emp_by = 'City'
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("SELECT Employee_id,First_name,Last_name,Gender,Dob,Doj,Department,Designation,Phone_no,Email_id,Salary,Team_name,Project_name,Location,locality,City,Pincode,State,Profile_img FROM employee WHERE " +str(search_emp_by)+" LIKE '%"+str(update_search_val.get())+"%'")
            data = my_cursor.fetchall()
            if len(data) != 0:
                update_members_table.delete(*update_members_table.get_children())
                for i in data:
                    update_members_table.insert('',END,values=i)
                cnx.commit()
                cnx.close()
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')

'''leave Window'''
def leave():
    home_frame.place_forget()
    profile_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=323)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=white_leave,bg='#7DA2F5').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    leave_applicant_id_entry.configure(text='')
    leave_applicant_name_entry.configure(text='')
    leave_applicant_department_entry.configure(text='')
    leave_applicant_designation_entry.configure(text='')
    leave_from_date_entry.configure(text='')
    leave_to_date_entry.configure(text='')
    leave_reason_entry.configure(text='')
    leave_frame.place(x=260,y=10)
    leave_bg_lbl.place(x=0,y=0)
    leave_member_frame.place(x=50,y=50)
    leave_table_frame.place(x=0,y=0,width=940,height=250)
    leave_scroll_x.pack(side=BOTTOM,fill=X)
    leave_scroll_y.pack(side=RIGHT,fill=Y)
    leave_members_table.pack(fill=BOTH,expand=1)
    leave_applicant_id_lbl.place(x=150,y=310)
    leave_applicant_id_box.place(x=140,y=335)
    leave_applicant_id_entry.place(x=155,y=345)
    leave_applicant_name_lbl.place(x=600,y=310)
    leave_applicant_name_box.place(x=590,y=335)
    leave_applicant_name_entry.place(x=605,y=345)
    leave_applicant_department_lbl.place(x=150,y=380)
    leave_applicant_department_box.place(x=140,y=405)
    leave_applicant_department_entry.place(x=155,y=415)
    leave_applicant_designation_lbl.place(x=600,y=380)
    leave_applicant_designation_box.place(x=590,y=405)
    leave_applicant_designation_entry.place(x=605,y=415)
    leave_from_date_lbl.place(x=150,y=450)
    leave_from_date_box.place(x=140,y=475)
    leave_from_date_entry.place(x=155,y=485)
    leave_to_date_lbl.place(x=600,y=450)
    leave_to_date_box.place(x=590,y=475)
    leave_to_date_entry.place(x=605,y=485)
    leave_reason_lbl.place(x=150,y=520)
    leave_reason_box.place(x=140,y=545)
    leave_reason_entry.place(x=155,y=555)
    leave_approve_btn.place(x=340,y=615)
    leave_approve_btn_lbl.place(x=375,y=622)
    leave_reject_btn.place(x=565,y=615)
    leave_reject_btn_lbl.place(x=605,y=622)
    show_leave_request()
    leave_members_table.bind("<ButtonRelease-1>",get_leave_cursor)

def show_leave_request():
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
        my_cursor = cnx.cursor()
        leave_status = 'PENDING'
        my_cursor.execute("SELECT * FROM employee_leave WHERE Leave_status=%s",(leave_status,))
        data = my_cursor.fetchall()
        if len(data) != 0:
            leave_members_table.delete(*leave_members_table.get_children())
            for i in data:
                leave_members_table.insert('',END,values=i)
                cnx.commit()
            cnx.close()
    except Exception as es:
        msg.showerror("Error",f"Error due to: {str(es)}")

def get_leave_cursor(ev=''):
    cursor_row = leave_members_table.focus()
    content = leave_members_table.item(cursor_row)
    row = content['values']
    cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
    my_cursor = cnx.cursor()
    my_cursor.execute("SELECT First_name,Last_name,Department,Designation FROM employee WHERE Employee_id=%s",(row[0],))
    data = my_cursor.fetchone()
    leave_applicant_id_entry.configure(text=row[0])
    leave_applicant_name_entry.configure(text=f'{data[0]} {data[1]}')
    leave_applicant_department_entry.configure(text=data[2])
    leave_applicant_designation_entry.configure(text=data[3])
    leave_from_date_entry.configure(text=row[1])
    leave_to_date_entry.configure(text=row[2])
    leave_reason_entry.configure(text=row[4])
    cnx.commit()
    cnx.close()

def approve_leave():
    ask = msg.askquestion("Approve Leave","Are you sure you want to approve this leave request?")
    if ask == 'yes':
        try:
            cursor_row = leave_members_table.focus()
            content = leave_members_table.item(cursor_row)
            row = content['values']
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02",database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("UPDATE employee_leave SET Leave_status=%s WHERE Leave_id=%s",("APPROVED",row[6]))
            cnx.commit()
            my_cursor.execute("SELECT First_name,Last_name,Email_id FROM employee WHERE Employee_id=%s",(leave_applicant_id_entry.cget('text'),))
            data = my_cursor.fetchone()
            my_cursor.execute("Select From_date,To_date FROM employee_leave WHERE Leave_id=%s",(row[6],))
            data1 = my_cursor.fetchone()
            from_ = "gtanish544@gmail.com"
            to_ = data[2]
            subject = "Leave Request"
            name=f'{data[0]} {data[1]}'
            body = f"Hi , {name}\nYour Leave Request from {data1[0]} to {data1[1]} has been approved. !!!\n\nThank You"
            mesage = f"Subject : {subject}\n\n{body}"
            pwd = "owkazpyhirsijoew"
            cntn = smtplib.SMTP("smtp.gmail.com",587)
            cntn.starttls()
            cntn.login(from_,pwd)
            cntn.sendmail(from_,to_,mesage)
            cntn.close()
            show_leave_request()
        except Exception as e:
            msg.showerror("Error",f"Error due to : {str(e)}")
    else:
        pass
    cnx.close()

def reject_leave():
    ask = msg.askquestion("Reject Leave","Are you sure you want to reject this leave request?")
    if ask == 'yes':
        try:
            cursor_row = leave_members_table.focus()
            content = leave_members_table.item(cursor_row)
            row = content['values']
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("UPDATE employee_leave SET Leave_status=%s WHERE Leave_id=%s",("REJECTED",row[6]))
            cnx.commit()
            my_cursor.execute("SELECT First_name,Last_name,Email_id FROM employee WHERE Employee_id=%s",(leave_applicant_id_entry.cget('text'),))
            data = my_cursor.fetchone()
            my_cursor.execute("Select From_date,To_date FROM employee_leave WHERE Leave_id=%s",(row[6],))
            data1 = my_cursor.fetchone()
            from_ = "gtanish544@gmail.com"
            to_ = data[2]
            subject = "Leave Request"
            name=f'{data[0]} {data[1]}'
            body = f"Hi , {name}\nYour Leave Request from {data1[0]} to {data1[1]} has been rejected. !!!\n\nThank You"
            mesage = f"Subject : {subject}\n\n{body}"
            pwd = "owkazpyhirsijoew"
            cntn = smtplib.SMTP("smtp.gmail.com",587)
            cntn.starttls()
            cntn.login(from_,pwd)
            cntn.sendmail(from_,to_,mesage)
            cntn.close()
            show_leave_request()
        except Exception as e:
            msg.showerror("Error",f"Error due to : {str(e)}")
    else:
        pass
    cnx.close()

'''Resign Window'''
def resign():
    home_frame.place_forget()
    profile_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=373)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=white_resign,bg='#7DA2F5').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=blue_info,bg='#5183F1').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    resign_applicant_id_entry.configure(text='')
    resign_applicant_name_entry.configure(text='')
    resign_applicant_department_entry.configure(text='')
    resign_applicant_designation_entry.configure(text='')
    resign_date_entry.configure(text='')
    resign_reason_entry.configure(text='')
    resign_frame.place(x=260,y=10)
    resign_bg_lbl.place(x=0,y=0)
    resign_member_frame.place(x=50,y=50)
    resign_table_frame.place(x=0,y=0,width=940,height=250)
    resign_scroll_x.pack(side=BOTTOM,fill=X)
    resign_scroll_y.pack(side=RIGHT,fill=Y)
    resign_members_table.pack(fill=BOTH,expand=1)
    resign_applicant_id_lbl.place(x=150,y=310)
    resign_applicant_id_box.place(x=140,y=335)
    resign_applicant_id_entry.place(x=155,y=345)
    resign_applicant_name_lbl.place(x=600,y=310)
    resign_applicant_name_box.place(x=590,y=335)
    resign_applicant_name_entry.place(x=605,y=345)
    resign_applicant_department_lbl.place(x=150,y=380)
    resign_applicant_department_box.place(x=140,y=405)
    resign_applicant_department_entry.place(x=155,y=415)
    resign_applicant_designation_lbl.place(x=600,y=380)
    resign_applicant_designation_box.place(x=590,y=405)
    resign_applicant_designation_entry.place(x=605,y=415)
    resign_date_lbl.place(x=150,y=450)
    resign_date_box.place(x=140,y=475)
    resign_date_entry.place(x=155,y=485)
    resign_reason_lbl.place(x=150,y=520)
    resign_reason_box.place(x=140,y=545)
    resign_reason_entry.place(x=155,y=555)
    resign_approve_btn.place(x=340,y=615)
    resign_approve_btn_lbl.place(x=375,y=622)
    resign_reject_btn.place(x=565,y=615)
    resign_reject_btn_lbl.place(x=605,y=622)
    show_resign_request()
    resign_members_table.bind("<ButtonRelease-1>",get_resign_cursor)

'''Show Resign Requests in Table'''

def show_resign_request():
    try:
        cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
        my_cursor = cnx.cursor()
        resign_status = 'PENDING'
        my_cursor.execute("SELECT * FROM resign WHERE Resign_status=%s",(resign_status,))
        data = my_cursor.fetchall()
        if len(data) != 0:
            resign_members_table.delete(*resign_members_table.get_children())
            for i in data:
                resign_members_table.insert('',END,values=i)
                cnx.commit()
            cnx.close()
    except EXCEPTION as es:
        msg.showerror("Error",f"Error Due To: {str(es)}")

'''Get cursor to the item in resign table'''

def get_resign_cursor(ev=''):
    cursor_row = resign_members_table.focus()
    content = resign_members_table.item(cursor_row)
    row = content['values']
    cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
    my_cursor = cnx.cursor()
    my_cursor.execute("SELECT First_name,Last_name,Department,Designation FROM employee WHERE Employee_id=%s",(row[0],))
    data = my_cursor.fetchone()
    resign_applicant_id_entry.configure(text=row[0])
    resign_applicant_name_entry.configure(text=f'{data[0]} {data[1]}')
    resign_applicant_department_entry.configure(text=data[2])
    resign_applicant_designation_entry.configure(text=data[3])
    resign_date_entry.configure(text=row[1])
    resign_reason_entry.configure(text=row[2])
    cnx.commit()
    cnx.close()

'''Approve Resignation Request'''

def approve_resign():
    ask = msg.askquestion('Approve Resignation','Are you sure you want to approve this resignation request?')
    if ask == 'yes':
        try:
            cursor_row = resign_members_table.focus()
            content = resign_members_table.item(cursor_row)
            row = content['values']
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("UPDATE resign SET Resign_status=%s WHERE Resign_Id=%s",("APPROVED",row[4]))
            cnx.commit()
            my_cursor.execute("SELECT First_name,Last_name,Email_id FROM employee WHERE Employee_id=%s",(resign_applicant_id_entry.cget('text'),))
            data = my_cursor.fetchone()
            from_ = "gtanish544@gmail.com"
            to_ = data[2]
            subject = "Resignation Request"
            name=f'{data[0]} {data[1]}'
            body = f"Hi , {name}\nYour Resignation Request has been approved. !!!\n\nThank You"
            mesage = f"Subject : {subject}\n\n{body}"
            pwd = "owkazpyhirsijoew"
            cntn = smtplib.SMTP("smtp.gmail.com",587)
            cntn.starttls()
            cntn.login(from_,pwd)
            cntn.sendmail(from_,to_,mesage)
            cntn.close()
            show_resign_request()
            msg.showinfo('Success','Resignation request approved successfully!')
            cnx.close()
        except Exception as e:
            msg.showerror('Error',f'Error due to : {str(e)}')

'''Reject Resignation Request'''

def reject_resign():
    ask = msg.askquestion('Reject Resignation','Are you sure you want to reject this resignation request?')
    if ask == 'yes':
        try:
            cursor_row = resign_members_table.focus()
            content = resign_members_table.item(cursor_row)
            row = content['values']
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("UPDATE resign SET Resign_status=%s WHERE Resign_Id=%s",("REJECTED",row[4]))
            cnx.commit()
            my_cursor.execute("SELECT First_name,Last_name,Email_id FROM employee WHERE Employee_id=%s",(resign_applicant_id_entry.cget('text'),))
            data = my_cursor.fetchone()
            from_ = "gtanish544@gmail.com"
            to_ = data[2]
            subject = "Resignation Request"
            name=f'{data[0]} {data[1]}'
            body = f"Hi , {name}\nYour Resignation Request has been rejected. !!!\n\nThank You"
            mesage = f"Subject : {subject}\n\n{body}"
            pwd = "owkazpyhirsijoew"
            cntn = smtplib.SMTP("smtp.gmail.com",587)
            cntn.starttls()
            cntn.login(from_,pwd)
            cntn.sendmail(from_,to_,mesage)
            cntn.close()
            show_resign_request()
            msg.showinfo('Success','Resignation request rejected successfully!')
            cnx.close()
        except Exception as e:
            msg.showerror('Error',f'Error due to : {str(e)}')

'''Help Support Window'''

def help_support():
    home_frame.place_forget()
    profile_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=523)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
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

'''Send Message'''

def send_msg():
    if not msg_entry.get(1.0,'end-1c'):
        msg.showerror('Error','Message cannot be empty')
    else:
        try:
            cnx = mysql.connector.connect(host="localhost", user="root", password="Tanish02" , database="ORG")
            my_cursor = cnx.cursor()
            my_cursor.execute("INSERT INTO enquiry(Employee_id,Message,Reply) VALUES(%s,%s,%s)",(log_name,
                            msg_entry.get(1.0,'end-1c')," "))
            cnx.commit()
            cnx.close()
            msg.showinfo('Message','Thank you for writing to us. We will get back to you soon.')
        except Exception as e:
            msg.showerror('Error',f'Due to: {str(e)}')

'''Info Window'''

def info():
    home_frame.place_forget()
    profile_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    navigation_bar.place(x=0,y=573)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    logout_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
    help_support_icon = Label(frame,image=blue_help,bg='#5183F1').place(x=20,y=525)
    info_icon = Label(frame,image=white_info,bg='#7DA2F5').place(x=20,y=575)
    logout_icon = Label(frame,image=blue_logout,bg='#5183F1').place(x=20,y=625)
    info_frame.place(x=260,y=10)
    info_bg_lbl.place(x=0,y=0)
    insta_btn.place(x=900,y=620)
    linkedin_btn.place(x=945,y=620)

'''Logout Window'''

def logout():
    home_frame.place_forget()
    profile_frame.place_forget()
    show_member_frame.place_forget()
    add_member_frame.place_forget()
    update_user_frame.place_forget()
    leave_frame.place_forget()
    resign_frame.place_forget()
    help_support_frame.place_forget()
    info_frame.place_forget()
    navigation_bar.place(x=0,y=623)
    home_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    profile_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    show_members_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    add_member_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    update_user_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    leave_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    resign_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    help_support_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    info_btn.configure(bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white')
    logout_btn.configure(bg='#7DA2F5',fg='white',activebackground='#7DA2F5',activeforeground='black')
    home_icon = Label(frame,image=blue_home,bg='#5183F1').place(x=20,y=75)
    profile_icon = Label(frame,image=blue_profile,bg='#5183F1').place(x=20,y=125)
    show_members_icon = Label(frame,image=blue_members,bg='#5183F1').place(x=20,y=175)
    add_member_icon = Label(frame,image=blue_add,bg='#5183F1').place(x=20,y=225)
    update_user_icon = Label(frame,image=blue_update,bg='#5183F1').place(x=20,y=275)
    leave_icon = Label(frame,image=blue_leave,bg='#5183F1').place(x=20,y=325)
    resign_icon = Label(frame,image=blue_resign,bg='#5183F1').place(x=20,y=375)
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

'''intialization of Root Window and its Properties'''

root = Tk()
root.geometry("1280x690")
root.title(" Advance Employee Management System  ")
root.config(background="#5183F1")
root.wm_iconbitmap("icon/ems.ico")

'''Style Treeview'''

style = ttk.Style()
style.configure("Treeview.Heading", font=('Poppins', 12,))
style.configure("Treeview.Item", font=('Poppins', 10),padding=5)

'''Navigation bar'''

ems_icon_img = ImageTk.PhotoImage(Image.open('Navbar Components/ems.png').resize((45,45),Image.Resampling.LANCZOS))

'''Blue icons'''

blue_home = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/home.png').resize((35,35),Image.Resampling.LANCZOS))

blue_profile = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/profile.png').resize((35,35),Image.Resampling.LANCZOS))

blue_members = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/users.png').resize((35,35),Image.Resampling.LANCZOS))

blue_add = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/add_user.png').resize((35,35),Image.Resampling.LANCZOS))

blue_update = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/update_user.png').resize((35,35),Image.Resampling.LANCZOS))

blue_leave = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/leave.png').resize((35,35),Image.Resampling.LANCZOS))

blue_resign = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/resign.png').resize((35,35),Image.Resampling.LANCZOS))

blue_help = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/help_support.png').resize((35,35),Image.Resampling.LANCZOS))

blue_info = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/info.png').resize((35,35),Image.Resampling.LANCZOS))

blue_logout = ImageTk.PhotoImage(Image.open('Navbar Components/Blue icons/logout.png').resize((35,35),Image.Resampling.LANCZOS))

'''white icons'''

white_home = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/home.png').resize((35,35),Image.Resampling.LANCZOS))

white_profile = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/profile.png').resize((35,35),Image.Resampling.LANCZOS))

white_members = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/users.png').resize((35,35),Image.Resampling.LANCZOS))

white_add = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/add_user.png').resize((35,35),Image.Resampling.LANCZOS))

white_update = ImageTk.PhotoImage(Image.open('Navbar Components/White icons/update_user.png').resize((35,35),Image.Resampling.LANCZOS))

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

members_icon = Label(frame,image=blue_members,bg='#5183F1')
members_icon.place(x=20,y=175)

add_icon = Label(frame,image=blue_add,bg='#5183F1')
add_icon.place(x=20,y=225)

update_icon = Label(frame,image=blue_update,bg='#5183F1')
update_icon.place(x=20,y=275)

leave_icon = Label(frame,image=blue_leave,bg='#5183F1')
leave_icon.place(x=20, y=325)

resign_icon = Label(frame,image=blue_resign,bg='#5183F1')
resign_icon.place(x=20, y=375)

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

show_members_btn = Button(frame,text='Users',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=show_members)
show_members_btn.place(x=65,y=179)

add_member_btn = Button(frame,text='Add new Employee',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=add_member)
add_member_btn.place(x=65,y=229)

update_user_btn = Button(frame,text='Update Record',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=update_user)
update_user_btn.place(x=65,y=279)

leave_btn = Button(frame,text='Leave Applications',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=leave)
leave_btn.place(x=65,y=329)

resign_btn = Button(frame,text='Resign Applications',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=resign)
resign_btn.place(x=65,y=379)

help_support_btn = Button(frame,text='Help & Support',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=help_support)
help_support_btn.place(x=65,y=529)

info_btn = Button(frame,text='Info',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=info)
info_btn.place(x=65,y=579)

logout_btn = Button(frame,text='Logout',bg='#5183F1',fg='black',activebackground='#5183F1',activeforeground='white',cursor='hand2' ,bd=0,font=('Poppins',13),command=logout)
logout_btn.place(x=65,y=629)

'''Home Window Initialization'''

home_frame = Frame(root,bg='#5183F1',width=1000,height=670)

home_bg = ImageTk.PhotoImage(Image.open('images/home/home_bg.png'))

home_lbl = Label(home_frame,image=home_bg,bg='#5183F1')
home_lbl.place(x=0,y=0)

slogan_lbl = Label(home_frame)
player = tkvideo("videos/home/home_slogan.mp4",slogan_lbl, loop = 0,size = (430,160))
player.play()

slogan_lbl.place(x=30,y=150,width=430,height=160)

home_frame.place(x=260,y=10)

'''Profile Window Initialization'''

profile_frame = Frame(root,bg='#5183F1',width=1000,height=670)

profile_bg = ImageTk.PhotoImage(Image.open('images/profile/profile_bg.png'))

profile_lbl = Label(profile_frame,image=profile_bg,bg='#5183F1')

hi_lbl = Label(profile_frame,text='Hi,',bg='white',fg='black',font=('Poppins',25))

user_name = "Tanish Gupta"

name_lbl = Label(profile_frame,text=user_name,bg='white',fg='#5183F1',font=('Poppins',25))

profile_img = ImageTk.PhotoImage(Image.open('images/profile/emp1.png').resize((180,160),Image.Resampling.LANCZOS))

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

'''Users Window Initialization'''

show_member_frame = Frame(root,bd=0,width=1000,height=670,bg='#5183F1')

member_bg = ImageTk.PhotoImage(Image.open('images/users/record_bg.png'))

member_bg_lbl = Label(show_member_frame,image=member_bg,bg='#5183F1')

show_search_by = StringVar()

search_by = ttk.Combobox(show_member_frame,textvariable=show_search_by,font=('Poppins',12),width=25,state='readonly')
search_by['values'] = ('Search By','Employee ID','Name','E - mail','Phone No.','Department','City')

search_by.current(0)

search_value_lbl = Label(show_member_frame,text='Search Value : ',bg='white',font=('Poppins',12))

search_box = ImageTk.PhotoImage(Image.open('images/Users/search_box.png')) 

search_box_lbl = Label(show_member_frame,image=search_box,bg='white')

show_search = StringVar()
search_entry = Entry(show_member_frame,textvariable=show_search, bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

btn_bg = ImageTk.PhotoImage(Image.open('images/Users/btn.png'))

search_btn = Button(show_member_frame, image=btn_bg,borderwidth=0, background="white",activebackground='white', cursor="hand2",command=search_emp_data)

search_lbl_btn = Button(show_member_frame,text='Search',bg='#293D4D',fg='white',activebackground='#293D4D',activeforeground='black',cursor='hand2' ,bd=0,font=('Poppins',14),command=search_emp_data)

show_btn = Button(show_member_frame, image=btn_bg,borderwidth=0, background="white",activebackground='white', cursor="hand2",command=show_all_user)

show_lbl_btn = Button(show_member_frame,text='Show all',bg='#293D4D',fg='white',activebackground='#293D4D',activeforeground='black',cursor='hand2' ,bd=0,font=('Poppins',14),command=show_all_user)

members_frame = Frame(show_member_frame,bg='white',bd=0,relief=RIDGE,width=970,height=500)

table_frame = Frame(members_frame,bd=0)

scroll_x = Scrollbar(table_frame,orient=HORIZONTAL,repeatdelay=0,width=12,bd=0)
scroll_y = Scrollbar(table_frame,orient=VERTICAL,repeatdelay=0,width=12,bd=0)

members_table = ttk.Treeview(table_frame,columns=('emp_id','f_name','l_name','gen','dob','id_typ','id_no','doj','dep','design','phone','email','salary','city','home_locality','home_city','home_pincode','home state',))

members_table.heading('emp_id',text='Employee ID',)
members_table.heading('f_name',text='First Name')
members_table.heading('l_name',text='Last Name')
members_table.heading('gen',text='Gender')
members_table.heading('dob',text='DOB')
members_table.heading('id_typ',text='ID Type')
members_table.heading('id_no',text='ID No.')
members_table.heading('doj',text='DOJ')
members_table.heading('dep',text='Department')
members_table.heading('design',text='Designation')
members_table.heading('phone',text='Phone No.')
members_table.heading('email',text='E-mail')
members_table.heading('salary',text='Salary')
members_table.heading('city',text='Location')
members_table.heading('home_locality',text='Locality')
members_table.heading('home_city',text='City')
members_table.heading('home_pincode',text='Pincode')
members_table.heading('home state',text='State')

members_table['show'] = 'headings'

members_table.column('emp_id',width=100)
members_table.column('f_name',width=100)
members_table.column('l_name',width=100)
members_table.column('gen',width=100)
members_table.column('dob',width=100)
members_table.column('id_typ',width=100)
members_table.column('id_no',width=100)
members_table.column('doj',width=100)
members_table.column('dep',width=100)
members_table.column('design',width=100)
members_table.column('phone',width=100)
members_table.column('email',width=100)
members_table.column('salary',width=100)
members_table.column('city',width=100)
members_table.column('home_locality',width=100)
members_table.column('home_city',width=100)
members_table.column('home_pincode',width=100)
members_table.column('home state',width=100)

scroll_x.config(command=members_table.xview)
scroll_y.config(command=members_table.yview)

'''Add Member Window Initialization'''

'''Variables to add employee details'''

f_name = StringVar()
l_name = StringVar()
gender = StringVar()
dob = StringVar()
id_type = StringVar()
id_no = StringVar()
doj = StringVar()
department = StringVar()
designation = StringVar()
employee_id = StringVar()
phone_no = IntVar()
email_id = StringVar()
salary = DoubleVar()
location = StringVar()
locality = StringVar()
city = StringVar()
state = StringVar()
pincode = StringVar()

add_member_frame = Frame(root,bd=0,width=1000,height=670,bg='#5183F1')

window_bg = ImageTk.PhotoImage(Image.open('images/add_user/add_bg.png'))

window_bg_lbl = Label(add_member_frame,image=window_bg,bg='#5183F1')

user_img = ImageTk.PhotoImage(Image.open('images/add_user/user_default_profile.png'))

user_img_lbl = Label(add_member_frame,image=user_img,bg='white')

upload_btn = Button(add_member_frame,text='Upload Photo',bg='white',fg='#26A0F8',activebackground='white',activeforeground='black',cursor='hand2' ,bd=0,font=('Poppins',10),command=upload_photo)

add_entry_bg = ImageTk.PhotoImage(Image.open('images/add_user/entry_bg.png'))

add_first_name_lbl = Label(add_member_frame,text='First Name : ',bg='white',font=('Poppins',10))

add_first_name_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_first_name_entry = Entry(add_member_frame,textvariable=f_name,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_last_name_lbl = Label(add_member_frame,text='Last Name : ',bg='white',font=('Poppins',10))

add_last_name_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_last_name_entry = Entry(add_member_frame,textvariable=l_name,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_gender_entry = ttk.Combobox(add_member_frame,textvariable=gender,font=('Poppins',12),width=30,state='readonly')
add_gender_entry['values'] = ('Select Gender','Male','Female')

add_gender_entry.current(0)

add_dob_lbl = Label(add_member_frame,text='DOB (Date of Birth) : ',bg='white',font=('Poppins',10))

add_dob_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_dob_entry = Entry(add_member_frame,textvariable=dob,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_id_entry = ttk.Combobox(add_member_frame,textvariable=id_type,font=('Poppins',12),width=30,state='readonly')
add_id_entry['values'] = ('Select ID Proof','Aadhar Card','PAN Card','Driving License')

add_id_entry.current(0)

add_id_no_lbl = Label(add_member_frame,text='ID Number : ',bg='white',font=('Poppins',10))

add_id_no_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_id_no_entry = Entry(add_member_frame,textvariable=id_no,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_doj_lbl = Label(add_member_frame,text='DOJ (Date of Joining) : ',bg='white',font=('Poppins',10))

add_doj_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_doj_entry = Entry(add_member_frame,textvariable=doj,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_department_entry = ttk.Combobox(add_member_frame,textvariable=department,font=('Poppins',12),width=30,state='readonly')
add_department_entry['values'] = ('Select Department','Admin','Development','HR','Marketing','Sales')

add_department_entry.current(0)

add_designation_lbl = Label(add_member_frame,text='Designation : ',bg='white',font=('Poppins',10))

add_designation_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_designation_entry = Entry(add_member_frame,textvariable=designation,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_emp_id_lbl = Label(add_member_frame,text='Employee ID : ',bg='white',font=('Poppins',10))

add_emp_id_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_emp_id_entry = Entry(add_member_frame,textvariable=employee_id,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_phone_lbl = Label(add_member_frame,text='Phone No. : ',bg='white',font=('Poppins',10))

add_phone_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_phone_entry = Entry(add_member_frame,textvariable=phone_no,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_email_lbl = Label(add_member_frame,text='Email - ID : ',bg='white',font=('Poppins',10))

add_email_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_email_entry = Entry(add_member_frame,textvariable=email_id,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_salary_lbl = Label(add_member_frame,text='Salary : ',bg='white',font=('Poppins',10))

add_salary_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_salary_entry = Entry(add_member_frame,textvariable=salary,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_location_lbl = Label(add_member_frame,text='Location : ',bg='white',font=('Poppins',10))

add_location_box = Label(add_member_frame,image=add_entry_bg,bg='white')

add_location_entry = Entry(add_member_frame,textvariable=location,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_address_box = LabelFrame(add_member_frame,text='Address :',bg='white',font=('Poppins',10))

add_locality_lbl = Label(add_address_box,text='Locality : ',bg='white',font=('Poppins',10))

locality_box_img = ImageTk.PhotoImage(Image.open('images/add_user/locality_entry.png'))

add_locality_box = Label(add_address_box,image=locality_box_img,bg='white')

add_locality_entry = Entry(add_address_box,textvariable=locality,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_city_lbl = Label(add_address_box,text='City : ',bg='white',font=('Poppins',10))

add_city_box = Label(add_address_box,image=add_entry_bg,bg='white')

add_city_entry = Entry(add_address_box,textvariable=city,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_pincode_lbl = Label(add_address_box,text='Pincode : ',bg='white',font=('Poppins',10))

add_pincode_box = Label(add_address_box,image=add_entry_bg,bg='white')

add_pincode_entry = Entry(add_address_box,textvariable=pincode,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

add_state_entry = ttk.Combobox(add_address_box,textvariable=state,font=('Poppins',12),width=28,state='readonly')
add_state_entry['values'] = ('Select State',"Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")

add_state_entry.current(0)

add_btn_img = ImageTk.PhotoImage(Image.open('images/add_user/add_btn.png'))

add_btn = Button(add_member_frame,image=add_btn_img,bg='white',bd=0,cursor='hand2',activebackground='white',command=add_user)

add_btn_lbl = Button(add_member_frame,text='Add Employee',bg='#293D4D',fg='white',font=('Poppins',14),activebackground='#293D4D',bd=0,cursor='hand2',command=add_user)

'''Update User Window'''

update_user_frame = Frame(root,bg='#5183F1',width=1000,height=670)

update_user_bg = ImageTk.PhotoImage(Image.open('images/update_user/update_bg.png'))

update_user_bg_lbl = Label(update_user_frame,image=update_user_bg,bg='#5183F1')

update_emp_id = StringVar()

update_emp_id_lbl = Label(update_user_frame,text='Employee ID : ',bg='#E3EFFB',font=('Poppins',10))

update_profile_img = ImageTk.PhotoImage(Image.open('images/update_user/user_default_profile.png'))

update_profile_lbl = Label(update_user_frame,image=update_profile_img,bg='#E3EFFB')

change_upload_btn = Button(update_user_frame,text='Change / Upload Photo',bg='#E3EFFB',fg='#26A0F8',font=('Poppins',12),activebackground='#E3EFFB',activeforeground='black',bd=0,cursor='hand2',command=change_photo)

update_first_name_lbl = Label(update_user_frame,text='First Name : ',bg='#E3EFFB',font=('Poppins',13))

update_last_name_lbl = Label(update_user_frame,text='Last Name : ',bg='#E3EFFB',font=('Poppins',13))

update_gender_lbl = Label(update_user_frame,text = 'Gender : ',bg='#E3EFFB',font=('Poppins',13))

update_dob_lbl = Label(update_user_frame,text='DOB : ',bg='#E3EFFB',font=('Poppins',13))

update_doj_lbl = Label(update_user_frame,text='DOJ : ',bg='#E3EFFB',font=('Poppins',13))

update_department_lbl = Label(update_user_frame,text='Department : ',bg='#E3EFFB',font=('Poppins',13))

update_search_by_val = StringVar()

update_search_by = ttk.Combobox(update_user_frame,textvariable=update_search_by_val,font=('Poppins',12),width=22,state='readonly')
update_search_by['values'] = ('Search By','Employee ID','Name','E - mail','Phone No.','Department','Location')

update_search_by.current(0)

update_search_val = StringVar()

update_search_lbl = Label(update_user_frame,text='Search value : ',bg='white',font=('Poppins',10))

search_entry_img = ImageTk.PhotoImage(Image.open('images/update_user/search_entry.png'))

update_search_box = Label(update_user_frame,image=search_entry_img,bg='white')

update_search_entry = Entry(update_user_frame,textvariable=update_search_val,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

search_btn_img = ImageTk.PhotoImage(Image.open('images/update_user/search_btn.png'))

update_search_btn = Button(update_user_frame,image=search_btn_img,bg='white',bd=0,cursor='hand2',activebackground='white',command=search_update_emp_data)

update_search_btn_lbl = Button(update_user_frame,text='Search',bg='#293D4D',fg='white',font=('Poppins',14),activebackground='#293D4D',bd=0,cursor='hand2',command=search_update_emp_data)

update_member_frame = Frame(update_user_frame,bg='white',bd=0,relief=RIDGE,width=700,height=155)

update_table_frame = Frame(update_member_frame,bd=0)

update_scroll_x = Scrollbar(update_table_frame,orient=HORIZONTAL,repeatdelay=0,width=12,bd=0)
update_scroll_y = Scrollbar(update_table_frame,orient=VERTICAL,repeatdelay=0,width=12,bd=0)

update_members_table = ttk.Treeview(update_table_frame,columns=('emp_id','f_name','l_name','gen','dob','doj','dep','design','phone','email','salary','team_name','project_name','city','locality','home_city','home state','home_pincode',))

update_members_table.heading('emp_id',text='Employee ID',)
update_members_table.heading('f_name',text='First Name')
update_members_table.heading('l_name',text='Last Name')
update_members_table.heading('gen',text='Gender')
update_members_table.heading('dob',text='DOB')
update_members_table.heading('doj',text='DOJ')
update_members_table.heading('dep',text='Department')
update_members_table.heading('design',text='Designation')
update_members_table.heading('phone',text='Phone No.')
update_members_table.heading('email',text='E-mail')
update_members_table.heading('salary',text='Salary')
update_members_table.heading('team_name',text='Team')
update_members_table.heading('project_name',text='Project')
update_members_table.heading('city',text='Work City')
update_members_table.heading('locality',text='Locality')
update_members_table.heading('home_city',text='City')
update_members_table.heading('home state',text='State')
update_members_table.heading('home_pincode',text='Pincode')

update_members_table['show'] = 'headings'

update_members_table.column('emp_id',width=100)
update_members_table.column('f_name',width=100)
update_members_table.column('l_name',width=100)
update_members_table.column('gen',width=100)
update_members_table.column('dob',width=100)
update_members_table.column('doj',width=100)
update_members_table.column('dep',width=100)
update_members_table.column('design',width=100)
update_members_table.column('phone',width=100)
update_members_table.column('email',width=100)
update_members_table.column('salary',width=100)
update_members_table.column('team_name',width=100)
update_members_table.column('project_name',width=100)
update_members_table.column('city',width=100)
update_members_table.column('locality',width=100)
update_members_table.column('home_city',width=100)
update_members_table.column('home state',width=100)
update_members_table.column('home_pincode',width=100)

update_scroll_x.config(command=update_members_table.xview)
update_scroll_y.config(command=update_members_table.yview)

'''Variables Initialization'''

update_team = StringVar()
update_project = StringVar()
update_phone = IntVar()
update_email = StringVar()
update_designation = StringVar()
update_salary = DoubleVar()
update_location = StringVar()
update_locality = StringVar()
update_city = StringVar()
update_state = StringVar()
update_pincode = IntVar()

update_team_lbl = Label(update_user_frame,text='Team :',bg='white',font=('Poppins',10))

update_entry_img = ImageTk.PhotoImage(Image.open('images/update_user/entry_bg.png'))

update_team_box = Label(update_user_frame,image=update_entry_img,bg='white')

update_team_entry = Entry(update_user_frame,textvariable=update_team,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_project_lbl = Label(update_user_frame,text='Project :',bg='white',font=('Poppins',10))

update_project_box = Label(update_user_frame,image=update_entry_img,bg='white')

update_project_entry = Entry(update_user_frame,textvariable=update_project,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_phone_lbl = Label(update_user_frame,text='Phone No. :',bg='white',font=('Poppins',10))

update_phone_box = Label(update_user_frame,image=update_entry_img,bg='white')

update_phone_entry = Entry(update_user_frame,textvariable=update_phone,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_email_lbl = Label(update_user_frame,text='E-mail :',bg='white',font=('Poppins',10))

update_email_box = Label(update_user_frame,image=update_entry_img,bg='white')

update_email_entry = Entry(update_user_frame,textvariable=update_email,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_designation_lbl = Label(update_user_frame,text='Designation :',bg='white',font=('Poppins',10))

update_designation_box = Label(update_user_frame,image=update_entry_img,bg='white')

update_designation_entry = Entry(update_user_frame,textvariable=update_designation,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_salary_lbl = Label(update_user_frame,text='Salary :',bg='white',font=('Poppins',10))

update_salary_box = Label(update_user_frame,image=update_entry_img,bg='white')

update_salary_entry = Entry(update_user_frame,textvariable=update_salary,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_location_lbl = Label(update_user_frame,text='Location :',bg='white',font=('Poppins',10))

update_location_box = Label(update_user_frame,image=update_entry_img,bg='white')

update_location_entry = Entry(update_user_frame,textvariable=update_location,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_address_box = LabelFrame(update_user_frame,text='Address : ',bg='white',font=('Poppins',10))

update_locality_lbl = Label(update_address_box,text='Locality :',bg='white',font=('Poppins',10))

update_locality_img = ImageTk.PhotoImage(Image.open('images/update_user/locality_entry.png'))

update_locality_box = Label(update_address_box,image=update_locality_img,bg='white')

update_locality_entry = Entry(update_address_box,textvariable=update_locality,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_city_lbl = Label(update_address_box,text='City :',bg='white',font=('Poppins',10))

update_city_img = ImageTk.PhotoImage(Image.open('images/update_user/city_entry.png'))

update_city_box = Label(update_address_box,image=update_city_img,bg='white')

update_city_entry = Entry(update_address_box,textvariable=update_city,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_pincode_lbl = Label(update_address_box,text='Pincode :',bg='white',font=('Poppins',10))

update_pincode_box = Label(update_address_box,image=update_city_img,bg='white')

update_pincode_entry = Entry(update_address_box,textvariable=update_pincode,bd=0,background="#F5F5F5", fg="black", font="Poppins 12")

update_state_entry = ttk.Combobox(update_address_box,textvariable=update_state,font=('Poppins',12),width=25,state='readonly')
update_state_entry['values'] = ('Select State',"Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal")

update_state_entry.current(0)

update_btn_img = ImageTk.PhotoImage(Image.open('images/update_user/update_btn.png'))

update_record_btn = Button(update_user_frame,image=update_btn_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=update_emp_data)

update_record_btn_lbl = Button(update_user_frame,text='Update',bg='#D5E8E0',fg='#4B806E',activebackground='#D5E8E0',activeforeground='black',bd=0,cursor='hand2',font=('Poppins',14,'bold'),command=update_emp_data)

delete_btn_img = ImageTk.PhotoImage(Image.open('images/update_user/delete_btn.png'))

delete_record_btn = Button(update_user_frame,image=delete_btn_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=delete_emp_data)

delete_record_btn_lbl = Button(update_user_frame,text='Delete',bg='#F4DFD9',fg='#C42B1C',activebackground='#F4DFD9',activeforeground='black',bd=0,cursor='hand2',font=('Poppins',14,'bold'),command=delete_emp_data)

'''Leave Window'''
leave_frame = Frame(root,bg='#5183F1',width=1000,height=670)

leave_bg = ImageTk.PhotoImage(Image.open('images/leave/leave_bg.png'))

leave_bg_lbl = Label(leave_frame,image=leave_bg,bg='#5183F1')

leave_member_frame = Frame(leave_frame,bg='white',bd=0,relief=RIDGE,width=940,height=250)

leave_table_frame = Frame(leave_member_frame,bd=0)

leave_scroll_x = Scrollbar(leave_table_frame,orient=HORIZONTAL,repeatdelay=0,width=12,bd=0)
leave_scroll_y = Scrollbar(leave_table_frame,orient=VERTICAL,repeatdelay=0,width=12,bd=0)

leave_members_table = ttk.Treeview(leave_table_frame,columns=('emp_id','from_date','to_date','no_of_day','reason','leave_status',))

leave_members_table.heading('emp_id',text='Employee Id',)
leave_members_table.heading('from_date',text='From Date',)
leave_members_table.heading('to_date',text='To Date')
leave_members_table.heading('no_of_day',text='No. of Days')
leave_members_table.heading('reason',text='Reason For Leave')
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

leave_entry_img = ImageTk.PhotoImage(Image.open('images/leave/entry_bg.png'))

leave_applicant_id_lbl = Label(leave_frame,text='Applicant ID :',bg='white',font=('Poppins',12))

leave_applicant_id_box = Label(leave_frame,image=leave_entry_img,bg='white')

leave_applicant_id_entry = Label(leave_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

leave_applicant_name_lbl = Label(leave_frame,text='Applicant Name :',bg='white',font=('Poppins',12))

leave_applicant_name_box = Label(leave_frame,image=leave_entry_img,bg='white')

leave_applicant_name_entry = Label(leave_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

leave_applicant_department_lbl = Label(leave_frame,text='Applicant Department :',bg='white',font=('Poppins',12))

leave_applicant_department_box = Label(leave_frame,image=leave_entry_img,bg='white')

leave_applicant_department_entry = Label(leave_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

leave_applicant_designation_lbl = Label(leave_frame,text='Applicant Designation :',bg='white',font=('Poppins',12))

leave_applicant_designation_box = Label(leave_frame,image=leave_entry_img,bg='white')

leave_applicant_designation_entry = Label(leave_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

leave_from_date_lbl = Label(leave_frame,text='From Date :',bg='white',font=('Poppins',12))

leave_from_date_box = Label(leave_frame,image=leave_entry_img,bg='white')

leave_from_date_entry = Label(leave_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

leave_to_date_lbl = Label(leave_frame,text='To Date :',bg='white',font=('Poppins',12))

leave_to_date_box = Label(leave_frame,image=leave_entry_img,bg='white')

leave_to_date_entry = Label(leave_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

leave_reason_lbl = Label(leave_frame,text='Reason :',bg='white',font=('Poppins',12))

leave_reason_entry_img = ImageTk.PhotoImage(Image.open('images/leave/reason_entry.png'))

leave_reason_box = Label(leave_frame,image=leave_reason_entry_img,bg='white')

leave_reason_entry = Label(leave_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

leave_approve_btn_img = ImageTk.PhotoImage(Image.open('images/leave/approve_btn.png'))

leave_approve_btn = Button(leave_frame,image=leave_approve_btn_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=approve_leave)

leave_approve_btn_lbl = Button(leave_frame,text='Approve',bg='#D5E8E0',fg='#4B806E',activebackground='#D5E8E0',activeforeground='black',bd=0,cursor='hand2',font=('Poppins',14),command=approve_leave)

leave_reject_btn_img = ImageTk.PhotoImage(Image.open('images/leave/deny_btn.png'))

leave_reject_btn = Button(leave_frame,image=leave_reject_btn_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=reject_leave)

leave_reject_btn_lbl = Button(leave_frame,text='Reject',bg='#F4DFD9',fg='#C42B1C',activebackground='#F4DFD9',activeforeground='black',bd=0,cursor='hand2',font=('Poppins',14),command=reject_leave)

'''Resign Window'''
resign_frame = Frame(root,bg='#5183F1',width=1000,height=670)

resign_bg = ImageTk.PhotoImage(Image.open('images/resign/resign_bg.png'))

resign_bg_lbl = Label(resign_frame,image=resign_bg,bg='#5183F1')

resign_member_frame = Frame(resign_frame,bg='white',bd=0,relief=RIDGE,width=940,height=250)

resign_table_frame = Frame(resign_member_frame,bd=0)

resign_scroll_x = Scrollbar(resign_table_frame,orient=HORIZONTAL,repeatdelay=0,width=12,bd=0)
resign_scroll_y = Scrollbar(resign_table_frame,orient=VERTICAL,repeatdelay=0,width=12,bd=0)

resign_members_table = ttk.Treeview(resign_table_frame,columns=('emp_id','resign_date','resign_reason','resign_status',))

resign_members_table.heading('emp_id',text='Employee Id',)
resign_members_table.heading('resign_date',text='Relieving Date',)
resign_members_table.heading('resign_reason',text='Reason for Resignation')
resign_members_table.heading('resign_status',text='Resignation Status')

resign_members_table['show'] = 'headings'

resign_members_table.column('emp_id',width=150)
resign_members_table.column('resign_date',width=100)
resign_members_table.column('resign_reason',width=250)
resign_members_table.column('resign_status',width=150)

resign_scroll_x.config(command=resign_members_table.xview)
resign_scroll_y.config(command=resign_members_table.yview)

resign_entry_img = ImageTk.PhotoImage(Image.open('images/resign/entry_bg.png'))

resign_applicant_id_lbl = Label(resign_frame,text='Applicant ID :',bg='white',font=('Poppins',12))

resign_applicant_id_box = Label(resign_frame,image=resign_entry_img,bg='white')

resign_applicant_id_entry = Label(resign_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

resign_applicant_name_lbl = Label(resign_frame,text='Applicant Name :',bg='white',font=('Poppins',12))

resign_applicant_name_box = Label(resign_frame,image=resign_entry_img,bg='white')

resign_applicant_name_entry = Label(resign_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

resign_applicant_department_lbl = Label(resign_frame,text='Department :',bg='white',font=('Poppins',12))

resign_applicant_department_box = Label(resign_frame,image=resign_entry_img,bg='white')

resign_applicant_department_entry = Label(resign_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

resign_applicant_designation_lbl = Label(resign_frame,text='Designation :',bg='white',font=('Poppins',12))

resign_applicant_designation_box = Label(resign_frame,image=resign_entry_img,bg='white')

resign_applicant_designation_entry = Label(resign_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

resign_date_lbl = Label(resign_frame,text='Relieving Date :',bg='white',font=('Poppins',12))

resign_date_box = Label(resign_frame,image=resign_entry_img,bg='white')

resign_date_entry = Label(resign_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

resign_reason_lbl = Label(resign_frame,text='Reason for Resignation :',bg='white',font=('Poppins',12))

resign_reason_entry_img = ImageTk.PhotoImage(Image.open('images/resign/reason_entry.png'))

resign_reason_box = Label(resign_frame,image=resign_reason_entry_img,bg='white')

resign_reason_entry = Label(resign_frame,text='',bd=0,background="#F5F5F5", fg="black", font="Poppins 14")

resign_approve_btn_img = ImageTk.PhotoImage(Image.open('images/resign/approve_btn.png'))

resign_approve_btn = Button(resign_frame,image=resign_approve_btn_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=approve_resign)

resign_approve_btn_lbl = Button(resign_frame,text='Approve',bg='#D5E8E0',fg='#4B806E',activebackground='#D5E8E0',activeforeground='black',bd=0,cursor='hand2',font=('Poppins',14),command=approve_resign)

resign_reject_btn_img = ImageTk.PhotoImage(Image.open('images/resign/deny_btn.png'))

resign_reject_btn = Button(resign_frame,image=resign_reject_btn_img,bg='white',activebackground='white',bd=0,cursor='hand2',command=reject_resign)

resign_reject_btn_lbl = Button(resign_frame,text='Reject',bg='#F4DFD9',fg='#C42B1C',activebackground='#F4DFD9',activeforeground='black',bd=0,cursor='hand2',font=('Poppins',14),command=reject_resign)

'''Help Support Window Initialization'''

help_support_frame = Frame(root,bg='#5183F1',width=1000,height=670)

help_support_bg = ImageTk.PhotoImage(Image.open('images/help_support/help_bg.png'))

help_support_bg_lbl = Label(help_support_frame,image=help_support_bg,bg='#5183F1')

msg_lbl = Label(help_support_frame,text='Message : ',bg='white',fg='black',font=('Poppins',16,'bold'))

msg_entry_img = ImageTk.PhotoImage(Image.open('images/help_support/message_entry.png'))

msg_entry_lbl = Label(help_support_frame,image=msg_entry_img,bg='white')

msg_entry = Text(help_support_frame,bg='#F5F5F5',fg='black',font=('Poppins',16),bd=0,wrap=WORD)

send_img = ImageTk.PhotoImage(Image.open('images/help_support/send_btn.png'))

send_btn_lbl = Button(help_support_frame,image=send_img,bg='white',activebackground='white',cursor='hand2',bd=0,command=send_msg)

send_btn = Button(help_support_frame,text='Send',bg='#5183F1',fg='#F5F5F5',bd=0,activebackground='#5183F1',activeforeground='black',cursor='hand2',font=('Poppins',14),command=send_msg)

'''Info Window Initialization'''

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