class Star_Cinema:
    __hall_list = [] 

    def entry_hall(self, hall):
        
        self.__hall_list.append(hall)

    def get_hall_list(self):  
        return self.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        
        super().__init__()
        self.__seats = {}  
        self.__show_list = []  
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.entry_hall(self)  

    def entry_show(self, id, movie_name, time):
        
        self.__show_list.append((id, movie_name, time))
        seats = [['free' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def book_seats(self, id, seat_list):
        
        if id in self.__seats:
            for row, col in seat_list:
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if self.__seats[id][row][col] == 'free':
                        self.__seats[id][row][col] = 'booked'
                        print(f"Seat ({row}, {col}) booked successfully!")
                    else:
                        print(f"Seat ({row}, {col}) is already booked.")
                else:
                    print(f"Invalid seat ({row}, {col})")
        else:
            print("Invalid")

    def view_show_list(self):
        
        if self.__show_list:
            for id, movie_name, time in self.__show_list:
                print(f"ID: {id}, Movie: {movie_name}, Time: {time}")
        else:
            print("No show")

    def view_available_seats(self, id):
        
        if id in self.__seats:
            print(f"Available seats for show ID {id}:")
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if self.__seats[id][row][col] == 'free':
                        print(f"({row}, {col})", end=" ")
                print() 
        else:
            print("Invalid")


def counter(cinema):
    
    while True:
        print("\nCounter:")
        print("1. View all shows")
        print("2. View available seats ")
        print("3. Book seats")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            for hall in cinema.get_hall_list(): 
                print(f"\nShows in Hall {hall._Hall__hall_no}:")  
                hall.view_show_list()
        elif choice == '2':
            show_id = input("Enter the show ID: ")
            hall_no = int(input("Enter the hall number: "))
            try:
                hall = cinema.get_hall_list()[hall_no - 1]
                hall.view_available_seats(show_id)
            except IndexError:
                print("Invalid hall number.")
        elif choice == '3':
            show_id = input("Enter the show ID: ")
            hall_no = int(input("Enter the hall number: "))
            try:
                hall = cinema.get_hall_list()[hall_no - 1]
                num_seats = int(input("Enter the number of seats to book: "))
                seat_list = []
                for i in range(num_seats):
                    row = int(input(f"Enter row number for seat {i+1}: "))
                    col = int(input(f"Enter column number for seat {i+1}: "))
                    seat_list.append((row, col))
                hall.book_seats(show_id, seat_list)
            except IndexError:
                print("Invalid hall number.")
            except ValueError:
                print("Invalid input. Please enter numbers for row and column.")
        elif choice == '4':
            print("Exit counter")
            break
        else:
            print("Invalid choice.")


cinema = Star_Cinema()
Jalmal_hall = Hall(rows=6, cols=12, hall_no=2)
Notun_hall= Hall(rows=8, cols=14, hall_no=4)

Jalmal_hall.entry_show("X", "Jawan", "10:00 AM")
Jalmal_hall.entry_show("Y", "Bindass", "2:00 PM")
Notun_hall.entry_show("Z", "Killer Hasina", "6:00 PM")


counter(cinema)