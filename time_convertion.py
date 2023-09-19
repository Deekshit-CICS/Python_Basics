from datetime import datetime

# This is an example with inbuild method datetime, it may not work with exam scenarios 
# input 12:05:00 AM      space after time and AM/PM is mandatory
#  output: 00:05:00 

def convert24(time):
    # Parse the time string into a datetime object
    t = datetime.strptime(time, '%I:%M:%S %p')
    # Format the datetime object into a 24-hour time string
    return t.strftime('%H:%M:%S')
 
print(convert24('11:21:30 PM'))  # Output: '23:21:30'
print(convert24('12:12:20 AM'))  # Output: '00:12:20'
