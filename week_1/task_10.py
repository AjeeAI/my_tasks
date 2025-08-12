"""This is a program to receive the details of a student's school and fees, calculate and then 
   display the total fees."""
# Program description: Receive details of a student's school and fees, calculate, and display total fees

# Prompt user to enter the school name
# Prompt user to enter the tuition fee
# Prompt user to enter the hostel fee
# Prompt user to enter the feeding fee

# Calculate the total fee by summing tuition, hostel, and feeding fees

# Display fees in a fixed-width table format (for assignment purposes)

# Calculate widths for each fee type based on input lengths
# Determine the maximum width to make the output responsive
# Ensure a minimum width of 50 characters

# Display fees in a dynamically adjusted table format


school_name = input("Enter the school name: ")
tuition_fee = input("Enter the tuition fee: ")
hostel_fee = input("Enter the hostel fee: ")
feeding_fee = input("Enter the feeding fee: ")
# school_name = "DayWaterman"
# tuition_fee = 50000
# hostel_fee = 30000
# feeding_fee = 20000
total_fee = float(tuition_fee) + float(hostel_fee) + float(feeding_fee)

# This method of displaying the output is not responsive so I will create another that is.
#This first one is only for assignment purposes.
print("_________________________________")
print(f"\n|\t   {school_name}\t\t|\n\n|\ttuition fee: ₦{float(tuition_fee):,}\t|\n|\t hostel fee: ₦{float(hostel_fee):,}\t|\n|\tfeeding fee: ₦{float(feeding_fee):,}\t|\n|\t  total fee: ₦{total_fee:,}\t|")
print("|_______________________________|")

# Now for the responsive part
# I created width variables for each fee type that gets the length of the values in our inputs
# The "width" itself is now the maximum of all the individual widths

total_fee = float(tuition_fee) + float(hostel_fee) + float(feeding_fee)
width_school_name = len(school_name) + 2
width_tuition_fee = len(str(tuition_fee)) + 2
width_hostel_fee = len(str(hostel_fee)) + 2
width_feeding_fee = len(str(feeding_fee)) + 2
width_total_fee = len(str(total_fee)) + 2
width = max(width_school_name, width_tuition_fee, width_hostel_fee, width_feeding_fee, width_total_fee) 
max_width = max(50, width * 2) # This ensures a minimum width of 50 characters


print("_" * max_width)
print(f"{school_name.center(max_width)}\n")
print(f"\tTuition fee: \t₦{float(tuition_fee):,.2f}".ljust(max_width))
print(f"\tHostel fee: \t₦{float(hostel_fee):,.2f}".ljust(max_width))
print(f"\tFeeding fee: \t₦{float(feeding_fee):,.2f}".ljust(max_width))
print(f"\tTotal fee: \t₦{float(total_fee):,.2f}".ljust(max_width))
print("_" *max_width)