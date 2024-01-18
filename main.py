
import random

class Tour:
    def __init__(self, location, price, duration):
        self.location = location
        self.price = price
        self.duration = duration

class Agencjaturystyczna:
    def __init__(self):
        self.tours = []
        self.selected_tour = None
        self.num_of_people = 0

    def add_tour(self, location, price, duration):
        tour = Tour(location, price, duration)
        self.tours.append(tour)

    def display_tours(self):
        for i, tour in enumerate(self.tours):
            print(f"Opcja {i+1}: {tour.location}, {tour.duration} dni, ${tour.price}") 

    def select_tour(self, option):
        if option < 1 or option > len(self.tours):
            print("Nieprawidłowa opcja!")
            return

        self.selected_tour = self.tours[option-1]

    def set_num_of_people(self, num):
        self.num_of_people = num

    def display_summary(self):
        if self.selected_tour is None:
            print("Nie wybrano wycieczki!")
            return 

        print("Podsumowanie wycieczki:")
        print(f"Lokalizacja: {self.selected_tour.location}")
        print(f"Czas trwania: {self.selected_tour.duration} dni")
        print(f"Cena za osobę: {self.selected_tour.price}")
        print(f"Ilość osób: {self.num_of_people}")
        total_price = self.selected_tour.price * self.num_of_people
        print(f"Łączna cena: ${total_price}")

def generate_random_tours(agency):
    locations = ["Pekin", "Bangkok", "Tokyo", "Seul", "Hondkong"]
    durations = [2, 4, 7, 14]
    for _ in range(5):
        location = random.choice(locations)
        duration = random.choice(durations)
        price = random.randint(1000, 5000)
        agency.add_tour(location, price, duration)

def main():
    agency = Agencjaturystyczna()
    generate_random_tours(agency)
    
    while True:
        print("\nWitamy w naszej agencji turystycznej!")
        print("1. Wyświetl dostępne wycieczki")
        print("2. Wybierz wycieczkę")
        print("3. Ustal liczbę osób")
        print("4. Wyświetlanie podsumowania wycieczki")
        print("5. Wyjście")

        choice = int(input("Wpisz swój wybór:"))
        
        if choice == 1:
            agency.display_tours()
        elif choice == 2:
            option = int(input("Wejdź w opcję wycieczki: "))
            agency.select_tour(option)
        elif choice == 3:
            num_of_people = int(input("Podaj liczbę osób: "))
            agency.set_num_of_people(num_of_people)
        elif choice == 4:
            agency.display_summary()
        elif choice == 5:
            break
        else:
            print("Nieprawidłowy wybór! Spróbuj ponownie.")

if __name__ == "__main__":
    main()


  



 

