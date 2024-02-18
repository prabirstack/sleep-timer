#Main
# Import the os and time modules
import os
import time

# Define a function to shutdown the pc
def shutdown_pc(n):
  # Convert n to an integer
  n = int(n)
  # Check if n is positive
  if n > 0:
    # Print a message
    print(f"Your pc will shutdown in {n} seconds.")
    # Wait for n seconds
    time.sleep(n)
    # Execute the shutdown command
    os.system("shutdown /s /t 1")
  else:
    # Print an error message
    print("Invalid input. Please enter a positive number of seconds.")

# Ask the user for the number of seconds
n = input("Enter the number of seconds to shutdown your pc: ")
# Call the function with n
shutdown_pc(n)
