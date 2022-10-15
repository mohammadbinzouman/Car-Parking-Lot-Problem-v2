from parking_spot import *
from tkinter import *
import random

def assigned_spots_list_def(number_of_parking_spots, number_of_colors, algo):
    if algo == 'BACKTRACKING':
        return [ParkingSpotBacktracking(i) for i in range(0, number_of_parking_spots)]
    else:
        return [ParkingSpotForwardChecking(i, number_of_colors) for i in range(0, number_of_parking_spots)]
    
def available_colors_list_def(number_of_colors, all_colors_tuple):
    return [all_colors_tuple[i] for i in range(0, number_of_colors)]
    
def car_list_def(number_of_parking_spots, available_colors_list, dict1, seed):
    random.seed(seed)

    car_list = []
    i = 0
    while i < number_of_parking_spots:  # while loop filling list2 randomly, and making sure the list is solvable. *read Note#1*
        r = random.choice(available_colors_list)
        if dict1[r] == 0:
            available_colors_list.remove(r)
            continue
        else:
            dict1[r] = dict1[r] - 1
            car_list.append(r)

        i += 1
    return car_list

def number_of_colors_left_dict_def(color_dict, car_list):
    number_of_colors_left_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    for i in range(1, len(color_dict)+1):
        for car in car_list:
            if car == color_dict[i]:
                number_of_colors_left_dict[i] += 1
    return number_of_colors_left_dict

def isSafe(spot_number, assigned_spots_list, color):
    # 0 1 2 3 4,     10 11 12 13 14,      20 21 22 23 24,      30 31 32 33 34,     40 41 42 43 44,      50 51 52 53 54
    # 5 6 7 8 9      15 16 17 18 19       25 26 27 28 29       35 36 37 38 39      45 46 47 48 49       55 56 57 58 59
    spot = assigned_spots_list[spot_number]
    for s in spot.adjacency_list:
        if assigned_spots_list[s].color == color: # NOT SAFE.
            return False
        else:
            continue
    
    return True # SAFE.

def check_domains(spot_number, assigned_spots_list, color):

    spot = assigned_spots_list[spot_number]
    for s in spot.adjacency_list:
        if len(assigned_spots_list[s].value_domain_list) == 1 and color in assigned_spots_list[s].value_domain_list: # NOT SAFE. EMPTY DOMAIN.
            return False
        else:
            continue
    return True # SAFE. 

def update_value_domain(spot_no, assigned_spots_list, color, flag):
    if flag == 'add':
        spot = assigned_spots_list[spot_no]
        for s in spot.adjacency_list:
            if color not in assigned_spots_list[s].value_domain_list:
                assigned_spots_list[s].value_domain_list.append(color) 

    if flag == 'remove':
        spot = assigned_spots_list[spot_no]
        for s in spot.adjacency_list:
            if color in assigned_spots_list[s].value_domain_list:
                assigned_spots_list[s].value_domain_list.remove(color)

def is_there_an_empty_domain(spot_no, assigned_spots_list, color):

    for i in range(spot_no+1, len(assigned_spots_list)):
        if color in assigned_spots_list[i].value_domain_list:
            if len(assigned_spots_list[i].value_domain_list) == 1:
                return True
    return False