#Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print ("Current date: ", now.strftime("%d/%m/%y"))
print ("Current Time: ", now.strftime("%H:%M:%S"))
