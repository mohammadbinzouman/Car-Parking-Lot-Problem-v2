class ParkingSpotBacktracking:
    
    def __init__(self, spot_number):
        self.spot_number = spot_number

        self.adjacency_list = []
        self.color = None

        # 0 1 2 3 4,     10 11 12 13 14,      20 21 22 23 24,      30 31 32 33 34,     40 41 42 43 44,      50 51 52 53 54
        # 5 6 7 8 9      15 16 17 18 19       25 26 27 28 29       35 36 37 38 39      45 46 47 48 49       55 56 57 58 59
        if self.spot_number in [0, 10, 20, 30, 40, 50]: # First row + first spot.     
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number + 5)
            return

        if self.spot_number in [4, 14, 24, 34, 44, 54]: # First row + last spot.
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number + 5)
            return

        if self.spot_number in [5, 15, 25, 35, 45, 55]: # Second row + first spot.
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number - 5)
            return

        if self.spot_number in [9, 19, 29, 39, 49, 59]: # Second row + last spot.
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number - 5)
            return

        if self.spot_number in [1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53]: # First row + in the middle spots.
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number + 5)
            return
        
        if self.spot_number in [6, 7, 8, 16, 17, 18, 26, 27, 28, 36, 37, 38, 46, 47, 48, 56, 57, 58]: # Second row + in the middle spots.
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number - 5)
            return

class ParkingSpotForwardChecking:
    
    def __init__(self, spot_number, number_of_colors):
        self.spot_number = spot_number

        self.adjacency_list = []
        self.color = None

        all_colors_list = ['red', 'blue', 'green', 'yellow', 'indigo', 'orange', 'violet']
        self.value_domain_list = all_colors_list[:number_of_colors]

        # 0 1 2 3 4,     10 11 12 13 14,      20 21 22 23 24,      30 31 32 33 34,     40 41 42 43 44,      50 51 52 53 54
        # 5 6 7 8 9      15 16 17 18 19       25 26 27 28 29       35 36 37 38 39      45 46 47 48 49       55 56 57 58 59
        if self.spot_number in [0, 10, 20, 30, 40, 50]: # First row + first spot.     
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number + 5)
            return

        if self.spot_number in [4, 14, 24, 34, 44, 54]: # First row + last spot.
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number + 5)
            return

        if self.spot_number in [5, 15, 25, 35, 45, 55]: # Second row + first spot.
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number - 5)
            return

        if self.spot_number in [9, 19, 29, 39, 49, 59]: # Second row + last spot.
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number - 5)
            return

        if self.spot_number in [1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33, 41, 42, 43, 51, 52, 53]: # First row + in the middle spots.
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number + 5)
            return
        
        if self.spot_number in [6, 7, 8, 16, 17, 18, 26, 27, 28, 36, 37, 38, 46, 47, 48, 56, 57, 58]: # Second row + in the middle spots.
            self.adjacency_list.append(self.spot_number + 1)
            self.adjacency_list.append(self.spot_number - 1)
            self.adjacency_list.append(self.spot_number - 5)
            return