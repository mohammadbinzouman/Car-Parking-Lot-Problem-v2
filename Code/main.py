import os
import random
from PIL import ImageTk
import PIL.Image 
from tkinter import * 
import time
import sys
from helper_module import *

global algo
global calls 
calls = -1

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

tuple_canvas = [os.path.abspath('CodeImages\parking_lot_layout_zoneA.png'),
                os.path.abspath('CodeImages\parking_lot_layout_zoneB.png'),
                os.path.abspath('CodeImages\parking_lot_layout_zoneC.png'),
                os.path.abspath('CodeImages\parking_lot_layout_zoneD.png'),
                os.path.abspath('CodeImages\parking_lot_layout_zoneE.png'),
                os.path.abspath('CodeImages\parking_lot_layout_zoneF.png')]

all_parking_spots = ((35, 188), (87, 188), (139, 188), (191, 188), (243, 188), (35, 295), (87, 295), (139, 295), (191, 295), (243, 295),
                     (408, 188), (460, 188), (512, 188), (564, 188), (616, 188), (408, 295), (460, 295), (512, 295), (564, 295), (616, 295),
                     (786, 188), (838, 188), (890, 188), (942, 188), (994, 188), (786, 300), (838, 300), (890, 300), (942, 300), (994, 300),
                     (35, 535), (87, 535), (139, 535), (191, 535), (243, 535), (35, 642), (87, 642), (139, 642), (191, 642), (243, 642),
                     (408, 535), (460, 535), (512, 535), (564, 535), (616, 535), (408, 642), (460, 642), (512, 642), (564, 642), (616, 642),
                     (786, 535), (838, 535), (890, 535), (942, 535), (994, 535), (786, 642), (838, 642), (890, 642), (942, 642), (994, 642))

waiting_cars_spots = ((1080, 11), (1130, 11), (1180, 11), (1230, 11), (1280, 11), (1330, 11), (1380, 11), (1430, 11), (1480, 11), 
                      (1080, 118), (1130, 118), (1180, 118), (1230, 118), (1280, 118), (1330, 118), (1380, 118), (1430, 118), (1480, 118), 
                      (1080, 225), (1130, 225), (1180, 225), (1230, 225), (1280, 225), (1330, 225), (1380, 225), (1430, 225), (1480, 225), 
                      (1080, 332), (1130, 332), (1180, 332), (1230, 332), (1280, 332), (1330, 332), (1380, 332), (1430, 332), (1480, 332), 
                      (1080, 439), (1130, 439), (1180, 439), (1230, 439), (1280, 439), (1330, 439), (1380, 439), (1430, 439), (1480, 439), 
                      (1080, 546), (1130, 546), (1180, 546), (1230, 546), (1280, 546), (1330, 546), (1380, 546), (1430, 546), (1480, 546), 
                      (1080, 651), (1130, 651), (1180, 651), (1230, 651), (1280, 651), (1330, 651), (1380, 651), (1430, 651), (1480, 651), 
                      (1080, 332), (1130, 572), (1180, 572), (1230, 572), (1280, 572))
# contains all spots positions.

all_colors_tuple = ('red', 'blue', 'green', 'yellow', 'indigo', 'orange', 'violet')

conf_lot_window = Tk()
conf_lot_window.title("Car Parking Lot")
conf_lot_window.iconbitmap(default=os.path.abspath('CodeImages\parking_sign.ico'))
conf_lot_window.attributes("-topmost", True)
conf_lot_window.configure(width=500, height=300)
conf_lot_window.resizable(0, 0) #Don't allow resizing the window.
conf_lot_window.geometry('500x400') # Fixing Geometry.
conf_lot_window.eval('tk::PlaceWindow . center')

conf_lot_window.protocol("WM_DELETE_WINDOW", on_closing)

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

number_of_zones = input1.get()
number_of_colors = input2.get()
seed = input3.get()

if seed == '':
    seed = random.randint(1, 1000000000)

lot_window = Tk()
lot_window.title("Car Parking Lot")

#lot_window.protocol("WM_DELETE_WINDOW", on_closing)

w, h = lot_window.winfo_screenwidth(), lot_window.winfo_screenheight()
lot_window.geometry("%dx%d-0+0" % (w, h-80))

lw_canvas = Canvas(lot_window, width=w, height=h+300) #width=1074, height=630
lw_canvas.configure(background='#4f4f4f')
lw_canvas.pack()

red_car_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\RedC.png')).resize((45, 100)))  # Red car image
blue_car_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\BlueC.png')).resize((45, 100)))  # Blue car image
green_car_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\GreenC.png')).resize((45, 100)))  # Green car image
yellow_car_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\YellowC.png')).resize((45, 100)))  # Yellow car image
indigo_car_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\IndigoC.png')).resize((45, 100)))  # Indigo car image
orange_car_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\OrangeC.png')).resize((45, 100)))  # orange car image
violet_car_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\VioletC.png')).resize((45, 100)))  # Violet car image
Number_of_Cars = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\\Number_of_Cars.png')))  # Number of Cars
empty_spot_image = ImageTk.PhotoImage(PIL.Image.open(os.path.abspath('CodeImages\\EmptySpot.png')).resize((45, 100)))

parking_lot_image = PhotoImage(file=tuple_canvas[number_of_zones - 1])
lw_canvas.create_image(0, 150, anchor=NW, image=parking_lot_image)

number_of_parking_spots = number_of_zones * 10

available_colors_list = available_colors_list_def(number_of_colors, all_colors_tuple)

max_num = number_of_parking_spots / 2  # maximum number of cars for one color.
dict1 = {'red': max_num, 'blue': max_num, 'green': max_num, 'yellow': max_num, 'indigo': max_num, 'orange': max_num, 'violet': max_num}  # a dictionary with all the 7 colors with their maximum amount.

#car_list = car_list_def(number_of_parking_spots, available_colors_list, dict1, seed)

######################################
#car_list = ['yellow', 'blue', 'green', 'orange', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'red', 'green', 'violet', 'yellow', 'red', 'violet', 'indigo', 'indigo', 'yellow', 'red', 'yellow', 'orange', 'indigo', 'blue', 'violet', 'orange', 'indigo', 'violet', 'orange', 'indigo', 'yellow', 'green', 'violet', 'violet', 'indigo', 'orange', 'yellow', 'blue', 'violet', 'orange', 'orange', 'blue', 'green', 'green', 'red', 'yellow', 'orange', 'indigo', 'blue', 'blue', 'indigo', 'blue', 'violet', 'red', 'violet', 'blue', 'orange', 'indigo', 'red', 'yellow']

#car_list = ['red', 'yellow', 'red', 'green', 'red', 'orange', 'orange', 'violet', 'violet', 'green', 'indigo', 'red', 'orange', 'orange', 'blue', 'green', 'violet', 'blue', 'orange', 'orange', 'yellow', 'violet', 'yellow', 'red', 'green', 'indigo', 'yellow', 'yellow', 'yellow', 'violet', 'indigo', 'green', 'orange', 'blue', 'green', 'violet', 'red', 'blue', 'violet', 'violet', 'indigo', 'orange', 'yellow', 'indigo', 'blue', 'blue', 'orange', 'yellow', 'indigo', 'red', 'yellow', 'yellow', 'yellow', 'orange', 'orange', 'yellow', 'violet', 'orange', 'blue', 'orange']

car_list = ['red', 'blue', 'yellow', 'green', 'red', 'blue', 'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'green', 'red', 'green', 'yellow', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'yellow', 'blue', 'blue', 'red', 'yellow', 'red', 'red', 'red', 'red', 'green', 'yellow', 'green', 'yellow', 'blue', 'yellow', 'red', 'green', 'blue', 'green', 'red', 'yellow', 'red', 'red', 'blue', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'red', 'green', 'blue', 'green', 'red']
######################################


car_image_dict = {'red': red_car_image, 'blue': blue_car_image, 'green': green_car_image, 'yellow': yellow_car_image,
                  'indigo': indigo_car_image, 'orange': orange_car_image, 'violet': violet_car_image}

color_dict = {1: 'red', 2: 'blue', 3: 'green', 4: 'yellow', 5: 'indigo', 6: 'orange', 7: 'violet'}

number_of_colors_left_dict = number_of_colors_left_dict_def(color_dict, car_list)

waiting_cars_temp = []
index = []
counter = 0
for key, value in number_of_colors_left_dict.items():
    index.append(value)
    for i in range(0, value):
        waiting_cars_temp.append([lw_canvas.create_image(waiting_cars_spots[counter][0], waiting_cars_spots[counter][1], 
                               anchor=NW, image=car_image_dict[color_dict[key]]), color_dict[key]])
        counter += 1
lw_canvas.update()

lw_canvas.create_image(225, 8, anchor=NW, image=Number_of_Cars)

listC = ((262, 110), (356, 110), (450, 110), (548, 110), (644, 110), (742, 110), (836, 110))

i = 1
while i <= number_of_colors:
    lw_canvas.create_text(listC[i-1][0], listC[i-1][1], anchor=NE, font=(
        "Arial", 25), fill=color_dict[i], text=number_of_colors_left_dict[i])
    i += 1
lw_canvas.update()

def display_results(status, start, fill_color='green'):

    result_window = Tk()
    result_window.title("Car Parking Lot")
    result_window.iconbitmap(default=os.path.abspath('CodeImages\parking_sign.ico'))
    result_window.configure(width=500, height=300)
    result_window.resizable(0, 0) #Don't allow resizing the window.
    result_window.geometry('500x300') # Fixing Geometry.
    result_window.eval('tk::PlaceWindow . center')

    result_window.protocol("WM_DELETE_WINDOW", on_closing)

    result_canvas = Canvas(result_window, width=w, height=h+300) #width=1074, height=630
    result_canvas.pack()

    result_canvas.create_text(125, 50, anchor=NW, font=("Arial", 40), fill=fill_color, text=status)

    end = time.time()
    time_taken = (end - start)

    get_minutes, get_seconds = divmod(time_taken, 60)

    if get_minutes == 0:
        result_canvas.create_text(175, 125, anchor=NW, font=("Arial", 20), fill="red", text=str(round(get_seconds))+' Seconds')
    else:
        result_canvas.create_text(200, 125, anchor=NW, font=("Arial", 20), fill="red", text=str(round(get_minutes))+'m'+str(round(get_seconds))+'s')

    result_canvas.create_text(140, 165, anchor=NW, font=("Arial", 20), fill="red", text=str(calls)+' Recursive Calls')
    result_canvas.create_text(130, 205, anchor=NW, font=("Arial", 15), fill="red", text='SEED')
    
    temp = Entry(result_canvas)
    temp.insert(END, seed)
    temp.place(x=190, y=207)

    result_canvas.update()
    
    python = sys.executable

    """ Frame(result_canvas, width=126, height=29, background='#023047', highlightbackground = "#8ecae6",
          highlightthickness=3).place(x=118, y=249) """
    Button(result_canvas, borderwidth=3, highlightthickness=3, width=16, height=1, text='Start Over', 
           font=("Arial", 8, 'bold'), command=lambda: (result_window.destroy(), lot_window.destroy(), os.execl(python, python, *sys.argv))).place(x=120, y=250)

    """ Frame(result_canvas, width=131, height=33, highlightbackground="black",
          highlightthickness=3).place(x=258, y=249) """
    Button(result_canvas, borderwidth=3, highlightthickness=3, width=16, height=1, text='Exit', 
           font=("Arial", 8, 'bold'), command=lambda: (result_window.destroy(), lot_window.destroy())).place(x=260, y=250)

    result_window.mainloop()

def Backtraking(assigned_spots_list, spot_no=0):

    global calls
    calls += 1

    if assigned_spots_list[-1].color != None: # Finished.
        return True

    i = 1
    while(i <= number_of_colors):
        
        key = i
        value = number_of_colors_left_dict[key]
        if value != 0:
            color = color_dict[key]
            if isSafe(spot_no, assigned_spots_list, color):
                assigned_spots_list[spot_no].color = color
                number_of_colors_left_dict[key] -= 1

                temp = lw_canvas.create_image(all_parking_spots[spot_no][0], all_parking_spots[spot_no][1], anchor=NW, image=car_image_dict[color])
                time.sleep(0.03)
                lw_canvas.update()
                
                for c in range(number_of_parking_spots-1, -1, -1):
                    if waiting_cars_temp[c][1] == color:
                        temp2 = waiting_cars_temp[c][0]
                        lw_canvas.itemconfig(temp2, image=empty_spot_image)
                        waiting_cars_temp[c][1] = 'empty'
                        #time.sleep(0.2)
                        lw_canvas.update()
                        break
                
                if Backtraking(assigned_spots_list, spot_no + 1):
                    return True
                else:
                    assigned_spots_list[spot_no].color = None
                    number_of_colors_left_dict[key] += 1

                    lw_canvas.itemconfig(temp, image=empty_spot_image)
                    time.sleep(0.03)
                    lw_canvas.update()

                    for c in range(number_of_parking_spots):
                        if waiting_cars_temp[c][1] == 'empty':
                            temp2 = waiting_cars_temp[c][0]
                            lw_canvas.itemconfig(temp2, image=car_image_dict[color])
                            waiting_cars_temp[c][1] = color
                            #time.sleep(0.2)
                            lw_canvas.update()
                            break
                    
        i += 1
    return False

def ForwardChecking(assigned_spots_list, spot_no=0):

    global calls
    calls += 1
    
    if assigned_spots_list[-1].color != None: # Finished.
        return True

    i = 1
    while(i <= number_of_colors):
        
        key = i
        value = number_of_colors_left_dict[key]
        if value != 0:
            color = color_dict[key]
            if value == 1:
                if is_there_an_empty_domain(spot_no, assigned_spots_list, color):
                    i += 1
                    continue 

            if check_domains(spot_no, assigned_spots_list, color):
                if isSafe(spot_no, assigned_spots_list, color): # 
                    assigned_spots_list[spot_no].color = color
                    number_of_colors_left_dict[key] -= 1

                    update_value_domain(spot_no, assigned_spots_list, color, 'remove')

                    temp = lw_canvas.create_image(all_parking_spots[spot_no][0], all_parking_spots[spot_no][1], anchor=NW, image=car_image_dict[color])
                    #time.sleep(0.6)
                    lw_canvas.update()

                    for c in range(number_of_parking_spots-1, -1, -1):
                        if waiting_cars_temp[c][1] == color:
                            temp2 = waiting_cars_temp[c][0]
                            lw_canvas.itemconfig(temp2, image=empty_spot_image)
                            waiting_cars_temp[c][1] = 'empty'
                            #time.sleep(0.3)
                            lw_canvas.update()
                            break
                        
                    if ForwardChecking(assigned_spots_list, spot_no+1):
                        return True
                    else:
                        update_value_domain(spot_no, assigned_spots_list, assigned_spots_list[spot_no].color, 'add')

                        assigned_spots_list[spot_no].color = None
                        number_of_colors_left_dict[key] += 1

                        lw_canvas.itemconfig(temp, image=empty_spot_image)
                        #time.sleep(0.6)
                        lw_canvas.update()

                        for c in range(number_of_parking_spots):
                            if waiting_cars_temp[c][1] == 'empty':
                                temp2 = waiting_cars_temp[c][0]
                                lw_canvas.itemconfig(temp2, image=car_image_dict[color])
                                waiting_cars_temp[c][1] = color
                                #time.sleep(0.3)
                                lw_canvas.update()
                                break

        i += 1
    return False

def ArcConsistency(assigned_spots_list, spot_no=0):

    global calls
    calls += 1
    
    if assigned_spots_list[-1].color != None: # Finished.
        return True

    i = 1
    while(i <= number_of_colors):
        
        key = i
        value = number_of_colors_left_dict[key]
        if value != 0:
            color = color_dict[key]
            if value == 1:
                if is_there_an_empty_domain(spot_no, assigned_spots_list, color):
                    i += 1
                    continue 

            if check_domains(spot_no, assigned_spots_list, color):
                if isSafe(spot_no, assigned_spots_list, color): # 
                    assigned_spots_list[spot_no].color = color
                    number_of_colors_left_dict[key] -= 1

                    update_value_domain(spot_no, assigned_spots_list, color, 'remove')
                    
                    for s in assigned_spots_list[spot_no].adjacency_list:
                        s_spot = assigned_spots_list[s]
                        if s_spot.color == None:
                            for sp in assigned_spots_list[s].adjacency_list:
                                sp_spot = assigned_spots_list[sp]
                                if sp_spot.color == None:
                                    if len(s_spot.value_domain_list) == 1 and len(sp_spot.value_domain_list) == 1:
                                        if s_spot.value_domain_list == sp_spot.value_domain_list:
                                            update_value_domain(spot_no, assigned_spots_list, assigned_spots_list[spot_no].color, 'add')
                                            assigned_spots_list[spot_no].color = None
                                            number_of_colors_left_dict[key] += 1
                                            i += 1
                                            continue

                    temp = lw_canvas.create_image(all_parking_spots[spot_no][0], all_parking_spots[spot_no][1], anchor=NW, image=car_image_dict[color])
                    #time.sleep(0.6)
                    lw_canvas.update()

                    for c in range(number_of_parking_spots-1, -1, -1):
                        if waiting_cars_temp[c][1] == color:
                            temp2 = waiting_cars_temp[c][0]
                            lw_canvas.itemconfig(temp2, image=empty_spot_image)
                            waiting_cars_temp[c][1] = 'empty'
                            #time.sleep(0.3)
                            lw_canvas.update()
                            break
                        
                    if ArcConsistency(assigned_spots_list, spot_no+1):
                        return True
                    else:
                        update_value_domain(spot_no, assigned_spots_list, assigned_spots_list[spot_no].color, 'add')

                        assigned_spots_list[spot_no].color = None
                        number_of_colors_left_dict[key] += 1

                        lw_canvas.itemconfig(temp, image=empty_spot_image)
                        #time.sleep(0.6)
                        lw_canvas.update()

                        for c in range(number_of_parking_spots):
                            if waiting_cars_temp[c][1] == 'empty':
                                temp2 = waiting_cars_temp[c][0]
                                lw_canvas.itemconfig(temp2, image=car_image_dict[color])
                                waiting_cars_temp[c][1] = color
                                #time.sleep(0.3)
                                lw_canvas.update()
                                break

        i += 1
    return False

def run_backtaking():
    start = time.time()
    assigned_spots_list = assigned_spots_list_def(number_of_parking_spots, number_of_colors, algo)
    if Backtraking(assigned_spots_list):
        print('SUCCESS!!!', end='\n')
    
        display_results('SUCCESS!', start)
        for i in range(len(assigned_spots_list)):
            print(str(i), assigned_spots_list[i].color)
        print('-=-=-=-=-=-=-=-=-END-=-=-=-=-=-=-=-=-')
    else:
        print('FAILURE???')
        display_results('FAILURE!', start, fill_color='red') 
        print('-=-=-=-=-=-=-=-=-END-=-=-=-=-=-=-=-=-')

def run_forward_checking():
    start = time.time()
    assigned_spots_list = assigned_spots_list_def(number_of_parking_spots, number_of_colors, algo)
    if ForwardChecking(assigned_spots_list):
        print('SUCCESS!!!', end='\n')

        display_results('SUCCESS!', start)
        for i in range(len(assigned_spots_list)):
            print(str(i), assigned_spots_list[i].color)
        print('-=-=-=-=-=-=-=-=-END-=-=-=-=-=-=-=-=-')
    else:
        print('FAILURE???')
        display_results('FAILURE!', start, fill_color='red') 
        print('-=-=-=-=-=-=-=-=-END-=-=-=-=-=-=-=-=-')

def run_arc_consistency():
    start = time.time()
    assigned_spots_list = assigned_spots_list_def(number_of_parking_spots, number_of_colors, algo)
    if ArcConsistency(assigned_spots_list):
        print('SUCCESS!!!', end='\n')

        display_results('SUCCESS!', start)
        for i in range(len(assigned_spots_list)):
            print(str(i), assigned_spots_list[i].color)
        print('-=-=-=-=-=-=-=-=-END-=-=-=-=-=-=-=-=-')
    else:
        print('FAILURE???')
        display_results('FAILURE!', start, fill_color='red')
        print('-=-=-=-=-=-=-=-=-END-=-=-=-=-=-=-=-=-')

if algo == 'BACKTRACKING':
    print('-=-=-=-=-=-=-=-=-START-=-=-=-=-=-=-=-=-')
    print("BACKTRACKING Running... \n")
    print('--> SEED: ', seed, end='\n')
    print('--> car_list: ', car_list, end='\n')
    print('--> number_of_colors_left: ', number_of_colors_left_dict, end='\n')
    print('--> Calls: ', calls)
    run_backtaking()

elif algo == 'FORWARD_CHECKING':
    print('-=-=-=-=-=-=-=-=-START-=-=-=-=-=-=-=-=-')
    print("FORWARD_CHECKING Running... ")
    print('--> SEED: ', seed, end='\n')
    print('--> car_list: ', car_list, end='\n')
    print('--> number_of_colors_left: ', number_of_colors_left_dict, end='\n')
    print('--> Calls: ', calls)
    run_forward_checking()

elif algo == 'ARC_CONSISTENCY':
    print('-=-=-=-=-=-=-=-=-START-=-=-=-=-=-=-=-=-')
    print("ARC_CONSISTENCY Running... ")
    print('--> SEED: ', seed, end='\n')
    print('--> car_list: ', car_list, end='\n')
    print('--> number_of_colors_left: ', number_of_colors_left_dict, end='\n')
    print('--> Calls: ', calls)
    run_arc_consistency()

lot_window.mainloop()