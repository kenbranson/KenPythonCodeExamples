import time

''' Multi-line comment example...
    with more here
    and finally finishing here.'''

ticks = time.time()    # seconds since 1/1/1970 12:00:00am
print "Ticks since epoch:", ticks

timenow = time.localtime(time.time())
print "Current time :", timenow
print "Year: ", timenow[0], " Month: ", timenow[1]
timenow = time.asctime(time.localtime(time.time()))    # better formatting
print "Current time :", timenow

# Adding a comment...