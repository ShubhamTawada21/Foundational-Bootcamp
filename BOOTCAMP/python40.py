class Ticket:
    def __init__(self, movie, seats_available, seats_requested):
        self.movie = movie
        self.seats_available = seats_available
        self.seats_requested = seats_requested
        self.confirmed_seats = min(seats_available, seats_requested)
        
        if seats_requested <= seats_available:
            self.message = f"Full request met! All {self.confirmed_seats} seats confirmed."
        else:
            self.message = f"Partial fulfillment. Only {self.confirmed_seats} out of {seats_requested} seats confirmed."

    def display_outcome(self):
        print(f"Movie: {self.movie}")
        print(f"Requested: {self.seats_requested} | Available: {self.seats_available}")
        print(f"Status: {self.message}")
        print("-" * 40)


ticket1 = Ticket("Inception", seats_available=10, seats_requested=4)
ticket2 = Ticket("Interstellar", seats_available=2, seats_requested=5)
ticket3 = Ticket("The Matrix", seats_available=3, seats_requested=3)

print("--- Booking Outcomes ---\n")
ticket1.display_outcome()
ticket2.display_outcome()
ticket3.display_outcome()


