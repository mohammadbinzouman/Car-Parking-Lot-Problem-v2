from tkinter import *
import os
import sys

def bt_bttn():
    global algo
    algo = 'BACKTRACKING'
    
def fc_bttn():
    global algo
    algo = 'FORWARD_CHECKING'

def ac_bttn():
    global algo
    algo = 'ARC_CONSISTENCY' 
    
def on_closing():
        sys.exit(0)

conf_lot_window = Tk()
conf_lot_window.title("Car Parking Lot")
conf_lot_window.iconbitmap(default=os.path.abspath('Code Images\parking_sign.ico'))
conf_lot_window.attributes("-topmost", True)
conf_lot_window.configure(width=500, height=300)
conf_lot_window.resizable(0, 0) #Don't allow resizing the window.
conf_lot_window.geometry('500x400') # Fixing Geometry.
conf_lot_window.eval('tk::PlaceWindow . center')

conf_lot_window.protocol("WM_DELETE_WINDOW", on_closing)

""" frame1 = Frame(conf_lot_window, width=200, height=100, background="#023047", highlightbackground="#8ecae6",
               highlightthickness=2).place(x=150, y=20)
frame2 = Frame(conf_lot_window, width=200, height=100, background="#023047", highlightbackground="#8ecae6", 
               highlightthickness=2).place(x=150, y=140)
frame3 = Frame(conf_lot_window, width=200, height=75, background="#023047", highlightbackground="#8ecae6", 
               highlightthickness=2).place(x=150, y=260)

# start
Label(frame1, text="Select The Number of Zones", bg="#023047", fg="#8ecae6", anchor=CENTER, font=('Arial', 10, 'bold')).place(x=157, y=10)
Label(frame2, text="Select The Number of Colors", bg="#023047", fg="#8ecae6", anchor=CENTER, font=('Arial', 10, 'bold')).place(x=156, y=130)
Label(frame3, text="Enter a Seed or Leave Empty", bg="#023047", fg="#8ecae6", anchor=CENTER, font=('Arial', 10, 'bold')).place(x=155, y=250)

input1 = IntVar(None, 1)
input2 = IntVar(None, 2)
input3 = StringVar()

Radiobutton(frame1, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="1", value=1, variable=input1).place(x=200, y=40)
Radiobutton(frame1, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="2", value=2, variable=input1).place(x=200, y=60)
Radiobutton(frame1, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="3", value=3, variable=input1).place(x=200, y=80)
Radiobutton(frame1, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="4", value=4, variable=input1).place(x=270, y=40)
Radiobutton(frame1, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="5", value=5, variable=input1).place(x=270, y=60)
Radiobutton(frame1, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="6", value=6, variable=input1).place(x=270, y=80) 

Radiobutton(frame2, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="2", value=2, variable=input2).place(x=200, y=160)
Radiobutton(frame2, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="3", value=3, variable=input2).place(x=200, y=180) 
Radiobutton(frame2, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="4", value=4, variable=input2).place(x=200, y=200) 
Radiobutton(frame2, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="5", value=5, variable=input2).place(x=270, y=160) 
Radiobutton(frame2, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="6", value=6, variable=input2).place(x=270, y=180) 
Radiobutton(frame2, selectcolor='#023047', bg='#023047', fg="#8ecae6", text="7", value=7, variable=input2).place(x=270, y=200) 

Entry(conf_lot_window, textvariable=input3).place(x=188, y=290)

# Frame for button border.
button_border1 = Frame(frame2, width=126, height=29, background='#023047', highlightbackground = "#8ecae6", 
                       highlightthickness=3).place(x=68, y=353)

Button(button_border1, bg='#023047', fg="#8ecae6", width=16, height=1, text='BACKTRACKING', font=("Arial", 8, 'bold'), 
                       command=lambda: (conf_lot_window.destroy(), bt_bttn())).place(x=70, y=355)

button_border2 = Frame(frame2, width=126, height=29, background='#023047', highlightbackground = "#8ecae6", 
                       highlightthickness=3).place(x=194, y=353)
Button(button_border2, bg='#023047', fg="#8ecae6", width=16, height=1, text='FORWARD CHECKING', font=("Arial", 8, 'bold'), 
                       command=lambda: (conf_lot_window.destroy(), fc_bttn())).place(x=195, y=355) 

button_border3 = Frame(frame2, width=126, height=29, background='#023047', highlightbackground = "#8ecae6",
                       highlightthickness=3).place(x=319, y=353)
Button(button_border3, bg='#023047', fg="#8ecae6", width=16, height=1, text='ARC CONSISTENCY', font=("Arial", 8, 'bold'), 
                       command=lambda: (conf_lot_window.destroy(), ac_bttn())).place(x=320, y=355) """


zones_label_frame = LabelFrame(conf_lot_window, text="Select The Number of Zones", width=200, height=100).place(x=150, y=20)
colors_label_frame = LabelFrame(conf_lot_window, text="Select The Number of Colors", width=200, height=100).place(x=150, y=140)
seed_label_frame = LabelFrame(conf_lot_window, text="Enter a Seed or Leave Empty", width=200, height=75).place(x=150, y=260)

Button(conf_lot_window, borderwidth=3, highlightthickness=3,  width=16, height=1, text='BACKTRACKING', font=("Arial", 8, 'bold'), 
                       command=lambda: (conf_lot_window.destroy(), bt_bttn())).place(x=50, y=355)

Button(conf_lot_window, borderwidth=3, highlightthickness=3, width=16, height=1, text='FORWARD CHECKING', font=("Arial", 8, 'bold'), 
                       command=lambda: (conf_lot_window.destroy(), fc_bttn())).place(x=185, y=355) 
 
Button(conf_lot_window, borderwidth=3, highlightthickness=3, width=16, height=1, text='ARC CONSISTENCY', font=("Arial", 8, 'bold'), 
                       command=lambda: (conf_lot_window.destroy(), ac_bttn())).place(x=320, y=355)

input1 = IntVar(None, 1)
input2 = IntVar(None, 2)
input3 = StringVar()

Radiobutton(zones_label_frame, text="1", value=1, variable=input1).place(x=200, y=40)
Radiobutton(zones_label_frame, text="2", value=2, variable=input1).place(x=200, y=60)
Radiobutton(zones_label_frame, text="3", value=3, variable=input1).place(x=200, y=80)
Radiobutton(zones_label_frame, text="4", value=4, variable=input1).place(x=270, y=40)
Radiobutton(zones_label_frame, text="5", value=5, variable=input1).place(x=270, y=60)
Radiobutton(zones_label_frame, text="6", value=6, variable=input1).place(x=270, y=80) 

Radiobutton(colors_label_frame, text="2", value=2, variable=input2).place(x=200, y=160)
Radiobutton(colors_label_frame, text="3", value=3, variable=input2).place(x=200, y=180) 
Radiobutton(colors_label_frame, text="4", value=4, variable=input2).place(x=200, y=200) 
Radiobutton(colors_label_frame, text="5", value=5, variable=input2).place(x=270, y=160) 
Radiobutton(colors_label_frame, text="6", value=6, variable=input2).place(x=270, y=180) 
Radiobutton(colors_label_frame, text="7", value=7, variable=input2).place(x=270, y=200) 

Entry(conf_lot_window, textvariable=input3).place(x=188, y=292)

conf_lot_window.mainloop()