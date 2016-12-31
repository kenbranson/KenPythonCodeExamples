import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise        # This allows you to catch the exception, do something, and then reraise it.
finally:
    print("Exiting the try clause")  #Will always be executed even if an exception is raised.  Good for releasing resources.

with open("myfile.txt") as f:     # Makes sure the file is released/closed once the statement is completed.
    for line in f:
        print line,