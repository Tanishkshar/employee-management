from tkinter import *
from tkinter import ttk
# for styling
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x750+0+0')
        self.root.title("Employee Management System")

        # creating text variables for backend
        self.dep = StringVar()
        self.name = StringVar()
        self.phone = StringVar()
        self.design = StringVar()
        self.address = StringVar()
        self.country = StringVar()
        self.email = StringVar()
        self.marital = StringVar()
        self.dob = StringVar()
        self.doj = StringVar()
        self.salary = StringVar()
        self.gender = StringVar()
        self.id = StringVar()

        title_main = Label(self.root, font=("times new roman", 18, 'bold'), fg='red', bg='white',
                           text="EMPLOYEE MANAGEMENT SYSTEM")
        title_main.place(x=0, y=0, width=1300, height=50)
        logo = Image.open('emp_images/img1.jpg')
        # resizing image
        logo = logo.resize((50, 50), Image.ANTIALIAS)
        self.logo_img = ImageTk.PhotoImage(logo)
        self.logoon = Label(self.root, image=self.logo_img)
        self.logoon.place(x=389, y=0, width=50, height=50)

        # frame for images
        frame1 = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        frame1.place(x=0, y=50, width=1300, height=150)

        # placing images in our frame

        # image 1
        im1 = Image.open('emp_images/im1.jpg')
        # resizing image
        im1 = im1.resize((432, 150), Image.ANTIALIAS)
        self.im1_img = ImageTk.PhotoImage(im1)
        self.im1go = Label(self.root, image=self.im1_img)
        self.im1go.place(x=0, y=54, height=150)

        # image 2
        im2 = Image.open('emp_images/im2.jpg')
        # resizing image
        im2 = im2.resize((432, 150), Image.ANTIALIAS)
        self.im2_img = ImageTk.PhotoImage(im2)
        self.im2go = Label(self.root, image=self.im2_img)
        self.im2go.place(x=432, y=54, height=150)

        # image 3
        im3 = Image.open('emp_images/im3.jpg')
        # resizing image
        im3 = im3.resize((432, 150), Image.ANTIALIAS)
        self.im3_img = ImageTk.PhotoImage(im3)
        self.im3go = Label(self.root, image=self.im3_img)
        self.im3go.place(x=864, y=54, height=150)

        # main frame
        main_frame = Frame(self.root, relief=RIDGE, bd=2, bg='white')
        main_frame.place(x=0, y=207, width=1300, height=540)

        # frame inside main frame
        in1 = LabelFrame(main_frame, bd=2, relief=RIDGE, text='Employee Data', font=('arial', 9, 'bold'), fg='green',
                         bg='white')
        in1.place(x=5, y=5, width=1289, height=250)

        # down frame inside main
        in2 = LabelFrame(main_frame, bd=2, relief=RIDGE, text='Employee Database', font=('arial', 9, 'bold'),
                         fg='green', bg='white')
        in2.place(x=5, y=260, width=1289, height=270)

        # labels and entry fields
        # upper frame
        lb1 = Label(in1, text='Department', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb1.grid(row=0, column=0, padx=2, pady=8)

        # combo box
        dep = ttk.Combobox(in1, textvariable=self.dep, font=('arial', 8, 'bold'), width=18)
        dep['value'] = (
            'Select Department', 'HR', 'SDE1', 'SDE2', 'SDE3', 'data Analyst', 'Backend Developer', 'Supervisor')
        dep.grid(row=0, column=1, padx=2, pady=8)

        lb2 = Label(in1, text='Name:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb2.grid(row=1, column=0, padx=2, pady=8)

        lb2_entry = ttk.Entry(in1, textvariable=self.name, font=('times new roman', 8, 'bold'), width=18)
        lb2_entry.grid(row=1, column=1, padx=2, pady=6)

        lb3 = Label(in1, text='Phone No:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb3.grid(row=2, column=0, padx=2, pady=8)

        lb3_entry = ttk.Entry(in1, textvariable=self.phone, font=('times new roman', 8, 'bold'), width=18)
        lb3_entry.grid(row=2, column=1, padx=2, pady=6)

        lb4 = Label(in1, text='Designation:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb4.grid(row=3, column=0, padx=2, pady=8)

        lb4_entry = ttk.Entry(in1, textvariable=self.design, font=('times new roman', 8, 'bold'), width=18)
        lb4_entry.grid(row=3, column=1, padx=2, pady=6)

        lb5 = ttk.Combobox(in1, font=('times new roman', 8, 'bold'), width=18, state='readonly')
        lb5['values'] = ('Select Id Proof', 'Aadhar Card', 'Pan Card', 'Driving Licence', 'Marriage Certificate')
        lb5.current(0)
        lb5.grid(row=4, column=0, padx=2, pady=8)

        lb5_entry = ttk.Entry(in1, textvariable=self.id, font=('times new roman', 8, 'bold'), width=18)
        lb5_entry.grid(row=4, column=1, padx=2, pady=6)

        lb6 = Label(in1, text='Marital Status:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb6.grid(row=0, column=2, padx=2, pady=8)

        lb6_entry = ttk.Entry(in1, textvariable=self.marital, font=('times new roman', 8, 'bold'), width=18)
        lb6_entry.grid(row=0, column=3, padx=2, pady=6)

        lb7 = Label(in1, text='Address:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb7.grid(row=1, column=2, padx=2, pady=8)

        lb7_entry = ttk.Entry(in1, textvariable=self.address, font=('times new roman', 8, 'bold'), width=18)
        lb7_entry.grid(row=1, column=3, padx=2, pady=6)

        lb8 = Label(in1, text='Date Of Joining:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb8.grid(row=2, column=2, padx=2, pady=8)

        lb8_entry = ttk.Entry(in1, textvariable=self.doj, font=('times new roman', 8, 'bold'), width=18)
        lb8_entry.grid(row=2, column=3, padx=2, pady=6)

        lb9 = Label(in1, text='Gender:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb9.grid(row=3, column=2, padx=2, pady=8)

        lb9_entry = ttk.Entry(in1, textvariable=self.gender, font=('times new roman', 8, 'bold'), width=18)
        lb9_entry.grid(row=3, column=3, padx=2, pady=6)

        lb10 = Label(in1, text='Salary:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb10.grid(row=0, column=4, padx=2, pady=8)

        lb10_entry = ttk.Entry(in1, textvariable=self.salary, font=('times new roman', 8, 'bold'), width=18)
        lb10_entry.grid(row=0, column=5, padx=2, pady=6)

        lb11 = Label(in1, text='Date Of Birth:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb11.grid(row=1, column=4, padx=2, pady=8)

        lb11_entry = ttk.Entry(in1, textvariable=self.dob, font=('times new roman', 8, 'bold'), width=18)
        lb11_entry.grid(row=1, column=5, padx=2, pady=6)

        lb12 = Label(in1, text='Country:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb12.grid(row=2, column=4, padx=2, pady=8)

        lb12_entry = ttk.Entry(in1, textvariable=self.country, font=('times new roman', 8, 'bold'), width=18)
        lb12_entry.grid(row=2, column=5, padx=2, pady=6)

        lb13 = Label(in1, text='Email:', font=('times new roman', 12, 'bold'), bg='white', fg='black')
        lb13.grid(row=3, column=4, padx=2, pady=8)

        lb13_entry = ttk.Entry(in1, textvariable=self.email, font=('times new roman', 8, 'bold'), width=18)
        lb13_entry.grid(row=3, column=5, padx=2, pady=6)

        # image on side
        im4 = Image.open('emp_images/im5.jpg')
        # resizing image
        im4 = im4.resize((230, 220), Image.ANTIALIAS)
        self.im4_img = ImageTk.PhotoImage(im4)
        self.im4go = Label(in1, image=self.im4_img)
        self.im4go.place(x=900, y=0, height=220)

        # frame for buttons
        btn_fr = Frame(in1, bd=2, relief=RIDGE, bg='white')
        btn_fr.place(x=1140, y=0, width=120, height=220)

        # creating buttons inside it
        btn_add = Button(btn_fr, command=self.add, text='Add', font=('Arial', 10, 'bold'), width=14, bg='red',
                         fg='white', height=2)
        btn_add.grid(row=0, column=0)

        btn_upd = Button(btn_fr, command=self.update, text='Update', font=('Arial', 10, 'bold'), width=14, bg='red',
                         fg='white', height=2)
        btn_upd.grid(row=1, column=0)

        btn_delete = Button(btn_fr, command=self.delete, text='Delete', font=('Arial', 10, 'bold'), width=14, bg='red',
                            fg='white', height=2)
        btn_delete.grid(row=2, column=0)

        btn_clear = Button(btn_fr, command=self.clear, text='Clear', font=('Arial', 10, 'bold'), width=14, bg='red',
                           fg='white', height=2)
        btn_clear.grid(row=3, column=0)

        btn_exit = Button(btn_fr, command=self.exit, text='Exit', font=('Arial', 10, 'bold'), width=14, bg='red',
                          fg='white', height=2)
        btn_exit.grid(row=4, column=0)

        # search frame
        search = LabelFrame(in2, bd=2, relief=RIDGE, bg='white', text='Search Employee',
                            font=('times new roman', 9, 'bold'), fg='blue')
        search.place(x=2, y=0, width=1280, height=50)

        # labels for search frame
        lbl_search = Label(search, font=('arial', 10, 'bold'), text='Search By', width=20, fg='white', bg='blue')
        lbl_search.grid(row=0, column=0, padx=4, pady=2)

        self.var_search = StringVar()
        self.entry_search = StringVar()
        search_combo = ttk.Combobox(search, textvariable=self.var_search, width=20, height=50, state='readonly',
                                    font=('arial', 10, 'bold'))
        search_combo['values'] = (
            'Phone', 'Department', 'Designation', 'Name', 'Marital Status', 'Country', 'Email', 'Date of Birth',
            'Gender',
            'Salary', 'Address', 'Date of Joining', 'Country')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=2)

        search_ent = ttk.Entry(search, textvariable=self.entry_search, font=('arial', 9, 'bold'), width=20)
        search_ent.grid(row=0, column=2, padx=2, pady=2)

        srch_btn = Button(search, command=self.search, text='Search', font=('arial', 10, 'bold'), width=20, bg='blue',
                          fg='white')
        srch_btn.grid(row=0, column=3, padx=2, pady=2)

        show_all = Button(search, command=self.fetch, text='Show All', font=('arial', 10, 'bold'), width=20, bg='blue',
                          fg='white')
        show_all.grid(row=0, column=4, padx=2, pady=2)

        # logo image in side
        log = Image.open('emp_images/im6.jpg')
        log = log.resize((50, 50), Image.ANTIALIAS)
        self.log_img = ImageTk.PhotoImage(log)
        self.logon = Label(search, image=self.log_img)
        self.logon.place(x=950, y=0, width=50, height=30)

        lbl_slogan = Label(search, font=('times new roman', 15, 'bold'), text='Azaadi Ka Amrit Mahotsav', bg='white',
                           fg='green')
        lbl_slogan.place(x=1000, y=0, height=30)

        # database table
        # first creating scrollbars
        tab_fr = Frame(in2, bd=2, bg='grey', relief=RIDGE)
        tab_fr.place(x=0, y=55, width=1295, height=190)

        hor_scroll = ttk.Scrollbar(tab_fr, orient=HORIZONTAL)
        ver_scroll = ttk.Scrollbar(tab_fr, orient=VERTICAL)

        self.emp_data = ttk.Treeview(tab_fr, columns=(
            'id', 'Department', 'Name', 'Address', 'Gender', 'Date of Birth', 'Date of Joining', 'Marital Status',
            'Salary',
            'Designation',
            'Country', 'Email', 'Phone',), xscrollcommand=hor_scroll.set,
                                     yscrollcommand=ver_scroll.set)
        hor_scroll.pack(side=BOTTOM, fill=X)
        ver_scroll.pack(side=RIGHT, fill=Y)

        hor_scroll.config(command=self.emp_data.xview)
        ver_scroll.config(command=self.emp_data.yview)

        self.emp_data.heading('id', text='id')
        self.emp_data.heading('Department', text='Department')
        self.emp_data.heading('Name', text='Name')
        self.emp_data.heading('Address', text='Address')
        self.emp_data.heading('Gender', text='Gender')
        self.emp_data.heading('Date of Birth', text='Date of Birth')
        self.emp_data.heading('Date of Joining', text='Date of Joining')
        self.emp_data.heading('Marital Status', text='Marital Status')
        self.emp_data.heading('Salary', text='Salary')
        self.emp_data.heading('Designation', text='Designation')
        self.emp_data.heading('Country', text='Country')
        self.emp_data.heading('Email', text='Email')
        self.emp_data.heading('Phone', text='Phone')
        self.fetch()
        self.emp_data.bind("<ButtonRelease>", self.cursor)
        self.emp_data.pack(fill=BOTH, expand=1)

        # for resizing all columns
        self.emp_data['show'] = 'headings'
        self.emp_data.column('Department', width=70)
        self.emp_data.column('Name', width=70)
        self.emp_data.column('Phone', width=70)
        self.emp_data.column('id', width=70)
        self.emp_data.column('Designation', width=70)
        self.emp_data.column('Marital Status', width=70)
        self.emp_data.column('Address', width=70)
        self.emp_data.column('Country', width=70)
        self.emp_data.column('Date of Joining', width=70)
        self.emp_data.column('Gender', width=70)
        self.emp_data.column('Salary', width=70)
        self.emp_data.column('Date of Birth', width=70)
        self.emp_data.column('Email', width=70)

        # connection with database and backend now

    def add(self):

        if self.id.get() == '' or self.name.get() == '' or self.dep.get() == '':
            messagebox.showerror("Please fill id , name and department!")

        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='tanishk123',
                                           database='employee', port=3306)
            cursor = conn.cursor()
            cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key "
                           "update id=id+9", (
                               self.id.get(),
                               self.dep.get(),
                               self.name.get(),
                               self.address.get(),
                               self.gender.get(),
                               self.dob.get(),
                               self.doj.get(),
                               self.marital.get(),
                               self.salary.get(),
                               self.design.get(),
                               self.country.get(),
                               self.email.get(),
                               self.phone.get(),
                           ))

            conn.commit()
            self.fetch()
            conn.close()
            messagebox.showinfo("Success!", "Record is inserted")

    def fetch(self):
        first_connection = mysql.connector.connect(host="localhost", user="root", password="tanishk123",
                                                   database="employee", port=3306)
        cursor = first_connection.cursor()
        cursor.execute("select * from employee")
        fetch_rows = cursor.fetchall()
        if len(fetch_rows) != 0:
            # first we delete any residue data that is left before
            self.emp_data.delete(*self.emp_data.get_children())
            for i in fetch_rows:
                self.emp_data.insert("", END, values=i)
            first_connection.commit()
        first_connection.close()

    def cursor(self, event=""):
        rows = self.emp_data.focus()
        content = self.emp_data.item(rows)
        row = content['values']
        self.id.set(row[0])
        self.dep.set(row[1])
        self.name.set(row[2])
        self.address.set(row[3])
        self.gender.set(row[4])
        self.dob.set(row[5])
        self.doj.set(row[6])
        self.marital.set(row[7])
        self.salary.set(row[8])
        self.design.set(row[9])
        self.country.set(row[10])
        self.email.set(row[11])
        self.phone.set(row[12])

    def update(self):
        try:

            first_connection = mysql.connector.connect(host="localhost", user="root", password="tanishk123",
                                                       database="employee", port=3306)
            cursor = first_connection.cursor()
            up = messagebox.askyesno('Attention', 'Do you want to update this Data?')
            if up > 0:

                cursor.execute(

                    "update employee set `Dep`=%s, `Name`=%s, `Address`=%s, `Gender`=%s, `Dob`=%s, `Doj`=%s, "
                    "`Marital_status`=%s, `Salary`=%s,`Designation`=%s, `Country`=%s, `Email`=%s, `Phone`=%s where "
                    "`Id`=%s",
                    (
                        self.dep.get(),
                        self.name.get(),
                        self.address.get(),
                        self.gender.get(),
                        self.dob.get(),
                        self.doj.get(),
                        self.marital.get(),
                        self.salary.get(),
                        self.design.get(),
                        self.country.get(),
                        self.email.get(),
                        self.phone.get(),
                        self.id.get(),
                    ))


            else:

                if not up:
                    return
            first_connection.commit()
            self.fetch()
            first_connection.close()
            messagebox.showinfo('Success', 'Record is updated', parent=self.root)
        except Exception as es:
            messagebox.showerror('Error', f'Due To:{str(es)}', parent=self.root)

    def delete(self):
        first_connection = mysql.connector.connect(host="localhost", user="root", password="tanishk123",
                                                   database="employee", port=3306)
        cursor = first_connection.cursor()
        if self.dep.get() == '' or self.name.get() == '' or self.email.get() == '':
            messagebox.showerror('Oops', 'Please fill dep,Name,Email')
        else:
            try:
                dele = messagebox.askyesno('Attention', 'Do you want to delete this row?')
                if dele > 0:
                    query = "delete from employee where id=%s"
                    value = (self.id.get(),)
                    cursor.execute(query, value)
                    first_connection.commit()
                    first_connection.close()
                    self.fetch()
                    messagebox.showinfo("Success", "Employee has been deleted successfully!")
            except:
                pass

    def clear(self):
        self.id.set("")
        self.design.set("")
        self.dep.set("")
        self.address.set("")
        self.gender.set("")
        self.phone.set("")
        self.dob.set("")
        self.doj.set("")
        self.marital.set("")
        self.name.set("")
        self.country.set("")
        self.email.set("")
        self.salary.set("")

    def exit(self):
        exit_con = messagebox.askyesno("employee database", "Confirm Exit?")
        if exit_con > 0:
            root.destroy()
            return

    def search(self):
        if self.var_search.get() == '' or self.entry_search.get() == '':
            messagebox.showerror('Oops', 'Please Select any option')
        else:
            try:
                first_connection = mysql.connector.connect(host="localhost", user="root", password="tanishk123",
                                                           database="employee", port=3306)
                cursor = first_connection.cursor()
                cursor.execute('select * from employee where ' + str(self.var_search.get()) + " LIKE '%" + str(
                    self.entry_search.get() + "%'"))
                row = cursor.fetchall()
                if len(row) != 0:
                    self.emp_data.delete(*self.emp_data.get_children())
                    for i in row:
                        self.emp_data.insert("", END, values=i)
                first_connection.commit()
                first_connection.close()
            except:
                pass


root = Tk()
obj = employee(root)
root.mainloop()
