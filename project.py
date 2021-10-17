import tkinter as tk
import mysql.connector
from tkinter import *
# import mysql.connector to connect database
# import tkinter to write interface
db = mysql.connector.connect(host="127.0.0.1",
                             port=3306,
                             user="root",
                             password="wilson",
                             db="inn")
cursor = db.cursor()
# input ip, port, db to access database


def insert():

    in_table = insert_table.get()
    in_data = insert_data.get()

    sqlStuff = "INSERT INTO {} VALUES ({}) ".format(
        in_table, in_data)  # use sql to execute mysql on database
    cursor.execute(sqlStuff)
    db.commit()  # make database update
    tl = Toplevel()  # write another window to output the result
    label = tk.Label(tl, text='Insert Success!')
    label.place(x=50, y=50, width=100)


def jump():
    def delete():
        a = variable.get().split(',')
        # find the key attribute of the select one
        cursor.execute("SHOW COLUMNS FROM inn.{}".format(de_table))
        result = cursor.fetchall()
        delete_users = "DELETE FROM {} WHERE {} = {}".format(  # use sql to execute mysql on database
            de_table, result[0][0], a[0][1:])
        cursor.execute(delete_users)
        db.commit()  # update database
        tl1 = Toplevel()
        label = tk.Label(tl1, text='Delete Success!')
        label.place(x=50, y=50, width=100)
    tl = Toplevel()  # write another window
    de_table = delete_table.get()
    de_schema = delete_schema.get()
    de_data = delete_data.get()
    cursor.execute(
        "SELECT * FROM {} WHERE {} = {}".format(de_table, de_schema, de_data))  # to find which to delete
    result = cursor.fetchall()
    # result=[0]
    variable.set(result[0])
    w = tk.OptionMenu(tl, variable, *result)  # make a pull-down menu to select
    w.place(x=50, y=50, width=100)
    # put the select one to delete
    b = Button(tl, text="DELETE", command=delete)
    b.place(x=75, y=90, width=50)


def update():
    up_table = update_table.get()
    up_schema = update_schema.get()
    up_data = update_data.get()
    key_id = key_upid.get()
    key_data = key_updata.get()
    cursor.execute("UPDATE {} SET {} = {} WHERE {} = {}".format(  # use sql to execute mysql on database
        up_table, up_schema, up_data, key_id, key_data))
    db.commit()  # update database
    tl = Toplevel()  # write another window to output the result
    label = tk.Label(tl, text='Update Success!')
    label.place(x=50, y=50, width=100)


def SFW():
    sel = SFW_select.get()
    fr = SFW_from.get()
    wh = SFW_where.get()
    # use sql to execute mysql on database
    cursor.execute("SELECT {} FROM {} WHERE {}".format(sel, fr, wh))
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    tl.geometry("300x400")
    j = 20
    for i in result:
        label = tk.Label(tl, text=i)
        label.place(x=20, y=j, width=230)
        j += 20


def IN():
    in1 = in_con.get()
    in2 = in_con1.get()
    # use sql to execute mysql on database
    cursor.execute("{} IN ({})".format(in1, in2))
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    tl.geometry("300x400")
    j = 20
    for i in result:
        label = tk.Label(tl, text=i)
        label.place(x=50, y=j, width=230)
        j += 20


def NOT_IN():
    in1 = notin_con.get()
    in2 = notin_con1.get()
    # use sql to execute mysql on database
    cursor.execute("{} NOT IN ({})".format(in1, in2))
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    tl.geometry("300x400")
    j = 20
    for i in result:
        label = tk.Label(tl, text=i)
        label.place(x=50, y=j, width=230)
        j += 20


def EXISTS():
    in1 = ex_con.get()
    in2 = ex_con1.get()
    # use sql to execute mysql on database
    cursor.execute("{} EXISTS ({})".format(in1, in2))
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    tl.geometry("300x400")
    j = 20
    for i in result:
        label = tk.Label(tl, text=i)
        label.place(x=50, y=j, width=230)
        j += 20


def NOT_EXISTS():
    in1 = notex_con.get()
    in2 = notex_con1.get()
    # use sql to execute mysql on database
    cursor.execute("{} NOT EXISTS ({})".format(in1, in2))
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    tl.geometry("300x400")
    j = 20
    for i in result:
        label = tk.Label(tl, text=i)
        label.place(x=50, y=j, width=230)
        j += 20


def COUNT():
    c1 = c_cou.get()
    c2 = c_table.get()
    c3 = c_con.get()
    cursor.execute("SELECT COUNT({}) FROM {} where {}".format(
        c1, c2, c3))  # use sql to execute mysql on database
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    label = tk.Label(tl, text=result)
    label.place(x=50, y=50, width=100)


def SUM():
    c1 = s_sum.get()
    c2 = s_table.get()
    c3 = s_con.get()
    cursor.execute("SELECT SUM({}) FROM {} where {}".format(
        c1, c2, c3))  # use sql to execute mysql on database
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    label = tk.Label(tl, text=result)
    label.place(x=50, y=50, width=100)


def MAX():
    c1 = max_sum.get()
    c2 = max_table.get()
    c3 = max_con.get()
    cursor.execute("SELECT MAX({}) FROM {} where {}".format(
        c1, c2, c3))  # use sql to execute mysql on database
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    label = tk.Label(tl, text=result)
    label.place(x=50, y=50, width=100)


def MIN():
    c1 = min_sum.get()
    c2 = min_table.get()
    c3 = min_con.get()
    cursor.execute("SELECT MIN({}) FROM {} where {}".format(
        c1, c2, c3))  # use sql to execute mysql on database
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    label = tk.Label(tl, text=result)
    label.place(x=50, y=50, width=100)


def AVG():
    c1 = avg_sum.get()
    c2 = avg_table.get()
    c3 = avg_con.get()
    cursor.execute("SELECT AVG({}) FROM {} where {}".format(
        c1, c2, c3))  # use sql to execute mysql on database
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    label = tk.Label(tl, text=result)
    label.place(x=50, y=50, width=100)


def HAV():
    c1 = hav_sel.get()
    c2 = hav_table.get()
    c3 = hav_wh.get()
    c4 = hav_gb.get()
    c5 = hav_con.get()
    cursor.execute(
        "SELECT {} FROM {} where {} GROUP BY {} HAVING {}".format(c1, c2, c3, c4, c5))  # use sql to execute mysql on database
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    tl.geometry("300x400")
    j = 20
    for i in result:
        label = tk.Label(tl, text=i)
        label.place(x=50, y=j, width=230)
        j += 20


def QUERY():
    c1 = query.get()
    cursor.execute(c1)  # use sql to execute mysql on database
    result = cursor.fetchall()
    tl = Toplevel()  # write another window to output the result
    tl.geometry("300x400")
    j = 20
    for i in result:
        label = tk.Label(tl, text=i)
        label.place(x=10, y=j, width=230)
        j += 20


root = tk.Tk()  # set the root window
root.geometry("600x750")  # set window size
root.title("DBMS Project")  # set window title


# Definging the first row
# ----------Select From Where-----------
SFWselect = tk.Label(root, text="Select")  # print words
SFWselect.place(x=20, y=20)
SFW_select = tk.Entry(root, width=35)  # put the place to input
SFW_select.place(x=150, y=20, width=100)

SFWfrom = tk.Label(root, text="from")  # print words
SFWfrom.place(x=20, y=40)
SFW_from = tk.Entry(root, width=35)  # put the place to input
SFW_from.place(x=150, y=40, width=100)

SFWwhere = tk.Label(root, text="where")  # print words
SFWwhere.place(x=20, y=60)
SFW_where = tk.Entry(root, width=35)  # put the place to input
SFW_where.place(x=150, y=60, width=100)

SFWbtn = Button(root, text="SELECT FROM WHERE", bg='white',
                command=SFW)  # set the buttom to go to the function
SFWbtn.place(x=150, y=80, width=140)

# ----------------Delete----------------
variable = StringVar()
detable = tk.Label(root, text="delete table")  # print words
detable.place(x=20, y=120)
delete_table = tk.Entry(root, width=35)  # put the place to input
delete_table.place(x=150, y=120, width=100)

deschema = tk.Label(root, text="delete attribute")  # print words
deschema.place(x=20, y=140)
delete_schema = tk.Entry(root, width=35)  # put the place to input
delete_schema.place(x=150, y=140, width=100)

dedata = tk.Label(root, text="delete data")  # print words
dedata.place(x=20, y=160)
delete_data = tk.Entry(root, width=35)  # put the place to input
delete_data.place(x=150, y=160, width=100)

# set the buttom to go to the function
deletebtn = Button(root, text="Choose To Delete", bg='yellow', command=jump)
deletebtn.place(x=150, y=180, width=120)

# ----------------Insert----------------
intable = tk.Label(root, text="Insert table")  # print words
intable.place(x=20, y=220)
insert_table = tk.Entry(root, width=35)  # put the place to input
insert_table.place(x=150, y=220, width=100)

indata = tk.Label(root, text="Insert data")  # print words
indata.place(x=20, y=240)
insert_data = tk.Entry(root, width=35)  # put the place to input
insert_data.place(x=150, y=240, width=100)

insertbtn = tk.Button(root, text="INSERT",
                      bg='red', command=insert)  # set the buttom to go to the function
insertbtn.place(x=150, y=260, width=70)

# ----------------Update----------------
uptable = tk.Label(root, text="update table")  # print words
uptable.place(x=20, y=300)
update_table = tk.Entry(root, width=35)  # put the place to input
update_table.place(x=150, y=300, width=100)

upschema = tk.Label(root, text="update schema")  # print words
upschema.place(x=20, y=320)
update_schema = tk.Entry(root, width=35)  # put the place to input
update_schema.place(x=150, y=320, width=100)

updata = tk.Label(root, text="update data")  # print words
updata.place(x=20, y=340)
update_data = tk.Entry(root, width=35)  # put the place to input
update_data.place(x=150, y=340, width=100)

upid = tk.Label(root, text="update key attribute")  # print words
upid.place(x=20, y=360)
key_upid = tk.Entry(root, width=35)  # put the place to input
key_upid.place(x=150, y=360, width=100)

updata = tk.Label(root, text="update key data")  # print words
updata.place(x=20, y=380)
key_updata = tk.Entry(root, width=35)  # put the place to input
key_updata.place(x=150, y=380, width=100)

# set the buttom to go to the function
updatebtn = Button(root, text="UPDATE", bg='blue', command=update)
updatebtn.place(x=150, y=400, width=70)

# ----------------IN----------------
incon = tk.Label(root, text="condition")  # print words
incon.place(x=20, y=440)
in_con = tk.Entry(root, width=35)  # put the place to input
in_con.place(x=150, y=440, width=100)

incon1 = tk.Label(root, text="condition")  # print words
incon1.place(x=20, y=460)
in_con1 = tk.Entry(root, width=35)  # put the place to input
in_con1.place(x=150, y=460, width=100)

inbtn = tk.Button(root, text="IN",
                  bg='orange', command=IN)  # set the buttom to go to the function
inbtn.place(x=150, y=480, width=70)

# ----------------NOT IN----------------
notincon = tk.Label(root, text="condition")  # print words
notincon.place(x=20, y=520)
notin_con = tk.Entry(root, width=35)  # put the place to input
notin_con.place(x=150, y=520, width=100)

notincon1 = tk.Label(root, text="condition")  # print words
notincon1.place(x=20, y=540)
notin_con1 = tk.Entry(root, width=35)  # put the place to input
notin_con1.place(x=150, y=540, width=100)

notinbtn = tk.Button(root, text="NOT IN",
                     bg='purple', command=NOT_IN)  # set the buttom to go to the function
notinbtn.place(x=150, y=560, width=70)

# ----------------EXISTS----------------
excon = tk.Label(root, text="condition")  # print words
excon.place(x=20, y=600)
ex_con = tk.Entry(root, width=35)  # put the place to input
ex_con.place(x=150, y=600, width=100)

excon1 = tk.Label(root, text="condition")  # print words
excon1.place(x=20, y=620)
ex_con1 = tk.Entry(root, width=35)  # put the place to input
ex_con1.place(x=150, y=620, width=100)

exbtn = tk.Button(root, text="EXISTS",
                  bg='pink', command=EXISTS)  # set the buttom to go to the function
exbtn.place(x=150, y=640, width=70)

# ----------------NOT EXISTS----------------
notexcon = tk.Label(root, text="condition")  # print words
notexcon.place(x=320, y=20)
notex_con = tk.Entry(root, width=35)  # put the place to input
notex_con.place(x=450, y=20, width=100)

notexcon1 = tk.Label(root, text="condition")  # print words
notexcon1.place(x=320, y=40)
notex_con1 = tk.Entry(root, width=35)  # put the place to input
notex_con1.place(x=450, y=40, width=100)

notexbtn = tk.Button(root, text="NOT EXISTS",
                     bg='white', command=NOT_EXISTS)  # set the buttom to go to the function
notexbtn.place(x=450, y=60, width=80)

# ----------------COUNT----------------
ccou = tk.Label(root, text="count ()")  # print words
ccou.place(x=320, y=100)
c_cou = tk.Entry(root, width=35)  # put the place to input
c_cou.place(x=450, y=100, width=100)

ctable = tk.Label(root, text="count table")  # print words
ctable.place(x=320, y=120)
c_table = tk.Entry(root, width=35)  # put the place to input
c_table.place(x=450, y=120, width=100)

ccon = tk.Label(root, text="condition")  # print words
ccon.place(x=320, y=140)
c_con = tk.Entry(root, width=35)  # put the place to input
c_con.place(x=450, y=140, width=100)

# set the buttom to go to the function
cbtn = Button(root, text="COUNT", bg='yellow', command=COUNT)
cbtn.place(x=450, y=160, width=70)

# ----------------SUM----------------
ssum = tk.Label(root, text="sum ()")  # print words
ssum.place(x=320, y=200)
s_sum = tk.Entry(root, width=35)  # put the place to input
s_sum.place(x=450, y=200, width=100)

stable = tk.Label(root, text="count table")  # print words
stable.place(x=320, y=220)
s_table = tk.Entry(root, width=35)  # put the place to input
s_table.place(x=450, y=220, width=100)

scon = tk.Label(root, text="condition")  # print words
scon.place(x=320, y=240)
s_con = tk.Entry(root, width=35)  # put the place to input
s_con.place(x=450, y=240, width=100)

# set the buttom to go to the function
sbtn = Button(root, text="SUM", bg='red', command=SUM)
sbtn.place(x=450, y=260, width=70)

# ----------------MAX----------------
maxsum = tk.Label(root, text="max ()")  # print words
maxsum.place(x=320, y=300)
max_sum = tk.Entry(root, width=35)  # put the place to input
max_sum.place(x=450, y=300, width=100)

maxtable = tk.Label(root, text="max table")  # print words
maxtable.place(x=320, y=320)
max_table = tk.Entry(root, width=35)  # put the place to input
max_table.place(x=450, y=320, width=100)

maxcon = tk.Label(root, text="condition")  # print words
maxcon.place(x=320, y=340)
max_con = tk.Entry(root, width=35)  # put the place to input
max_con.place(x=450, y=340, width=100)

# set the buttom to go to the function
maxbtn = Button(root, text="MAX", bg='blue', command=MAX)
maxbtn.place(x=450, y=360, width=70)

# ----------------MIN----------------
minsum = tk.Label(root, text="min ()")  # print words
minsum.place(x=320, y=400)
min_sum = tk.Entry(root, width=35)  # put the place to input
min_sum.place(x=450, y=400, width=100)

mintable = tk.Label(root, text="min table")  # print words
mintable.place(x=320, y=420)
min_table = tk.Entry(root, width=35)  # put the place to input
min_table.place(x=450, y=420, width=100)

mincon = tk.Label(root, text="condition")  # print words
mincon.place(x=320, y=440)
min_con = tk.Entry(root, width=35)  # put the place to input
min_con.place(x=450, y=440, width=100)

# set the buttom to go to the function
minbtn = Button(root, text="MIN", bg='orange', command=MIN)
minbtn.place(x=450, y=460, width=70)

# ----------------AVG----------------
avgsum = tk.Label(root, text="avg ()")  # print words
avgsum.place(x=320, y=500)
avg_sum = tk.Entry(root, width=35)  # put the place to input
avg_sum.place(x=450, y=500, width=100)

avgtable = tk.Label(root, text="avg table")  # print words
avgtable.place(x=320, y=520)
avg_table = tk.Entry(root, width=35)  # put the place to input
avg_table.place(x=450, y=520, width=100)

avgcon = tk.Label(root, text="condition")  # print words
avgcon.place(x=320, y=540)
avg_con = tk.Entry(root, width=35)  # put the place to input
avg_con.place(x=450, y=540, width=100)

# set the buttom to go to the function
avgbtn = Button(root, text="AVG", bg='purple', command=AVG)
avgbtn.place(x=450, y=560, width=70)

# ----------------HAVING----------------
havsel = tk.Label(root, text="select")  # print words
havsel.place(x=320, y=600)
hav_sel = tk.Entry(root, width=35)  # put the place to input
hav_sel.place(x=450, y=600, width=100)

havtable = tk.Label(root, text="hav table")  # print words
havtable.place(x=320, y=620)
hav_table = tk.Entry(root, width=35)  # put the place to input
hav_table.place(x=450, y=620, width=100)

havwh = tk.Label(root, text="where condition")  # print words
havwh.place(x=320, y=640)
hav_wh = tk.Entry(root, width=35)  # put the place to input
hav_wh.place(x=450, y=640, width=100)

havgb = tk.Label(root, text="group by")  # print words
havgb.place(x=320, y=660)
hav_gb = tk.Entry(root, width=35)  # put the place to input
hav_gb.place(x=450, y=660, width=100)

havcon = tk.Label(root, text="having condition")  # print words
havcon.place(x=320, y=680)
hav_con = tk.Entry(root, width=35)  # put the place to input
hav_con.place(x=450, y=680, width=100)

# set the buttom to go to the function
havbtn = Button(root, text="HAV", bg='pink', command=HAV)
havbtn.place(x=450, y=700, width=70)

# ----------------Query----------------
querytext = tk.Label(root, text="Query")  # print words
querytext.place(x=20, y=680)
query = tk.Entry(root, width=35)  # put the place to input
query.place(x=150, y=680, width=150)
# set the buttom to go to the function
querybtn = Button(root, text="QUERY", bg='gray', command=QUERY)
querybtn.place(x=150, y=700, width=70)

root.mainloop()
