def hotel_cost(num_nights): # This function will take num_nights as an argument and return a total cost for the hotel stay
    """Calculate the total cost of the hotel stay.""" # This is a docstring, it explains what the code does
    price_per_night = 100  # This is the cost per night in dollars
    return num_nights * price_per_night # This will return the total cost of hotel stay


def plane_cost(city_flight): # This function will take city_flight as an argument and return a cost for the flight
    """Return the cost of the flight based on the destination city.""" # This is a docstring, it explains what the code does
    if city_flight.lower() == "birmingham": # This option is to choose Birmingham City and the cost of 150 dollars
        return 150
    if city_flight.lower() == "london": # This option is to choose London City and the cost of 180 dollars
        return 180
    if city_flight.lower() == "armsterdam": # This option is to choose Armsterdam City and the cost of 190 dollars
        return 190
    if city_flight.lower() == "paris": # This option is to choose Paris City and the cost of 220 dollars
        return 220
    elif city_flight.lower() == "dubai": # This option is to choose Dubai and the cost of 195 dollars
        return 195
    elif city_flight.lower() == "qatar": # This option is to choose Qatar and the cost of 275 dollars
        return 275
    else:
        return 350  # This is the price for any other city not specified


def car_rental(rental_days): # This function will take rental_days as an argument and return the total cost of the car rental
    """Calculate the total cost of car rental.""" # This is a docstring, it explains what the code does
    daily_rental_cost = 35  # This is the daily rental cost in dollars
    return rental_days * daily_rental_cost # This wil return the total car rental services rendered


def holiday_cost(num_nights, city_flight, rental_days): # This function takes three arguments: num_nights, city_flight, and rental_days. Using these three arguments, call the
#hotel_cost(), plane_cost(), and car_rental() functions with their respective arguments, and finally return the total cost for the holiday
    """Calculate the total cost of the holiday.""" # This is a docstring, it explains what the code does
    total_hotel_cost = hotel_cost(num_nights) # This will calculate the total hotel cost
    total_plane_cost = plane_cost(city_flight) # The will calculate the total plane cost
    total_car_cost = car_rental(rental_days) # This will calculate the totalcar rental cost
    return total_hotel_cost + total_plane_cost + total_car_cost # This will return the total of hotel cost, plane cost and car rental cost


def main(): # This is the main program 
    """Main function to interact with the user and calculate the holiday cost.""" # This is a docstring, it explains what the code does


# Get user inputs
city_flight = input("Enter the city you will be flying to (options: Birmingham, London, Armstadam, Paris, Dubai, Qatar): ") # This will get the user input for city
num_nights = int(input("Enter the number of nights you will be staying at the hotel: ")) # This will get the user input for number of nights to stay in the hotel
rental_days = int(input("Enter the number of days you will be hiring a car: ")) # This will get the user input for the number of days of hiring the car


total_cost = holiday_cost(num_nights, city_flight, rental_days) # This will calculate the total cost for number of nights in the hotel, plane cost and car hiring cost


print("\n--- Please this is your Holiday Cost Details ---") # This will print out the information heading
print(f"Your Destination City: {city_flight.capitalize()}") # This will print out the name of the city with first letter in capital
print(f"Hotel Stay Cost: {num_nights} nights at ${hotel_cost(num_nights)}") # This will print out the cost of stay in the hotel
print(f"Flight Cost: ${plane_cost(city_flight)}") # This will print out the cost of plane
print(f"Car Rental Cost: {rental_days} days at ${car_rental(rental_days)}") # This will print out the car rental cost
print(f"Total Holiday Cost: ${total_cost}") # This will print out the over all cost


if __name__ == "__main__": # This will check for the main program and execute it
    main() # This is the main program