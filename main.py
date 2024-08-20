# Function to calculate payment
def payment_calculation(distance, weight, weight_type="normal"):
    # Extra fee depending on weight type
    extra_fee = 0
    if weight_type == "dangerous":
        extra_fee = 100  # Extra $100 fee for dangerous weight type
    elif weight_type == "food":
        extra_fee = 50
    elif weight_type == "liquid":
        extra_fee = 50

    # Calculation of fee depending on distance and weight
    if distance < 100:
        payment = weight * 1
    elif distance < 500:
        payment = weight * 1.5
    else:
        payment = weight * 2

    # Adding extra fee to normal fee
    return payment + extra_fee


def main():
    while True:
        where = "None"
        address = "None"
        # Asking if user is in America or not
        while where not in ["yes", "no"]:
            where = input("Are you in America? (Yes/No):  ").lower()
        if where == "yes":
            state_list = ["alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut",
                          "delaware", "florida", "georgia", "hawaii", "idaho", "illinois", "indiana", "iowa",
                          "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts", "michigan",
                          "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new hampshire",
                          "new jersey", "new mexico", "new york", "north carolina", "north dakota", "ohio", "oklahoma",
                          "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota", "tennessee",
                          "texas", "utah", "vermont", "virginia", "washington", "west virginia", "wisconsin", "wyoming"]
            state = input("Please enter your state: ").lower()
            # Asking for user's state in America
            while state not in state_list:
                state = input("Please enter a state in America: ").lower()
            street = input("Please enter your street: ").lower()
            address = state.capitalize()+"/"+street.capitalize()
        elif where == "no":
            country = str(input("Please enter your country: "))
            city = str(input("Please enter your city: "))
            street = str(input("Please enter your street: "))
            address = country.capitalize()+"/"+city.capitalize()+"/"+street.capitalize()
        distance = 0
        weight = 0
        weight_type = "None"
        retry = "None"
        # Input for distance
        while distance is not float:
            try:
                distance = float(input("Please enter the distance in kilometers: "))
                if distance < 0:
                    print("Please enter a positive number.")
                    distance = "None"
            except ValueError:
                print("Please enter a number.")
            if type(distance) is float:
                break
        # Input for weight
        while weight is not float:
            try:
                weight = float(input("Please enter the weight in kilograms: "))
                if weight < 0:
                    print("Please enter a positive number.")
                    weight = "None"
            except ValueError:
                print("Please enter a number.")
            if type(weight) is float:
                break
        weight_type_list = ["normal", "dangerous", "food", "liquid", "other"]
        # Input for weight type
        while weight_type not in weight_type_list:
            weight_type = input("Please enter a weight type. (Normal/Dangerous/Food/Liquid/Other): ").lower()
        if weight_type == "other":
            weight_type = input("Please enter your weight type: ")
        payment = payment_calculation(distance, weight, weight_type)
        print()
        print("Payment:", payment, "Dollars")
        # Printing user's address
        print("Your address: "+address)

        print("Your weight type: "+weight_type)
        print()
        # Asking if user wants to make another calculation
        while retry not in ["yes", "no"]:
            retry = input("Do you want to make another calculation? (Yes/No): ").lower()
            if retry == "no":
                exit()
            elif retry != "yes":
                print("Please enter Yes or No.")
        print()


main()