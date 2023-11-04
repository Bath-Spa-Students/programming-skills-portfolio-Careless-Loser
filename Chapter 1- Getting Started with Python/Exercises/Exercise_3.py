#The first line is importing the "datetime", the datetime module which supplies classes for manipulating dates and times.
import datetime
#The second line is "now" which creates the current datetime object for the current date and time
now = datetime.datetime.now()
#The Third line is the print string "Current date and time"
print (" Current date and time : ")
#The fourth line is printing the actual date and time which includes
#%Y: Year, %m: Month, %d: Day, %H: hour, %M: minute and %S: seconds 
print (now.strftime("%Y-%m-%d %H:%M:%S"))