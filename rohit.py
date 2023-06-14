import tkinter

from tkinter import *

from tkinter import messagebox,ttk

from PIL import Image,ImageTk

import sqlite3 as c

import os

import re

global add_btn # global done due to avoid "local variable error reference before assignment"

mydb=c.connect("inventory.db")

def addtables():
    mydb=c.connect("inventory.db")
    db=mydb.cursor()
    db.execute("""create table if not exists inventory ( 

    Product_ID int(5) primary key,

    Product_Name varchar(20),

    Price varchar(10),

    Quantity varchar(10),

    Company varchar(20),

    Contact varchar(10),

    address varchar(30))""")

    print("Table is created")

    sql="CREATE TABLE if not exists login (\
        fullname varchar(30),\
        username varchar(30) UNIQUE,\
        contact varchar(30),\
        recode varchar(30),\
        pass varchar(30),\
        conpass varchar(30),\
        PRIMARY KEY (recode));"
    db.execute(sql)







def clear_button_2_is_clicked():

    Field.delete(*Field.get_children())





def search_button_is_clicked():

    cur = mydb.cursor()

    global root

    global Combo_Search

    global Search_Bar

    if str(Combo_Search.get())=="" or str(Search_Bar.get())=="":

        
        messagebox.showerror("Error","Please Enter Data to search")
    else:
    
        cur.execute("select * from inventory where "+str(Combo_Search.get())+" LIKE '"+str(Search_Bar.get())+"%'")

        rows = cur.fetchall()

        if len(rows) != 0:

            Field.delete(*Field.get_children())

            for row in rows:

                Field.insert('', END, values=row)

                mydb.commit()



        else :
            messagebox.showerror("Error","No Data Found")



def update_2_is_clicked():

    global ID_txt

    global NAME_txt

    global PRICE_txt

    global QUANTITY_txt

    global COMPANY_txt

    global CONTACT_txt

    global ADDRESS_txt

    global Field

    cursor_row = Field.focus()

    content = Field.item(cursor_row)

    row =content['values']

    ID_txt.delete(0,END)
    
    NAME_txt.delete(0,END)

    PRICE_txt.delete(0,END)

    QUANTITY_txt.delete(0,END)

    COMPANY_txt.delete(0,END)

    CONTACT_txt.delete(0,END)

    ID_txt.insert(0,row[0])
    
    NAME_txt.insert(0,row[1])

    PRICE_txt.insert(0,row[2])

    QUANTITY_txt.insert(0,row[3])

    COMPANY_txt.insert(0,row[4])

    CONTACT_txt.insert(0,row[5])

    ADDRESS_txt.delete("1.0", END)

    ADDRESS_txt.insert(END,row[6])



def add_btn():

    global Product_ID 

    global Product_Name 

    global Price 

    global Quantity 

    global Contact 

    global Company 

    global ID_txt

    global NAME_txt

    global PRICE_txt

    global QUANTITY_txt

    global COMPANY_txt

    global CONTACT_txt

    global ADDRESS_txt

    global Field

    ADDRESS=ADDRESS_txt.get('1.0',END)

    mobile=str(CONTACT_txt.get())

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)

    if str(ID_txt.get())=="" or str(NAME_txt.get())=="" or str(PRICE_txt.get())=="" or str(QUANTITY_txt.get())=="" or str(COMPANY_txt.get())=="" or str(CONTACT_txt.get())=="" or str(ADDRESS)=="":
        messagebox.showerror("Error","All fields required")

    elif not str(ID_txt.get()).isdigit():
        messagebox.showerror("Error","Please Fill Digits only in PRODUCT ID")
        
    elif not str(NAME_txt.get()).isalpha():
        messagebox.showerror("Error","Please Fill Alphabets only in PRODUCT Name")

    elif not str(PRICE_txt.get()).isdigit():
        messagebox.showerror("Error","Please Fill Digits only in PRODUCT PRICE")

    elif not str(QUANTITY_txt.get()).isdigit():
        messagebox.showerror("Error","Please Fill Digits only in PRODUCT QUANTITY")

    
    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number")
        
    else:
        
        cur = mydb.cursor()

        cur.execute("insert into inventory (Product_ID,Product_Name,Price,Quantity,Company,Contact,address)values('%s','%s','%s','%s','%s','%s','%s')"%(str(ID_txt.get()),str(NAME_txt.get()),(PRICE_txt.get()),(QUANTITY_txt.get()),str(COMPANY_txt.get()),str(CONTACT_txt.get()),str(ADDRESS)))
        mydb.commit()



        cur = mydb.cursor()

        select = "select * from inventory"

        cur.execute(select)

        rows = cur.fetchall()

        if len(rows) != 0:

            Field.delete(*Field.get_children())

            for row in rows:

                Field.insert('', END, values=row)

                mydb.commit()



def search_all_bth():

    global Field

    cur = mydb.cursor()

    select = "select * from inventory "

    cur.execute(select)

    rows = cur.fetchall()

    Field.delete(* Field.get_children())

    for row in rows :

        Field.insert('',END,values = row)

        mydb.commit()



def delete_button_is_clicked():

    global Field

    cursor_row = Field.focus()

    content = Field.item(cursor_row)

    row = content['values']

    cur = mydb.cursor()

    select = (f"delete from inventory where Product_ID = {row[0]}")

    cur.execute(select)

    mydb.commit()

    search_all_bth()



def clear_button_is_clicked():
    global Field

    ID_txt.delete(0,END)

    NAME_txt.delete(0, END)

    PRICE_txt.delete(0, END)

    CONTACT_txt.delete(0, END)

    COMPANY_txt.delete(0, END)

    QUANTITY_txt.delete(0, END)

    ADDRESS_txt.delete("1.0",END)



def update_button_is_clicked():

    global Product_ID 

    global Product_Name 

    global Price 

    global Quantity 

    global Contact 

    global Company 

    global ID_txt

    global NAME_txt

    global PRICE_txt

    global QUANTITY_txt

    global COMPANY_txt

    global CONTACT_txt

    global ADDRESS_txt

    global Combo_Search

    global Search_Bar

    global Field



    ADDRESS = ADDRESS_txt.get('1.0', END)

    mobile=str(CONTACT_txt.get())

    def isvalidmobile(s):
        Pattern=re.compile("(0|91)?[6-9][0-9]{9}")
        return Pattern.match(s)

    if str(ID_txt.get())=="" or str(NAME_txt.get())=="" or str(PRICE_txt.get())=="" or str(QUANTITY_txt.get())=="" or str(COMPANY_txt.get())=="" or str(CONTACT_txt.get())=="" or str(ADDRESS)=="":
        messagebox.showerror("Error","All fields required")

    elif not str(ID_txt.get()).isdigit():
        messagebox.showerror("Error","Please Fill Digits only in PRODUCT ID")
        
    elif not str(NAME_txt.get()).isalpha():
        messagebox.showerror("Error","Please Fill Alphabets only in PRODUCT Name")

    elif not str(PRICE_txt.get()).isdigit():
        messagebox.showerror("Error","Please Fill Digits only in PRODUCT PRICE")

    elif not str(QUANTITY_txt.get()).isdigit():
        messagebox.showerror("Error","Please Fill Digits only in PRODUCT QUANTITY")

    
    elif (isvalidmobile(mobile)) is None:
        messagebox.showerror("Error","Incorrect Mobile Number"+"\nPlease Enter Indian Mobile Number")

    else:
        
        cur = mydb.cursor()

        sql1="UPDATE inventory SET Product_Name='%s' WHERE Product_ID='%s';"%(str(NAME_txt.get()),ID_txt.get())
        sql2="UPDATE inventory SET Price='%s' WHERE Product_ID='%s';"%(str(PRICE_txt.get()),ID_txt.get())
        sql3="UPDATE inventory SET Quantity='%s' WHERE Product_ID='%s';"%(str(QUANTITY_txt.get()),ID_txt.get())
        sql4="UPDATE inventory SET Contact='%s' WHERE Product_ID='%s';"%(str(CONTACT_txt.get()),ID_txt.get())
        sql5="UPDATE inventory SET address='%s' WHERE Product_ID='%s';"%(str(ADDRESS),ID_txt.get())

        cur.execute(sql1)
        mydb.commit()
        cur.execute(sql2)
        mydb.commit()
        cur.execute(sql3)
        mydb.commit()
        cur.execute(sql4)
        mydb.commit()
        cur.execute(sql5)
        mydb.commit()
        
        cur = mydb.cursor()

        select = "select * from inventory"

        cur.execute(select)

        rows = cur.fetchall()

        if len(rows) != 0:

            Field.delete(*Field.get_children())

            for row in rows:

                Field.insert('', END, values=row)

                mydb.commit()




def product_details():

    pop = Toplevel()

    pop.title("Prodcut Details ")

    ws = pop.winfo_screenwidth()

    hs = pop.winfo_screenheight()

    w = 630

    h = 280

    x = int(ws / 2 - w / 2 - 20)

    y = int(hs / 2 - h / 2 - 30)

    data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)

    pop.geometry(data)

    pop.configure(bg="#ffffff")

    pop.resizable(0, 0)

    cursor_row = Field.focus()

    content = Field.item(cursor_row)

    row = content['values']

    label1 = Label(pop, text=(f"Product ID "), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))

    label1.grid(row=0, column=0, sticky="w", padx=30)



    label2 = Label(pop, text=(f"Product Name"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))

    label2.grid(row=1, column=0, sticky="w", padx=30)



    label3 = Label(pop, text=(f"Price "), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))

    label3.grid(row=2, column=0, sticky="w", padx=30)
  


    label4 = Label(pop, text=(f"Quantity"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))

    label4.grid(row=3, column=0, sticky="w", padx=30)



    label5 = Label(pop, text=(f"Mfg Company "), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))

    label5.grid(row=4, column=0, sticky="w", padx=30)



    label6 = Label(pop, text=(f"Phone No"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))

    label6.grid(row=5, column=0, sticky="w", padx=30, pady=(0, 0))



    label7 = Label(pop, text=(f"Address"), bg="#ffffff", anchor=W, font=("Times New Roman", 22, "bold"))

    label7.grid(row=6, column=0, sticky="w", padx=30, pady=(0, 0))



    label8 = Label(pop, text=(f":    {row[0]}"), bg="#ffffff",fg = "#676767", anchor=W,

                   font=("Times New Roman", 19, "bold"))

    label8.grid(row=0, column=1, sticky="w")



    label9 = Label(pop, text=(f":    {row[1]}"), bg="#ffffff",fg = "#676767", anchor=W,

                   font=("Times New Roman", 19, "bold"))

    label9.grid(row=1, column=1, sticky="w")



    label10 = Label(pop, text=(f":    {row[2]}"), bg="#ffffff",fg = "#676767", anchor=W,

                    font=("Times New Roman", 19, "bold"))

    label10.grid(row=2, column=1, sticky="w")



    label11 = Label(pop, text=(f":    {row[3]}"), bg="#ffffff",fg = "#676767", anchor=W,

                    font=("Times New Roman", 19, "bold"))

    label11.grid(row=3, column=1, sticky="w")



    label12 = Label(pop, text=(f":    {row[4]}"), bg="#ffffff",fg = "#676767", anchor=W,

                    font=("Times New Roman", 19, "bold"))

    label12.grid(row=4, column=1, sticky="w")



    label13 = Label(pop, text=(f":    {row[5]}"), bg="#ffffff",fg = "#676767", anchor=W,

                    font=("Times New Roman", 19, "bold"))

    label13.grid(row=5, column=1, sticky="w")



    label14 = Label(pop, text=(f"     {row[6]}"), bg="#ffffff",fg = "#676767", anchor=W,

                    font=("Times New Roman", 19, "bold"))

    label14.grid(row=6, column=1, sticky="w")





    label15 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,

                   font=("Times New Roman", 22, "bold"))

    label15.grid(row=0, column=1, sticky="w")

    label16 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,

                   font=("Times New Roman", 22, "bold"))

    label16.grid(row=1, column=1, sticky="w")

    label17 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,

                    font=("Times New Roman", 22, "bold"))

    label17.grid(row=2, column=1, sticky="w")

    label18 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,

                    font=("Times New Roman", 22, "bold"))

    label18.grid(row=3, column=1, sticky="w")

    label19 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,

                    font=("Times New Roman", 22, "bold"))

    label19.grid(row=4, column=1, sticky="w")

    label20 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,

                    font=("Times New Roman", 22, "bold"))

    label20.grid(row=5, column=1, sticky="w")

    label21 = Label(pop, text=(f":"), bg="#ffffff", anchor=W,

                    font=("Times New Roman", 22, "bold"))

    label21.grid(row=6, column=1, sticky="w")


def main():
    

    root = tkinter.Tk()

    root.title("Warehouse Inventory Sales Purchase Management System  ")

    ws = root.winfo_screenwidth()

    hs = root.winfo_screenheight()

    w = 1350

    h = 703

    x = int(ws / 2 - w / 2 - 20)

    y = int(hs / 2 - h / 2 - 30)

    data = str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)

    root.geometry(data)

    root.configure(bg="black")

    root.resizable(0, 0)



    #*************************************Frame 1  (Title)**************

    

    title_frame = LabelFrame(root)

    title_frame.pack(fill="x")



    title = Label(title_frame,

                  text="Warehouse Inventory Purchase Management System",

                  font=("Comic Sans MS", 25, "bold"),

                  bg="black",

                  fg="#ffffff",

                  anchor="center",

                  bd=4)

    title.pack(expand=True, fil="x")



    # ************************************ Frame 2 (Border Line)*****



    f2 = Label(root, text=" ", font=("Comic Sans MS", 15, "bold", "italic"), bg="#cacaca", bd=1)

    f2.place(x=0, y=55, relwidth=50)



    # ************************************ Frame 3 (Entry)*****



    Manage_Frame_canvas = Frame(root, bd=2, relief=GROOVE, )

    Manage_Frame_canvas.place(x=13, y=95, width=459, height=545)



    Manage_Frame = Frame(root, bd=1, bg="#fff000", relief=GROOVE, )

    Manage_Frame.place(x=13, y=95, width=457, height=470)



    Manage_Frame3 = LabelFrame(Manage_Frame, text=" Put the Details", font=("Comic Sans MS", 22, "bold", "italic"),

                               fg="red", bd=0, bg="#fff000", relief=SUNKEN, )

    Manage_Frame3.place(y=0, x=0, width=457, height=545)



    # ***************************************** Variables For Entering Data **********

    global Product_ID 

    global Product_Name 

    global Price 

    global Quantity 

    global Contact 

    global Company 

    global ID_txt

    global NAME_txt

    global PRICE_txt

    global QUANTITY_txt

    global COMPANY_txt

    global CONTACT_txt

    global ADDRESS_txt

    global Field

    global Combo_Search

    global Search_Bar
    
    Product_ID =StringVar()

    Product_Name =StringVar()

    Price =StringVar()

    Quantity =StringVar()

    Contact =StringVar()

    Company =StringVar()



    # **********************  Labels and Entries_____________



    ID_lbl = Label(Manage_Frame, text="Product ID:", bg="#fff000", fg="red", font=("Comic Sans MS", 19, "bold"))

    ID_lbl.grid(row=1, column=0, pady=(50, 0), padx=20, sticky="w")



    ID_txt = Entry(Manage_Frame,width=18, font=("Comic Sans MS", 15), fg="red", bd=1, relief=GROOVE, )

    ID_txt.grid(row=1, column=2, sticky="w", pady=(50, 0))



    NAME_lbl = Label(Manage_Frame, text="Product Name:", bg="#fff000", fg="red", font=("Comic Sans MS", 19, "bold"))

    NAME_lbl.grid(row=2, column=0, pady=10, padx=20, sticky="w")



    NAME_txt = Entry(Manage_Frame,width=18, fg="red", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )

    NAME_txt.grid(row=2, column=2, sticky="w")



    PRICE_lbl = Label(Manage_Frame, text="Product Price:", bg="#fff000", fg="red", font=("Comic Sans MS", 19, "bold"))

    PRICE_lbl.grid(row=3, column=0, pady=10, padx=20, sticky="w")



    PRICE_txt = Entry(Manage_Frame, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )

    PRICE_txt.grid(row=3, column=2, sticky="w")



    QUANTITY_lbl = Label(Manage_Frame, text="Quantity:", bg="#fff000", fg="red", font=("Comic Sans MS", 19, "bold"))

    QUANTITY_lbl.grid(row=4, column=0, pady=10, padx=20, sticky="w")



    QUANTITY_txt = Entry(Manage_Frame, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )

    QUANTITY_txt.grid(row=4, column=2, sticky="w")



    COMPANY_lbl = Label(Manage_Frame, text="Mfg Company:", bg="#fff000", fg="red", font=("Comic Sans MS", 19, "bold"))

    COMPANY_lbl.grid(row=5, column=0, pady=10, padx=20, sticky="w")

    COMPANY_txt = Entry(Manage_Frame, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )

    COMPANY_txt.grid(row=5, column=2, sticky="w")



    CONTACT_lbl = Label(Manage_Frame, text="Phone.No:", bg="#fff000", fg="red",font=("Comic Sans MS", 19, "bold"))

    CONTACT_lbl.grid(row=6, column=0, pady=10, padx=20, sticky="w")



    CONTACT_txt = Entry(Manage_Frame, width=18, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )

    CONTACT_txt.grid(row=6, column=2, sticky="w")



    ADDRESS_lbl = Label(Manage_Frame, text="Mfg Address:", bg="#fff000", fg="red", font=("Comic Sans MS", 19, "bold"))

    ADDRESS_lbl.grid(row=7, column=0, pady=10, padx=20, sticky="w")
    

    

    ADDRESS_txt = Text(Manage_Frame, width=27, height=2, fg="#000000", bd=1 / 2, relief=GROOVE, )

    ADDRESS_txt.grid(row=7, column=2, sticky="w")





    # ***************************************** Frame 3 (Button Frame 1)*****



    button_frame1 = Frame(root, bd=2, relief=RIDGE, bg="#00a6ff")

    button_frame1.place(x=13, y=575, width=455, height=54, )



    # ******************************************* Buttons (For Frame 3 ) _______________

    global add_btn

    add_btn = Button(button_frame1, width=10, text="Add", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",

                             fg="#000000", relief=SUNKEN,command = add_btn).grid(row=0, column=0, padx=4, pady=7)



    update_btn = Button(button_frame1, width=10, text="Update", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,

                                bg="#ffffff", fg="#000000", relief=SUNKEN,command = update_button_is_clicked).grid(row=0, column=1, padx=1, pady=7)



    clear_btn = Button(button_frame1, width=10, text="Clear", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,

                                bg="#ffffff", fg="#000000", relief=SUNKEN,command = clear_button_is_clicked).grid(row=0, column=2, padx=2, pady=7)



    def logoutfunc():
        x=messagebox.askyesno("Logout","Do you want to logout ?",parent=root)
        if x>0:
            root.destroy()
            log()
            
    Logout_btn = Button(button_frame1, width=10, text="Logout", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",

                               fg="#000000", relief=SUNKEN,command =logoutfunc).grid(row=0, column=3, padx=2, pady=7)



    #*********************************************Frame 4 ( For Management ) ************************



    Main_Frame = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")

    Main_Frame.place(x=480, y=95, width=856, height=544)



    #**********************************************Frame 5 (For Searching)**************************



    Searching_Frame = Frame(root, bd=1, relief=RIDGE, )

    Searching_Frame.place(x=480, y=95, width=856, height=54)



    Search_By_Label = Label(Searching_Frame, text="Search By", fg="#676767", font=("Comic Sans MS", 17, "bold"))

    Search_By_Label.grid(row=0, column=0, pady=10, padx=20, sticky="w")



    

    Combo_Search = ttk.Combobox(Searching_Frame,font=("Comic Sans MS", 14), width=11, state="readonly")



    Combo_Search["values"] = ("Product_ID", "Product_Name","Company","Contact","Quantity")

    Combo_Search.current(0)

    Combo_Search.grid(row=0, column=1)






    Search_Bar = Entry(Searching_Frame,width=16, fg="#000000", font=("Comic Sans MS", 15), bd=1, relief=GROOVE, )

    Search_Bar.grid(row=0, column=2, sticky="w", padx=27)



    Search_Button = Button(Searching_Frame, width=10, text="Search", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,bg="#ffffff",

                        fg="#000000", relief=SUNKEN,command = search_button_is_clicked).grid(row=0, column=3, padx=(10, 0), pady=7, sticky="e")



    Search_All_Button = Button(Searching_Frame, width=10, text="Search All", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,

                                bg="#ffffff",

                                fg="#000000", relief=SUNKEN,command =search_all_bth).grid(row=0, column=4, padx=20, pady=7, sticky="e")



    #*******************************************************Frame 6 (Database Window)*********************



    Database_Window = Frame(root, bd=1, relief=RIDGE, bg="#ffffff")

    Database_Window.place(x=480, y=148, width=856, height=415)



    #********************************************************* Scrrollbars () *****************************



    Horizontal_Scrollbar = Scrollbar(Database_Window, orient=HORIZONTAL)

    Vertical_Scrollbar = Scrollbar(Database_Window, orient=VERTICAL)

    Field = ttk.Treeview(Database_Window,columns=("Product ID", "Product Name", "Product Price", "Product Quantity",

                       "Mfg Company", "Phone.No" ,"Mfg Address"),

                       yscrollcommand=Vertical_Scrollbar.set,

                         xscrollcommand=Horizontal_Scrollbar.set)

    Horizontal_Scrollbar.pack(side=BOTTOM, fill=X)

    Vertical_Scrollbar.pack(side=RIGHT, fill=Y)

    Horizontal_Scrollbar.config(command=Field.xview, )

    Vertical_Scrollbar.config(command=Field.yview, )



    #************************************************ Field Headings of  the Table ()******************************



    Field.heading("Product ID", text="Product ID")

    Field.heading("Product Name", text="Name")

    Field.heading("Product Price", text="Price")

    Field.heading("Product Quantity", text="Quantity")

    Field.heading("Mfg Company", text="Mfg Company")

    Field.heading("Phone.No", text="Phone.No")

    Field.heading("Mfg Address", text="Mfg Address")

    Field['show'] = "headings"



    Field.column("Product Name", width=200)

    Field.column("Mfg Address", width=300)

    Field.pack(expand=True, fill=BOTH)



    #************************************************Frame 7 (Button Frame 2)*************************



    button_frame2 = Frame(root, bd=2, relief=RIDGE, bg="#00a6ff")

    button_frame2.place(x=492, y=575, width=830, height=54, )



    # *********************************************** Buttons (For Frame 7)***************************



    Show_button = Button(button_frame2, width=10, text="Show", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",

                        fg="#000000",

                        relief=SUNKEN,command = product_details).grid(row=0, column=0, padx=(180, 0), pady=7)



    Update_button = Button(button_frame2, width=10, text="Update", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,

                        bg="#ffffff", fg="#000000",

                        relief=SUNKEN,command =update_2_is_clicked).grid(row=0, column=1, padx=10, pady=7)



    delete_button = Button(button_frame2, width=10, text="Delete", font=("Comic Sans MS", 12, "bold"), bd=1 / 2,

                        bg="#ffffff", fg="#000000", relief=SUNKEN,command =delete_button_is_clicked).grid(row=0, column=2, padx=(0, 0), pady=7)



    Clear_button = Button(button_frame2, width=10, text="Clear", font=("Comic Sans MS", 12, "bold"), bd=1 / 2, bg="#ffffff",

                       fg="#000000", relief=SUNKEN,command =clear_button_2_is_clicked).grid(row=0, column=3, padx=(9, 0), pady=7)



    # ***************************************************Frame 8 (For Credit) ****************



    Credit_Frame = Frame(root, bg="#ff0000", bd=0)

    Credit_Frame.place(x=0, y=643, relwidth=1, relheight=0.08, )



    Credit_Label = Label(Credit_Frame,

                         text="Developed By : Rohit",

                         font=("times new roman", 15, "bold"),

                         fg="#ffffff",

                         bg="#ff0000"

                         )

    Credit_Label.grid(row=0, column=0, padx=870, pady=10, sticky="w")

    search_all_bth()



    root.mainloop()

addtables()


def log():
    global root
    global fname_entry
    global l_entry
    global txt_contact
    global txt_recode
    global txt_pass
    global txt_conpass
    root=Tk()
    def Register():
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global checkbtn

        root.title("Register")
        root.geometry("1600x900+0+0")

        #background image

        bg1=ImageTk.PhotoImage(file=r"hdimage5.jpg")
            
        bg1_lbl=Label(root,image=bg1,relief=RIDGE)
        bg1_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #bg 2
        bgimage=Image.open("hdimage2.jpg")
        bgimage=bgimage.resize((460,550),Image.ANTIALIAS)
        bg2=ImageTk.PhotoImage(bgimage)

        
        bg2_lbl=Label(root,image=bg2,bd=4,relief=RIDGE)
        bg2_lbl.place(x=130,y=130,width=460,height=550)

        #side frame

        frame=Frame(root,bg="white")
        frame.place(x=590,y=130,width=800,height=550)

        #frame inside work

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen")
        register_lbl.place(x=20,y=20)

        #--login button--#

        loginbtnreg=Button(frame,command=Login_Window,text="Login Now",font=("Arial",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtnreg.place(x=630,y=20,width=120,height=35)

        #labels and entry fields

        framename=Label(frame,text="First Name",font=("times new roman",20,"bold"),bg="white")
        framename.place(x=50,y=100)

        #entry field for first name

        fname_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        fname_entry.place(x=50,y=135,width=230)

        #last name

        l_name=Label(frame,text="User Name",font=("times new roman",20,"bold"),bg="white")
        l_name.place(x=370,y=100)

        l_entry=ttk.Entry(frame,font=("times new roman",16,"bold"))
        l_entry.place(x=370,y=136,width=230)

        #contact

        contact_name=Label(frame,text="Contact No",font=("times new roman",20,"bold"),bg="white")
        contact_name.place(x=50,y=170)

        txt_contact=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_contact.place(x=50,y=210,width=230)

        #recovery  code

        recode=Label(frame,text="Recovery Code",font=("times new roman",20,"bold"),bg="white")
        recode.place(x=370,y=170)

        txt_recode=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_recode.place(x=370,y=207,width=230)
        
        #password

        password=Label(frame,text="Password",font=("times new roman",20,"bold"),bg="white")
        password.place(x=50,y=245)

        txt_pass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_pass.place(x=50,y=282,width=230)

        #confirm pass

        conpass=Label(frame,text="Confirm Password",font=("times new roman",20,"bold"),bg="white")
        conpass.place(x=370,y=240)

        txt_conpass=ttk.Entry(frame,font=("times new roman",16,"bold"))
        txt_conpass.place(x=370,y=277,width=230)


        #check btn terms and conditions
        global var_check
        var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=var_check,text="I Agree the Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)
        def registerclick():
            global var_check
            global fname_entry
            global l_entry
            global txt_contact
            global txt_recode
            global txt_pass
            global txt_conpass



            if str(fname_entry.get())=="" or str(l_entry.get())=="" or str(txt_contact.get())=="" or str(txt_recode.get())=="" or str(txt_pass.get())=="" or str(txt_conpass.get())=="":
                messagebox.showerror("Error","All fields are required",parent=root)

            elif not fname_entry.get().isalpha() or not l_entry.get().isalpha():
                messagebox.showerror("Error","Please Enter Name in alphabets",parent=root)
            elif not str(txt_contact.get()).isdigit() or not str(txt_recode.get()).isdigit():
                messagebox.showerror("Error","Please Enter Digits in the desired box",parent=root)
            elif str(txt_pass.get())!=str(txt_conpass.get()):
                messagebox.showerror("Error","Password & Confirm Password must be same",parent=root)
            elif var_check.get()==0:
                messagebox.showerror("Error","Please agree our terms and conditions",parent=root)
            else:
                messagebox.showinfo("Done","Welcome to our Warehouse Management",parent=root)
                mydb=c.connect("inventory.db")
                my_cursor=mydb.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(l_entry.get())))
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist with same details\nPlease try again",parent=root)
                else:
                    my_cursor.execute("insert into login (fullname,username,contact,recode,pass,conpass)values('%s','%s','%s','%s','%s','%s')"%(str(fname_entry.get()),str(l_entry.get()),str(txt_contact.get()),str(txt_recode.get()),str(txt_pass.get()),str(txt_conpass.get())))
                    mydb.commit()
                    messagebox.showinfo("Registered","Data registered successfully",parent=root)
                    mydb.close()
        #register now

        img=Image.open("regisnow.png")
        img=img.resize((170,50),Image.ANTIALIAS)
        photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=photoimage,borderwidth=0,command=registerclick,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=203,y=390,width=300)

        

        root.mainloop()

    def Login_Window():
        global root
        global fname_entry
        global l_entry
        global txt_contact
        global txt_recode
        global txt_pass
        global txt_conpass
        global txtuser
        global txtpass
        global txt_newpass
        
        root.title("Warehouse Management Login Pannel")
        root.geometry("1550x800+0+0")

        bgimage=Image.open(r"hdimage4.jpg")
        bgimage=bgimage.resize((1550,800),Image.ANTIALIAS)
        bg=ImageTk.PhotoImage(bgimage)

        lbl_bg=Label(root,image=bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(root,bg="black")
        frame.place(x=603,y=175,width=340,height=450) #x and y pos value and width and height size of box

        img1=Image.open(r"hdimage.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=180,width=100,height=100)

            #get started label

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=107,y=100)

            #user name label

        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=60,y=155)
            
        txtuser=ttk.Entry(frame,font=("times new roman",13,"bold"))       
        txtuser.place(x=35,y=180,width=270)

            #password label

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=60,y=225)

        txtpass=ttk.Entry(frame,font=("times new roman",13,"bold"),show="*")       
        txtpass.place(x=35,y=250,width=270)

            #Icon Images of username 

        img2=Image.open(r"hdimage3.jpg")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=640,y=330,width=25,height=25)

            #Icon Images of password

        img3=Image.open(r"hdimage2.jpg")
        img3=img3.resize((55,25),Image.ANTIALIAS)
        photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=639,y=400,width=25,height=25)
            
            #login btn in login pannel               here command ka kaam click karne par def login ko call karna hai
        def login():
            global txtuser
            global txtpass
            global txt_recode

            if str(txtuser.get())=="" or str(txtpass.get())=="":
                messagebox.showerror("Error","All fields required",parent=root)
            else:
                mydb=c.connect("inventory.db")
                my_cursor=mydb.cursor()
                my_cursor.execute("select * from login where username='%s' and pass='%s'"%(str(txtuser.get()),str(txtpass.get())))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username & Password",parent=root)
                else:
                    root.destroy()
                    main()


        loginbtn=Button(frame,command=login,text="Login",font=("times new roman",13,"bold"),bd=3,relief=RIDGE,fg="black",bg="aqua",activeforeground="black",activebackground="aqua")
        loginbtn.place(x=105,y=300,width=120,height=35)

            # registerbutton for new users

        registerbtn=Button(frame,text="New User Register",command=Register,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=5,y=353,width=160)

            #forgot passbtn
        def forgotpass():
            global txtuser
            global txtpass
            global txt_recode
            global txt_newpass

            if str(txtuser.get())=="":
                messagebox.showerror("Error","Please Enter User Name to reset Password",parent=root)
            else:
                conn=c.connect("hotel.db")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from login where username='%s'"%(str(txtuser.get())))
                row=my_cursor.fetchone()

                if row==None:
                    messagebox.showerror("Error","Please enter valid username",parent=root)
                else:
                    conn.close()
                    root2=Toplevel()
                    root2.title("Forgot Password")
                    root2.geometry("360x480+590+170")

                    l=Label(root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="blue",bg="cyan")
                    l.place(x=0,y=10,relwidth=1)

                    #recovery  code

                    recode=Label(root2,text="Recovery Code",font=("times new roman",20,"bold"),bg="cyan")
                    recode.place(x=88,y=80)

                    txt_recode=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_recode.place(x=50,y=130,width=250)
                    
                    #password

                    newpassword=Label(root2,text="New Password",font=("times new roman",20,"bold"),bg="cyan")
                    newpassword.place(x=88,y=180)

                    txt_newpass=ttk.Entry(root2,font=("times new roman",16,"bold"))
                    txt_newpass.place(x=50,y=220,width=250)
                    
                    def resetpass():
                        global txtuser
                        global txt_newpass
                        global txt_recode

                        

                        if str(txt_recode.get())=="":
                            messagebox.showerror("Error","Please enter Recovery Code",parent=root2)
                        elif not str(txt_recode.get()).isdigit():
                            messagebox.showerror("Error","Please enter Recovery Code in Digits",parent=root2)
                        else:
                            mydb=c.connect("inventory.db")
                            my_cursor=mydb.cursor()
                            my_cursor.execute("select * from login where username='%s' and recode='%s'"%(str(txtuser.get()),str(txt_recode.get())))
                            row=my_cursor.fetchone()
                            if row==None:
                                messagebox.showerror("Error","Please enter Correct Recovery Code",parent=root2)
                            else:
                                my_cursor.execute("update login set pass='%s' where username='%s' and recode='%s'"%(str(txt_newpass.get()),str(txtuser.get()),str(txt_recode.get())))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Info","Your password has been reset\nYou can login with your new password",parent=root2) 
                                root2.destroy()


                        



                    #btn for reset

                    btn=Button(root2,text="Reset Password",command=resetpass,font=("times new roman",15,"bold"),fg="white",bg="blue")
                    btn.place(x=100,y=290)

        forgotpassbtn=Button(frame,text="Forgot Password",command=forgotpass,font=("times new roman",11,"bold"),bd=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=7,y=382,width=140)

        #click login func

        

        root.mainloop()
    Login_Window()



log()











