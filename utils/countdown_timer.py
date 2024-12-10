import time 

def calculate_timer (start_time, total_time):
  current_time = time.time()
  elapsed_time = current_time - start_time
  remaining_time = total_time - elapsed_time

  # check if time has run out
  if remaining_time <= 0:
    return "\nTime's up!"
  else:
  # Display remaining time
    minutes, seconds = divmod(int(remaining_time), 60)
    return f"Time Remaining: {minutes} minutes and {seconds} seconds"

