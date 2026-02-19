import time

def start_timer(minutes):
    # Convert minutes to total seconds
    total_seconds = minutes * 60
    start_time = time.time()


    print(f"Starting {minutes}-minute timer...")
    try:

        while True :
            # Calculate elapsed time
            elapsed = time.time() - start_time
            # print('time.time',time.time())

            # Calculate minutes and seconds passed
            mins, secs = divmod(int(elapsed), 60)

            # Format time as MM:SS
            timer_format = '{:02d}:{:02d}'.format(mins, secs)

            # Print on the same line using \r (carriage return)
            print(f"Time Elapsed: {timer_format}", end="\n")

            # If we reached the goal
            if elapsed >= total_seconds:
                print(f"\n{minutes} minutes are up!")
                if minutes==3:
                    return 1
                elif minutes==1:
                    return 0




            # Pause for 1 second
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nTimer stopped.")


# Start a 25-minute timer

returncode=start_timer(3)
if returncode==1:
    start_timer(1)
elif returncode==0:
    start_timer(3)
else:
    start_timer(20)

# return code 1 is task
# return code 0 is break


