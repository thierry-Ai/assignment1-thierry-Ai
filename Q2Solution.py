#Solution to question 2 goes here
def calculate_rent(start_time, end_time):
    # Check if input times are valid
    if start_time < 0 or start_time > 24 or end_time < 0 or end_time > 24 or start_time >= end_time:
        print("Invalid input")
        return
    
    total_amount = 0
    
    # Loop through each hour from start to end
    for hour in range(start_time, end_time):
        if 0 <= hour < 7 or 21 <= hour <= 24:
            total_amount += 500
        elif 7 <= hour < 10 or 19 <= hour < 21:
            total_amount += 1000
        elif 10 <= hour < 19:
            total_amount += 1500
    
    print(f"Total amount to be paid: RWF {total_amount}")

# Get user input
try:
    start_time = int(input("Enter the start time (0-24): "))
    end_time = int(input("Enter the end time (0-24): "))
    
    # Call the function to calculate the rent
    calculate_rent(start_time, end_time)
except ValueError:
    print("Invalid input, please enter an integer.")
