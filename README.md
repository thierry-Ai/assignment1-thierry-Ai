
Solution for Question 1: Bicycle Rental Program
python
Copy code
def calculate_rent(start_time, end_time):
    # Check for invalid inputs
    if start_time > end_time or start_time < 0 or end_time > 24:
        return "Invalid input. Please enter a valid time range (0-24)."
    
    total_amount = 0
    
    # Rates based on time intervals
    for hour in range(start_time, end_time):
        if (0 <= hour < 7) or (21 <= hour < 24):  # 500 RWF per hour
            total_amount += 500
        elif (7 <= hour < 10) or (19 <= hour < 21):  # 1000 RWF per hour
            total_amount += 1000
        elif 10 <= hour < 19:  # 1500 RWF per hour
            total_amount += 1500
    
    return f"The total amount to be paid is: RWF {total_amount}"

# Input for start and end times
start_time = int(input("Enter the starting time (0-24): "))
end_time = int(input("Enter the ending time (0-24): "))

# Calculate and print the rent
print(calculate_rent(start_time, end_time))
