def check_palindrome(_input : str) -> bool:
    return _input == input_[::-1]

input_ = 'abcba'
print(f'Is Palindrome!: {check_palindrome(input_)}')

# -----------------------------------------------

from datetime import datetime
import time

def measure_elapsed_time():
    print("Measuring time...")

    # Capture the current time as start time
    start_time = datetime.now()
    print(f"Start time: {start_time}")

    # Simulate some work with a delay (you can remove or adjust this)
    time.sleep(5)  # Wait for 5 seconds

    # Capture the current time as end time
    end_time = datetime.now()
    print(f"End time: {end_time}")

    # Calculate difference
    elapsed_time = end_time - start_time
    total_seconds = elapsed_time.total_seconds()

    print(f"Total time elapsed in seconds: {total_seconds}")

# Run the function
measure_elapsed_time()
