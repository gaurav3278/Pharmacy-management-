from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:

    def Update(self):
        conn = mysql.connector.connect(
            host='localhost', database='pharmacy', username='root', passwd='GauravRai@1234')
        my_cursor = conn.cursor()
        temp = True
        my_cursor.execute("SELECT * from pharma")
        myresult = my_cursor.fetchall()
        for row in myresult:
            if self.ref_var.get() == row[0]:
                temp = True
                break
            else:
                temp = False
        if temp == True:
            stmt = 'update pharma set Medi_name=%s where Reference=%s'
            data = (self.addmed_var.get(), self.ref_var.get())
            my_cursor.execute(stmt, data)
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Medicine updated successfully")
        else:
            stmt1 = 'update pharma set Reference=%s where Medi_name=%s'
            data1 = (self.ref_var.get(), self.addmed_var.get())
            my_cursor.execute(stmt1, data1)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Medicine updated successfully")

    def Delete(self):
        conn = mysql.connector.connect(
            host='localhost', database='pharmacy', username='root', passwd='GauravRai@1234')
        my_cursor = conn.cursor()
        stmt = 'delete from pharma where Reference=%s'
        data = (self.ref_var.get(),)
        my_cursor.execute(stmt, data)
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Medicine deleted successfully")

    def Clear(self):
        self.ref_var.set("")
        self.addmed_var.set("")

    def Addmed(self):
        conn = mysql.connector.connect(
            host='localhost', database='pharmacy', username='root', passwd='GauravRai@1234')
        my_cursor = conn.cursor()
        stmt = 'insert into pharma(Reference,Medi_name) values(%s,%s)'
        data = (self.ref_var.get(), self.addmed_var.get())
        my_cursor.execute(stmt, data)
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Medicine added successfully")

    def AddInfo(self):
        conn = mysql.connector.connect(
            host='localhost', database='pharmacy', username='root', passwd='GauravRai@1234')
        my_cursor = conn.cursor()
        stmt = 'insert into pharma_info (Reference_no, company_name,type_med,medicine_name,lot_no,issue_date,expiry_date,uses,side_effects,dosage,price,quantity) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (self.reference.get(), self.company.get(), self.type.get(), self.medicine.get(), self.lotNo.get(), self.id.get(
        ), self.expiry.get(), self.use.get(), self.se.get(), self.dose.get(), self.price.get(), self.quantity.get())
        my_cursor.execute(stmt, data)
        conn.commit()
        self.fetch_datainfo()
        conn.close()

        messagebox.showinfo("Success", "Medicine Info added successfully")

    def UpdateInfo(self):
        conn = mysql.connector.connect(
            host='localhost', database='pharmacy', username='root', passwd='GauravRai@1234')
        my_cursor = conn.cursor()
        stmt = 'update pharma_info set company_name=%s,type_med=%s,medicine_name=%s,lot_no=%s,issue_date=%s,expiry_date=%s,uses=%s,side_effects=%s,dosage=%s,price=%s,quantity=%s where Reference_no=%s'
        data = (self.company.get(), self.type.get(), self.medicine.get(), self.lotNo.get(), self.id.get(), self.expiry.get(
        ), self.use.get(), self.se.get(), self.dose.get(), self.price.get(), self.quantity.get(), self.reference.get())
        my_cursor.execute(stmt, data)
        conn.commit()
        self.fetch_datainfo()
        conn.close()

        messagebox.showinfo("Success", "Medicine Info updated successfully")

    def DeleteInfo(self):
        conn = mysql.connector.connect(
            host='localhost', database='pharmacy', username='root', passwd='GauravRai@1234')
        my_cursor = conn.cursor()
        stmt = 'delete from pharma_info where Reference_no=%s'
        data = (self.reference.get(),)
        my_cursor.execute(stmt, data)
        conn.commit()
        self.fetch_datainfo()
        conn.close()

        messagebox.showinfo("Success", "Medicine Info deleted successfully")

    def ClearInfo(self):
        self.reference.set("")
        self.company.set("")
        self.medicine.set("")
        self.type.set("")
        self.lotNo.set("")
        self.id.set("")
        self.expiry.set("")
        self.use.set("")
        self.se.set("")
        self.dose.set("")
        self.price.set("")
        self.quantity.set("")

    def Exit(self):
        self.root.destroy()

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", passwd="GauravRai@1234", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values=i)
                conn.commit()
        conn.close()

    def fetch_datainfo(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", passwd="GauravRai@1234", database="pharmacy")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma_info")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for j in row:
                self.pharmacy_table.insert("", END, values=j)
                conn.commit()
        conn.close()

    def searchData(self):
        conn = mysql.connector.connect(
            host="localhost", user="root", passwd="GauravRai@1234", database="pharmacy")
        my_cursor = conn.cursor()
        print(self.search_var.get())
        print(self.search_type.get())
        if(self.search_type.get()=='Reference'):
            stmt = 'select * from pharma_info where Reference_no=%s'
            data = (self.search_var.get(),)
            my_cursor.execute(stmt, data)
            rows = my_cursor.fetchall()
            print(rows)
            print(len(rows))
            if len(rows) != 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in rows:
                    self.pharmacy_table.insert("", END, values=i)
                    conn.commit()
                    messagebox.showinfo('Success', 'Medicine found')
        elif(self.search_type.get()=='Med name'):
            stmt = 'select * from pharma_info where medicine_name=%s'
            data = (self.search_var.get(),)
            my_cursor.execute(stmt, data)
            rows = my_cursor.fetchall()
            print(rows)
            print(len(rows))
            if len(rows) != 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in rows:
                    self.pharmacy_table.insert("", END, values=i)
                    conn.commit()
                    messagebox.showinfo('Success', 'Medicine found')
        elif(self.search_type.get()=='Lot number'):
            stmt = 'select * from pharma_info where lot_no=%s'
            data = (self.search_var.get(),)
            my_cursor.execute(stmt, data)
            rows = my_cursor.fetchall()
            print(rows)
            print(len(rows))
            if len(rows) != 0:
                self.pharmacy_table.delete(*self.pharmacy_table.get_children())
                for i in rows:
                    self.pharmacy_table.insert("", END, values=i)
                    conn.commit()
                    messagebox.showinfo('Success', 'Medicine found')

        conn.close()

    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management Sysytem")
        self.root.geometry("1580x800+0+0")

        self.addmed_var = StringVar()
        self.ref_var = StringVar()
        self.search_var = StringVar()
        self.search_type = StringVar()

        self.reference = StringVar()
        self.company = StringVar()
        self.medicine = StringVar()
        self.type = StringVar()
        self.lotNo = StringVar()
        self.id = StringVar()
        self.expiry = StringVar()
        self.use = StringVar()
        self.se = StringVar()
        self.dose = StringVar()
        self.price = DoubleVar()
        self.quantity = IntVar()

        labeltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
                           bg='white', fg='darkgreen', font=("times new roman", 30, 'bold'), padx=2, pady=4)

        labeltitle.pack(side=TOP, fill=X)
        img1 = Image.open("./logo.jpg")
        img1 = img1.resize((80, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=195, y=12)

        Dataframe = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        Dataframe.place(x=0, y=95, width=1270, height=310)
        Dataframeleft = LabelFrame(Dataframe, text="Medicine Information",
                                   bd=10, relief=RIDGE, fg="dark green", font=("arial", 15, 'bold'))
        Dataframeleft.place(x=0, y=5, width=700, height=270)
        DataframeRight = LabelFrame(Dataframe, text="Medicine Add Department",
                                    bd=10, relief=RIDGE, fg="dark green", font=("arial", 15, 'bold'))
        DataframeRight.place(x=710, y=5, width=498, height=270)

        Buttonframe = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        Buttonframe.place(x=0, y=405, width=1270, height=65)

        btnAddData = Button(Buttonframe, text="Add Medicine", font=(
            "arial", 11, 'bold'), bg="dark green", fg="white", command=self.AddInfo)
        btnAddData.grid(row=0, column=0)
        btnupdateData = Button(Buttonframe, text="Update", width=12, font=(
            "arial", 11, 'bold'), bg="dark green", fg="white", command=self.UpdateInfo)

        btnupdateData.grid(row=0, column=1)
        btndelData = Button(Buttonframe, text="Delete", width=12, font=(
            "arial", 11, 'bold'), bg="red", fg="white", command=self.DeleteInfo)
        btndelData.grid(row=0, column=2)
        btnresetData = Button(Buttonframe, text="Reset", width=12, font=(
            "arial", 11, 'bold'), bg="dark green", fg="white", command=self.ClearInfo)
        btnresetData.grid(row=0, column=3)
        btnexitData = Button(Buttonframe, text="Exit", width=12, font=(
            "arial", 11, 'bold'), bg="dark green", fg="white", command=self.Exit)
        btnexitData.grid(row=0, column=4)

        lblSearch = Label(Buttonframe, font=("arial", 12, "bold"),
                          text="Search", width=8, padx=10, bg="black", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        search_combo = ttk.Combobox(Buttonframe, width=12, font=(
            "arial", 11, "bold"), state='readonly',textvariable=self.search_type)
        search_combo["values"] = ("Reference", "Med name", "Lot number")
        search_combo.grid(row=0, column=6)
        search_combo.current(newindex=0)

        txtsearch = Entry(Buttonframe, bd=3, relief=RIDGE,
                          width=15, font=("arial", 10, "bold"), textvariable=self.search_var)
        txtsearch.grid(row=0, column=7)

        btnsearchData = Button(Buttonframe, text="Search", width=12, font=(
            "arial", 11, 'bold'), bg="dark green", fg="white", command=self.searchData)
        btnsearchData.grid(row=0, column=8)
        btnshowData = Button(Buttonframe, text="Show All", width=12, font=(
            "arial", 11, 'bold'), bg="dark green", fg="white",command=self.fetch_datainfo)
        btnshowData.grid(row=0, column=9)

        lblrefnum = Label(Dataframeleft, text="Reference No.", font=(
            "arial", 11, "bold"), width=11, fg="black", padx=2)
        lblrefnum.grid(row=0, column=0, sticky=W)
        txtrefnum = Entry(Dataframeleft, bd=3, textvariable=self.reference, font=(
            "arial", 10, "bold"), width=25, relief=RIDGE)
        txtrefnum.grid(row=0, column=1)

        lblcomname = Label(Dataframeleft, text="Company name:", font=(
            "arial", 11, "bold"), width=11, fg="black", padx=5)
        txtcomname = Entry(Dataframeleft, width=25, textvariable=self.company, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblcomname.grid(row=1, column=0, sticky=W)
        txtcomname.grid(row=1, column=1)

        lbltype = Label(Dataframeleft, text="Type Medicine", font=(
            "arial", 12, "bold"), width=11, fg="black", padx=2)
        lbltype.grid(row=2, column=0, sticky=W)

        type_combo = ttk.Combobox(
            Dataframeleft, width=23, font=("arial", 10, "bold"), textvariable=self.type)
        type_combo["values"] = ("Tablet", "Injection",
                                "Syrup", "Capsule", "Equipments")
        type_combo.grid(row=2, column=1)

        lblmedname = Label(Dataframeleft, text="Medicine Name", font=(
            "arial", 11, "bold"), width=11, fg="black", padx=2)
        lblmedname.grid(row=3, column=0, sticky=W)

        med_combo = Entry(Dataframeleft, width=25, bd=3, relief=RIDGE, font=(
            "arial", 10, "bold"), textvariable=self.medicine)
        med_combo.grid(row=3, column=1)

        lbllotnum = Label(Dataframeleft, text="Lot No.  :", font=(
            "arial", 11, "bold"), width=7, fg="black", padx=5)
        txtlotnum = Entry(Dataframeleft, width=25, textvariable=self.lotNo, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lbllotnum.grid(row=4, column=0, sticky=W)
        txtlotnum.grid(row=4, column=1)

        lblIssueDate = Label(Dataframeleft, text="Issue Date :", font=(
            "arial", 11, "bold"), width=10, fg="black", padx=2)
        txtIssueDate = Entry(Dataframeleft, width=25, textvariable=self.id, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(Dataframeleft, text="Expiry Date :", font=(
            "arial", 11, "bold"), width=10, fg="black", padx=2)
        txtExpDate = Entry(Dataframeleft, width=25, textvariable=self.expiry, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate.grid(row=6, column=1)

        lbluses = Label(Dataframeleft, text="Uses", font=(
            "arial", 11, "bold"), width=5, fg="black", padx=2)
        txtuses = Entry(Dataframeleft, width=25, textvariable=self.use, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lbluses.grid(row=7, column=0, sticky=W)
        txtuses.grid(row=7, column=1)

        lblSideeffects = Label(Dataframeleft, text="Side Effects", font=(
            "arial", 11, "bold"), width=10, fg="black", padx=2)
        txtSideeffects = Entry(Dataframeleft, width=25, textvariable=self.se, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblSideeffects.grid(row=8, column=0, sticky=W)
        txtSideeffects.grid(row=8, column=1)

        lblDosage = Label(Dataframeleft, text="Dosage :", font=(
            "arial", 11, "bold"), width=12, fg="black", padx=2)
        txtDosage = Entry(Dataframeleft, width=25, textvariable=self.dose, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblDosage.grid(row=0, column=4, sticky=W)
        txtDosage.grid(row=0, column=5)

        lblprice = Label(Dataframeleft, text="Tablets Price :", font=(
            "arial", 11, "bold"), width=12, fg="black", padx=2)
        txtprice = Entry(Dataframeleft, width=25, textvariable=self.price, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblprice.grid(row=1, column=4, sticky=W)
        txtprice.grid(row=1, column=5)

        lblquantity = Label(Dataframeleft, text="Tablets Qty :", font=(
            "arial", 11, "bold"), width=12, fg="black", padx=2)
        txtquantity = Entry(Dataframeleft, width=25, textvariable=self.quantity, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblquantity.grid(row=2, column=4, sticky=W)
        txtquantity.grid(row=2, column=5)

        img2 = Image.open("./download.jpg")
        img2 = img2.resize((200, 150), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)
        b2 = Button(self.root, image=self.img2, borderwidth=0)
        b2.place(x=350, y=220)

        img3 = Image.open("./pic1.jpg")
        img3 = img3.resize((200, 150), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img3)
        b3 = Button(self.root, image=self.img3, borderwidth=0)
        b3.place(x=515, y=220)

        img4 = Image.open("./pic2.jpg")
        img4 = img4.resize((340, 50), Image.ANTIALIAS)
        self.img4 = ImageTk.PhotoImage(img4)
        b4 = Button(self.root, image=self.img4, borderwidth=0)
        b4.place(x=760, y=145)

        img5 = Image.open("./pic1.jpg")
        img5 = img5.resize((120, 110), Image.ANTIALIAS)
        self.img5 = ImageTk.PhotoImage(img5)
        b3 = Button(self.root, image=self.img5, borderwidth=0)
        b3.place(x=1110, y=145)

        lblref1 = Label(DataframeRight, text="Reference No. :", font=(
            "arial", 12, "bold"), width=12, fg="black", padx=2)
        lblref1.place(x=0, y=60)
        txtref1 = Entry(DataframeRight, width=25, textvariable=self.ref_var, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        txtref1.place(x=135, y=60)
        # self.ref_var = txtref1.get()

        lblmed1 = Label(DataframeRight, text="Medicine Name :", font=(
            "arial", 12, "bold"), width=12, fg="black", padx=2)
        lblmed1.place(x=0, y=90)
        txtmed1 = Entry(DataframeRight, width=25, textvariable=self.addmed_var, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        txtmed1.place(x=135, y=90)

        # self.addmed_var = txtmed1.get()

        side_frame = Frame(DataframeRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=5, y=120, width=290, height=110)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(
            side_frame, xscrollcommand=sc_x.set, yscrollcommand=sc_y.set, column=("Ref", "Med name"))

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("Ref", text="Ref")
        self.medicine_table.heading("Med name", text="MedName")

        self.medicine_table["show"] = ("headings")
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("Ref", width=100)
        self.medicine_table.column("Med name", width=100)

        down_frame = Frame(DataframeRight, bd=4, relief=RIDGE, bg="white")
        down_frame.place(x=350, y=120, width=100, height=115)

        btnAddmed = Button(down_frame, text="ADD", font=(
            "arial", 8, "bold"), width=12, bg="lime", fg="black", pady=2, command=self.Addmed)
        btnAddmed.grid(row=0, column=0)

        btnupdatemed = Button(down_frame, text="UPDATE", font=(
            "arial", 8, "bold"), width=12, bg="blue", fg="black", pady=2, command=self.Update)
        btnupdatemed.grid(row=1, column=0)

        btndelmed = Button(down_frame, text="DELETE", font=(
            "arial", 8, "bold"), width=12, bg="red", fg="black", pady=2, command=self.Delete)
        btndelmed.grid(row=2, column=0)

        btnclrmed = Button(down_frame, text="CLEAR", font=(
            "arial", 8, "bold"), width=12, bg="orange", fg="black", pady=2, command=self.Clear)
        btnclrmed.grid(row=3, column=0)

        frame_details = Frame(self.root, bd=15, relief=RIDGE)
        frame_details.place(x=0, y=470, width=1270, height=180)

        scroll_x = ttk.Scrollbar(frame_details, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(frame_details, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(frame_details, column=("Ref", "Companyname", "type", "Medname", "lotno.", "issuedate",
                                           "expdate", "uses", "sideeffects", "dosage", "price", "productqty"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("Ref", text="Reference No.")
        self.pharmacy_table.heading("Companyname", text="Company Name")
        self.pharmacy_table.heading("type", text="Type of medicine")
        self.pharmacy_table.heading("Medname", text="Medicine Name")
        self.pharmacy_table.heading("lotno.", text="Lot No.")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Expiry Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideeffects", text="Side effects")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqty", text="Product Quantity")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("Ref", width=100)
        self.pharmacy_table.column("Companyname", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("Medname", width=100)
        self.pharmacy_table.column("lotno.", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideeffects", width=100)
        self.pharmacy_table.column("dosage", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("productqty", width=100)
        self.fetch_data()
        self.fetch_datainfo()


if __name__ == '__main__':
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()